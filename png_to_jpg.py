import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def convert_to_jpg():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    
    if file_path:
        try:
            img = Image.open(file_path)
            
            # Convert the image to RGB mode if it has an alpha channel
            if img.mode == "RGBA":
                img = img.convert("RGB")
            
            jpg_file_path = file_path[:-4] + ".jpg"  # Change file extension to .jpg
            img.save(jpg_file_path)
            messagebox.showinfo("Success", "Image converted to JPG")
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Conversion Failed")

# Create the main window
root = tk.Tk()
root.title("PNG to JPG Converter")

# Calculate center position of the window
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a frame to hold the content
frame = tk.Frame(root)
frame.pack(expand=True)

# Button to select file and convert to JPG
select_button = tk.Button(frame, text="Browse for PNG", command=convert_to_jpg)
select_button.pack()

# Run the application
root.mainloop()
