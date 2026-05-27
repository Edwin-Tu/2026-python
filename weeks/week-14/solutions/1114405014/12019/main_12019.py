DOOMSDAY = {
    1: 10, 2: 21, 3: 7, 4: 4, 5: 9, 6: 6,
    7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12
}

WEEKDAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

DAYS_IN_MONTH = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def solve():
    t = int(input().strip())
    for _ in range(t):
        m, d = map(int, input().split())
        doomsday = DOOMSDAY[m]
        diff = d - doomsday
        # 2012 doomsday = Wednesday (index 2)
        weekday_idx = (2 + diff) % 7
        print(WEEKDAY[weekday_idx])


if __name__ == "__main__":
    solve()
