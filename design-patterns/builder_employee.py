from dataclasses import dataclass
from typing import Optional


# 1. The product: a simple data container
@dataclass
class Employee:
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    department: str = ""
    position: str = ""
    salary: float = 0.0
    start_date: Optional[str] = None
    manager_id: Optional[int] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    emergency_contact: Optional[str] = None
    has_parking: bool = False
    has_laptop: bool = False
    has_vpn_access: bool = False
    has_admin_rights: bool = False
    office_location: Optional[str] = None
    contract_type: str = "permanent"


# 2. The builder: small methods, each returns self so they can be chained
class EmployeeBuilder:
    def __init__(self):
        self._employee = Employee()

    def with_name(self, first_name, last_name):
        self._employee.first_name = first_name
        self._employee.last_name = last_name
        return self

    def with_email(self, email):
        self._employee.email = email
        return self

    def with_job(self, department, position, salary):
        self._employee.department = department
        self._employee.position = position
        self._employee.salary = salary
        return self

    def with_start_date(self, start_date):
        self._employee.start_date = start_date
        return self

    def with_manager(self, manager_id):
        self._employee.manager_id = manager_id
        return self

    def with_contact(self, phone=None, address=None, emergency_contact=None):
        self._employee.phone = phone
        self._employee.address = address
        self._employee.emergency_contact = emergency_contact
        return self

    def with_equipment(self, laptop=False, parking=False):
        self._employee.has_laptop = laptop
        self._employee.has_parking = parking
        return self

    def with_access(self, vpn=False, admin=False):
        self._employee.has_vpn_access = vpn
        self._employee.has_admin_rights = admin
        return self

    def with_office(self, location):
        self._employee.office_location = location
        return self

    def with_contract(self, contract_type):
        self._employee.contract_type = contract_type
        return self

    # All validation in one place, checked before returning the employee
    def build(self):
        e = self._employee
        if not e.first_name or not e.last_name:
            raise ValueError("Name is required")
        if not e.email or "@" not in e.email:
            raise ValueError("Valid email is required")
        if e.salary < 0:
            raise ValueError("Salary cannot be negative")
        return e


# 3. Presets: a senior developer ALWAYS gets laptop, VPN and admin rights
class DeveloperBuilder(EmployeeBuilder):
    def __init__(self, first_name, last_name, email):
        super().__init__()
        (self.with_name(first_name, last_name)
             .with_email(email)
             .with_job("Engineering", "Senior Developer", 75000)
             .with_equipment(laptop=True)
             .with_access(vpn=True, admin=True)
             .with_office("Paris HQ"))


class InternBuilder(EmployeeBuilder):
    def __init__(self, first_name, last_name, email, department):
        super().__init__()
        (self.with_name(first_name, last_name)
             .with_email(email)
             .with_job(department, "Intern", 15000)
             .with_equipment(laptop=True)
             .with_office("Paris HQ")
             .with_contract("internship"))


if __name__ == "__main__":
    # Fluent, readable creation
    employee = (
        EmployeeBuilder()
        .with_name("John", "Doe")
        .with_email("john.doe@company.com")
        .with_job("Engineering", "Senior Developer", 75000)
        .with_equipment(laptop=True, parking=False)
        .with_access(vpn=True, admin=True)
        .build()
    )
    print(employee)
    print()

    # Using presets
    dev = DeveloperBuilder("John", "Doe", "john.doe@company.com").build()
    print(dev)
    print()

    # A preset can still be customized before build()
    intern = (
        InternBuilder("Jane", "Smith", "jane.smith@company.com", "Marketing")
        .with_manager(42)
        .with_start_date("2024-02-01")
        .build()
    )
    print(intern)
