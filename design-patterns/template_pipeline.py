import time
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class DataPipeline(ABC):
    name = "Generic"         # e.g. "CSV"
    source_label = "source"  # e.g. "CSV file"
    required_fields = []     # every record must have these keys

    def __init__(self, source):
        self.source = source
        self.data = None

    # ===== TEMPLATE METHOD: the workflow, defined ONCE =====
    # Subclasses should not override run()
    def run(self):
        self.before_run()    # hook
        self.connect()
        self.extract()
        self.transform()
        self.validate()
        self.load()
        self.cleanup()
        self.after_run()     # hook
        return f"{self.name} Pipeline finished"

    # ===== Common steps: implemented once for everyone =====
    def connect(self):
        print(f"Connecting to {self.source_label}: {self.source}")
        time.sleep(0.5)
        print(f"{self.name} connection established")

    def extract(self):
        print(f"Extracting data from {self.name}...")
        self.data = self.extract_records()
        print(f"Extracted {len(self.data)} records")

    def transform(self):
        print(f"Transforming {self.name} data...")
        for record in self.data:
            self.transform_record(record)
        print("Transformation complete")

    def validate(self):
        print("Validating data...")
        for record in self.data:
            for field in self.required_fields:
                if field not in record:
                    raise ValueError(f"Invalid record structure: missing '{field}'")
        print("Validation passed")

    def load(self):
        print("Loading data to destination...")
        time.sleep(0.5)
        print(f"Loaded {len(self.data)} records successfully")

    def cleanup(self):
        print("Cleaning up resources...")
        self.data = None
        print("Cleanup complete")

    # ===== Abstract steps: each pipeline MUST implement these =====
    @abstractmethod
    def extract_records(self) -> list:
        pass

    @abstractmethod
    def transform_record(self, record: dict):
        pass

    # ===== Hooks: optional, do nothing by default =====
    def before_run(self):
        pass

    def after_run(self):
        pass


# ===== Concrete pipelines: only what's unique =====
class CSVPipeline(DataPipeline):
    name = "CSV"
    source_label = "CSV file"
    required_fields = ["id", "name"]

    def extract_records(self):
        return [
            {"id": 1, "name": "Alice", "age": 30},
            {"id": 2, "name": "Bob", "age": 25},
        ]

    def transform_record(self, record):
        record["age"] = int(record["age"])
        record["name"] = record["name"].upper()


class APIPipeline(DataPipeline):
    name = "API"
    source_label = "API"
    required_fields = ["user_id", "username"]

    def extract_records(self):
        return [
            {"user_id": 101, "username": "charlie", "score": 85},
            {"user_id": 102, "username": "diana", "score": 92},
        ]

    def transform_record(self, record):
        record["score"] = int(record["score"])
        record["username"] = record["username"].lower()
        record["grade"] = "A" if record["score"] >= 90 else "B"


class DatabasePipeline(DataPipeline):
    name = "Database"
    source_label = "database"
    required_fields = ["product_id", "price"]

    def extract_records(self):
        return [
            {"product_id": 501, "product_name": "Laptop", "price": 1200},
            {"product_id": 502, "product_name": "Mouse", "price": 25},
        ]

    def transform_record(self, record):
        record["price"] = float(record["price"])
        record["product_name"] = record["product_name"].title()
        record["tax"] = record["price"] * 0.2


# NEW: XML pipeline, same workflow, only XML-specific parts written
class XMLPipeline(DataPipeline):
    name = "XML"
    source_label = "XML file"
    required_fields = ["order_id", "customer"]

    # Simulates the content of data/orders.xml
    XML_CONTENT = """<orders>
    <order><order_id>9001</order_id><customer>emma</customer><amount>49.90</amount></order>
    <order><order_id>9002</order_id><customer>lucas</customer><amount>120.00</amount></order>
</orders>"""

    def extract_records(self):
        root = ET.fromstring(self.XML_CONTENT)
        return [{child.tag: child.text for child in order} for order in root]

    def transform_record(self, record):
        record["order_id"] = int(record["order_id"])
        record["customer"] = record["customer"].capitalize()
        record["amount"] = float(record["amount"])
        record["is_large_order"] = record["amount"] > 100

    # Hook example: extra step only for this pipeline
    def after_run(self):
        print(f"[hook] XML pipeline archived source file: {self.source}")


if __name__ == "__main__":
    print("RUNNING CSV PIPELINE")
    print("=" * 70)
    result = CSVPipeline("data/users.csv").run()
    print(f"\n{result}\n")

    print("RUNNING API PIPELINE")
    print("=" * 70)
    result = APIPipeline("https://api.example.com/users").run()
    print(f"\n{result}\n")

    print("RUNNING DATABASE PIPELINE")
    print("=" * 70)
    result = DatabasePipeline("postgresql://localhost/mydb").run()
    print(f"\n{result}\n")

    print("RUNNING XML PIPELINE (NEW!)")
    print("=" * 70)
    result = XMLPipeline("data/orders.xml").run()
    print(f"\n{result}\n")
