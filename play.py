#!/usr/bin/env python3
"""
🎮 TIC TAC TOE - GAME LAUNCHER 🎮
This launcher checks dependencies and starts the game
"""

import sys
import subprocess

def check_pygame():
    """Check if pygame is installed"""
    try:
        import pygame
        print("✅ Pygame is installed (version {})".format(pygame.version.ver))
        return True
    except ImportError:
        print("❌ Pygame is not installed!")
        return False

def install_pygame():
    """Install pygame using pip"""
    print("\n📦 Installing pygame...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
        print("✅ Pygame installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install pygame")
        print("\nPlease install manually:")
        print("  pip3 install pygame")
        return False

def main():
    """Main launcher function"""
    print("=" * 60)
    print("  🎮 TIC TAC TOE - GAME LAUNCHER ❌⭕")
    print("=" * 60)
    print()
    
    # Check pygame
    if not check_pygame():
        print("\n🔧 Pygame is required to run this game.")
        response = input("Would you like to install it now? (y/n): ").lower().strip()
        
        if response == 'y' or response == 'yes':
            if not install_pygame():
                sys.exit(1)
        else:
            print("\n⚠️  Cannot start game without pygame.")
            print("Install it manually with: pip3 install pygame")
            sys.exit(1)
    
    # Import and start game
    print("\n🚀 Starting game...")
    print("-" * 60)
    print()
    
    try:
        from tictactoe import TicTacToe
        game = TicTacToe()
        game.run()
    except Exception as e:
        print(f"\n❌ Error starting game: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure all files are in place")
        print("2. Check that assets/ folder exists")
        print("3. Try running: python3 tictactoe.py directly")
        sys.exit(1)

if __name__ == "__main__":
    main()
