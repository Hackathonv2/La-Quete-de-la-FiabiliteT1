import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

graph = {}

try:
    nb_machines = int(lines[0][:lines[0].find(' ')])
    nb_lines = int(lines[0][lines[0].find(' '):])
    for i in range(1, nb_lines + 1):
        key = lines[i][:5]
        value = lines[i][6:]
        if key not in graph:
            graph[key] = [value]
        else:
            if value not in graph[key]:
                graph[key].append(value)

except ValueError:
    print('Error: Input must be an integer')
    exit(0)
except IndexError:
    print('input too short')
    exit(0)
    
def find_machines(key:str):
    for value in graph[key]:
        machines = [key, value]
        if value in graph:
            for term in graph[value]:
                if term not in machines:
                    machines.append(term)
    return machines

for key in graph:
    if len(find_machines(key)) > nb_machines - 1:
        print(key)
