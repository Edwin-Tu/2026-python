import unittest
from pathlib import Path
from task1_grouped_bar import load_year, get_top_depts


DATA_DIR = Path(__file__).parent.parent.parent.parent.parent.parent / "assets" / "stu-data"
YEARS = [112, 113, 114]


class TestLoadYear(unittest.TestCase):

    def test_load_year_returns_dict(self):
        result = load_year(112, DATA_DIR)
        self.assertIsInstance(result, dict)
        if result:
            key = next(iter(result))
            self.assertIsInstance(key, str)

    def test_load_year_counts_correct(self):
        dept_counts = load_year(114, DATA_DIR)
        known_dept = "應用外語系"
        count = dept_counts.get(known_dept, 0)
        self.assertGreater(count, 0)

    def test_load_year_total_positive(self):
        dept_counts = load_year(112, DATA_DIR)
        total = sum(dept_counts.values())
        self.assertGreater(total, 0)


class TestGetTopDepts(unittest.TestCase):

    def setUp(self):
        self.year_data = {y: load_year(y, DATA_DIR) for y in YEARS}

    def test_get_top_depts_length(self):
        result = get_top_depts(self.year_data, top_n=8)
        self.assertLessEqual(len(result), 8)

    def test_get_top_depts_includes_popular(self):
        result = get_top_depts(self.year_data, top_n=8)
        known_popular = "資訊工程系"
        self.assertIn(known_popular, result)


if __name__ == "__main__":
    unittest.main()
