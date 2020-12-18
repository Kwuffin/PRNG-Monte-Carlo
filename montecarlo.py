# Different number generators:
from lcg import lcg
from mersenneTwister import mersenne

import numpy as np
import pandas as pd


def initData(loops, rng):
    # Houdt totaal aantal punten bij voor gehele simulatie.
    totalPoints = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}
    totalWins = []

    # Numpy array met kansen (win-/gelijkspel-/verlieskans).
    chances = np.array([[[], [65, 17, 18], [54, 21, 25], [74, 14, 12], [78, 13, 9]],  # Ajax
                        [[31, 21, 49], [], [37, 24, 39], [51, 22, 27], [60, 21, 19]],  # Feyenoord
                        [[39, 22, 39], [54, 22, 24], [], [62, 20, 18], [62, 22, 16]],  # PSV
                        [[25, 14, 61], [37, 23, 40], [29, 24, 47], [], [52, 23, 25]],  # FC Utrecht
                        [[17, 18, 65], [20, 26, 54], [23, 24, 53], [37, 25, 38], []]])  # Willem II

    posDict = {"0": [0, 0, 0, 0, 0],
               "1": [0, 0, 0, 0, 0],
               "2": [0, 0, 0, 0, 0],
               "3": [0, 0, 0, 0, 0],
               "4": [0, 0, 0, 0, 0]}

    monte_carlo(loops, chances, totalPoints, totalWins, posDict, rng)


def monte_carlo(loops, chances, totalPoints, totalWins, posDict, rng):
    # Vergelijking van beide RNG's:
    if rng == 3:
        rng = 1

    # Mersenne Twister
    if rng == 1:
        # Geeft een lijst met willekeurige getallen uit mersenneTwister.py
        bigRandomNumbers = mersenne(loops * 5 * 5)

        # Pakt de laatste twee getallen
        randomNumbers = []
        for n in bigRandomNumbers:
            if 2 >= len(str(n)):
                randomNumbers.append(int(n))

            else:
                randomNumbers.append(int(str(n)[-2:]))

    # Linear Congruential Generator
    elif rng == 2:
        # Geeft een lijst met willekeurige getallen uit lcg.py
        randomNumbers = lcg(loops=loops * 5 * 5)

    rngCounter = 0

    # For aantal loops
    for _ in range(loops):

        # Hou punten bij voor elke competitie
        points = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}

        # Voor elk thuis-team.
        for row in range(len(chances)):

            # Voor elk uit-team
            for col in range(len(chances[0])):

                # Als thuis-team is hetzelfde als uit-team.
                if row == col:
                    continue  # Voer niks uit, ga verder.

                # Als thuis-team wint
                if randomNumbers[rngCounter] <= chances[row][col][0]:
                    totalPoints[str(row)] += 3
                    points[str(row)] += 3

                # Als gelijkspel
                elif chances[row][col][0] < randomNumbers[rngCounter] <= chances[row][col][1]:
                    totalPoints[str(row)] += 1
                    points[str(row)] += 1
                    points[str(col)] += 1

                rngCounter += 1

        wList = []  # Lijst met de positie van teams op volgorde.
        pointsCopy = points.copy()  # Deepcopy van points, om de keys in te loopen en te verwijderen.

        # Append OP VOLGORDE de positie van de teams van de competitie.
        for _ in range(len(points)):
            wList.append(max(pointsCopy, key=points.get))  # Append de key met de hoogste waarde
            pointsCopy.pop(max(pointsCopy, key=points.get))  # pop de key met de hoogste waarde
        totalWins.append(wList.copy())

    # Append de lijst met volgorde van positie teams naar een lijst die alles bijhoudt.
    for lst in totalWins:
        posCounter = 0
        for x in lst:
            posDict[str(x)][posCounter] += 1
            posCounter += 1

    vizData(posDict, loops)


def vizData(posDict, loops):
    # Geeft keys namen van de juiste teams
    final = {"Ajax": 0, "Feyenoord": 0, "PSV": 0, "FC Utrecht": 0, "Willem II": 0}
    counter = 0
    for x in final:
        final[x] = posDict[str(counter)]
        counter += 1

    # Maakt Pandas DataFrame
    finalDF = pd.DataFrame.from_dict(final, orient='index', columns=['1e', '2e', '3e', '4e', '5e'])

    finalDF = finalDF.applymap(lambda i: (i / loops) * 100).sort_values(by=['1e'], ascending=False)

    print(finalDF)


def main():
    try:
        loops = int(input("Aantal competities:\n> "))
        rngChoose = int(input("\nWelke RNG wil je gebruiken ('1' of '2')?\n"
                              "  1. Mersenne Twister\n"
                              "  2. Linear Congruential Generator\n"
                              "  3. Vergelijk beide\n"
                              "> "))
    except ValueError:
        print("Voer een getal in.")
        exit()

    # Als optie 3 is gekozen (Vergelijking van beide RNG's):
    rngChoose2 = 0
    if rngChoose == 3:
        rngChoose2 = 3

        print("\n\nMersenne Twister:")
    initData(loops, rngChoose)

    if rngChoose2 == 3:
        print("\n\nLinear Congruential Generator:")
        initData(loops, 2)


if __name__ == '__main__':
    main()
