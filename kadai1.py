# 〇課題１
# パラメーターを1つ受け取り
# ・数字以外は例外処理で「数字以外が入力されました」と表示させる
# 数字の場合は、10進数、2進数、16進数を表示させるプログラムを作成しなさい
# ※2進数、16進数は関数等は使用せずに自分で判定させるプログラムを作成すること


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
        print("数字を入力してください")

if __name__ == "__main__":
    main()
