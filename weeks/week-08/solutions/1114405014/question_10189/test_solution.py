import pytest
from solution import count_mines, solve, process_grid


class TestCountMines:
    def test_single_mine_around(self):
        grid = [
            ['*', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        assert count_mines(grid, 1, 1, 3, 3) == 1

    def test_no_mine_around(self):
        grid = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        assert count_mines(grid, 1, 1, 3, 3) == 0

    def test_all_eight_mines(self):
        grid = [
            ['*', '*', '*'],
            ['*', '.', '*'],
            ['*', '*', '*']
        ]
        assert count_mines(grid, 1, 1, 3, 3) == 8

    def test_corner_position(self):
        grid = [
            ['*', '.', '*'],
            ['.', '.', '.'],
            ['*', '.', '*']
        ]
        assert count_mines(grid, 0, 0, 3, 3) == 2
        assert count_mines(grid, 0, 2, 3, 3) == 2
        assert count_mines(grid, 2, 0, 3, 3) == 2
        assert count_mines(grid, 2, 2, 3, 3) == 2


class TestProcessGrid:
    def test_process_grid_with_mines(self):
        grid = [
            ['*', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '*']
        ]
        result = process_grid(grid, 3, 3)
        assert result[0][0] == '*'
        assert result[2][2] == '*'
        assert result[1][1] == 2


class TestSolve:
    def test_basic_input(self, capsys):
        import io
        import sys
        input_data = "4 4\n*...\n....\n.*..\n....\n0 0\n"
        sys.stdin = io.StringIO(input_data)
        solve()
        output = capsys.readouterr().out
        assert "Field #1:" in output
        assert "*100" in output