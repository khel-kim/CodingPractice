def calculator(number, power, option, star):
    now_star = False
    if power == "S":
        score = number ** 1
    elif power == "D":
        score = number ** 2
    else:
        score = number ** 3
    if option == "*":
        score *= 2
        now_star = True
    elif option == "#":
        score *= -1
    if star:
        score *= 2
    return score, now_star


def solution(dartResult):
    dart_result = []
    for i, char in enumerate(dartResult):
        if char in "SDT":
            if i - 2 >= 0:
                if dartResult[i - 2].isdigit():
                    if i + 1 < len(dartResult) and dartResult[i + 1] in "*#":
                        dart_result.append(dartResult[i - 2:i + 2])
                    else:
                        dart_result.append(dartResult[i - 2:i + 1])
                else:
                    if i + 1 < len(dartResult) and dartResult[i + 1] in "*#":
                        dart_result.append(dartResult[i - 1:i + 2])
                    else:
                        dart_result.append(dartResult[i - 1:i + 1])
            else:
                if i + 1 < len(dartResult) and dartResult[i + 1] in "*#":
                    dart_result.append(dartResult[i - 1:i + 2])
                else:
                    dart_result.append(dartResult[i - 1:i + 1])

    dart_result = dart_result[::-1]
    result = 0
    star = False
    for dart in dart_result:
        if len(dart) == 4:
            number = int(dart[:2])
            power = dart[2]
            option = dart[3]

        elif len(dart) == 3:
            if dart[-1] in "#*":
                number = int(dart[:1])
                power = dart[1]
                option = dart[2]
            else:
                number = int(dart[:2])
                power = dart[2]
                option = False
        else:
            number = int(dart[0])
            power = dart[1]
            option = False

        score, star = calculator(number, power, option, star)
        result += score
    return result