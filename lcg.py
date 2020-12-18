def lcg(a=1664525, c=1013904223, m=2**32, seed=1, loops=0, maxdigits=2):
    """
    Formula for LCG:
    x[n+1] = (a * x[n] + c) MOD m

    :param a: Multiplicative
    :param c: Constant
    :param m: Modulus
    :param seed: Seed
    :param loops: Amount of loops
    :param maxdigits: Maximum amount of digits the RNG can return

    :return: [int] List of generated integers
    """
    seedList = [seed]  # List voor alle gegenereerde waarden
    valueList = [seed] # List van slices van gegenereerde waarden (maxdigits=n)

    # Aantal getallen dat gegenereerd moet worden
    for step in range(loops):
        number = (a * seedList[step] + c) % m
        seedList.append(number)
        number = str(number)

        # Check of gegenereerde getallen langer zijn dan maxdigits
        if maxdigits >= len(number):
            valueList.append(int(number))

        else:
            valueList.append(int(number[-maxdigits:]))

    # Als loops=1, geef integer <int> terug i.p.v. [int]
    if len(valueList) == 1:
        return valueList[0]
    else:
        return valueList


if __name__ == '__main__':
    print(lcg(loops=10000))
