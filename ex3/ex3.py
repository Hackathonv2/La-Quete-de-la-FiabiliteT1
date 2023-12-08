import sys
from math import gcd

def ppcm(a, b):
    return a * b // gcd(a, b)

def trouver_machine_optimale(n, temps_pannes):
    ppcm_initial = temps_pannes[0]
    for temps in temps_pannes[1:]:
        ppcm_initial = ppcm(ppcm_initial, temps)

    meilleur_retard = 0
    indice_optimal = -1

    for i, temps in enumerate(temps_pannes):
        nouveaux_temps = temps_pannes[:i] + [temps + 1] + temps_pannes[i+1:]
        ppcm_nouveau = nouveaux_temps[0]
        for t in nouveaux_temps[1:]:
            ppcm_nouveau = ppcm(ppcm_nouveau, t)

        retard = ppcm_nouveau - ppcm_initial
        if retard > meilleur_retard:
            meilleur_retard = retard
            indice_optimal = i

    return indice_optimal

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))

    n = int(lines[0])
    temps_pannes = list(map(int, lines[1].split()))

    indice_optimal = trouver_machine_optimale(n, temps_pannes)
    print(indice_optimal)

if __name__ == "__main__":
    main()
