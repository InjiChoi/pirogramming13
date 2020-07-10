# 피보나치 수열의 index n의 값을 리턴
# 피보나치 수열 : 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
def fibo(n):
    # 재귀함수는 탈출조건이 꼭 필요하다.
    if n == 0 or n == 1:
        return 1
    return fibo(n-2) + fibo(n-1)

# index n 수
def fib(n):
    return fibo(n-1)
