class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size


def test_teamlead_attributes():
    lead = TeamLead("Alice", 9000, "Development", "Python", 6)

    assert hasattr(lead, "name"), "Missing attribute: name"
    assert hasattr(lead, "salary"), "Missing attribute: salary"
    assert hasattr(lead, "department"), "Missing attribute: department (from Manager)"
    assert hasattr(lead, "programming_language"), "Missing attribute: programming_language (from Developer)"
    assert hasattr(lead, "team_size"), "Missing attribute: team_size (TeamLead specific)"

    print("All attribute tests passed!")


if __name__ == "__main__":
    test_teamlead_attributes()

