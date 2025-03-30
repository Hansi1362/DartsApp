import os
import winshell

target_file = os.path.abspath("PressHereToStartTheApp")
desktop = winshell.desktop()
shortcut_path = os.path.join(desktop, "DartsApp2.0.lnk")

# Create the shortcut
with winshell.shortcut(shortcut_path) as shortcut:
    shortcut.path = target_file
    shortcut.description = "Shortcut to DartsApp2.0"
    shortcut.working_directory = os.path.dirname(target_file)

print(f"Shortcut created on desktop: {shortcut_path}")
