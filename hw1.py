#Furkan AKGUN
import sys


def compareLogosXDirection(dotGrid):
    tempList = []
    index = 0
    for x in range(0, 21, 1):
        for y in range(0, 21, 1):
            if dotGrid[x][y] == "-":
                tempList.append("-")
            elif dotGrid[x][y] == "|":
                tempList.append("|")
    return tempList


def compareLogosYDirection(dotGrid):
    tempList = []
    index = 0
    for y in range(0, 21, 1):
        for x in range(0, 21, 1):
            if dotGrid[x][y] == "-":
                tempList.append("-")
            elif dotGrid[x][y] == "|":
                tempList.append("|")
    return tempList


def changeDirectionsOnDotGrid(dotGrid):
    for x in range(0, 21, 1):
        for y in range(0, 21, 1):
            if dotGrid[x][y] == "-":
                dotGrid[x][y] = "|"
            elif dotGrid[x][y] == "|":
                dotGrid[x][y] = "-"
    return dotGrid


def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    A = changeDirectionsOnDotGrid(A)
    return A


def reverseRow(data, index):
    cols = len(data[index])
    for i in range(cols // 2):
        temp = data[index][i]
        data[index][i] = data[index][cols - i - 1]
        data[index][cols - i - 1] = temp

    return data


def rorotateMatrix180Degree(data):
    rows = len(data)
    cols = len(data[0])

    if (rows % 2):
        data = reverseRow(data, len(data) // 2)
        for i in range(rows // 2):
            for j in range(cols):
                temp = data[i][j]
                data[i][j] = data[rows - i - 1][cols - j - 1]
                data[rows - i - 1][cols - j - 1] = temp

        return data


def rotate90DegreeAntiClockWise(mat):
    N = len(mat)

    for i in range(N):
        for j in range(i):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp

    for i in range(N // 2):
        for j in range(N):
            temp = mat[i][j]
            mat[i][j] = mat[N - i - 1][j]
            mat[N - i - 1][j] = temp

    mat = changeDirectionsOnDotGrid(mat)
    return mat


def printLogo(dotGrid):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in dotGrid]))


def setLogoDesign(logo):
    x = int(logo.startX)
    y = int(logo.startY)
    x += x - 2
    y += y - 2
    for c in logo.directionList:
        if (c == "L"):
            y = y - 1
            logo.dotGrid[x][y] = "-"
            y = y - 1
        if (c == "R"):
            y = y + 1
            logo.dotGrid[x][y] = "-"
            y = y + 1
        if (c == "U"):
            x = x - 1
            logo.dotGrid[x][y] = "|"
            x = x - 1
        if (c == "D"):
            x = x + 1
            logo.dotGrid[x][y] = "|"
            x = x + 1


class Logo:
    def __init__(self, name, directionList, startX, startY, dotGrid):
        self.name = name
        self.directionList = directionList
        self.startX = startX
        self.startY = startY
        self.dotGrid = dotGrid


def engrave(logoEngraveName, startX, startY):
    logoEngraved = logoDic[logoEngraveName]
    logoEngraved.startX = startX
    logoEngraved.startY = startY
    logoDic.update({logoEngraveName: logoEngraved})
    setLogoDesign(logoEngraved)


def mySplitFunction(word):
    return [char for char in word]


# File open read
with open(sys.argv[1], "r") as f:
    lines = f.readlines()

    logoDic = {}


    # Main section
    for command in lines:
        commandList = command.split(" ")
        if commandList[0] == "LOGO":
            name = commandList[1]
            directionList = mySplitFunction(commandList[2])
            # Dot 2d array decleration
            dotGrid = [[" " for x in range(21)] for y in range(21)]
            for x in range(0, 21, 2):
                for y in range(0, 21, 2):
                    dotGrid[x][y] = "."
            logo = Logo(name, directionList, 4, 5, dotGrid)
            logoDic[logo.name] = logo
            print(logo.name + ' defined')
        if commandList[0] == "ENGRAVE":
            engrave(commandList[1], commandList[2], commandList[3])
            printLogo(logoDic[commandList[1]].dotGrid)

        if commandList[0] == "SAME":
            logo1Name = commandList[1].replace("\n", "")
            logo2Name = commandList[2].replace("\n", "")
            logo1 = logoDic[logo1Name]
            logo2 = logoDic[logo2Name]
            engrave(logo1.name, logo1.startX, logo1.startY)
            engrave(logo2.name, logo2.startX, logo2.startY)
            if (logo1.dotGrid == logo2.dotGrid):
                print('Yes')
            elif(compareLogosXDirection(logo1.dotGrid)== compareLogosXDirection(logo2.dotGrid)):
                print('Yes')
            elif (compareLogosYDirection(logo1.dotGrid) == compareLogosYDirection(logo2.dotGrid)):
                print('Yes')
            elif (compareLogosXDirection(rotate90DegreeAntiClockWise(logo1.dotGrid)) == compareLogosYDirection(logo2.dotGrid)):
                print('Yes')
            elif (compareLogosYDirection(rotate90DegreeAntiClockWise(logo1.dotGrid)) == compareLogosXDirection( logo2.dotGrid)):
                print('Yes')
            elif (compareLogosXDirection(rotate90Clockwise(logo1.dotGrid)) == compareLogosYDirection(logo2.dotGrid)):
                print('Yes')
            elif (compareLogosYDirection(rotate90Clockwise(logo1.dotGrid)) == compareLogosXDirection(logo2.dotGrid)):
                print('Yes')
            elif (compareLogosXDirection(rorotateMatrix180Degree(logo1.dotGrid)) == compareLogosYDirection(logo2.dotGrid)):
                print('Yes')
            elif (compareLogosYDirection(rorotateMatrix180Degree(logo1.dotGrid)) == compareLogosXDirection(logo2.dotGrid)):
                print('Yes')
            else:
                print('No')
