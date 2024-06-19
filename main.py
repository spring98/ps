def solution(lines):
    def timeToMillis(time):
        hh, mm, ss = time.split(':')
        ss, ms = ss.split('.')

        return (int(hh) * 3600 + int(mm)*60 + int(ss))*1000 + int(ms)

    logs = []

    for line in lines:
        date, time, duration = line.split(' ')
        millis = timeToMillis(time)
        duration = int(float(duration[:-1])*1000)
        logs.append((millis-duration+1, millis))

    answer = 0
    for i in range(len(logs)):
        local_count = 1
        for j in range(i+1, len(logs)):
            current_start, current_end = logs[i]
            next_start, next_end = logs[j]

            # print(current_start, current_end, next_start, next_end)
            # print(next_start, current_end + 999)

            if next_start <= current_end + 999:
                local_count += 1

        answer = max(answer, local_count)

    return answer

# print(f'result: {solution(["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"])}')
# print(f'result: {solution(["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"])}')
print(f'result: {solution(["2016-09-15 20:59:57.421 0.351s","2016-09-15 20:59:58.233 1.181s","2016-09-15 20:59:58.299 0.8s","2016-09-15 20:59:58.688 1.041s","2016-09-15 20:59:59.591 1.412s","2016-09-15 21:00:00.464 1.466s","2016-09-15 21:00:00.741 1.581s","2016-09-15 21:00:00.748 2.31s","2016-09-15 21:00:00.966 0.381s","2016-09-15 21:00:02.066 2.62s"])}')
