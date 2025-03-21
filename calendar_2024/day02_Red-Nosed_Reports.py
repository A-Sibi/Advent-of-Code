safe_count = 0

with open('calendar_2024/data/day2.txt') as file:
    for line in file:
        safe = True
        report = [int(x) for x in line.split()]
        if report[1] > report[0]:
            sign = '+'
        elif report[1] < report[0]:
            sign = '-'
        else:
            safe = False
            continue
        if sign == '+':
            for i in range(len(report) - 1):
                if report[i] < report[i+1] and abs(report[i] - report[i+1]) <= 3:
                    continue
                else:
                    safe = False
                    break
        if sign == '-':
            for i in range(len(report) - 1):
                if report[i] > report[i+1] and abs(report[i] - report[i+1]) <= 3:
                    continue
                else:
                    safe = False
                    break
        if safe:
            safe_count += 1

print(safe_count)

# part 2
safe_count = 0

with open('calendar_2024/data/day2e.txt') as file:
    for line in file:
        safe = True
        report = [int(x) for x in line.split()]
        all_versions = [report[:i] + report[i+1:] for i in range(len(report))]
        for v in all_versions:
            safe = True
            if v[1] > v[0]:
                sign = '+'
            elif v[1] < v[0]:
                sign = '-'
            else:
                safe = False
                continue
            if sign == '+':
                for i in range(len(v) - 1):
                    if v[i] < v[i+1] and abs(v[i] - v[i+1]) <= 3:
                        continue
                    else:
                        safe = False
                        break
            if sign == '-':
                for i in range(len(v) - 1):
                    if v[i] > v[i+1] and abs(v[i] - v[i+1]) <= 3:
                        continue
                    else:
                        safe = False
                        break
            if safe:
                safe_count += 1
                break

print(safe_count) 