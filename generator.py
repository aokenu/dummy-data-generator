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