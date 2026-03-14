import unittest

from task3_log_summary import solve


class TestTask3LogSummary(unittest.TestCase):
    def test_sample_case(self):
        input_text = "\n".join([
            "8",
            "alice login",
            "bob login",
            "alice view",
            "alice logout",
            "bob view",
            "bob view",
            "chris login",
            "bob logout",
        ])
        expected = "\n".join([
            "bob 4",
            "alice 3",
            "chris 1",
            "top_action: login 3",
        ])
        self.assertEqual(solve(input_text), expected)

    def test_user_count_tie_sorted_by_name(self):
        input_text = "\n".join([
            "4",
            "bob login",
            "alice view",
            "bob logout",
            "alice logout",
        ])
        expected = "\n".join([
            "alice 2",
            "bob 2",
            "top_action: logout 2",
        ])
        self.assertEqual(solve(input_text), expected)

    def test_action_tie_sorted_by_action_name(self):
        input_text = "\n".join([
            "4",
            "alice view",
            "bob login",
            "chris view",
            "dora login",
        ])
        expected = "\n".join([
            "alice 1",
            "bob 1",
            "chris 1",
            "dora 1",
            "top_action: login 2",
        ])
        self.assertEqual(solve(input_text), expected)

    def test_empty_logs(self):
        input_text = "0"
        expected = "top_action: None 0"
        self.assertEqual(solve(input_text), expected)

    def test_single_user_multiple_actions(self):
        input_text = "\n".join([
            "5",
            "alice login",
            "alice view",
            "alice view",
            "alice logout",
            "alice login",
        ])
        expected = "\n".join([
            "alice 5",
            "top_action: login 2",
        ])
        self.assertEqual(solve(input_text), expected)


if __name__ == "__main__":
    unittest.main()