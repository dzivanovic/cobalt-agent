import pandas as pd

def format_lightspeed_trades(input_file, output_file):
    valid_rows = []
    
    # 1. Parse the file line-by-line to bypass the broken daily headers
    with open(input_file, "r") as f:
        for line in f:
            parts = [p.strip() for p in line.split(',')]
            # Identify actual trade rows (they have 'Long' or 'Short' in the 5th column)
            if len(parts) >= 21 and parts[4] in ['Long', 'Short']:
                valid_rows.append(parts[:21])

    # The exact columns from the Lightspeed export
    columns = ['Opened','Closed','Held','Symbol','Type','Entry','Exit',
               'Qty','Gross','Comm','Ecn Fee','SEC','ORF','CAT','TAF',
               'NFA','NSCC','Acc','Clr','Misc','Net']
    
    df = pd.DataFrame(valid_rows, columns=columns)

    # 2. Convert necessary string columns to numeric for calculation
    for col in ['Entry', 'Exit', 'Qty', 'Gross', 'Net']:
        df[col] = pd.to_numeric(df[col].replace('', '0'), errors='coerce')

    # 3. Calculate Total Cost and Proceeds
    df['Total Cost'] = df['Qty'] * df['Entry']
    df['Total Proceeds'] = df['Qty'] * df['Exit']

    # 4. Map everything to the IRS Form 4797 standard columns
    irs_df = pd.DataFrame({
        '(a) Description': df['Symbol'],
        '(b) Date Acquired': df['Opened'].str.split(' ').str[0], # Strips out the time
        '(c) Date Sold': df['Closed'].str.split(' ').str[0] if df['Closed'].str.contains(' ').any() else df['Opened'].str.split(' ').str[0],
        '(d) Gross Sales Price': df['Total Proceeds'].round(2),
        '(e) Depreciation': 0,
        '(f) Cost or other basis': df['Total Cost'].round(2),
        '(g) Gain or loss': df['Net'].round(2) # The final net figure matches the exact broker total
    })

    # 5. Export to a clean CSV
    irs_df.to_csv(output_file, index=False)
    
    total_net = irs_df['(g) Gain or loss'].sum()
    print(f"File formatted successfully. Total Net Loss: ${total_net:,.2f}")
    print(f"Saved to: {output_file}")

# Execute the function
format_lightspeed_trades("LightspeedTrades2025.xlsx - Sheet1.csv", "IRS_Formatted_Lightspeed_2025.csv")
