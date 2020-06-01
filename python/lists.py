l = []
if __name__ == '__main__':
    for i in range(int(input())):
        s = input().split()
        s1 = s[0]
        s2 = s[1:]
        if s1 == 'print':
            print(l)
        else:
            eval('l.{0}{1}'.format(s1, '('+','.join(s2)+')'))
