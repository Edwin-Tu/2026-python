from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

students = [
    {"name": "王小明", "math": 80, "english": 70},
    {"name": "李大華", "math": 65, "english": 90},
    {"name": "張三", "math": 95, "english": 55},
]

def get_score(student, subject):
    return student[subject]

by_math = partial(get_score, subject="math")
by_english = partial(get_score, subject="english")

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cost_in_base(n, base, costs):
    if n == 0:
        return costs[0]
    total = 0
    while n > 0:
        total += costs[n % base]
        n //= base
    return total

uniform_costs = [1] * 36
calc = partial(cost_in_base, costs=uniform_costs)

print_same_line = partial(print, end=" ")

double_lambda = lambda x: power(x, 2)
double_partial = partial(power, exp=2)
