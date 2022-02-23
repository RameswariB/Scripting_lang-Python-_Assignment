# functin defination
def spiralPrint(endRowIndex, endColIndex, a,searchWord):
    startingPoint = 0
    startingcolIndex = 0

    searchIndex=0;
    while (startingPoint < endRowIndex and startingcolIndex < endColIndex):
        for i in range(startingcolIndex, endColIndex):
            if(a[startingPoint][i] == searchWord[searchIndex]):
                print(f'[{startingPoint},{i}]')
                searchIndex +=1
                if searchIndex == len(searchWord):
                    break;
        startingPoint += 1


# main method
board = [["A","B","C","E"],
     ["S","F","C","S"],
     ["A","D","E","E"]]
row = len(board)
col = len(board[0])
word="ABCCDE"
spiralPrint(row, col, board,word)