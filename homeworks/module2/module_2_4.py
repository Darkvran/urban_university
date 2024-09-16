numbers = [number for number in range (1, 100)]

primes = []
not_primes = []

for i in range(0, len(numbers)):
    is_prime = True
    for k in range(1, i-1):
        if numbers[i] % numbers[k] == 0:
            is_prime = False
            break
    if is_prime and numbers[i] != 1:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print(primes)
print(not_primes)