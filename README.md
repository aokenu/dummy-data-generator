# dummy-data-generator
Dummy Data Generator is a Python-based tool designed to help data professionals create realistic synthetic datasets without relying on sensitive or production data.
It provides flexible utilities for generating structured, domain-specific dummy records — with a strong focus on fintech payment data.

🔒 Why This Project Matters

Organizations increasingly operate under strict data protection regulations such as NDPA, GDPR, and DPA. These frameworks prohibit the use of live or personally identifiable information for testing, development, training, and demonstrations.
This project solves that challenge by offering a safe, configurable way to generate high-quality synthetic datasets that mimic real-world patterns while containing no actual user data.

🎯 Key Features

Fully synthetic, regulation-compliant datasets

Realistic fintech-style payment events

Customizable providers (currencies, payment methods, merchant categories, timestamps, etc.)

Easy integration with analytics workflows, data pipelines, or ML model testing

Fast generation of large datasets (CSV, DataFrame, or custom formats)

🛠️ Technologies

Python

Faker library

Pandas

Randomization + custom logic for fintech realism

🚀 Use Cases

Testing ETL/ELT pipelines

Mocking payment systems

Teaching and demos

Data modeling and schema validation

Experimenting with analytics or dashboards

Building prototypes without touching real data

🧪 Example Output

Transactional-style payment records with fields like:
transaction_id, user_id, timestamp, amount, currency,
payment_method, merchant_category, status, country, and more.
