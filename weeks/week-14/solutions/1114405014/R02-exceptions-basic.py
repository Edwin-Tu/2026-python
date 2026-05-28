"""
R02：例外處理基本用法（記憶層）

對應 Cookbook：
- 14.6 處理多個例外
- 14.7 捕獲所有例外
- 14.8 建立自定義例外

執行：
    python R02-exceptions-basic.py
"""
import traceback


# ---------- 14.6 多個例外 ----------
def parse_value(s):
    """同一個 except 用 tuple 列出多種例外類別。
    若 s 無法轉為 int，可能拋出 ValueError（格式錯誤）或 TypeError（型別錯誤），
    用 (ValueError, TypeError) 可同時捕捉兩者，避免重複撰寫相同的錯誤處理邏輯"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        return None


# ---------- 14.7 捕獲所有例外 ----------
def safe_run(func, *args):
    """except Exception，而不是裸 except:。
    裸 except: 會捕捉到 SystemExit、KeyboardInterrupt 等不該攔截的系統級例外，
    導致程式無法正常終止。使用 except Exception 則只捕捉應用層的例外，
    保留 Ctrl+C 中斷程式的能力"""
    try:
        return func(*args)
    except Exception as e:
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        traceback.print_exc()


# ---------- 14.8 自定義例外 ----------
class NetworkError(Exception):
    """所有網路錯誤的基底類別；繼承 Exception 而不是 BaseException。
    自定義例外應繼承 Exception（或它的子類），而非 BaseException，
    因為 BaseException 包含 SystemExit、KeyboardInterrupt 等不該被當作一般錯誤處理的例外"""


class HostnameError(NetworkError):
    """找不到主機，屬於 NetworkError 的一種具體類型。
    分層設計讓上層 except NetworkError 可一次捕獲所有網路相關例外"""


class ConnectionTimeout(NetworkError):
    """連線逾時，附帶 host / seconds 屬性，方便上層判斷。
    透過 __init__ 儲存額外上下文資訊，讓捕獲端可以依據 host 或逾時秒數做出不同反應"""
    def __init__(self, host, seconds):
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    """根據 host 與 timeout 參數模擬網路連線；
    若 host 為空字串則拋出 HostnameError，
    若 timeout 小於 1 則拋出 ConnectionTimeout 附帶詳細資訊"""
    if host == "":
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    return f"connected to {host}"


if __name__ == "__main__":
    print("--- 14.6 ---")
    parse_value("abc")
    parse_value(None)

    print("\n--- 14.7 ---")
    safe_run(lambda: 1 / 0)

    print("\n--- 14.8 ---")
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            print(connect(host, t))
        except NetworkError as e:
            print(f"接到 {type(e).__name__}: {e}")
