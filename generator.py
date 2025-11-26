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