"""
Sound File Generator for Tic Tac Toe Game
This script creates simple sound effects using Python
"""

import wave
import struct
import math
import os

def create_beep_sound(filename, frequency=440, duration=0.1, volume=0.3):
    """Create a simple beep sound"""
    sample_rate = 44100
    num_samples = int(sample_rate * duration)
    
    # Generate samples
    samples = []
    for i in range(num_samples):
        # Generate sine wave
        sample = volume * math.sin(2 * math.pi * frequency * i / sample_rate)
        # Apply envelope (fade out)
        envelope = 1.0 - (i / num_samples) ** 2
        sample *= envelope
        # Convert to 16-bit integer
        samples.append(int(sample * 32767))
    
    # Write to WAV file
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 2 bytes per sample
        wav_file.setframerate(sample_rate)
        
        # Pack samples as binary data
        for sample in samples:
            wav_file.writeframes(struct.pack('<h', sample))

def create_chord_sound(filename, frequencies, duration=0.5, volume=0.2):
    """Create a chord sound (multiple frequencies)"""
    sample_rate = 44100
    num_samples = int(sample_rate * duration)
    
    # Generate samples
    samples = []
    for i in range(num_samples):
        sample = 0
        # Add all frequencies
        for freq in frequencies:
            sample += volume * math.sin(2 * math.pi * freq * i / sample_rate)
        
        # Normalize
        sample /= len(frequencies)
        
        # Apply envelope (fade out)
        envelope = 1.0 - (i / num_samples) ** 1.5
        sample *= envelope
        
        # Convert to 16-bit integer
        samples.append(int(sample * 32767))
    
    # Write to WAV file
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        
        for sample in samples:
            wav_file.writeframes(struct.pack('<h', sample))

def create_voice_sound(filename, text, duration=1.0):
    """Create a simple placeholder voice sound (just a tone pattern)"""
    sample_rate = 44100
    num_samples = int(sample_rate * duration)
    
    # Different patterns for different text
    if "win" in text.lower():
        # Ascending pattern
        base_freq = 300
        freq_change = 200
    elif "draw" in text.lower():
        # Flat pattern
        base_freq = 400
        freq_change = 0
    else:
        # Descending pattern
        base_freq = 500
        freq_change = -200
    
    samples = []
    for i in range(num_samples):
        # Varying frequency
        progress = i / num_samples
        freq = base_freq + freq_change * progress
        
        sample = 0.3 * math.sin(2 * math.pi * freq * i / sample_rate)
        
        # Apply envelope
        envelope = math.sin(math.pi * progress)
        sample *= envelope
        
        samples.append(int(sample * 32767))
    
    # Write to WAV file
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        
        for sample in samples:
            wav_file.writeframes(struct.pack('<h', sample))

# Create assets/sounds directory if it doesn't exist
os.makedirs('assets/sounds', exist_ok=True)

print("Creating sound files...")

# Create game sounds
print("- Creating move sound...")
create_beep_sound('assets/sounds/move.wav', frequency=600, duration=0.05, volume=0.3)

print("- Creating win sound...")
create_chord_sound('assets/sounds/win.wav', [523, 659, 784], duration=0.8, volume=0.25)  # C major chord

print("- Creating draw sound...")
create_beep_sound('assets/sounds/draw.wav', frequency=400, duration=0.3, volume=0.25)

# Create voice sounds (placeholder tones)
print("- Creating 'You Win' voice...")
create_voice_sound('assets/sounds/you_win.wav', "you win", duration=1.2)

print("- Creating 'AI Wins' voice...")
create_voice_sound('assets/sounds/ai_wins.wav', "ai wins", duration=1.2)

print("- Creating 'Draw' voice...")
create_voice_sound('assets/sounds/draw_voice.wav', "draw", duration=1.0)

print("\n✅ All sound files created successfully!")
print("\nNote: These are simple synthesized sounds.")
print("For better quality voice audio, you can:")
print("1. Record your own voice saying 'You Win', 'AI Wins', 'Draw'")
print("2. Use text-to-speech services")
print("3. Replace the .wav files in assets/sounds/ folder")
