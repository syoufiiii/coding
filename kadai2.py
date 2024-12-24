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