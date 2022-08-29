def sieve(num):
    assert type(num) == int, "Input must be an integer"
    assert num > 1, "Input must be greater than 1"

    primes = []

    A = [True] * num
    j_ = []

    for i in range(2, (num ** 1 / 2)):
        if A[i]:
            for j in range(n):
                j_.append()
            for ji in j_:
                A[j] = False

    return primes


if __name__ == "__main__":
    print(600851475143)
    print('Prime factors of 13195: 5->', 13195 % 5)
    print('Prime factors of 13195: 7->', 13195 % 7)
    print('Prime factors of 13195: 13->', 13195 % 13)
    print('Prime factors of 13195: 29->', 13195 % 29)

    sieve(2)
