import os
import winshell
import subprocess
import sys
# List of required libraries
required_libraries = ["winshell", 'gtts', 're', 'pygame', 'tkinter']

# Check and install missing libraries
for library in required_libraries:
    try:
        __import__(library)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])
        
# Define the target file and shortcut details
target_file = os.path.abspath("PressHereToStartTheApp")
desktop = winshell.desktop()
shortcut_path = os.path.join(desktop, "DartsApp2.0.lnk")

# Create the shortcut
with winshell.shortcut(shortcut_path) as shortcut:
    shortcut.path = target_file
    shortcut.description = "Shortcut to DartsApp2.0"
    shortcut.working_directory = os.path.dirname(target_file)

print(f"Shortcut created on desktop: {shortcut_path}")