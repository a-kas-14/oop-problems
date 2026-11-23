import json
from abc import ABC, abstractmethod


# 1. Strategy interface: the contract every format must follow
class ReportFormatStrategy(ABC):
    @abstractmethod
    def format(self, data: list) -> str:
        pass

    @abstractmethod
    def get_extension(self) -> str:
        pass


# 2. Concrete strategies: one class per format
class PDFFormatStrategy(ReportFormatStrategy):
    def format(self, data):
        report = "PDF REPORT\n"
        report += "=" * 50 + "\n"
        for item in data:
            report += f"| {item['name']:20} | {item['value']:10} |\n"
        report += "=" * 50 + "\n"
        report += "End of PDF Report"
        return report

    def get_extension(self):
        return ".pdf"


class ExcelFormatStrategy(ReportFormatStrategy):
    def format(self, data):
        report = "EXCEL REPORT\n"
        report += "-" * 50 + "\n"
        report += "Name\tValue\n"
        for item in data:
            report += f"{item['name']}\t{item['value']}\n"
        report += "-" * 50 + "\n"
        return report

    def get_extension(self):
        return ".xlsx"


class CSVFormatStrategy(ReportFormatStrategy):
    def format(self, data):
        report = "name,value\n"
        for item in data:
            report += f"{item['name']},{item['value']}\n"
        return report

    def get_extension(self):
        return ".csv"


class JSONFormatStrategy(ReportFormatStrategy):
    def format(self, data):
        return json.dumps(data, indent=2)

    def get_extension(self):
        return ".json"


# 3. Context: uses whatever strategy it is given
class ReportGenerator:
    def __init__(self, data, strategy=None):
        self.data = data
        self._strategy = strategy

    def set_strategy(self, strategy: ReportFormatStrategy):
        self._strategy = strategy

    def generate_report(self) -> str:
        if self._strategy is None:
            raise ValueError("No format strategy set. Call set_strategy() first.")
        return self._strategy.format(self.data)

    def save_report(self, filename: str) -> str:
        content = self.generate_report()
        path = filename + self._strategy.get_extension()
        with open(path, "w") as f:
            f.write(content)
        print(f"Report saved to {path}")
        return path


# NEW: HTML format added WITHOUT modifying any code above
class HTMLFormatStrategy(ReportFormatStrategy):
    def format(self, data):
        rows = "\n".join(
            f"    <tr><td>{item['name']}</td><td>{item['value']}</td></tr>"
            for item in data
        )
        return (
            "<html>\n<body>\n<h1>Report</h1>\n<table>\n"
            "    <tr><th>Name</th><th>Value</th></tr>\n"
            f"{rows}\n"
            "</table>\n</body>\n</html>"
        )

    def get_extension(self):
        return ".html"


if __name__ == "__main__":
    data = [
        {"name": "Sales Q1", "value": 15000},
        {"name": "Sales Q2", "value": 18000},
        {"name": "Sales Q3", "value": 22000},
        {"name": "Sales Q4", "value": 25000},
    ]

    generator = ReportGenerator(data)

    print("=== PDF FORMAT ===")
    generator.set_strategy(PDFFormatStrategy())
    print(generator.generate_report())

    print("\n" + "=" * 60 + "\n")

    # Switch to CSV format dynamically
    print("=== CSV FORMAT ===")
    generator.set_strategy(CSVFormatStrategy())
    print(generator.generate_report())

    print("\n" + "=" * 60 + "\n")

    print("=== JSON FORMAT ===")
    generator.set_strategy(JSONFormatStrategy())
    print(generator.generate_report())

    print("\n" + "=" * 60 + "\n")

    print("=== HTML FORMAT (NEW!) ===")
    generator.set_strategy(HTMLFormatStrategy())
    print(generator.generate_report())

    print("\n" + "=" * 60 + "\n")

    generator.set_strategy(CSVFormatStrategy())
    generator.save_report("sales_report")
