import unittest


class TestRobotMovement(unittest.TestCase):
    def setUp(self):
        self.world = World(5, 5)

    def test_robot_initialization(self):
        robot = Robot(1, 2, 'N', self.world)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 2)
        self.assertEqual(robot.direction, 'N')
        self.assertFalse(robot.lost)

    def test_turn_left(self):
        robot = Robot(1, 2, 'N', self.world)
        robot.execute_instruction('L')
        self.assertEqual(robot.direction, 'W')
        robot.execute_instruction('L')
        self.assertEqual(robot.direction, 'S')
        robot.execute_instruction('L')
        self.assertEqual(robot.direction, 'E')
        robot.execute_instruction('L')
        self.assertEqual(robot.direction, 'N')

    def test_turn_right(self):
        robot = Robot(1, 2, 'N', self.world)
        robot.execute_instruction('R')
        self.assertEqual(robot.direction, 'E')
        robot.execute_instruction('R')
        self.assertEqual(robot.direction, 'S')
        robot.execute_instruction('R')
        self.assertEqual(robot.direction, 'W')
        robot.execute_instruction('R')
        self.assertEqual(robot.direction, 'N')

    def test_move_forward_north(self):
        robot = Robot(1, 2, 'N', self.world)
        robot.execute_instruction('F')
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.direction, 'N')

    def test_move_forward_south(self):
        robot = Robot(1, 2, 'S', self.world)
        robot.execute_instruction('F')
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)

    def test_move_forward_east(self):
        robot = Robot(1, 2, 'E', self.world)
        robot.execute_instruction('F')
        self.assertEqual(robot.x, 2)
        self.assertEqual(robot.y, 2)

    def test_move_forward_west(self):
        robot = Robot(1, 2, 'W', self.world)
        robot.execute_instruction('F')
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 2)

    def test_robot_falls_off_north_boundary(self):
        robot = Robot(1, 4, 'N', self.world)
        robot.execute_instruction('F')
        self.assertTrue(robot.lost)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 4)
        self.assertIn((1, 4), self.world.scent_marks)

    def test_robot_falls_off_south_boundary(self):
        robot = Robot(1, 0, 'S', self.world)
        robot.execute_instruction('F')
        self.assertTrue(robot.lost)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 0)

    def test_robot_falls_off_east_boundary(self):
        robot = Robot(4, 2, 'E', self.world)
        robot.execute_instruction('F')
        self.assertTrue(robot.lost)
        self.assertEqual(robot.x, 4)
        self.assertEqual(robot.y, 2)

    def test_robot_falls_off_west_boundary(self):
        robot = Robot(0, 2, 'W', self.world)
        robot.execute_instruction('F')
        self.assertTrue(robot.lost)
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 2)

    def test_scent_mark_prevents_fall(self):
        robot1 = Robot(1, 4, 'N', self.world)
        robot1.execute_instruction('F')
        self.assertTrue(robot1.lost)

        robot2 = Robot(1, 4, 'N', self.world)
        robot2.execute_instruction('F')
        self.assertFalse(robot2.lost)
        self.assertEqual(robot2.x, 1)
        self.assertEqual(robot2.y, 4)
        self.assertEqual(robot2.direction, 'N')

    def test_execute_instruction_sequence(self):
        robot = Robot(1, 2, 'N', self.world)
        instructions = "LFRF"
        robot.execute_instructions(instructions)
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.direction, 'N')
        self.assertFalse(robot.lost)

    def test_robot_output_format(self):
        robot = Robot(1, 2, 'N', self.world)
        self.assertEqual(str(robot), "1 2 N")

        robot.lost = True
        self.assertEqual(str(robot), "1 2 N LOST")

    def test_multiple_robots(self):
        robot1 = Robot(1, 2, 'N', self.world)
        robot1.execute_instructions("F")
        self.assertEqual(robot1.x, 1)
        self.assertEqual(robot1.y, 3)

        robot2 = Robot(3, 3, 'E', self.world)
        robot2.execute_instructions("LF")
        self.assertEqual(robot2.x, 3)
        self.assertEqual(robot2.y, 2)
        self.assertEqual(robot2.direction, 'N')


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scent_marks = set()


class Robot:
    def __init__(self, x, y, direction, world):
        self.x = x
        self.y = y
        self.direction = direction
        self.world = world
        self.lost = False

    def execute_instruction(self, instruction):
        if self.lost:
            return

        if instruction == 'L':
            self._turn_left()
        elif instruction == 'R':
            self._turn_right()
        elif instruction == 'F':
            self._move_forward()

    def execute_instructions(self, instructions):
        for instr in instructions:
            self.execute_instruction(instr)

    def _turn_left(self):
        directions = ['N', 'W', 'S', 'E']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def _turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def _move_forward(self):
        dx, dy = self._get_direction_delta()
        new_x = self.x + dx
        new_y = self.y + dy

        if self._is_out_of_bounds(new_x, new_y):
            if (self.x, self.y) in self.world.scent_marks:
                return
            self.lost = True
            self.world.scent_marks.add((self.x, self.y))
        else:
            self.x = new_x
            self.y = new_y

    def _get_direction_delta(self):
        if self.direction == 'N':
            return 0, 1
        elif self.direction == 'S':
            return 0, -1
        elif self.direction == 'E':
            return 1, 0
        elif self.direction == 'W':
            return -1, 0

    def _is_out_of_bounds(self, x, y):
        return x < 0 or x > self.world.width or y < 0 or y > self.world.height

    def __str__(self):
        result = f"{self.x} {self.y} {self.direction}"
        if self.lost:
            result += " LOST"
        return result


if __name__ == '__main__':
    unittest.main()