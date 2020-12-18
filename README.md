# Pseudo Random Number Generators in Monte Carlo simulations
### Made by Kwuffin

In this repository you will find my Monte Carlo simulation for an assignment I had to make for subject 'Simulation Modelling'

### Case
Maak een Monte Carlo Simulatie die meerdere keren (duizenden) de competitie speelt met gebruik van deze tabel van kansen. Hoe vaker je een competitie speelt, hoe nauwkeuriger je voorspelling wordt. Houd bij hoeveel punten elk team scoort in de competitie (3 punten voor winst, 1 punt voor gelijk, 0 voor verlies), en maak een overzicht (ranking) van de teams.

Gebruik je eigen geprogrammeerde Random Number Generator voor het uitvoeren van deze Monte Carlo Simulatie!

Maak een overzicht van de gemiddelden rank van de teams. D.w.z. bepaal je eindantwoord als een matrix, waarbij per team wordt aangegeven welke kans deze heeft om op die plek in het eindklassement te eindigen, op basis van de gesimuleerde spelletjes.

### Contents
In montecarlo.py you will find my Monte Carlo simulation that will utilize either one or both of my RNG's.

mersenneTwister.py contains my Mersenne Twister number generator.

lcg.py contains my Linear Congruential Generator.