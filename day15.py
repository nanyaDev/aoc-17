a_seed = 699
b_seed = 124
a_fac = 16807
b_fac = 48271
div = 2147483647

count = 0
pairs = 0
a = a_seed
b = b_seed

for _ in range(5_000_000):
    while True:
        a *= a_fac
        a %= div
        
        if a % 4 == 0:
            break

    while True:
        b *= b_fac
        b %= div

        if b % 8 == 0:
            break

    if bin(a)[-16:] == bin(b)[-16:]:
        count += 1

print(count)
