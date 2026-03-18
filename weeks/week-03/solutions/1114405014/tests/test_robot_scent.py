import unittest

from robot_core import Robot, execute_command, execute_commands


class TestRobotScent(unittest.TestCase):
    def test_first_robot_falling_off_should_leave_scent(self):
        robot = Robot(5, 3, "N")
        scents = set()

        updated = execute_command(robot, "F", 5, 3, scents)

        self.assertTrue(updated.lost)
        self.assertEqual((updated.x, updated.y, updated.direction), (5, 3, "N"))
        self.assertIn((5, 3, "N"), scents)

    def test_second_robot_same_position_and_direction_should_ignore_dangerous_forward(self):
        scents = {(5, 3, "N")}
        robot = Robot(5, 3, "N")

        updated = execute_command(robot, "F", 5, 3, scents)

        self.assertFalse(updated.lost)
        self.assertEqual((updated.x, updated.y, updated.direction), (5, 3, "N"))
        self.assertEqual(scents, {(5, 3, "N")})

    def test_same_position_but_different_direction_should_not_share_scent(self):
        scents = {(5, 3, "N")}
        robot = Robot(5, 3, "E")

        updated = execute_command(robot, "F", 5, 3, scents)

        self.assertTrue(updated.lost)
        self.assertEqual((updated.x, updated.y, updated.direction), (5, 3, "E"))
        self.assertIn((5, 3, "N"), scents)
        self.assertIn((5, 3, "E"), scents)

    def test_same_position_same_direction_with_scent_should_continue_to_next_command(self):
        scents = {(5, 3, "N")}
        robot = Robot(5, 3, "N")

        updated = execute_commands(robot, "LFF", 5, 3, scents)

        self.assertFalse(updated.lost)
        self.assertEqual((updated.x, updated.y, updated.direction), (3, 3, "W"))

    def test_scent_should_be_based_on_last_safe_position_and_current_direction(self):
        robot = Robot(0, 0, "S")
        scents = set()

        updated = execute_command(robot, "F", 5, 3, scents)

        self.assertTrue(updated.lost)
        self.assertEqual((updated.x, updated.y, updated.direction), (0, 0, "S"))
        self.assertIn((0, 0, "S"), scents)

    def test_robot_should_move_normally_when_forward_is_not_out_of_bounds_even_if_other_scents_exist(self):
        scents = {(5, 3, "N"), (0, 0, "S")}
        robot = Robot(1, 1, "E")

        updated = execute_command(robot, "F", 5, 3, scents)

        self.assertFalse(updated.lost)
        self.assertEqual((updated.x, updated.y, updated.direction), (2, 1, "E"))
        self.assertEqual(scents, {(5, 3, "N"), (0, 0, "S")})

    def test_repeated_dangerous_forward_with_existing_scent_should_not_create_duplicate_entries(self):
        scents = {(5, 3, "N")}
        robot = Robot(5, 3, "N")

        first = execute_command(robot, "F", 5, 3, scents)
        second = execute_command(first, "F", 5, 3, scents)

        self.assertFalse(first.lost)
        self.assertFalse(second.lost)
        self.assertEqual(len(scents), 1)
        self.assertIn((5, 3, "N"), scents)


if __name__ == "__main__":
    unittest.main()