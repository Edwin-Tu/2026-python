"""
R01：unittest 基本用法（記憶層 — 直接複製可執行）

對應 Cookbook：
- 14.1 測試 stdout 輸出
- 14.2 在單元測試中給物件打補丁
- 14.3 在單元測試中測試例外情況

執行：
    python R01-unittest-basics.py
"""
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


# ---------- 被測函式 ----------
def url_print(host, domain):
    """將主機名稱與網域組合成 URL 並印出，供後續測試 stdout 使用"""
    print(f"https://{host}.{domain}")


def parse_int(s):
    """將字串轉為整數；若傳入空字串則拋出 ValueError，用來示範例外測試"""
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    """透過 api 物件的 get 方法向遠端索取使用者資料，方便後續用 mock 取代真實請求"""
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    """測試函式輸出到標準輸出（stdout）的內容是否如預期"""

    def test_url_print(self):
        """使用 io.StringIO 搭配 redirect_stdout 捕捉 print 的內容，
        再用 assertEqual 驗證輸出字串是否正確，確保函式產生預期的 URL"""
        buf = io.StringIO()
        with redirect_stdout(buf):
            url_print("www", "example.com")
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    """示範如何用 mock 物件隔離外部依賴，讓測試不仰賴真實的網路或服務"""

    def test_fetch_user_with_mock(self):
        """建立 MagicMock 取代真實 API 物件，設定回傳值後呼叫被測函式，
        驗證回傳結果正確，且 API 被以正確參數呼叫恰好一次"""
        fake_api = MagicMock()
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user(fake_api, 1)

        self.assertEqual(result["name"], "Alice")
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        """使用 @patch 裝飾器直接將內建的 print 取代為 mock，
        不須重新導向 stdout 即可驗證 url_print 是否印出正確字串"""
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    """驗證函式在特定輸入下是否拋出預期的例外，確保錯誤處理機制正常運作"""

    def test_raises(self):
        """使用 assertRaises 上下文管理器檢查 parse_int 傳入空字串時是否拋出 ValueError"""
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        """使用 assertRaisesRegex 同時檢查例外類型與錯誤訊息內容，
        比單純 assertRaises 更精準，能確保錯誤訊息也符合預期"""
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        """正常輸入時應回傳正確的整數值，確認函式在正常路徑下仍可運作"""
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
