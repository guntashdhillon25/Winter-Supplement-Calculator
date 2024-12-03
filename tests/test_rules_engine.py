import unittest
from app.rules_engine import calc_supplement

class TestRulesEngine(unittest.TestCase):

    def test_single_no_children(self):
        data = {
            "id": "test1",
            "numberOfChildren": 0,
            "familyComposition": "single",
            "familyUnitInPayForDecember": True
        }
        result = calc_supplement(data)
        self.assertEqual(result["baseAmount"], 60)
        self.assertEqual(result["childrenAmount"], 0)
        self.assertEqual(result["supplementAmount"], 60)

    def test_couple_no_children(self):
        data = {
            "id": "test2",
            "numberOfChildren": 0,
            "familyComposition": "couple",
            "familyUnitInPayForDecember": True
        }
        result = calc_supplement(data)
        self.assertEqual(result["baseAmount"], 120)
        self.assertEqual(result["childrenAmount"], 0)
        self.assertEqual(result["supplementAmount"], 120)

    def test_family_with_children(self):
        data = {
            "id": "test3",
            "numberOfChildren": 2,
            "familyComposition": "single",
            "familyUnitInPayForDecember": True
        }
        result = calc_supplement(data)
        self.assertEqual(result["baseAmount"], 120)
        self.assertEqual(result["childrenAmount"], 40)
        self.assertEqual(result["supplementAmount"], 160)

    def test_ineligibility(self):
        data = {
            "id": "test4",
            "numberOfChildren": 1,
            "familyComposition": "couple",
            "familyUnitInPayForDecember": False
        }
        result = calc_supplement(data)
        self.assertFalse(result["isEligible"])
        self.assertEqual(result["baseAmount"], 0)
        self.assertEqual(result["childrenAmount"], 0)
        self.assertEqual(result["supplementAmount"], 0)

if __name__ == "__main__":
    unittest.main()
