import sys
from itertools import combinations

def distance(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

def cercle_minimal(machines):
    n = len(machines)
    if n == 0:
        return 0.0

    max_distance = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_distance = max(max_distance, distance(machines[i][0], machines[i][1], machines[j][0], machines[j][1]))

    # Le rayon est la moitié de la distance maximale, donc l'aire est pi * rayon^2
    aire = 3.14159 * (max_distance / 4)
    return aire

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))

    M = int(lines[0])
    machines = [tuple(map(int, line.split())) for line in lines[1:M+1]]

    aire_minimale = cercle_minimal(machines)
    print("{:.5f}".format(aire_minimale))

if __name__ == "__main__":
    main()
