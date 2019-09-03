def get_absolute_time(string):
    hour = int(string[:2])
    minute = int(string[-2:])
    return hour * 60 + minute


def get_time(integer):
    hour = str(integer // 60)
    minute = str(integer % 60)
    if len(hour) == 1 and len(minute) == 1:
        return "0%s:0%s" % (hour, minute)
    if len(minute) == 1:
        return "%s:0%s" % (hour, minute)
    if len(hour) == 1:
        return "0%s:%s" % (hour, minute)
    return "%s:%s" % (hour, minute)


def get_bus_timetable(number, time):
    start = get_absolute_time("09:00")
    bus_timetable = []
    for i in range(number):
        bus_timetable.append(start + i * time)
    return bus_timetable


def solution(n, t, timetable):
    absolute_time = []
    for time in timetable:
        absolute_time.append(get_absolute_time(time))

    absolute_time.sort()
    bus_timetable = get_bus_timetable(n, t)
    buses = [[] for _ in range(len(bus_timetable))]

    for i in range(len(bus_timetable)):
        while absolute_time:
            if len(buses[i]) <= m:
                if absolute_time[0] <= bus_timetable[i]:
                    buses[i].append(absolute_time.pop(0))
                else:
                    break
            else:
                break

    result = None
    if len(buses[-1]) < m:
        result = bus_timetable[-1]
    elif len(buses[-1]) == m:
        for j in range(len(buses[-1])-1, 0, -1):
            if buses[-1][j] != buses[-1][j-1]:
                result = buses[-1][j] - 1
                break
        else:
            result = buses[-1][0] - 1

    return get_time(result)

