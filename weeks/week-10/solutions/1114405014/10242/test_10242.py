import unittest
from main_10242 import solve, find_max_robbery

class TestUVA10242(unittest.TestCase):
    def test_basic_graph(self):
        """測試基本圖"""
        n, m = 6, 7
        edges = [(1, 2), (2, 3), (3, 5), (2, 4), (4, 1), (2, 6), (6, 5)]
        values = [10, 12, 8, 16, 1, 5]
        s, p = 1, 4
        pubs = [3, 5, 6, 4]
        
        result = find_max_robbery(n, edges, values, s, pubs)
        self.assertEqual(result, 47)

    def test_two_nodes(self):
        """測試兩個節點"""
        n, m = 2, 1
        edges = [(1, 2)]
        values = [10, 20]
        s, p = 1, 1
        pubs = [2]
        
        result = find_max_robbery(n, edges, values, s, pubs)
        self.assertEqual(result, 30)

    def test_no_path_to_pub(self):
        """測試沒有路徑到酒吧"""
        n, m = 3, 1
        edges = [(1, 2)]
        values = [10, 20, 30]
        s, p = 1, 1
        pubs = [3]
        
        result = find_max_robbery(n, edges, values, s, pubs)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()