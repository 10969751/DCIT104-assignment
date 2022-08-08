primeNum = []

number=int(input("Enter Number: "))
def NumisPrime(y):
    i = 2
    while (i < y):
        if y % i == 0:
            return False
        i = i + 1
    return True


def NumisPrime(l):
    k= 2
    while k <= l:
        if NumisPrime(k):
            primeNum.append(k)
        k= k + 1


printNum(number)

numOfPrime = len(primeNum)
sum = 0

c = 0
while g< numOfPrime:
    sum += primeNum[c]
    c = c + 1

ans = sum / numOfPrime

print(ans)
