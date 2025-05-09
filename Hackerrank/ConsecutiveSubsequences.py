def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        cnt = [0] * k
        cnt[0] = 1  # Initial count for sum = 0
        total = 0
        sum_mod = 0
        numbers = list(map(int, input().split()))
        
        for num in numbers:
            sum_mod = (sum_mod + num) % k
            cnt[sum_mod] += 1

        result = 0
        for c in cnt:
            result += c * (c - 1) // 2  # Number of pairs

        print(result)

if __name__ == "__main__":
    main()
