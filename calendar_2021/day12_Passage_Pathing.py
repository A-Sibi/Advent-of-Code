def read(file_name : str) -> list:
    with open(f'data/{file_name}.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

from collections import defaultdict
def createDict(lines: list) -> dict:
    paths = defaultdict(list)
    for line in lines:
        connection = line.split('-')
        paths[connection[0]].append(connection[1])
        paths[connection[1]].append(connection[0])
    paths['end'] = []
    for key in paths.keys():
        if 'start' in paths[key]:
            paths[key].remove('start')
    return paths

def NumOfPaths(connections: dict) -> int:
    allPaths = 0
    for element in connections['start']:
        pass


    return allPaths

data = read('day12_example')
print(createDict(data))