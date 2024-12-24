def to_binary(num):
    result = ""
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return result or "0"

def to_hex(num):
    hex_map = "0123456789ABCDEF"
    result = ""
    while num > 0:
        result = hex_map[num % 16] + result
        num //= 16
    return result or "0"

def main():
    try:
        num = int(input("数字を入れてください: "))
        print(f"10進数: {num}")
        print(f"2進数: {to_binary(num)}")
        print(f"16進数: {to_hex(num)}")
    except ValueError:
        print("数字じゃないです")

if __name__ == "__main__":
    main()
