import unittest
from pathlib import Path
from task2_zipcode_heatmap import zip_to_county, load_county_counts, get_top_counties


DATA_DIR = Path(__file__).parent.parent.parent.parent.parent.parent / "assets" / "stu-data"
YEARS = [109, 110, 111, 112, 113, 114]


class TestZipToCounty(unittest.TestCase):

    def test_zip_to_county_penghu(self):
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self):
        self.assertEqual(zip_to_county("999"), "其他")


class TestLoadCountyCounts(unittest.TestCase):

    def test_load_county_counts_type(self):
        result = load_county_counts(112, DATA_DIR)
        self.assertIsInstance(result, dict)

    def test_load_county_counts_penghu_positive(self):
        result = load_county_counts(112, DATA_DIR)
        penghu_count = result.get("澎湖縣", 0)
        self.assertGreater(penghu_count, 0)


class TestGetTopCounties(unittest.TestCase):

    def setUp(self):
        self.all_years = {y: load_county_counts(y, DATA_DIR) for y in YEARS}

    def test_get_top_counties_length(self):
        result = get_top_counties(self.all_years, top_n=10)
        self.assertLessEqual(len(result), 10)


if __name__ == "__main__":
    unittest.main()
