import sys
import random
from math import pi, hypot

def cercle_englobant(points, R=None):
    if R is None:
        R = []
    if not points or len(R) == 3:
        return cercle_deux_points(R) if R else ((0, 0), 0)

    p = points.pop()
    cercle = cercle_englobant(points, R)
    if est_dans_cercle(p, cercle):
        points.append(p)
        return cercle

    return cercle_englobant(points, R + [p])

def cercle_deux_points(points):
    if not points:
        return ((0, 0), 0)
    elif len(points) == 1:
        return (points[0], 0)
    elif len(points) == 2:
        centre = ((points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2)
        rayon = hypot(points[0][0] - points[1][0], points[0][1] - points[1][1]) / 2
        return (centre, rayon)
    else:
        return cercle_trois_points(points)

def cercle_trois_points(points):
    ax, ay, bx, by, cx, cy = points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1]
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    rayon = hypot(ax - ux, ay - uy)
    return ((ux, uy), rayon)

def est_dans_cercle(point, cercle):
    (cx, cy), r = cercle
    return hypot(point[0] - cx, point[1] - cy) <= r

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))

    n = int(lines[0])
    points = [tuple(map(int, line.split())) for line in lines[1:]]

    _, rayon = cercle_englobant(random.sample(points, len(points)), [])
    aire = pi * rayon**2
    print(f"{aire:.5f}")

if __name__ == "__main__":
    main()
