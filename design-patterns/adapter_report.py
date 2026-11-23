import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


# Legacy reporting system (can't modify - external library)
class LegacyReportGenerator:
    def generate_report(self, data: dict) -> str:
        """Returns XML format - old system"""
        xml = "<report>\n"
        for key, value in data.items():
            xml += f"  <{key}>{value}</{key}>\n"
        xml += "</report>"
        return xml


# New analytics dashboard expects JSON
class AnalyticsDashboard:
    def display(self, json_data: str):
        data = json.loads(json_data)
        print("=== Analytics Dashboard ===")
        for key, value in data.items():
            print(f"  {key}: {value}")


# 1. The interface the new tools expect: generate() returns JSON
class ReportGeneratorInterface(ABC):
    @abstractmethod
    def generate(self, data: dict) -> str:
        pass


# 2. The adapter: wraps the legacy system and converts XML -> JSON
class LegacyReportAdapter(ReportGeneratorInterface):
    def __init__(self, legacy_generator: LegacyReportGenerator):
        self._legacy = legacy_generator

    def generate(self, data: dict) -> str:
        xml_report = self._legacy.generate_report(data)   # old system makes XML
        return self._xml_to_json(xml_report)              # adapter translates it

    def _xml_to_json(self, xml_report: str) -> str:
        root = ET.fromstring(xml_report)
        result = {}
        for child in root:
            result[child.tag] = self._convert(child.text)
        return json.dumps(result)

    # XML stores everything as text: turn "1234" back into 1234, "121.55" into 121.55
    @staticmethod
    def _convert(text):
        if text is None:
            return None
        try:
            return int(text)
        except ValueError:
            try:
                return float(text)
            except ValueError:
                return text


# 3. Business logic: no conversion code here anymore
def show_sales_report(generator: ReportGeneratorInterface, dashboard: AnalyticsDashboard):
    report_data = {"total_sales": 150000, "orders": 1234, "avg_order": 121.55}
    dashboard.display(generator.generate(report_data))


def show_inventory_report(generator: ReportGeneratorInterface, dashboard: AnalyticsDashboard):
    report_data = {"total_items": 5000, "low_stock": 45, "out_of_stock": 12}
    dashboard.display(generator.generate(report_data))


if __name__ == "__main__":
    report_generator = LegacyReportAdapter(LegacyReportGenerator())
    dashboard = AnalyticsDashboard()

    show_sales_report(report_generator, dashboard)
    show_inventory_report(report_generator, dashboard)
