word = 'Muzi'
# pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]


def solution(word, pages):
    import re
    word = word.lower()
    dic_index = {}
    for index, page in enumerate(pages):
        dic_index[index] = page

    dic_link = {}
    for index in range(len(pages)):
        page = dic_index[index]
        content_re = re.compile('<body>[\W\w]*</body>')
        content_m = content_re.findall(page)
        base_re = re.compile('[^a-zA-Z]+%s[^a-zA-Z]+' % word, re.I)
        base_m = base_re.findall(content_m[0][5:-5])
        base_score = len(base_m)
        # print(base_m, base_score)

        link_re = re.compile(' content="[0-9a-zA-Z:./]+"/>')
        link_m = link_re.findall(page)
        link = link_m[0][link_m[0].index('"')+1:-3]
        # print(link_m[0])
        # print("link", link)

        outer_link_re = re.compile('a href="[0-9a-zA-Z:./]+"')
        outer_link_m = outer_link_re.findall(page)
        outer_links_list = []
        for outer_link in outer_link_m:
            outer_links_list.append(outer_link[outer_link.index('"') + 1:-1])
        # print("outer_links_list", outer_links_list)

        if dic_link.get(link):
            tmp = dic_link[link]
            dic_link[link] = [index, base_score, outer_links_list, tmp]
        else:
            dic_link[link] = [index, base_score, outer_links_list, 0]
        for outer_link in outer_links_list:
            if dic_link.get(outer_link):
                if isinstance(dic_link[outer_link], list):
                    dic_link[outer_link][3] += base_score / len(outer_links_list)
                else:
                    dic_link[outer_link] += base_score / len(outer_links_list)
            else:
                dic_link[outer_link] = base_score / len(outer_links_list)

    result = []
    for key, value in dic_link.items():
        if isinstance(value, float):
            continue
        index = value[0]
        match_score = value[1] + value[3]
        result.append((index, match_score))

    result = sorted(result, key=lambda x: (-x[1], x[0]))
    print(dic_link)
    print(result)
    print(result[0][0])
    return result[0][0]


print(solution(word, pages))