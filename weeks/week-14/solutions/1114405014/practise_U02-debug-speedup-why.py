import math
import timeit
import traceback


class AppError(Exception):
    pass


def low_level():
    raise ValueError("低階：值不對")


def variant_a():
    try:
        low_level()
    except ValueError as e:
        raise AppError("應用層失敗") from e


def variant_b():
    try:
        low_level()
    except ValueError:
        raise AppError("應用層失敗")


def variant_c_good():
    try:
        low_level()
    except ValueError:
        print("  [中途記 log]")
        raise


def variant_c_bad():
    try:
        low_level()
    except ValueError as e:
        raise e


def demo_raise_styles():
    for name, fn in [("A: raise X from e", variant_a),
                     ("B: raise X (隱式)", variant_b),
                     ("C-good: bare raise", variant_c_good),
                     ("C-bad : raise e", variant_c_bad)]:
        print(f"\n=== {name} ===")
        try:
            fn()
        except Exception:
            traceback.print_exc()


def demo_print_exc_vs_str():
    def will_crash():
        data = {"a": 1}
        return data["missing"]

    try:
        will_crash()
    except Exception as e:
        print("【壞示範】print(e)：")
        print(f"  {e}")
        print("【好示範】traceback.print_exc()：")
        traceback.print_exc()


def slow_version(items):
    result = []
    for x in items:
        result.append(math.sqrt(x))
    return result


def fast_version(items):
    sqrt = math.sqrt
    return [sqrt(x) for x in items]


def demo_speedup():
    data = list(range(1, 100_000))
    t1 = timeit.timeit(lambda: slow_version(data), number=10)
    t2 = timeit.timeit(lambda: fast_version(data), number=10)
    print(f"slow = {t1:.3f}s, fast = {t2:.3f}s, speedup = {t1/t2:.2f}x")


if __name__ == "__main__":
    print("########## 14.9 / 14.10 三種拋法 ##########")
    demo_raise_styles()

    print("\n########## 14.12 print_exc vs print(e) ##########")
    demo_print_exc_vs_str()

    print("\n########## 14.14 local 變數加速 ##########")
    demo_speedup()
