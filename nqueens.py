"""
CISC352 Assignment 1
Group 2
Febuary 15th 2019
Authors:
Michael Olson    20008033

"""
import random

## An instance of this class is one queen. Attributes that a
##  queen has are positon (x,y) and number of conflicts
class Queen():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.conflicts = 0
    ## Use the board to check if the queen conflicts
    ##      with any others. Update number and either
    ##      add or remove self to board.conflicts
    def checkConflicts(self, board):
        self.conflicts = 0
        for i in range(0, board.n):
            if (not self is board.queens[i]):
##                print("I am queen " + str(self.x) + " checking queen " + str(i))
##                t = self.conflicts
                if (board.queens[i].y == self.y):
                    self.conflicts += 1
                    
                elif (board.queens[i].y == self.y + i - self.x):
                    self.conflicts += 1
                
                elif (board.queens[i].y == self.y - i + self.x):
                    self.conflicts += 1
                    
##                print("\t checking y == " + str(self.y))
##                print("\t checking y == " + str(self.y + i - self.x))
##                print("\t checking y == " + str(self.y - i + self.x))
##                if (t < self.conflicts): print("Found conflict")

            if (self.conflicts != 0 and not board.conflicts.count(self)):
                board.conflicts.append(self)
            elif (self.conflicts == 0 and board.conflicts.count(self)):
                board.conflicts.remove(self)
    
## This is the chess board. The chess board should manage
##      the queens, and keep track of positons and conflicts
class Board():
    def __init__(self, n):
        self.n = n
        ## 2D matrix of 0 if no queen and instance in queen's position
        ## List of queen instances.
        self.queens = []
        for i in range(n):
            self.queens.append(Queen())
        
        ## List of queens that currently have at least one conflict
        self.conflicts = []
        self.rowConflicts = [0] * n
        self.leftDiag = [0] * 2 * n - 1
        self.rightDiag = [0] * 2 * n - 1

    ## If self.queens is empty, create queens
    ## randomize the postions, with one queen per row
    def randomizeQueens(self):
        for i in range(len(self.queens)):
            self.queens[i].x = i
            self.queens[i].y = random.randint(0,self.n-1)
            self.rowConflicts[self.queens[i].y] += 1
            self.leftDiag[self.n + self.queens[i].y - i - 1] += 1
            self.rightDiag[self.queens[i].y + i]
    ## Go through the list of queens, checking
    ##      how many conflicts there are. Should
    ##      also update self.conflicts
    def checkSolution(self):
        for q in self.queens:
            q.checkConflicts(self)
        if (self.conflicts == []):
            return True
        else: return False
## Main min conflicts algoritm, see assignment for algorithm.
##      return solution, or None if no solution is found.
def minConflicts(csp, maxSteps):
    for i in range(maxSteps):
        if (csp.checkSolution()):
            return convertBoard(csp)
        var = csp.conflicts[random.randint(0, len(csp.conflicts)-1)]
        value = findLeastconflicts(csp, var)
        var.y = value
        
    return None

## Should convert an instance of Board to a list of queen positions
## ex. return [2,0,1,4]
def convertBoard(board):
    positions = []
    for i in board.queens:
        positions.append(i.y)
    return positions

def findLeastconflicts(csp, queen):
    yPos = queen.y
    numConflicts = queen.conflicts
    bestPos = 0
    for i in range(csp.n):
        queen.y = i
        queen.checkConflicts(csp)
        if (queen.conflicts < numConflicts):
            numConflicts = queen.conflicts
            bestPos = i
    return bestPos

## Should read in "nqueens.txt" and return list of problems to solve
def inputFile(fileName):
    with open(fileName) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content] 

## Outputs found solutions to "nqueens_out.txt"
def outputFile(fileName, solutions):
    print (solutions)
##    file = open(fileName, 'w')
##    file.writelines(solutions)
##    file.close()

def runAlgorithm(n):
    csp = Board(n)
    solution = None
    while(solution == None):
        csp.randomizeQueens()
        solution = minConflicts(csp, 75)
    print(solution)

## problems is the list of n size solutions we must find
problems = []
## solutions is a list of lists, where each element is
##      a matrix of positons as shown in assignment
solutions = []

problems = inputFile("nqueens.txt")
for i in problems:
    solutions.append(runAlgorithm(i))
outputFile("nqueens_output.txt", solutions)

