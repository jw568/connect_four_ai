import math
from board import Board
import random


# This is the parent class AI bots.
class Bot:

    def __init__(self, depthLimit, isPlayerOne):

        self.isPlayerOne = isPlayerOne
        self.depthLimit = depthLimit

    # return a list of children and moves that generate them
    def generateChildren(self, board):
        children = []
        for i in range(0, board.width):
            if(len(board.board[i]) != board.height):
                new_board = Board(board)
                new_board.makeMove(i)
                children.append([i, new_board])
        return children

class minMaxBot(Bot):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # return the optimal column to move in
    def findMove(self, board):
        score, move = self.miniMax(board, self.depthLimit, self.isPlayerOne)
        return move

    # findMove helper function - minimax
    def miniMax(self, board, depth, player):
        # this function returns a tuple (score, move)
        # 1) if the board is in a final state (0,1 or 2), return heuristic.
        #    We don't care to return a move, so we can just return -1.
        # 2) if depth is 0, return the heuristic.
        #    We don't care to return a move, so we can just return -1.
        if (board.isGoal() == 0 or board.isGoal() == 1 or board.isGoal() == 2 or depth == 0):
            return (board.heuristic(), -1)
        # 3) miniMax algorithm
        bestMove = None
        bestScore = None

        if (player):
            bestScore = -math.inf
            for move in self.generateChildren(board):
                curScore = bestScore
                bestScore = max(bestScore, self.miniMax(move[1], depth - 1, not player)[0])
                if(bestScore > curScore):
                    bestMove = move[0]
            return (bestScore, bestMove)
        else: 
            bestScore = math.inf
            for move in self.generateChildren(board):
              curScore = bestScore
              bestScore = min(bestScore, self.miniMax(move[1], depth - 1, not player)[0])
              if (bestScore < curScore):
                bestMove = move[0]

            return (bestScore, bestMove)                   

        
        
class alphaBetaBot(Bot):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # returns the optimal column to move in
    def findMove(self, board):
        score, move = self.alphaBeta(board, self.depthLimit, self.isPlayerOne, -math.inf, math.inf)
        return move

    # findMove helper function - alpha beta pruning
    def alphaBeta(self, board, depth, player, alpha, beta):
        # this function returns a tuple (score, move)
        # 1) if the board is in a final state (0,1 or 2), return heuristic.
        #    We don't care to return a move, so we can just return -1.
        # 2) if depth is 0, return the heuristic.
        #    We don't care to return a move, so we can just return -1.
        if (board.isGoal() == 0 or board.isGoal() == 1 or board.isGoal() == 2 or depth == 0):
            return (board.heuristic(), -1)
        # 3) miniMax algorithm
        if (not player):
            bestScore = math.inf 
            for move in self.generateChildren(board):
              curScore = bestScore
              bestScore = min(bestScore, self.alphaBeta(move[1], depth - 1, not player, alpha, beta)[0])
              if bestScore <= alpha:
                return (bestScore, move)
              beta = min(beta, bestScore)
              if (curScore > bestScore):
                    bestMove = move[0]
            return (bestScore, bestMove)

        else: 
            bestScore = -math.inf
            for move in self.generateChildren(board):
                curScore = bestScore
                bestScore = max(bestScore, self.alphaBeta(move[1], depth - 1, not player, alpha, beta)[0])
                if bestScore >= beta:
                    return (bestScore, move)
                alpha = max(alpha, bestScore)
                if(curScore < bestScore):
                    bestMove = move[0]   
            return (bestScore, bestMove)                    




# random bot
class randomBot(Bot):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # return a random column to move in
    def findMove(self, board):
        move = random.randint(0, board.width - 1)
        while len(board.board[move]) == board.height:
            move = random.randint(0, board.width - 1)
        return move

# human player
class HumanPlayer:

    def __init__(self, depthLimit, isPlayerOne):
        pass

    def findMove(self, board):
        pass
