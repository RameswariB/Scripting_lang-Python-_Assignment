# functin defination
def spiralPrint(endRowIndex, endColIndex, a):
    startingPoint = 0
    startingcolIndex = 0

    while (startingPoint < endRowIndex and startingcolIndex < endColIndex):
        # Print the first row from
        for i in range(startingcolIndex, endColIndex):
            print(a[startingPoint][i], end=" ")
        startingPoint += 1
        # Print the last column from
        for i in range(startingPoint, endRowIndex):
            print(a[i][endColIndex - 1], end=" ")
        endColIndex -= 1
        # Print the last row from
        if (startingPoint < endRowIndex):
            for i in range(endColIndex - 1, (startingcolIndex - 1), -1):
                print(a[endRowIndex - 1][i], end=" ")
            endRowIndex -= 1
        # Print the first column from the remaining columns
        if (startingcolIndex < endColIndex):
            for i in range(endRowIndex - 1, startingPoint - 1, -1):
                print(a[i][startingcolIndex], end=" ")
            startingcolIndex += 1


# main method
input = [[1, 2, 3, 4],
         [5,6,7,8],
         [9,10,11,12]]
row = len(input)
col = len(input[0])
spiralPrint(row, col, input)