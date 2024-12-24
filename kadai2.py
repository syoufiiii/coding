# 〇課題２
# 関数オブジェクト or 内部関数を使用して再起呼び出するプログラムで受け取ったパラメーターを数字以外は「数字を入力してください。」を表示して終了。
# 数字の場合は、素因数分解して表示するプログラムを作成しなさい。
# ※内部関数を使用するのでfor文は使用する必要がありません。



def prime_factorization(num):
    def factorize(n, divisor=2):
        if n < 2:
            return []
        if n % divisor == 0:
            return [divisor] + factorize(n // divisor, divisor)
        return factorize(n, divisor + 1)

    return factorize(num)

def main():
    try:
        num = int(input("数字を入れてください: "))
        if num < 2:
            print("2以上の数字を入力してください")
        else:
            factors = prime_factorization(num)
            print(f"{num}の素因数分解: {factors}")
    except ValueError:
        print("数字を入力してください")

if __name__ == "__main__":
    main()