s = "********"
n = 0
while n < 5:
    n = n + 1
    #这里断言n不超过4。
    assert n < 5
    print(s[0:n])

