"""
🎮 TIC TAC TOE GAME WITH AI 🎮
================================
A professional Tic Tac Toe game using Python and Pygame
with an unbeatable AI using the Minimax algorithm.

Author: Professional Python Game Developer
Created: 2026
"""

import pygame
import sys
import time
from enum import Enum

# ============================================================================
# GAME CONSTANTS
# ============================================================================

# Screen dimensions
WIDTH = 600
HEIGHT = 700  # Extra space for title and mode selection

# Colors (RGB format)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)

# Grid settings
GRID_SIZE = 3
CELL_SIZE = 150
GRID_OFFSET_X = (WIDTH - CELL_SIZE * 3) // 2
GRID_OFFSET_Y = 150

# Line settings
LINE_WIDTH = 10


# ============================================================================
# GAME MODE ENUMERATION
# ============================================================================

class GameMode(Enum):
    """Enumeration for different game modes"""
    MENU = 0
    PVP = 1  # Player vs Player
    PVE = 2  # Player vs AI


# ============================================================================
# TIC TAC TOE GAME CLASS
# ============================================================================

class TicTacToe:
    """
    Main Tic Tac Toe game class that handles all game logic, rendering,
    and AI implementation using the Minimax algorithm.
    """
    
    def __init__(self):
        """Initialize the game"""
        # Initialize Pygame
        pygame.init()
        pygame.mixer.init()
        
        # Create game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic Tac Toe ❌⭕")
        
        # Clock for controlling frame rate
        self.clock = pygame.time.Clock()
        
        # Load assets (images and sounds)
        self.load_assets()
        
        # Initialize game state
        self.reset_game()
        
        # Game mode
        self.mode = GameMode.MENU
        
    def load_assets(self):
        """Load all game assets (images and sounds)"""
        try:
            # Load and scale images
            self.x_img = pygame.image.load('assets/x.png')
            self.x_img = pygame.transform.scale(self.x_img, (100, 100))
            
            self.o_img = pygame.image.load('assets/o.png')
            self.o_img = pygame.transform.scale(self.o_img, (100, 100))
            
            self.grid_img = pygame.image.load('assets/grid.png')
            self.grid_img = pygame.transform.scale(self.grid_img, (CELL_SIZE * 3, CELL_SIZE * 3))
            
            self.bg_img = pygame.image.load('assets/background.png')
            self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))
            
            # Load sounds
            self.move_sound = pygame.mixer.Sound('assets/sounds/move.wav')
            self.win_sound = pygame.mixer.Sound('assets/sounds/win.wav')
            self.draw_sound = pygame.mixer.Sound('assets/sounds/draw.wav')
            
            # Load voice sounds
            self.you_win_voice = pygame.mixer.Sound('assets/sounds/you_win.wav')
            self.ai_wins_voice = pygame.mixer.Sound('assets/sounds/ai_wins.wav')
            self.draw_voice = pygame.mixer.Sound('assets/sounds/draw_voice.wav')
            
        except pygame.error as e:
            print(f"Warning: Could not load some assets: {e}")
            print("Game will continue with fallback rendering.")
            # Set all assets to None to use fallback rendering
            self.x_img = None
            self.o_img = None
            self.grid_img = None
            self.bg_img = None
            self.move_sound = None
            self.win_sound = None
            self.draw_sound = None
            self.you_win_voice = None
            self.ai_wins_voice = None
            self.draw_voice = None
    
    def reset_game(self):
        """Reset the game to initial state"""
        # Game board (3x3 grid)
        # 0 = empty, 1 = X (player 1), 2 = O (player 2 or AI)
        self.board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        
        # Current player (1 = X, 2 = O)
        self.current_player = 1
        
        # Game state
        self.game_over = False
        self.winner = None  # None, 1, 2, or 'draw'
        
        # AI thinking flag
        self.ai_thinking = False
    
    def draw_board(self):
        """Draw the game board"""
        # Draw background
        if self.bg_img:
            self.screen.blit(self.bg_img, (0, 0))
        else:
            self.screen.fill(WHITE)
        
        # Draw title
        font_large = pygame.font.Font(None, 60)
        title = font_large.render("Tic Tac Toe ❌⭕", True, BLACK)
        title_rect = title.get_rect(center=(WIDTH // 2, 50))
        self.screen.blit(title, title_rect)
        
        # Draw grid
        if self.grid_img:
            self.screen.blit(self.grid_img, (GRID_OFFSET_X, GRID_OFFSET_Y))
        else:
            # Fallback: Draw grid lines
            for i in range(1, GRID_SIZE):
                # Vertical lines
                pygame.draw.line(
                    self.screen, BLACK,
                    (GRID_OFFSET_X + i * CELL_SIZE, GRID_OFFSET_Y),
                    (GRID_OFFSET_X + i * CELL_SIZE, GRID_OFFSET_Y + CELL_SIZE * 3),
                    LINE_WIDTH
                )
                # Horizontal lines
                pygame.draw.line(
                    self.screen, BLACK,
                    (GRID_OFFSET_X, GRID_OFFSET_Y + i * CELL_SIZE),
                    (GRID_OFFSET_X + CELL_SIZE * 3, GRID_OFFSET_Y + i * CELL_SIZE),
                    LINE_WIDTH
                )
        
        # Draw X's and O's
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                cell = self.board[row][col]
                if cell != 0:
                    # Calculate position
                    x = GRID_OFFSET_X + col * CELL_SIZE + CELL_SIZE // 2
                    y = GRID_OFFSET_Y + row * CELL_SIZE + CELL_SIZE // 2
                    
                    if cell == 1:  # X
                        if self.x_img:
                            img_rect = self.x_img.get_rect(center=(x, y))
                            self.screen.blit(self.x_img, img_rect)
                        else:
                            # Fallback: Draw X
                            offset = 40
                            pygame.draw.line(self.screen, RED,
                                           (x - offset, y - offset),
                                           (x + offset, y + offset), 8)
                            pygame.draw.line(self.screen, RED,
                                           (x + offset, y - offset),
                                           (x - offset, y + offset), 8)
                    else:  # O
                        if self.o_img:
                            img_rect = self.o_img.get_rect(center=(x, y))
                            self.screen.blit(self.o_img, img_rect)
                        else:
                            # Fallback: Draw O
                            pygame.draw.circle(self.screen, BLUE, (x, y), 40, 8)
        
        # Draw current player indicator
        if not self.game_over:
            font_medium = pygame.font.Font(None, 36)
            if self.mode == GameMode.PVP:
                player_text = f"Player {'X' if self.current_player == 1 else 'O'}'s Turn"
            else:  # PVE mode
                if self.current_player == 1:
                    player_text = "Your Turn (X)"
                else:
                    player_text = "AI's Turn (O)"
            
            text = font_medium.render(player_text, True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, 620))
            self.screen.blit(text, text_rect)
    
    def draw_menu(self):
        """Draw the main menu for mode selection"""
        # Draw background
        if self.bg_img:
            self.screen.blit(self.bg_img, (0, 0))
        else:
            self.screen.fill(WHITE)
        
        # Draw title
        font_large = pygame.font.Font(None, 70)
        title = font_large.render("Tic Tac Toe ❌⭕", True, BLACK)
        title_rect = title.get_rect(center=(WIDTH // 2, 100))
        self.screen.blit(title, title_rect)
        
        # Draw subtitle
        font_medium = pygame.font.Font(None, 40)
        subtitle = font_medium.render("Select Game Mode", True, BLACK)
        subtitle_rect = subtitle.get_rect(center=(WIDTH // 2, 200))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Draw buttons
        font_button = pygame.font.Font(None, 50)
        
        # Player vs Player button
        pvp_rect = pygame.Rect(WIDTH // 2 - 150, 300, 300, 80)
        pygame.draw.rect(self.screen, LIGHT_GRAY, pvp_rect, border_radius=10)
        pygame.draw.rect(self.screen, BLACK, pvp_rect, 3, border_radius=10)
        pvp_text = font_button.render("Player vs Player", True, BLACK)
        pvp_text_rect = pvp_text.get_rect(center=pvp_rect.center)
        self.screen.blit(pvp_text, pvp_text_rect)
        
        # Player vs AI button
        pve_rect = pygame.Rect(WIDTH // 2 - 150, 420, 300, 80)
        pygame.draw.rect(self.screen, LIGHT_GRAY, pve_rect, border_radius=10)
        pygame.draw.rect(self.screen, BLACK, pve_rect, 3, border_radius=10)
        pve_text = font_button.render("Player vs AI", True, BLACK)
        pve_text_rect = pve_text.get_rect(center=pve_rect.center)
        self.screen.blit(pve_text, pve_text_rect)
        
        # Instructions
        font_small = pygame.font.Font(None, 30)
        inst_text = font_small.render("Click a button to start!", True, GRAY)
        inst_rect = inst_text.get_rect(center=(WIDTH // 2, 580))
        self.screen.blit(inst_text, inst_rect)
        
        return pvp_rect, pve_rect
    
    def draw_game_over(self):
        """Draw the game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(WHITE)
        self.screen.blit(overlay, (0, 0))
        
        # Draw result
        font_large = pygame.font.Font(None, 70)
        font_medium = pygame.font.Font(None, 40)
        
        if self.winner == 'draw':
            result_text = "It's a Draw!"
            color = GRAY
        elif self.mode == GameMode.PVP:
            result_text = f"Player {'X' if self.winner == 1 else 'O'} Wins!"
            color = RED if self.winner == 1 else BLUE
        else:  # PVE mode
            if self.winner == 1:
                result_text = "You Win! 🎉"
                color = GREEN
            else:
                result_text = "AI Wins! 🤖"
                color = RED
        
        result = font_large.render(result_text, True, color)
        result_rect = result.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        self.screen.blit(result, result_rect)
        
        # Draw restart instruction
        restart = font_medium.render("Press R to Restart", True, BLACK)
        restart_rect = restart.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        self.screen.blit(restart, restart_rect)
        
        # Draw menu instruction
        menu = font_medium.render("Press M for Menu", True, BLACK)
        menu_rect = menu.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        self.screen.blit(menu, menu_rect)
    
    def get_cell_from_mouse(self, pos):
        """Convert mouse position to board cell coordinates"""
        x, y = pos
        
        # Check if click is within the grid
        if (GRID_OFFSET_X <= x <= GRID_OFFSET_X + CELL_SIZE * 3 and
            GRID_OFFSET_Y <= y <= GRID_OFFSET_Y + CELL_SIZE * 3):
            
            col = (x - GRID_OFFSET_X) // CELL_SIZE
            row = (y - GRID_OFFSET_Y) // CELL_SIZE
            
            return row, col
        
        return None, None
    
    def make_move(self, row, col):
        """
        Make a move on the board
        Returns True if move was valid, False otherwise
        """
        # Check if cell is empty
        if self.board[row][col] == 0:
            # Place the mark
            self.board[row][col] = self.current_player
            
            # Play move sound
            if self.move_sound:
                self.move_sound.play()
            
            # Check for winner or draw
            if self.check_winner():
                self.game_over = True
                self.winner = self.current_player
                # Play win sound and voice
                if self.win_sound:
                    self.win_sound.play()
                if self.mode == GameMode.PVE:
                    if self.winner == 1 and self.you_win_voice:
                        pygame.time.wait(500)  # Small delay
                        self.you_win_voice.play()
                    elif self.winner == 2 and self.ai_wins_voice:
                        pygame.time.wait(500)
                        self.ai_wins_voice.play()
            elif self.is_board_full():
                self.game_over = True
                self.winner = 'draw'
                # Play draw sound and voice
                if self.draw_sound:
                    self.draw_sound.play()
                if self.draw_voice:
                    pygame.time.wait(500)
                    self.draw_voice.play()
            else:
                # Switch player
                self.current_player = 3 - self.current_player  # Toggles between 1 and 2
            
            return True
        
        return False
    
    def check_winner(self):
        """
        Check if there's a winner
        Returns True if current player has won, False otherwise
        """
        # Check rows
        for row in range(GRID_SIZE):
            if (self.board[row][0] == self.board[row][1] == self.board[row][2] == self.current_player):
                return True
        
        # Check columns
        for col in range(GRID_SIZE):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_player):
                return True
        
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player):
            return True
        
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player):
            return True
        
        return False
    
    def is_board_full(self):
        """Check if the board is full (no empty cells)"""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] == 0:
                    return False
        return True
    
    # ========================================================================
    # AI IMPLEMENTATION - MINIMAX ALGORITHM
    # ========================================================================
    
    def get_empty_cells(self):
        """Get list of all empty cells on the board"""
        empty = []
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] == 0:
                    empty.append((row, col))
        return empty
    
    def minimax(self, depth, is_maximizing, alpha=-float('inf'), beta=float('inf')):
        """
        Minimax algorithm with Alpha-Beta pruning
        
        This is the core AI algorithm that makes the computer unbeatable.
        
        HOW MINIMAX WORKS:
        ------------------
        1. The algorithm simulates all possible future game states
        2. It assigns scores to terminal states (win/lose/draw)
        3. It recursively evaluates positions by:
           - Maximizing score when it's AI's turn
           - Minimizing score when it's player's turn
        4. Alpha-Beta pruning optimizes by skipping branches that
           won't affect the final decision
        
        Parameters:
        -----------
        depth : int
            Current depth in the game tree (for optimization)
        is_maximizing : bool
            True if it's the maximizing player's turn (AI)
            False if it's the minimizing player's turn (Human)
        alpha : float
            Best value that the maximizer can guarantee
        beta : float
            Best value that the minimizer can guarantee
        
        Returns:
        --------
        int : Score of the position
            +10 if AI wins
            -10 if player wins
            0 if draw
        """
        
        # Check terminal states
        # If AI (player 2) wins
        if self.check_winner_for_player(2):
            return 10 - depth  # Prefer faster wins
        
        # If human (player 1) wins
        if self.check_winner_for_player(1):
            return depth - 10  # Prefer slower losses
        
        # If board is full (draw)
        if self.is_board_full():
            return 0
        
        if is_maximizing:
            # AI's turn - maximize score
            max_eval = -float('inf')
            
            for row, col in self.get_empty_cells():
                # Try this move
                self.board[row][col] = 2  # AI is player 2 (O)
                
                # Recursively evaluate
                eval_score = self.minimax(depth + 1, False, alpha, beta)
                
                # Undo move
                self.board[row][col] = 0
                
                # Update maximum
                max_eval = max(max_eval, eval_score)
                
                # Alpha-Beta pruning
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break  # Beta cut-off
            
            return max_eval
        
        else:
            # Human's turn - minimize score
            min_eval = float('inf')
            
            for row, col in self.get_empty_cells():
                # Try this move
                self.board[row][col] = 1  # Human is player 1 (X)
                
                # Recursively evaluate
                eval_score = self.minimax(depth + 1, True, alpha, beta)
                
                # Undo move
                self.board[row][col] = 0
                
                # Update minimum
                min_eval = min(min_eval, eval_score)
                
                # Alpha-Beta pruning
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break  # Alpha cut-off
            
            return min_eval
    
    def check_winner_for_player(self, player):
        """Check if a specific player has won"""
        # Check rows
        for row in range(GRID_SIZE):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
                return True
        
        # Check columns
        for col in range(GRID_SIZE):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        
        return False
    
    def get_best_move(self):
        """
        Find the best move for AI using Minimax algorithm
        
        Returns:
        --------
        tuple : (row, col) of the best move
        """
        best_score = -float('inf')
        best_move = None
        
        # Try all empty cells
        for row, col in self.get_empty_cells():
            # Try this move
            self.board[row][col] = 2  # AI is player 2
            
            # Evaluate using minimax
            score = self.minimax(0, False)
            
            # Undo move
            self.board[row][col] = 0
            
            # Update best move if this is better
            if score > best_score:
                best_score = score
                best_move = (row, col)
        
        return best_move
    
    # ========================================================================
    # MAIN GAME LOOP
    # ========================================================================
    
    def run(self):
        """Main game loop"""
        running = True
        pvp_rect = None
        pve_rect = None
        
        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.mode == GameMode.MENU:
                        # Handle menu clicks
                        mouse_pos = pygame.mouse.get_pos()
                        if pvp_rect and pvp_rect.collidepoint(mouse_pos):
                            self.mode = GameMode.PVP
                            self.reset_game()
                        elif pve_rect and pve_rect.collidepoint(mouse_pos):
                            self.mode = GameMode.PVE
                            self.reset_game()
                    
                    elif not self.game_over and not self.ai_thinking:
                        # Handle game clicks
                        if self.mode == GameMode.PVP or self.current_player == 1:
                            mouse_pos = pygame.mouse.get_pos()
                            row, col = self.get_cell_from_mouse(mouse_pos)
                            
                            if row is not None and col is not None:
                                self.make_move(row, col)
                
                elif event.type == pygame.KEYDOWN:
                    if self.game_over:
                        if event.key == pygame.K_r:
                            # Restart game
                            self.reset_game()
                        elif event.key == pygame.K_m:
                            # Back to menu
                            self.mode = GameMode.MENU
                            self.reset_game()
            
            # AI move (in PVE mode)
            if (self.mode == GameMode.PVE and 
                self.current_player == 2 and 
                not self.game_over and
                not self.ai_thinking):
                
                self.ai_thinking = True
                
                # Draw the board before AI thinks
                self.draw_board()
                pygame.display.flip()
                
                # Small delay for realism (AI "thinking")
                pygame.time.wait(500)
                
                # Get and make best move
                row, col = self.get_best_move()
                self.make_move(row, col)
                
                self.ai_thinking = False
            
            # Drawing
            if self.mode == GameMode.MENU:
                pvp_rect, pve_rect = self.draw_menu()
            else:
                self.draw_board()
                if self.game_over:
                    self.draw_game_over()
            
            # Update display
            pygame.display.flip()
            
            # Control frame rate
            self.clock.tick(60)
        
        # Quit
        pygame.quit()
        sys.exit()


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    """
    Main entry point of the game
    Creates a TicTacToe instance and runs it
    """
    game = TicTacToe()
    game.run()
