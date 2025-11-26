import pandas as pd
from faker import Faker
import random
import json
import yaml
import os


# Initialize Faker
fake = Faker()


def load_schema(file_path):
    """Load schema from json or yaml file."""
    _, ext = os.path.splitext(file_path)
    with open(file_path, "r") as f:
        if ext.lower() == ".json":
            return json.load(f)
        elif ext.lower() in [".yml", ".yaml"]:
            return yaml.safe_load(f)
        else:
            raise ValueError("Unsupported schema format. Use JSON or YAML.")


def generate_dummy_data_from_schema(schema):
    """Generate dummy data based on schema definition."""
    table_name = schema.get("table_name", "dummy_table")
    num_rows = schema.get("rows", 10)
    columns = schema.get("columns", [])

    records = []
    for _ in range(num_rows):
        row = {}
        for col in columns:
            col_name = col["name"]
            col_type = col["type"].lower()

            if col_type == "name":
                row[col_name] = fake.name()
            elif col_type == "email":
                row[col_name] = fake.email()
            elif col_type == "company":
                row[col_name] = fake.company()
            elif col_type == "integer":
                row[col_name] = random.ran
                dint(col.get("min", 0), col.get("max", 100))
            elif col_type == "float":
                row[col_name] = round(
                    random.uniform(col.get("min", 0.0), col.get("max", 100.0)),
                    col.get("decimals", 2),
                )
            elif col_type == "date":
                row[col_name] = fake.date_this_year()
            elif col_type == "text":
                row[col_name] = fake.sentence()
            elif col_type == "choice":
                options = col.get("options", [])
                if options:
                    row[col_name] = random.choice(options)
                else:
                    row[col_name] = "[No options provided]"
            else:
                row[col_name] = f"[Unsupported type: {col_type}]"
        records.append(row)

    
    df = pd.DataFrame(records)
    filename = f"{table_name}.csv"
    df.to_csv(filename, index=False)
    print(f"\n✅ Dummy dataset generated and saved as '{filename}'")
    print(df.head())
                

if __name__ == "__main__":
    schema_file = input("Enter schema file path (JSON or YAML): ").strip()
    schema = load_schema(schema_file)
