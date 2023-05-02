try:
    from Xlib.display import Display
except ImportError:
    pass

import subprocess
import sys
import subprocess


def get_display_size():
    """
    Returns the size of the display in pixels as a tuple (width, height).

    This function tries different methods depending on the operating system to get the display size.
    If a method fails, it falls back to the next method.
    """
    width, height = None, None

    # Try using tkinter on Windows and macOS
    if sys.platform == "win32" or sys.platform == "darwin":
        try:
            import tkinter as tk

            root = tk.Tk()
            root.withdraw()
            width = root.winfo_screenwidth()
            height = root.winfo_screenheight()
            root.destroy()
        except:
            pass

    # Try using AppKit on macOS
    if sys.platform == "darwin" and (width is None or height is None):
        try:
            from AppKit import NSScreen

            width, height = NSScreen.mainScreen().frame().size
        except:
            pass

    # Try using Xlib on Linux and other Unix-based systems
    if sys.platform.startswith("linux") and (width is None or height is None):
        try:
            from Xlib.display import Display

            d = Display()
            s = d.screen()
            width = s.width_in_pixels
            height = s.height_in_pixels
        except:
            pass

    # Fallback method: parse output of xrandr command
    if width is None or height is None:
        try:
            output = subprocess.check_output(["xrandr"]).decode("utf-8")
            line = output.split("\n")[0]
            width, height = map(int, line.split()[-1].split("x"))
        except:
            pass

    # If all methods fail, return None
    if width is None or height is None:
        return None
    else:
        return width, height
