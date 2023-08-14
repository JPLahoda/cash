n = ""
n = input("How much change is owed?")

def isFloat(n):
    count = 0
    for char in n:
        if char == '.':
            count += 1
            if count >= 2:
                return False
    for char in n:
        if char == '.':
            continue
        elif char.isdigit() == False:
            return False

while isFloat(n) == False:
    print("Please enter a valid amount.", end=' ')
    n = input("How much change is owed?")

n = float(n)
    
def coins(n):
    count = 0
    divRemainder = 0
    while n > 0:
        n = round(n, ndigits=2)
        if (n / .25) >= 1:
            count += (n / .25)
            divRemainder = count % 1
            count -= divRemainder
            n -= (.25 * ((n / .25) - divRemainder))
            divRemainder = 0
        elif (n / .1) >= 1:
            count += (n / .1)
            divRemainder = count % 1
            count -= divRemainder
            n -= (.1 * ((n / .1) - divRemainder))
            divRemainder = 0
        elif (n / .05) >= 1:
            count += (n / .05)
            divRemainder = count % 1
            count -= divRemainder
            n -= (.05 * ((n / .05) - divRemainder))
            divRemainder = 0
        elif (n / .01) >= 1:
            count += (n / .01)
            divRemainder = count % 1
            count -= divRemainder
            n -= (.01 * ((n / .01) - divRemainder))
            divRemainder = 0
    print(int(count), "coins")

coins(n)
