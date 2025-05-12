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


if __name__ == "__main__":
    lead = TeamLead("Alice", 9000, "Development", "Python", 6)
    print(f"Name: {lead.name}")
    print(f"Salary: {lead.salary}")
    print(f"Department: {lead.department}")
    print(f"Language: {lead.programming_language}")
    print(f"Team Size: {lead.team_size}")
