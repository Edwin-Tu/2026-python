import sys


def parse_equation(s):
    s = s.rstrip('#')
    
    if '=' not in s:
        return None, None, None
    
    left, right = s.split('=', 1)
    
    left_num = ''
    left_ops = []
    for ch in left:
        if ch in '+-':
            left_ops.append(ch)
            left_num = ''
        else:
            left_num += ch
    
    right_num = ''
    right_ops = []
    for ch in right:
        if ch in '+-':
            right_ops.append(ch)
            right_num = ''
        else:
            right_num += ch
    
    return left, right, left_ops, right_ops


def solve():
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    line = line.rstrip('#')
    
    if '=' not in line:
        print("No")
        return
    
    left, right = line.split('=', 1)
    
    def evaluate(expr):
        result = 0
        num = ''
        op = '+'
        for ch in expr:
            if ch in '+-':
                if num:
                    if op == '+':
                        result += int(num)
                    else:
                        result -= int(num)
                    num = ''
                op = ch
            else:
                num += ch
        if num:
            if op == '+':
                result += int(num)
            else:
                result -= int(num)
        return result
    
    left_val = evaluate(left)
    right_val = evaluate(right)
    
    if left_val == right_val:
        print(line + "#")
        return
    
    left_digits = []
    right_digits = []
    
    i = 0
    while i < len(left):
        if left[i].isdigit():
            j = i
            while j < len(left) and left[j].isdigit():
                j += 1
            left_digits.append((i, left[i:j]))
            i = j
        else:
            i += 1
    
    i = 0
    while i < len(right):
        if right[i].isdigit():
            j = i
            while j < len(right) and right[j].isdigit():
                j += 1
            right_digits.append((i, right[i:j]))
            i = j
        else:
            i += 1
    
    all_nums = left_digits + right_digits
    
    DIGIT_STICKS = {
        '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
        '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
    }
    
    MOVEABLE_STICKS = {
        '0': (6, ['1', '7', '9']),
        '1': (2, ['7']),
        '2': (5, ['3']),
        '3': (5, ['2']),
        '4': (4, []),
        '5': (5, ['3', '6', '9']),
        '6': (6, ['0', '8', '9']),
        '7': (3, ['1']),
        '8': (7, []),
        '9': (6, ['0', '6', '8'])
    }
    
    for pos, num_str in all_nums:
        for digit in num_str:
            for target_digit, (sticks, _) in MOVEABLE_STICKS.items():
                if target_digit == digit:
                    continue
                if not MOVEABLE_STICKS[digit][1]:
                    continue
                if target_digit not in MOVEABLE_STICKS[digit][1]:
                    continue
                
                new_left = left
                new_right = right
                
                if (pos, num_str) in left_digits:
                    idx = left.find(num_str)
                    if idx != -1:
                        new_left = left[:idx] + target_digit + left[idx+len(num_str):]
                else:
                    idx = right.find(num_str)
                    if idx != -1:
                        new_right = right[:idx] + target_digit + right[idx+len(num_str):]
                
                if evaluate(new_left) == evaluate(new_right):
                    result = new_left + "=" + new_right + "#"
                    print(result)
                    return
    
    print("No")


if __name__ == "__main__":
    solve()