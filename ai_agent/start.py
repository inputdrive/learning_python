import numpy as np
import random

class TicTacToe:
    def __init__(self):
        self.board = np.array(['_'] * 9)  # 3x3 board flattened
        self.current_player = 'X'  # AI is X, opponent is O

    def reset(self):
        self.board = np.array(['_'] * 9)
        self.current_player = 'X'
        return self.board

    def get_available_actions(self):
        return [i for i, spot in enumerate(self.board) if spot == '_']

    def make_move(self, action, player):
        if self.board[action] == '_':
            self.board[action] = player
            return True
        return False

    def check_winner(self):
        # Check rows, columns, diagonals
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '_':
                return self.board[combo[0]]
        if '_' not in self.board:
            return 'Draw'
        return None

    def step(self, action):
        # AI move
        self.make_move(action, 'X')
        winner = self.check_winner()
        if winner == 'X':
            return self.board, 1, True
        if winner == 'Draw':
            return self.board, 0, True
        if winner == 'O':
            return self.board, -1, True

        # Opponent's random move
        self.current_player = 'O'
        available = self.get_available_actions()
        if available:
            opponent_action = random.choice(available)
            self.make_move(opponent_action, 'O')
        self.current_player = 'X'

        winner = self.check_winner()
        if winner == 'X':
            return self.board, 1, True
        if winner == 'Draw':
            return self.board, 0, True
        if winner == 'O':
            return self.board, -1, True
        return self.board, 0, False