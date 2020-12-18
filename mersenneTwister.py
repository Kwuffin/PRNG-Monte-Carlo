def mersenne(loops=1):
    """"
    x[ k + n] = x[ k + n] XOR ( x[u:] CONCAT x[:l] ) * A,
    where k >= 0
    """

    randomBits = [f"{seed:#034b}"]  # Changes seed to 32 bits

    for step in range(n):
        """"
        xi = f * (xi-1 XOR ( xi-1 >> ( w-2))) + i
        The number coming from this formula should be a 32-bit number, hence why we do & mask32.
        """
        randomBits.append(
            f"{mask32 & (f * (int(randomBits[step], 2) ^ (int(randomBits[step], 2) >> (w - 2))) + step):#034b}")

    generated_numbers = []

    for i in range(loops):
        """
        Concatenate:
         - the upper w-r bits of x[i]
         with:
         - the lower r bits of x[i+l]

         (x[i] ^ u) v (x[( i + 1) mod n]  ^ ll
        """
        conc = randomBits[i][:w - u + 1] + randomBits[((i + 1) % n)][w - u + 1:]

        """
        x[i] = x[(i + m) mod n] XOR (y >> 1)
        """
        xorred = int(randomBits[(i + m) % n], 2) ^ int(conc, 2)

        """
        If least significant bit == 0:
            rightshift(x) >> 1
        If least significant bit == 1:
            (rightshift(x) >> 1) XOR a
        """
        if bin(xorred)[-1] == 0:
            matrixed = xorred >> 1
        else:
            matrixed = (xorred >> 1) ^ a

        randomBits.append(bin(matrixed))

        # Multiplication operation x[i]*T
        y = randomBits[-1]
        y = int(y, 2) ^ (int(y, 2) >> u)
        y = y ^ ((y << s) ^ b)
        y = y ^ ((y << t) ^ c)
        y = y ^ (y >> l)

        generated_numbers.append(y)

    return generated_numbers


def main():
    print(mersenne(1))


# Given parameters
w = 32
r = 31
n = 624
m = 397
u = 11
s = 7
t = 15
l = 18
a = 0x9908b0df
b = 0x9d2c5680
c = 0xefc60000
f = 0x6c078965
mask32 = 0xffffffff

seed = 4564561201

if __name__ == '__main__':
    seed = int(input("Seed:\n> "))
    main()
