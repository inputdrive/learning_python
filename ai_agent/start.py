import numpy as np
import random

# Step 3: Tic-Tac-Toe Environment
class TicTacToe:
    def __init__(self):
        self.board = np.array(['_'] * 9)
        self.current_player = 'X'

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
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '_':
                return self.board[combo[0]]
        if '_' not in self.board:
            return 'Draw'
        return None

    def step(self, action):
        self.make_move(action, 'X')
        winner = self.check_winner()
        if winner == 'X':
            return self.board, 1, True
        if winner == 'Draw':
            return self.board, 0, True
        if winner == 'O':
            return self.board, -1, True

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

# Step 4: Q-Learning Agent
class QLearningAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, exploration_decay=0.995):
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay

    def get_state_key(self, board):
        return str(board)

    def choose_action(self, board, available_actions):
        state = self.get_state_key(board)
        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in available_actions}

        if random.random() < self.exploration_rate:
            return random.choice(available_actions)

        q_values = self.q_table[state]
        max_q = max(q_values.values())
        best_actions = [a for a, q in q_values.items() if q == max_q]
        return random.choice(best_actions)

    def update_q_table(self, state, action, reward, next_state, next_available_actions, done):
        state_key = self.get_state_key(state)
        next_state_key = self.get_state_key(next_state)

        # Initialize state_key in Q-table if it doesn't exist
        if state_key not in self.q_table:
            self.q_table[state_key] = {a: 0 for a in range(9)}  # All possible actions (0-8)

        # Ensure the action exists in the Q-table for this state
        if action not in self.q_table[state_key]:
            self.q_table[state_key][action] = 0

        # Initialize next_state_key if not done and not in Q-table
        if next_state_key not in self.q_table and not done:
            self.q_table[next_state_key] = {a: 0 for a in next_available_actions}

        current_q = self.q_table[state_key][action]
        future_q = 0 if done else max(self.q_table[next_state_key].values(), default=0)
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * future_q - current_q)
        self.q_table[state_key][action] = new_q

    def decay_exploration(self):
        self.exploration_rate *= self.exploration_decay

# Step 5: Training the Agent
def train_agent():
    env = TicTacToe()
    agent = QLearningAgent()
    episodes = 10000

    for episode in range(episodes):
        state = env.reset()
        done = False

        while not done:
            available_actions = env.get_available_actions()
            action = agent.choose_action(state, available_actions)
            next_state, reward, done = env.step(action)
            next_available_actions = env.get_available_actions() if not done else []
            agent.update_q_table(state, action, reward, next_state, next_available_actions, done)
            state = next_state

        agent.decay_exploration()

    print("Training complete!")
    return env, agent

# Step 6: Testing the Agent
def test_agent(env, agent):
    state = env.reset()
    done = False
    print(state.reshape(3, 3))

    while not done:
        available_actions = env.get_available_actions()
        action = agent.choose_action(state, available_actions)
        state, reward, done = env.step(action)
        print(state.reshape(3, 3))
        print(f"Reward: {reward}, Done: {done}")

# Run Training and Testing
if __name__ == "__main__":
    env, agent = train_agent()
    test_agent(env, agent)