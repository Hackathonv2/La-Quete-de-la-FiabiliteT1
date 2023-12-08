import sys

def calculer_temps_indisponibilite(f, p, r):
    return f * (p + r)

def trouver_systeme_le_plus_fiable(systemes):
    temps_min = float('inf')
    nom_systeme_fiable = ""

    for nom, f, p, r in systemes:
        temps = calculer_temps_indisponibilite(f, p, r)
        if temps < temps_min:
            temps_min = temps
            nom_systeme_fiable = nom

    return nom_systeme_fiable

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))

    systemes = []
    for line in lines:
        parts = line.split()
        nom = parts[0]
        f, p, r = map(int, parts[1:])
        systemes.append((nom, f, p, r))

    systeme_fiable = trouver_systeme_le_plus_fiable(systemes)
    print(systeme_fiable)

if __name__ == "__main__":
    main()
