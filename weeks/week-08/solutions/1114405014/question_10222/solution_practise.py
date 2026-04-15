def decode_text(encrypted):
    row1 = " 1234567890-="
    row2 = "qwertyuiop[]\\"
    row3 = "asdfghjkl;'"
    row4 = "zxcvbnm,./"
    
    result = ""
    for ch in encrypted:
        decoded = ch
        for row in [row1, row2, row3, row4]:
            if ch in row:
                idx = row.index(ch)
                if idx >= 1:
                    decoded = row[idx - 1]
                break
        result += decoded
    
    return result


def solve():
    import sys
    encoded = sys.stdin.read().strip()
    result = decode_text(encoded)
    print(result)


if __name__ == "__main__":
    solve()