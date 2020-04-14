from math import sqrt

def dist(x1, y1, x2, y2):
    return round(sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))

#parsare fisier coordonate
def parseFile(fileName):
    n = 51
    pair = []
    
    with open(fileName, "r") as f:
        for line in range(n):
            node, x, y = f.readline().split(" ")
            pair.append((int(node), int(x), int(y)))

    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for coord1 in pair:
        for coord2 in pair:
            matrix[coord1[0] - 1][coord2[0] - 1] = dist(coord1[1], coord2[1], coord1[2], coord2[2])
            matrix[coord1[0] - 1][coord2[0] - 1] = dist(coord1[1], coord2[1], coord1[2], coord2[2])
    return matrix

#parsare fisier text
def readnetwork(fileName):
    f = open(fileName, "r")
    network = {}
    n = int(f.readline())
    distances = []
    i = 0
    for line in f:
        while line != "" and line != "\n" and i < n:
            stringElems = line.split(",")
            elems = []
            for elem in stringElems:
                elems.append(int(elem))
            distances.append(elems)
            line = f.readline().strip()
            i += 1
    network["noNodes"]=n
    network["mat"] = distances

    """distances=parseFile(fileName)
    network["mat"]=distances
    n=len(distances)
    network["noNodes"] = n"""

    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if (distances[i][j] == 1):
                d += 1
            if (j > i):
                noEdges += distances[i][j]
        degrees.append(d)
    network["noEdges"] = noEdges
    network["degrees"] = degrees
    f.close()
    return network