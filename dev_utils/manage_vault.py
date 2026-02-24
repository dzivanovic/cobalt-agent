import sys
import os
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from cobalt_agent.security.vault import VaultManager

console = Console()

def main():
    console.print("\n[bold blue]🛡️ Cobalt Local Vault Manager[/bold blue]")
    vault = VaultManager()
    
    # Check if Master Key is in environment for ease of use during dev
    master_key = os.getenv("COBALT_MASTER_KEY")
    
    if not master_key:
        action = Prompt.ask("No COBALT_MASTER_KEY found in environment. Generate a new one?", choices=["y", "n"], default="y")
        if action == "y":
            new_key = vault.generate_master_key()
            console.print(f"\n[bold red]!!! CRITICAL: SAVE THIS KEY IN YOUR PASSWORD MANAGER !!![/bold red]")
            console.print(f"[bold green]export COBALT_MASTER_KEY='{new_key}'[/bold green]\n")
            console.print("Run this export command in your terminal, then run this script again.")
            return
        else:
            console.print("Exiting. You must set COBALT_MASTER_KEY to use the vault.")
            return

    if not vault.unlock(master_key):
        console.print("[red]Failed to unlock vault. Check your Master Key.[/red]")
        return
        
    while True:
        console.print("\n[bold cyan]--- Vault Menu ---[/bold cyan]")
        console.print("[1] List All Secret Names")
        console.print("[2] Retrieve a Secret")
        console.print("[3] Add/Update a Secret (String or JSON)")
        console.print("[4] Delete a Secret")
        console.print("[5] Exit and Lock Vault")
        
        choice = Prompt.ask("Choose an action", choices=["1", "2", "3", "4", "5"])
        
        if choice == "1":
            keys = vault.list_secrets()
            if keys:
                console.print("\n[bold green]Stored Keys:[/bold green]")
                for k in keys:
                    console.print(f" - {k}")
            else:
                console.print("[yellow]Vault is empty.[/yellow]")
                
        elif choice == "2":
            key_name = Prompt.ask("Enter Secret Name to retrieve")
            val = vault.get_secret(key_name)
            if val:
                console.print(f"\n[bold green]{key_name}:[/bold green]\n{val}")
            else:
                console.print(f"[red]Secret '{key_name}' not found.[/red]")
                
        elif choice == "3":
            key_name = Prompt.ask("Enter Secret Name (e.g., BROKER_CREDS)")
            console.print("[dim]Note: You can paste a flat string OR a JSON string like {\"url\":\"...\", \"user\":\"...\", \"pass\":\"...\"}[/dim]")
            secret_value = Prompt.ask("Enter Secret Value", password=True)
            if vault.set_secret(master_key, key_name, secret_value):
                console.print(f"[green]Successfully saved '{key_name}'[/green]")
                
        elif choice == "4":
            key_name = Prompt.ask("Enter Secret Name to delete")
            confirm = Prompt.ask(f"Are you sure you want to delete '{key_name}'?", choices=["y", "n"])
            if confirm == "y":
                if vault.delete_secret(master_key, key_name):
                    console.print(f"[green]Deleted '{key_name}'.[/green]")
                else:
                    console.print(f"[red]Failed to delete '{key_name}'.[/red]")
                    
        elif choice == "5":
            vault.lock()
            console.print("[bold blue]Vault locked. Goodbye.[/bold blue]")
            break

if __name__ == "__main__":
    main()