class game():
    def __init__(self):
        self.board = [['( )','( )','( )'],['( )','( )','( )'],['( )','( )','( )']]
        self.condition = True
        self.move = 0

    def play(self):
        if self.move % 2 == 0:
            self.p1choice()
        else:
            self.p2choice()
        self.condition = self.gamecontrol()

        if not self.condition:
            self.showboard()
            winner = ''
            if self.move % 2 == 0:
                winner = 'X'
            else:
                winner = 'O'

            print('Game finished, The Winner Is = {} '.format(winner))

        self.move +=1
    def p1choice(self):
        self.showboard()
        print('First player')
        line = int(input('Enter the line:'))
        while line <1 or line>3:
            line = int(input('line can be 1,2 or 3, try again:'))

        column = int(input('Enter the column:'))
        while column <1 or column>3:
            column = int(input('column can be 1,2 or 3, try again:'))

        if self.isitfull(line,column):
            self.p1choice()
        else:
            self.board[line-1][column-1] = 'X'

    def p2choice(self):
        self.showboard()
        print('Second player')
        line = int(input('Enter the line:'))
        while line < 1 or line > 3:
            line = int(input('line can be 1,2 or 3, try again:'))

        column = int(input('Enter the column'))
        while column < 1 or column > 3:
            column = int(input('colummn can be 1,2 or 3, try again:'))

        if self.isitfull(line, column):
            self.p2choice()
        else:
            self.board[line-1][column-1] = 'O'

    def isitfull(self,line,sutun):
        if self.board[line-1][sutun-1] != '( )':
            return True
        else:
            return False
    def showboard(self):
        for i in self.board:
            for j in i:
                print(j,end=' ')
            print('\n')
    def gamecontrol(self):
        #horizontal control
        if [self.board[0][0],self.board[0][1],self.board[0][2]] == ["X","X","X"] or [self.board[0][0],self.board[0][1],self.board[0][2]] == ["O","O","O"]:
            return False
        if [self.board[1][0],self.board[1][1],self.board[1][2]] == ["X","X","X"] or [self.board[1][0],self.board[1][1],self.board[1][2]] == ["O","O","O"]:
            return False
        if [self.board[2][0],self.board[2][1],self.board[2][2]] == ["X","X","X"] or [self.board[2][0],self.board[2][1],self.board[2][2]] == ["O","O","O"]:
            return False

        #perpendicular control
        if [self.board[0][0],self.board[1][0],self.board[2][0]] == ["X","X","X"] or [self.board[0][0],self.board[1][0],self.board[2][0]] == ["O","O","O"]:
            return False
        if [self.board[0][1],self.board[1][1],self.board[2][1]] == ["X","X","X"] or [self.board[0][1],self.board[1][1],self.board[2][1]] == ["O","O","O"]:
            return False
        if [self.board[0][2],self.board[1][2],self.board[2][2]] == ["X","X","X"] or [self.board[0][2],self.board[1][2],self.board[2][2]] == ["O","O","O"]:
            return False

        #dioganal control
        if [self.board[0][0],self.board[1][1],self.board[2][2]] == ["X","X","X"] or [self.board[0][0],self.board[1][1],self.board[2][2]] == ["O","O","O"]:
            return False
        if [self.board[0][2],self.board[1][1],self.board[2][0]] == ["X","X","X"] or [self.board[0][2],self.board[1][1],self.board[2][0]] == ["O","O","O"]:
            return False

        return True





game = game()
while game.condition:
    game.play()

