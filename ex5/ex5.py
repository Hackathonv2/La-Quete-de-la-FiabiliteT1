import sys

def traiter_requetes(P, S, requetes):
    memoire_allouee = {i: [] for i in range(S)}

    for id, a, b, t in requetes:
        if t == 1:  # Allocation
            portions_disponibles = []
            for i in range(len(memoire_allouee[id])):
                debut, fin = memoire_allouee[id][i]
                if b <= debut or a >= fin:
                    portions_disponibles.append((debut, fin))
                else:
                    if a > debut:
                        portions_disponibles.append((debut, a))
                    if b < fin:
                        portions_disponibles.append((b, fin))
            memoire_allouee[id] = portions_disponibles

            for i in range(S):
                if i != id:
                    nouvelle_allocation = []
                    for debut, fin in memoire_allouee[i]:
                        if debut >= b or fin <= a:
                            nouvelle_allocation.append((debut, fin))
                        else:
                            if debut < a:
                                nouvelle_allocation.append((debut, a))
                            if fin > b:
                                nouvelle_allocation.append((b, fin))
                    memoire_allouee[i] = nouvelle_allocation

        elif t == 0:  # Libération
            memoire_allouee[id] = [(debut, fin) for debut, fin in memoire_allouee[id] if fin <= a or debut >= b]

    return max(memoire_allouee, key=lambda x: sum(fin - debut for debut, fin in memoire_allouee[x]))

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))

    P, S, R = map(int, lines[0].split())
    requetes = [tuple(line.split()) for line in lines[1:]]
    requetes = [(int(id), float(a), float(b), int(t)) for id, a, b, t in requetes]

    serveur_plus_occupe = traiter_requetes(P, S, requetes)
    print(serveur_plus_occupe)

if __name__ == "__main__":
    main()
