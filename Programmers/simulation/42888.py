def solution(record):
    user_dic = {}
    for rec in record:
        list_rec = rec.split()
        if len(list_rec) == 3:
            user_dic[list_rec[1]] = list_rec[2]

    result = []
    for rec in record:
        string = ""
        list_rec = rec.split()
        if list_rec[0] == "Enter":
            string = "%s님이 들어왔습니다." % user_dic[list_rec[1]]
        elif list_rec[0] == "Leave":
            string = "%s님이 나갔습니다." % user_dic[list_rec[1]]
        if string:
            result.append(string)
    return result