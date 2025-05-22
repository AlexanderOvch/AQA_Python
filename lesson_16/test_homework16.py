import unittest
from homework16_01 import TeamLead


class TestTeamLeadAttributes(unittest.TestCase):
    def setUp(self):
        self.lead = TeamLead("Alice", 9000, "Development", "Python", 6)

    def test_name_attribute(self):
        self.assertTrue(hasattr(self.lead, "name"))

    def test_salary_attribute(self):
        self.assertTrue(hasattr(self.lead, "salary"))

    def test_department_attribute(self):
        self.assertTrue(hasattr(self.lead, "department"))

    def test_programming_language_attribute(self):
        self.assertTrue(hasattr(self.lead, "programming_language"))

    def test_team_size_attribute(self):
        self.assertTrue(hasattr(self.lead, "team_size"))


if __name__ == "__main__":
    unittest.main()
