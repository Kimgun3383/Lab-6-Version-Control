def decode(data):
    string = ""
    for item in data:
        item = int(item)
        item -= 3
        if item == -1:
            item = 9
        elif item == -2:
            item = 8
        elif item == -3:
            item = 7
        string += str(item)
    return string
