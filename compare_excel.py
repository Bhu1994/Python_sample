import pandas as pd

# === Step 1: Load both Excel files ===
file1_path = r"C:\Users\bhush\OneDrive\Desktop\Python\file1.xlsx"
file2_path = r"C:\Users\bhush\OneDrive\Desktop\Python\file2.xlsx"


# Load all sheets from both files
file1_sheets = pd.read_excel(file1_path, sheet_name=None, engine='openpyxl')
file2_sheets = pd.read_excel(file2_path, sheet_name=None, engine='openpyxl')

# === Step 2: Compare matching sheets ===
overall_mismatch_found = False  # Track any mismatch in all sheets

for i, (sheet1_name, df1) in enumerate(file1_sheets.items()):
    # Get corresponding sheet in file2 by index
    sheet2_name = list(file2_sheets.keys())[i]
    df2 = file2_sheets[sheet2_name]

    print(f"\n🔍 Comparing Sheet {i+1}: '{sheet1_name}' (file1) with '{sheet2_name}' (file2)")

    # Reset index and ignore headers
    df1 = df1.reset_index(drop=True)
    df2 = df2.reset_index(drop=True)

    max_rows = max(len(df1), len(df2))
    max_cols = max(len(df1.columns), len(df2.columns))

    sheet_mismatch_found = False

    for row in range(max_rows):
        for col in range(max_cols):
            val1 = df1.iloc[row, col] if row < len(df1) and col < len(df1.columns) else None
            val2 = df2.iloc[row, col] if row < len(df2) and col < len(df2.columns) else None

            if pd.isna(val1) and pd.isna(val2):
                continue  # Both are NaN, treat as same

            if val1 != val2:
                print(f"   Mismatch at Row {row+1}, Column {col+1}: File1 = '{val1}', File2 = '{val2}'")
                sheet_mismatch_found = True
                overall_mismatch_found = True

    if not sheet_mismatch_found:
        print("  ✅ No mismatches found in this sheet.")

# === Final Result ===
if not overall_mismatch_found:
    print("\n All sheets matched. All good.")


