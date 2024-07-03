#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install tk


# In[2]:


import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_board()
    
    # Create the buttons for the Tic-Tac-Toe board
    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    
    # Handle button click
    def button_click(self, row, col):
        button = self.buttons[row][col]
        
        if button["text"] == "" and self.current_player == "X":
            button["text"] = self.current_player
            if self.check_win():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O"
                self.ai_move()
    
    # AI makes a move
    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    self.buttons[row][col]["text"] = "O"
                    score = self.minimax(self.buttons, 0, False)
                    self.buttons[row][col]["text"] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        
        if best_move:
            row, col = best_move
            self.buttons[row][col]["text"] = "O"
            if self.check_win():
                messagebox.showinfo("Tic-Tac-Toe", "Player O (AI) wins!")
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "X"
    
    # Minimax algorithm
    def minimax(self, board, depth, is_maximizing):
        if self.check_win_static("O"):
            return 1
        if self.check_win_static("X"):
            return -1
        if self.check_tie_static():
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col]["text"] == "":
                        board[row][col]["text"] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[row][col]["text"] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col]["text"] == "":
                        board[row][col]["text"] = "X"
                        score = self.minimax(board, depth + 1, True)
                        board[row][col]["text"] = ""
                        best_score = min(score, best_score)
            return best_score
    
    # Check for a win in the current game state
    def check_win(self):
        for row in range(3):
            if self.buttons[row][0]["text"] == self.buttons[row][1]["text"] == self.buttons[row][2]["text"] != "":
                return True
        for col in range(3):
            if self.buttons[0][col]["text"] == self.buttons[1][col]["text"] == self.buttons[2][col]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False
    
    # Static check for a win
    def check_win_static(self, player):
        for row in range(3):
            if self.buttons[row][0]["text"] == self.buttons[row][1]["text"] == self.buttons[row][2]["text"] == player:
                return True
        for col in range(3):
            if self.buttons[0][col]["text"] == self.buttons[1][col]["text"] == self.buttons[2][col]["text"] == player:
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] == player:
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] == player:
            return True
        return False
    
    # Check for a tie in the current game state
    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    return False
        return True
    
    # Static check for a tie
    def check_tie_static(self):
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    return False
        return True
    
    # Reset the board
    def reset_board(self):
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""

# Initialize the game in a Jupyter Notebook
def start_game():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

# Start the game
start_game()


# In[ ]:




