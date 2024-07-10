import argparse
from cli import main
from gui import MyGUI
import tkinter as tk
from tkinter import ttk

def run_gui():
    print("Running GUI...")
    root = tk.Tk()
    my_gui = MyGUI(root)
    root.mainloop()  
   
def run_cli():
    print("Running CLI...")
    main()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the application in GUI or CLI mode.")
    
    # Define mutually exclusive group for --gui and --cli options
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--gui', action='store_true', help="Run the GUI interface.")
    group.add_argument('--cli', action='store_true', help="Run the CLI interface.")
    
    args = parser.parse_args()
    
    if args.gui:
        run_gui()
    elif args.cli:
        run_cli()