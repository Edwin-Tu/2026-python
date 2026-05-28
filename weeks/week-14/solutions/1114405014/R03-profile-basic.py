"""
R03：效能測量基本用法（記憶層）

對應 Cookbook：
- 14.13 給程式做效能測試（time / timeit / cProfile）

執行：
    python R03-profile-basic.py
"""
import cProfile
import math
import pstats
import time
import timeit
from functools import wraps


# ---------- 計時裝飾器（粗粒度） ----------
def timed(func):
    """裝飾器：自動測量被修飾函式的執行時間。
    使用 time.perf_counter（而非 time.time）以獲得最高精度的計時結果，
    適合測量從數毫秒到數秒的函式呼叫"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"[timed] {func.__name__}: {elapsed*1000:.2f} ms")
        return result
    return wrapper


@timed
def sum_of_squares(n):
    """計算 0 到 n-1 的平方和，作為效能測量的簡單基準"""
    return sum(i * i for i in range(n))


# ---------- timeit：量微小片段 ----------
def bench_timeit():
    """使用 timeit.timeit 比較生成式與 map+lambda 的效能差異。
    timeit 會自動關閉垃圾回收、多次執行取樣，適合測量微小的程式片段。
    number=1000 表示重複執行 1000 次後取總時間，降低隨機誤差"""
    n = 10_000
    t1 = timeit.timeit("sum(i*i for i in range(n))",
                       globals={"n": n}, number=1000)
    t2 = timeit.timeit("sum(map(lambda i: i*i, range(n)))",
                       globals={"n": n}, number=1000)
    print(f"[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s")


# ---------- cProfile：找熱點 ----------
def workload():
    """執行一些數學運算作為效能分析樣本，讓 cProfile 找出耗時的函式呼叫"""
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile():
    """使用 cProfile 統計各函式被呼叫的次數與累積時間。
    sort_stats("cumulative") 以累計時間排序，幫助找出真正的效能瓶頸。
    print_stats(5) 只顯示前 5 名，避免輸出過於冗長"""
    pr = cProfile.Profile()
    pr.enable()
    workload()
    pr.disable()
    print("[cProfile] 前 5 名：")
    pstats.Stats(pr).sort_stats("cumulative").print_stats(5)


if __name__ == "__main__":
    sum_of_squares(1_000_000)
    bench_timeit()
    bench_cprofile()
