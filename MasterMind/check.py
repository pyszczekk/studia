def check(tab, code):
    good_place = 0
    good_color = 0
    for i in range(4):
        if tab[i] == code[i]:
            good_place += 1
        else:
            for j in range(4):
                if tab[i] == code[j]:
                    good_color += 1

    return good_color, good_place


def check2(tab, code):
    good_place = 0
    good_color = 0
    colors = []
    good = []
    for i in range(4):
        colors.append(code[i])
    # print(colors)
    # sprawdzanie c:
    for i in range(4):
        #print(colors)
        if tab[i] == code[i]:
            good_place += 1
            has = 0
            for k in range(len(colors)):
                if colors[k] == tab[i]:
                    has = 1
                    break
            if has == 1:
                colors.remove(tab[i])
    for i in range(4):
        if tab[i] != code[i]:
            if len(colors) > 0:
                for j in range(len(colors)):
                    if tab[i] == colors[j]:
                        colors.remove(colors[j])
                        good_color += 1
                        break

    return good_color, good_place

