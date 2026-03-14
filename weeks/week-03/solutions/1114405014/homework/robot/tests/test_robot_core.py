import unittest

from robot_core import Robot, turn_left, turn_right, execute_command, execute_commands


class TestRobotCoreTurning(unittest.TestCase):
    def test_turn_left_from_north_should_face_west(self):
        self.assertEqual(turn_left("N"), "W")

    def test_turn_right_from_north_should_face_east(self):
        self.assertEqual(turn_right("N"), "E")

    def test_turn_right_four_times_should_return_to_original_direction(self):
        direction = "E"
        for _ in range(4):
            direction = turn_right(direction)
        self.assertEqual(direction, "E")

    def test_execute_command_l_should_only_change_direction(self):
        robot = Robot(1, 1, "N")
        scents = set()

        updated = execute_command(robot, "L", 5, 3, scents)

        self.assertEqual((updated.x, updated.y, updated.direction, updated.lost), (1, 1, "W", False))

    def test_execute_command_r_should_only_change_direction(self):
        robot = Robot(2, 2, "W")
        scents = set()

        updated = execute_command(robot, "R", 5, 3, scents)

        self.assertEqual((updated.x, updated.y, updated.direction, updated.lost), (2, 2, "N", False))


class TestRobotCoreMovement(unittest.TestCase):
    def test_forward_inside_grid_should_move_without_lost(self):
        robot = Robot(1, 1, "E")
        scents = set()

        updated = execute_command(robot, "F", 5, 3, scents)

        self.assertEqual((updated.x, updated.y, updated.direction, updated.lost), (2, 1, "E", False))
        self.assertEqual(scents, set())

    def test_forward_out_of_bounds_should_mark_robot_lost(self):
        robot = Robot(5, 3, "N")
        scents = set()

        updated = execute_command(robot, "F", 5, 3, scents)

        self.assertEqual((updated.x, updated.y, updated.direction, updated.lost), (5, 3, "N", True))
        self.assertIn((5, 3, "N"), scents)

    def test_lost_robot_should_not_execute_remaining_commands(self):
        robot = Robot(5, 3, "N")
        scents = set()

        updated = execute_commands(robot, "FFRFL", 5, 3, scents)

        self.assertEqual((updated.x, updated.y, updated.direction, updated.lost), (5, 3, "N", True))
        self.assertIn((5, 3, "N"), scents)

    def test_multiple_commands_should_follow_turn_and_move_rules(self):
        robot = Robot(1, 1, "N")
        scents = set()

        updated = execute_commands(robot, "RFRF", 5, 3, scents)

        self.assertEqual((updated.x, updated.y, updated.direction, updated.lost), (2, 0, "S", False))
        self.assertEqual(scents, set())


class TestRobotCoreValidation(unittest.TestCase):
    def test_invalid_single_command_should_raise_value_error(self):
        robot = Robot(1, 1, "N")
        scents = set()

        with self.assertRaises(ValueError):
            execute_command(robot, "X", 5, 3, scents)

    def test_invalid_command_in_command_sequence_should_raise_value_error(self):
        robot = Robot(1, 1, "N")
        scents = set()

        with self.assertRaises(ValueError):
            execute_commands(robot, "RFXL", 5, 3, scents)


if __name__ == "__main__":
    unittest.main()