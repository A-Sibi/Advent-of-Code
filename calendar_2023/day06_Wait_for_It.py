# part 1
times = [46, 80, 78, 66]
distances = [214, 1177, 1402, 1024]

# part 2
times = [46807866]
distances = [214117714021024]

records_mul = 1
for i in range(len(times)):
    local_records = 0
    for j in range(times[i]):
        if j * (times[i] - j) > distances[i]:
            local_records += 1
    records_mul *= local_records

print(f"Part 1/2: {records_mul}")
