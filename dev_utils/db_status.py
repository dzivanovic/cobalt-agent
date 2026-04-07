"""
Cobalt Agent: Database Status Audit Utility

A comprehensive full-stack database audit utility that connects to the cobalt_brain
PostgreSQL database and displays health metrics for all core tables using Rich formatting.

Zero-State UI: Displays clean rich tables for each table, with graceful handling of
missing/empty tables (no stack traces, all metrics show as 0).

Usage: uv run dev_utils/db_status.py
"""

import sys
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import psycopg2
from psycopg2.extras import RealDictCursor
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

from cobalt_agent.config import get_config

# Initialize Rich console
console = Console()


def create_db_connection():
    """Create and return a PostgreSQL database connection."""
    config = get_config()
    
    conn = psycopg2.connect(
        host=config.postgres.host,
        port=config.postgres.port,
        user=config.postgres.user,
        password=config.postgres.password,
        database=config.postgres.db
    )
    
    return conn


def extract_tables_from_schema(schema_path: Path) -> List[str]:
    """Extract table names from schema.sql using regex matching CREATE TABLE statements."""
    try:
        content = schema_path.read_text()
        # Match CREATE TABLE IF NOT EXISTS table_name or CREATE TABLE table_name
        pattern = r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?(\w+)\s*\('
        tables = re.findall(pattern, content, re.IGNORECASE)
        return tables
    except Exception as e:
        console.print(f"[red]Error reading schema file: {e}[/red]")
        return []


def get_zero_state_data_sample(table_name: str) -> Table:
    """Return a Data Sample table for missing/empty tables."""
    sample_table = Table(title=f"{table_name} - Data Sample", box=box.ROUNDED, style="bold cyan")
    sample_table.add_column("Status", style="dim")
    sample_table.add_row("Table missing or empty", "N/A")
    return sample_table


def get_zero_state_health_metrics(table_name: str) -> Table:
    """Return a Health Metrics table with all values set to 0 for missing/empty tables."""
    metrics_table = Table(title=f"{table_name} - Health Metrics", box=box.ROUNDED, style="bold green")
    metrics_table.add_column("Metric", style="cyan", no_wrap=True)
    metrics_table.add_column("Value", style="bold white")
    
    # Add all expected metric labels with 0 values
    if table_name == "instruments":
        metrics_table.add_row("Total Records", "0")
        metrics_table.add_row("Total Unique Tickers", "0")
        metrics_table.add_row("Total Tagged", "0")
        metrics_table.add_row("Total Untagged", "0")
        metrics_table.add_row("Total Active", "0")
        metrics_table.add_row("Total Inactive", "0")
    elif table_name == "daily_market_data":
        metrics_table.add_row("Total Records", "0")
        metrics_table.add_row("Total Unique Tickers", "0")
        metrics_table.add_row("Latest Date Recorded", "N/A")
    elif table_name == "corporate_events":
        metrics_table.add_row("Total Events", "0")
        metrics_table.add_row("Total Unique Tickers", "0")
        metrics_table.add_row("Events in Last 7 Days", "0")
    elif table_name == "intraday_bars":
        metrics_table.add_row("Total Records", "0")
        metrics_table.add_row("Total Unique Tickers", "0")
        metrics_table.add_row("Latest Timestamp", "N/A")
    elif table_name == "scanner_alerts":
        metrics_table.add_row("Total Alerts", "0")
        metrics_table.add_row("Alerts Today", "0")
    elif table_name == "strategy_signals":
        metrics_table.add_row("Total Signals", "0")
    elif table_name == "trade_proposals":
        metrics_table.add_row("Total Proposals", "0")
    elif table_name == "audit_logs":
        metrics_table.add_row("Total Logs", "0")
    
    return metrics_table


def audit_table(conn, table_name: str):
    from rich.table import Table
    from rich.console import Console
    console = Console()
    cur = conn.cursor()
    
    console.print(f"\n[bold cyan]=== {table_name.upper()} ===[/bold cyan]")
    
    try:
        # 1. Try to fetch a sample
        cur.execute(f"SELECT * FROM {table_name} LIMIT 2;")
        sample_rows = cur.fetchall()
        
        # 2. Try to fetch metrics
        if table_name == "instruments":
            cur.execute("SELECT COUNT(*) FROM instruments;")
            total = cur.fetchone()[0]
            cur.execute("SELECT COUNT(DISTINCT symbol) FROM instruments;")
            unique = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM instruments WHERE active_themes IS NOT NULL AND active_themes::text != '[]' AND active_themes::text != 'null';")
            tagged = cur.fetchone()[0]
            console.print(f"Metrics -> Total: {total} | Unique: {unique} | Tagged: {tagged}")
        else:
            cur.execute(f"SELECT COUNT(*) FROM {table_name};")
            total = cur.fetchone()[0]
            console.print(f"Metrics -> Total Records: {total}")
            
        # 3. Print the sample table
        if sample_rows:
            t = Table()
            for col in [desc[0] for desc in cur.description]:
                t.add_column(col)
            for row in sample_rows:
                t.add_row(*[str(item) for item in row])
            console.print(t)
        else:
            console.print("[yellow]0 rows found.[/yellow]")

    except Exception as e:
        # CRITICAL: Reset the transaction if the table is missing
        conn.rollback()
        console.print("[yellow]Table missing or empty.[/yellow]")
        console.print("Metrics -> Total Records: 0")
    finally:
        cur.close()


def display_data_sample_table(table_name: str, rows: Optional[List[Dict]] = None) -> None:
    """Display the Data Sample rich table."""
    sample_table = Table(title=f"{table_name} - Data Sample", box=box.ROUNDED, style="bold cyan")
    
    if rows is None or len(rows) == 0:
        # Zero-state: table missing or empty
        sample_table.add_column("Status", style="dim")
        sample_table.add_row("Table missing or empty", "N/A")
    else:
        # Get column names from first row keys
        columns = list(rows[0].keys())
        
        # Add columns to table
        for col in columns:
            sample_table.add_column(col, style="dim")
        
        # Add rows to table (max 2 rows)
        for row in rows[:2]:
            values = [str(row[col])[:50] for col in columns]  # Truncate long values
            sample_table.add_row(*values)
    
    console.print(sample_table)


def display_health_metrics_table(table_name: str, metrics: Dict) -> None:
    """Display the Health Metrics rich table with actual data."""
    metrics_table = Table(title=f"{table_name} - Health Metrics", box=box.ROUNDED, style="bold green")
    metrics_table.add_column("Metric", style="cyan", no_wrap=True)
    metrics_table.add_column("Value", style="bold white")
    
    if table_name == "instruments":
        metrics_table.add_row("Total Records", str(metrics.get("Total Records", 0)))
        metrics_table.add_row("Total Unique Tickers", str(metrics.get("Total Unique Tickers", 0)))
        metrics_table.add_row("Total Tagged", str(metrics.get("Total Tagged", 0)))
        metrics_table.add_row("Total Untagged", str(metrics.get("Total Untagged", 0)))
        metrics_table.add_row("Total Active", str(metrics.get("Total Active", 0)))
        metrics_table.add_row("Total Inactive", str(metrics.get("Total Inactive", 0)))
        
    elif table_name == "daily_market_data":
        metrics_table.add_row("Total Records", str(metrics.get("Total Records", 0)))
        metrics_table.add_row("Total Unique Tickers", str(metrics.get("Total Unique Tickers", 0)))
        metrics_table.add_row("Latest Date Recorded", str(metrics.get("Latest Date Recorded", "N/A")))
        
    elif table_name == "corporate_events":
        metrics_table.add_row("Total Events", str(metrics.get("Total Events", 0)))
        metrics_table.add_row("Total Unique Tickers", str(metrics.get("Total Unique Tickers", 0)))
        metrics_table.add_row("Events in Last 7 Days", str(metrics.get("Events in Last 7 Days", 0)))
        
    elif table_name == "intraday_bars":
        metrics_table.add_row("Total Records", str(metrics.get("Total Records", 0)))
        metrics_table.add_row("Total Unique Tickers", str(metrics.get("Total Unique Tickers", 0)))
        metrics_table.add_row("Latest Timestamp", str(metrics.get("Latest Timestamp", "N/A")))
        
    elif table_name == "scanner_alerts":
        metrics_table.add_row("Total Alerts", str(metrics.get("Total Alerts", 0)))
        metrics_table.add_row("Alerts Today", str(metrics.get("Alerts Today", 0)))
        
    elif table_name == "strategy_signals":
        metrics_table.add_row("Total Signals", str(metrics.get("Total Signals", 0)))
        
        # Add risk grade breakdown if available
        grade_breakdown = metrics.get("Risk Grade Breakdown", [])
        for row in grade_breakdown:
            metrics_table.add_row(f"Risk Grade: {row[0]}", str(row[1]))
        
        # Add status breakdown if available
        status_breakdown = metrics.get("Status Breakdown", [])
        for row in status_breakdown:
            metrics_table.add_row(f"Status: {row[0]}", str(row[1]))
            
    elif table_name == "trade_proposals":
        metrics_table.add_row("Total Proposals", str(metrics.get("Total Proposals", 0)))
        
        # Add HITL status breakdown if available
        status_breakdown = metrics.get("HITL Status Breakdown", [])
        for row in status_breakdown:
            metrics_table.add_row(f"HITL Status: {row[0]}", str(row[1]))
            
    elif table_name == "audit_logs":
        metrics_table.add_row("Total Logs", str(metrics.get("Total Logs", 0)))
        
        # Add department breakdown if available
        dept_breakdown = metrics.get("Department Breakdown", [])
        for row in dept_breakdown:
            metrics_table.add_row(f"Department: {row[0]}", str(row[1]))
        
        # Add status breakdown if available
        status_breakdown = metrics.get("Status Breakdown", [])
        for row in status_breakdown:
            metrics_table.add_row(f"Status: {row[0]}", str(row[1]))


def display_zero_state_metrics(table_name: str) -> None:
    """Display Health Metrics table with all values set to 0 (zero-state UI)."""
    metrics_table = Table(title=f"{table_name} - Health Metrics", box=box.ROUNDED, style="bold green")
    metrics_table.add_column("Metric", style="cyan", no_wrap=True)
    metrics_table.add_column("Value", style="bold white")
    
    # Add all expected metric labels with hardcoded 0 values - NO STACK TRACES
    if table_name == "instruments":
        metrics_table.add_row("Total Records", "0")
        metrics_table.add_row("Total Unique Tickers", "0")
        metrics_table.add_row("Total Tagged", "0")
        metrics_table.add_row("Total Untagged", "0")
        metrics_table.add_row("Total Active", "0")
        metrics_table.add_row("Total Inactive", "0")
    elif table_name == "daily_market_data":
        metrics_table.add_row("Total Records", "0")
        metrics_table.add_row("Total Unique Tickers", "0")
        metrics_table.add_row("Latest Date Recorded", "N/A")
    elif table_name == "corporate_events":
        metrics_table.add_row("Total Events", "0")
        metrics_table.add_row("Total Unique Tickers", "0")
        metrics_table.add_row("Events in Last 7 Days", "0")
    elif table_name == "intraday_bars":
        metrics_table.add_row("Total Records", "0")
        metrics_table.add_row("Total Unique Tickers", "0")
        metrics_table.add_row("Latest Timestamp", "N/A")
    elif table_name == "scanner_alerts":
        metrics_table.add_row("Total Alerts", "0")
        metrics_table.add_row("Alerts Today", "0")
    elif table_name == "strategy_signals":
        metrics_table.add_row("Total Signals", "0")
    elif table_name == "trade_proposals":
        metrics_table.add_row("Total Proposals", "0")
    elif table_name == "audit_logs":
        metrics_table.add_row("Total Logs", "0")
    
    console.print(metrics_table)


def run_audit():
    """Run the complete database audit."""
    console.print(Panel.fit("🔍 Cobalt Agent Database Audit Utility", style="bold magenta"))
    console.print()
    
    conn = None
    
    try:
        # Connect to database
        console.print("[dim]Connecting to cobalt_brain database...[/dim]")
        conn = create_db_connection()
        console.print("[green]✓ Connected successfully[/green]\n")
        
        # Dynamically extract tables from schema.sql
        schema_path = Path(__file__).parent.parent / "src" / "cobalt_agent" / "db" / "schema.sql"
        core_tables = extract_tables_from_schema(schema_path)
        
        if not core_tables:
            console.print("[red]No tables found in schema file.[/red]")
            sys.exit(1)
        
        console.print(f"[dim]Found {len(core_tables)} tables in schema.sql:[/dim]")
        for table in core_tables:
            console.print(f"\n[bold blue]{'='*60}[/]")
            console.print(f"[bold]Auditing table: {table}[/]\n")
            
            audit_table(conn, table)
        
        console.print(f"\n[bold green]{'='*60}[/]")
        console.print("[green]✓ Audit Complete![/green]")
        
    except psycopg2.OperationalError as e:
        console.print(f"[red]✗ Failed to connect to database:[/red] {e}")
        console.print("[dim]Ensure PostgreSQL is running and cobalt_brain database exists.[/dim]")
        sys.exit(1)
        
    except Exception as e:
        console.print(f"[red]✗ Unexpected error:[/red] {e}")
        sys.exit(1)
        
    finally:
        if conn is not None:
            conn.close()
            console.print("[dim]Database connection closed.[/dim]")


if __name__ == "__main__":
    run_audit()