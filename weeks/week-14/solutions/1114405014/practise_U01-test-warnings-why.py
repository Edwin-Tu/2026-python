import sys
import unittest
import warnings


class WhySkip(unittest.TestCase):

    @unittest.skipIf(sys.version_info < (3, 10), "需要 Python 3.10+")
    def test_match_case(self):
        x = 1
        match x:
            case 1:
                self.assertTrue(True)

    @unittest.skipUnless(sys.platform.startswith("darwin"), "只在 macOS")
    def test_mac_only(self):
        import os
        self.assertTrue(os.path.exists("/Users"))

    @unittest.expectedFailure
    def test_known_bug(self):
        self.assertEqual(2 + 2, 5)


def run_and_log(logfile="test_result.log"):
    with open(logfile, "w", encoding="utf-8") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        suite = unittest.TestLoader().loadTestsFromTestCase(WhySkip)
        runner.run(suite)
    print(f"結果寫入 {logfile}")


def old_api_bad(x):
    warnings.warn("old_api_bad 已棄用", DeprecationWarning)
    return x


def old_api_good(x):
    warnings.warn("old_api_good 已棄用", DeprecationWarning, stacklevel=2)
    return x


def demo_stacklevel():
    warnings.simplefilter("always")
    print("--- stacklevel=1（差）：行號指向函式內部 ---")
    old_api_bad(1)
    print("--- stacklevel=2（好）：行號指向呼叫端 ---")
    old_api_good(1)


def category_guide():
    warnings.warn("這是給開發者：API 即將移除", DeprecationWarning, stacklevel=2)
    warnings.warn("這是給使用者：輸入值偏大，結果可能不準", UserWarning, stacklevel=2)


if __name__ == "__main__":
    if "--log" in sys.argv:
        run_and_log()
    else:
        demo_stacklevel()
        print("\n--- 警告種類選擇 ---")
        warnings.simplefilter("default")
        category_guide()
        print("\n--- 跑 WhySkip 測試 ---")
        unittest.main(argv=[sys.argv[0]], exit=False)
