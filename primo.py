import math
def is_prime(number: int) -> bool:
    divisor = int(math.sqrt(number))
    isprime = True
    for i in range(2,divisor+1):
        if number%i == 0:
            isprime = False
            break
    return isprime

def run():
    print(is_prime(int(input())))

if __name__=='__main__':
    run()
