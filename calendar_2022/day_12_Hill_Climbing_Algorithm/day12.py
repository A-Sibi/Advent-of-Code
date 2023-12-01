from collections import deque

def find_shortest_path(heightmap):
    rows = len(heightmap)
    cols = len(heightmap[0])

    start = None
    end = None

    for i in range(rows):
        for j in range(cols):
            if heightmap[i][j] == 'S':
                start = (i, j)
            elif heightmap[i][j] == 'E':
                end = (i, j)

    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        (x, y), steps = queue.popleft()
        
        if (x, y) == end:
            return steps

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                current_elevation = ord(heightmap[x][y]) if heightmap[x][y] not in 'SE' else ord('a')
                next_elevation = ord(heightmap[nx][ny]) if heightmap[nx][ny] not in 'SE' else ord('a')
            elevation_diff = abs(next_elevation - current_elevation)
            if (nx, ny) not in visited and elevation_diff <= 1:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    return -1

heightmap = [
"Sabqponm",
"abcryxxl",
"accszExk",
"acctuvwj",
"abdefghi"
]

print(find_shortest_path(heightmap))