with open('app.txt') as s:
    #w, h = [int(x) for x in next(f).split()] # read first line
    array = []
    for line in s: # read rest of lines
        array.append([int(x) for x in line.split()])