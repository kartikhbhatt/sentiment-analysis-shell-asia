import csv
from datetime import datetime

# Indices for each type based on your schema
int_indices = [0]
bigint_indices = [5, 6, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 28]
date_indices = [7, 8, 14]
str_indices = [1, 2, 3, 4, 9, 11, 15, 16, 18, 19, 20, 21, 23, 25, 26, 27, 29, 30]

def clean(val, idx):
    val = val.strip().strip('"').strip("'")
    if val in ('', '-', ' -   '):
        return "NULL"
    if idx in date_indices:
        try:
            val = datetime.strptime(val, "%d-%m-%Y").strftime("%Y-%m-%d")
            return f"'{val}'"
        except Exception:
            return "NULL"
    if idx in int_indices or idx in bigint_indices:
        val = val.replace(",", "").replace(" ", "")
        if "." in val:
            val = val.split(".")[0]
        if not val.isdigit():
            return "NULL"
        return val
    val = val.replace("'", "''")
    return f"N'{val}'" if idx in str_indices else f"'{val}'"

with open('GSAP List of Vendors and Vendor Info.csv', encoding='utf-8-sig') as f, \
     open('insert_statements.sql', 'w', encoding='utf-8') as out:
    reader = csv.reader(f)
    headers = next(reader)
    while True:
        row = next(reader)
        if any(row):
            break

    column_names = ", ".join([h.strip().replace(" ", "_").replace("-", "_").replace("/", "_") for h in headers[:31]])

    # Write the first insert
    values = "(" + ", ".join([clean(v, i) for i, v in enumerate(row[:31])]) + ")"
    out.write(f"INSERT INTO vendors_master ({column_names}) VALUES {values};\n")

    # Write the rest
    for row in reader:
        if not any(row):
            continue
        values = "(" + ", ".join([clean(v, i) for i, v in enumerate(row[:31])]) + ")"
        out.write(f"INSERT INTO vendors_master ({column_names}) VALUES {values};\n")








# import csv
# from datetime import datetime

# # Indices for each type based on your schema
# int_indices = [0]
# bigint_indices = [5, 6, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
# date_indices = [7, 8]
# str_indices = [1, 2, 3, 4, 9, 11]

# def clean(val, idx):
#     val = val.strip().strip('"').strip("'")
#     if val in ('', '-', ' -   '):
#         return "NULL"
#     if idx in date_indices:
#         try:
#             val = datetime.strptime(val, "%d-%m-%Y").strftime("%Y-%m-%d")
#             return f"'{val}'"
#         except Exception:
#             return "NULL"
#     if idx in int_indices or idx in bigint_indices:
#         # Remove commas, decimals, and spaces
#         val = val.replace(",", "").replace(" ", "")
#         if "." in val:
#             val = val.split(".")[0]
#         # Handle empty after cleaning
#         if not val.isdigit():
#             return "NULL"
#         return val
#     # Strings
#     val = val.replace("'", "''")  # Escape single quotes for SQL
#     return f"N'{val}'" if idx in str_indices else f"'{val}'"

# with open('GSAP List of Vendors and Vendor Info v31.csv', encoding='utf-8-sig') as f, \
#      open('insert_statements.sql', 'w', encoding='utf-8') as out:
#     reader = csv.reader(f)
#     headers = next(reader)
#     # Skip empty line if present
#     while True:
#         row = next(reader)
#         if any(row):
#             break

#     out.write("INSERT INTO vendors (\n")
#     out.write(", ".join([h.strip().replace(" ", "_").replace("-", "_") for h in headers[:24]]))
#     out.write(")\nVALUES\n")

#     values = []
#     values.append("(" + ", ".join([clean(v, i) for i, v in enumerate(row[:24])]) + ")")

#     for row in reader:
#         if not any(row):
#             continue
#         values.append("(" + ", ".join([clean(v, i) for i, v in enumerate(row[:24])]) + ")")

#     out.write(",\n".join(values) + ";\n")
