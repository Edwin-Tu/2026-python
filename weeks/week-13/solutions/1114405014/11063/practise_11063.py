import sys


def rgb_to_xyz(pixels):
    raise NotImplementedError("Implement this function")


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    case_no = 1
    while idx < len(data):
        n = int(data[idx]); idx += 1
        pixels = []
        for _ in range(n * n):
            r = int(data[idx]); g = int(data[idx + 1]); b = int(data[idx + 2])
            idx += 3
            pixels.append((r, g, b))
        print(f"Case {case_no}:")
        case_no += 1
        xyz_list, avg_y = rgb_to_xyz(pixels)
        for x, y, z in xyz_list:
            print(f"{x:.4f} {y:.4f} {z:.4f}")
        print(f"The average of Y is {avg_y:.4f}")


if __name__ == "__main__":
    main()
