import csv

def csv_to_insert(csv_file, table_name, output_file=None):
    """
    Generate INSERT statements from a CSV file
    
    Args:
        csv_file: Path to the CSV file
        table_name: Name of the database table
        output_file: Optional output file path (if None, prints to console)
    """
    insert_statements = []
    
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        columns = ', '.join([f"['{h}']" for h in headers])
        
        for row_num, row in enumerate(reader, start=2):  # start=2 because headers are row 1
            try:
                # Handle NULL values and escape single quotes
                values = []
                for value in row:
                    if value == '' or value.upper() == 'NULL':
                        values.append('NULL')
                    else:
                        # Escape single quotes and wrap in quotes
                        escaped_value = value.replace("'", "''")
                        values.append(f"'{escaped_value}'")
                
                values_str = ', '.join(values)
                insert_stmt = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});"
                insert_statements.append(insert_stmt)
                
            except Exception as e:
                print(f"Error processing row {row_num}: {e}")
                continue
    
    # Output results
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            for stmt in insert_statements:
                f.write(stmt + '\n')
        print(f"Generated {len(insert_statements)} INSERT statements and saved to {output_file}")
    else:
        for stmt in insert_statements:
            print(stmt)
        print(f"\nGenerated {len(insert_statements)} INSERT statements")

# Usage examples:
if __name__ == "__main__":
    # Example 1: Print to console
    # csv_to_insert('vendor_master.csv', 'vendor_master')
    
    # Example 2: Save to file
    csv_to_insert('vendor_master.csv', 'vendor_master', 'insert_statements.sql')