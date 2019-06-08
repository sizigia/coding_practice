if __name__ == '__main__':
    n = int(input())


def print_funct(n):
    total = []
    for i in range(1, n+1):
        total.append(str(i))
    return ''.join(total)


print(print_funct(n))
