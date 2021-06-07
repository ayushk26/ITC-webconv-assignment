def Convert(string):
    li = list(string.split(", "))
    for item in li:
        i = li.index(item)
        li[i] = item[1:-1]
    return li