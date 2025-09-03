def get_prime(data):
    if data < 2:
        return f"{data} please check your number"
    for i in range(2, int(data**0.5) + 1):
        if data % i == 0:
            return f"{data} number is not prime"
    return f"{data} number is prime"
print(get_prime(25))