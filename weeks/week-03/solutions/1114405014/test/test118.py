import unittest

# 測試驅動開發 (TDD) 策略：
# 1. 紅燈階段：先寫測試，讓測試失敗
# 2. 綠燈階段：實現功能，讓測試通過
# 3. 重構階段：優化代碼，保持測試通過

class TestRobotMovement(unittest.TestCase):
    """
    測試機器人在矩形土地上的移動
    根據題目 UVA 118，處理指令 L、R、F，考慮邊界和標記
    """

    def setUp(self):
        """設置測試環境"""
        # 創建一個 5x5 的土地作為測試環境
        self.world = World(5, 5)

    def test_robot_initialization(self):
        """測試機器人初始化位置和方向"""
        robot = Robot(1, 2, 'N', self.world)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 2)
        self.assertEqual(robot.direction, 'N')
        self.assertFalse(robot.lost)

    def test_turn_left(self):
        """測試左轉指令 L"""
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
        """測試右轉指令 R"""
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
        """測試向前移動 F，面向北方"""
        robot = Robot(1, 2, 'N', self.world)
        robot.execute_instruction('F')
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.direction, 'N')

    def test_move_forward_south(self):
        """測試向前移動 F，面向南方"""
        robot = Robot(1, 2, 'S', self.world)
        robot.execute_instruction('F')
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)

    def test_move_forward_east(self):
        """測試向前移動 F，面向東方"""
        robot = Robot(1, 2, 'E', self.world)
        robot.execute_instruction('F')
        self.assertEqual(robot.x, 2)
        self.assertEqual(robot.y, 2)

    def test_move_forward_west(self):
        """測試向前移動 F，面向西方"""
        robot = Robot(1, 2, 'W', self.world)
        robot.execute_instruction('F')
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 2)

    def test_robot_falls_off_north_boundary(self):
        """測試機器人從北邊界掉落"""
        robot = Robot(1, 4, 'N', self.world)  # y=4 是北邊界
        robot.execute_instruction('F')
        self.assertTrue(robot.lost)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 4)  # 掉落前的位置
        # 檢查標記是否留下
        self.assertIn((1, 4), self.world.scent_marks)

    def test_robot_falls_off_south_boundary(self):
        """測試機器人從南邊界掉落"""
        robot = Robot(1, 0, 'S', self.world)
        robot.execute_instruction('F')
        self.assertTrue(robot.lost)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 0)

    def test_robot_falls_off_east_boundary(self):
        """測試機器人從東邊界掉落"""
        robot = Robot(4, 2, 'E', self.world)
        robot.execute_instruction('F')
        self.assertTrue(robot.lost)
        self.assertEqual(robot.x, 4)
        self.assertEqual(robot.y, 2)

    def test_robot_falls_off_west_boundary(self):
        """測試機器人從西邊界掉落"""
        robot = Robot(0, 2, 'W', self.world)
        robot.execute_instruction('F')
        self.assertTrue(robot.lost)
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 2)

    def test_scent_mark_prevents_fall(self):
        """測試標記防止機器人掉落"""
        # 先讓一個機器人掉落，留下標記
        robot1 = Robot(1, 4, 'N', self.world)
        robot1.execute_instruction('F')  # 掉落，留下標記 (1,4)
        self.assertTrue(robot1.lost)

        # 第二個機器人在同位置，嘗試前進
        robot2 = Robot(1, 4, 'N', self.world)
        robot2.execute_instruction('F')  # 應該忽略，因為有標記
        self.assertFalse(robot2.lost)
        self.assertEqual(robot2.x, 1)
        self.assertEqual(robot2.y, 4)
        self.assertEqual(robot2.direction, 'N')

    def test_execute_instruction_sequence(self):
        """測試執行一連串指令"""
        robot = Robot(1, 2, 'N', self.world)
        instructions = "LFRF"
        robot.execute_instructions(instructions)
        # L: W, F: (0,2), R: N, F: (0,3)
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.direction, 'N')
        self.assertFalse(robot.lost)

    def test_robot_output_format(self):
        """測試機器人輸出格式"""
        robot = Robot(1, 2, 'N', self.world)
        self.assertEqual(str(robot), "1 2 N")

        robot.lost = True
        self.assertEqual(str(robot), "1 2 N LOST")

    def test_multiple_robots(self):
        """測試多個機器人依序動作"""
        # 第一個機器人
        robot1 = Robot(1, 2, 'N', self.world)
        robot1.execute_instructions("F")
        self.assertEqual(robot1.x, 1)
        self.assertEqual(robot1.y, 3)

        # 第二個機器人
        robot2 = Robot(3, 3, 'E', self.world)
        robot2.execute_instructions("LF")
        self.assertEqual(robot2.x, 3)
        self.assertEqual(robot2.y, 2)
        self.assertEqual(robot2.direction, 'N')

# 以下是實現類別（在 TDD 中，這部分應該在測試通過後添加）
# 但為了完整性，先提供基本實現

class World:
    """代表矩形土地的世界"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scent_marks = set()  # 標記集合，儲存 (x, y) 座標

class Robot:
    """代表機器人"""
    def __init__(self, x, y, direction, world):
        self.x = x
        self.y = y
        self.direction = direction
        self.world = world
        self.lost = False

    def execute_instruction(self, instruction):
        """執行單個指令"""
        if self.lost:
            return

        if instruction == 'L':
            self._turn_left()
        elif instruction == 'R':
            self._turn_right()
        elif instruction == 'F':
            self._move_forward()

    def execute_instructions(self, instructions):
        """執行一連串指令"""
        for instr in instructions:
            self.execute_instruction(instr)

    def _turn_left(self):
        """左轉 90 度"""
        directions = ['N', 'W', 'S', 'E']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def _turn_right(self):
        """右轉 90 度"""
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def _move_forward(self):
        """向前移動一格"""
        dx, dy = self._get_direction_delta()
        new_x = self.x + dx
        new_y = self.y + dy

        # 檢查是否會掉落
        if self._is_out_of_bounds(new_x, new_y):
            # 如果有標記，忽略指令
            if (self.x, self.y) in self.world.scent_marks:
                return
            # 否則掉落並留下標記
            self.lost = True
            self.world.scent_marks.add((self.x, self.y))
        else:
            # 正常移動
            self.x = new_x
            self.y = new_y

    def _get_direction_delta(self):
        """獲取方向的位移"""
        if self.direction == 'N':
            return 0, 1
        elif self.direction == 'S':
            return 0, -1
        elif self.direction == 'E':
            return 1, 0
        elif self.direction == 'W':
            return -1, 0

    def _is_out_of_bounds(self, x, y):
        """檢查座標是否超出邊界"""
        return x < 0 or x > self.world.width or y < 0 or y > self.world.height

    def __str__(self):
        """輸出機器人狀態"""
        result = f"{self.x} {self.y} {self.direction}"
        if self.lost:
            result += " LOST"
        return result

if __name__ == '__main__':
    unittest.main()