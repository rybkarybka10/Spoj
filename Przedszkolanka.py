N = int(input())
def cukierki():
    a, b = input().split()
    a = int(a)
    b = int(b)
    b1 = int(b)
    a1 = int(a)
    while a != b:
        if int(a) > int(b):
            b += b1
        else:
            a += a1
    print(a)
for i in range(0, N): cukierki()