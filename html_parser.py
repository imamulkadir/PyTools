import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.scrolledtext as scrolledtext
import pyperclip

root = tk.Tk()
root.title("HTML Code Copy")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the Tk root window to be centered
x_coordinate = int((screen_width - 800) / 2)  # Assuming width = 800
y_coordinate = int((screen_height - 500) / 2)  # Assuming height = 500

root.geometry(f"800x500+{x_coordinate}+{y_coordinate}")

# Dictionary to store HTML codes for each button
html_codes = {
    "Black Line Code": '''<TABLE CELLSPACING="0" CELLPADDING="0" STYLE="width: 100%; border-collapse: collapse">
<TR STYLE="vertical-align: top">
<TD STYLE="width: 100%; border-bottom: #A6A6A6 1pt solid; font: 7pt Arial, Helvetica, Sans-Serif; padding-right: 5.4pt; padding-left: 5.4pt">&nbsp;</TD></TR>
</TABLE>''',
    "Footer w/ Image": '''<P STYLE="font: 10pt Arial, Helvetica, Sans-Serif; margin: 6pt 0 8pt 0pt; text-align: center"><IMG SRC="image_002.jpg" ALT="" STYLE="height: 28px; width: 258px"></P>
<P STYLE="font: 7pt/7pt Arial, Helvetica, Sans-Serif; margin: 8pt 0 8pt 0pt; text-align: center"><B>Selling Agent</B></P>''',
    "Footer w/o Image": '''<P align="center" STYLE="margin: 6pt; font: 16pt Calibri, Helvetica, Sans-Serif; color: #002060"><b>BofA Securities</b></P>
<P STYLE="font: 9pt/93% Calibri, Helvetica, Sans-Serif; margin: 0; text-align: center; color: #58595B"><B>Selling Agent</B></P>''',
    "Underlying Stock Image": '''<IMG SRC="image_002.jpg" ALT="" STYLE="height: 20pt; width: 90pt; vertical-align: middle">''',
    "1st Graphic Table": '''<P STYLE="text-align: center;font: 10pt Arial, Helvetica, Sans-Serif; margin: 0 0 0 0pt"><IMG SRC="image_gt1.jpg" ALT="" STYLE="height: 177.75pt; width: 558pt"></P>''',
    "2nd Graphic Table": '''<P STYLE="text-align: center;font: 10pt Arial, Helvetica, Sans-Serif; margin: 0 0 6pt 0pt"><IMG SRC="image_gt2.jpg" ALT="" STYLE="height: 330pt; width: 558pt"></P>''',
    "Single Graphic Table": '''<P STYLE="font: bold 11pt Calibri, Helvetica, Sans-Serif; margin: 5pt 0 3 0pt; color: #E84563"><IMG SRC="image_gt.jpg" STYLE="height: 700pt; width: 650pt"></P>''',
    "Provided": "Proofs will be provided shortly.",
    "Updated": "Proofs have been updated.",
    "gg": "gg"
}

# Text area for displaying HTML code
html_display = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
html_display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Function to copy HTML code to clipboard
def copy_html(button_text):
    code_to_copy = html_codes.get(button_text, "No HTML code found")
    pyperclip.copy(code_to_copy)
    html_display.delete('1.0', tk.END)  # Clear the text area
    html_display.insert(tk.END, code_to_copy)  # Display copied HTML code

# Function to create buttons and assign copy functionality
def create_button(button_text, row_val, col_val):
    button = tk.Button(root, text=button_text, command=lambda text=button_text: copy_html(text))
    button.grid(row=row_val, column=col_val, padx=5, pady=5)  # Use grid for button placement
    button.config(width=20)  # Set button width for uniform size

# Create 5 buttons in the first row
for i, button_text in enumerate(list(html_codes.keys())[:5]):
    create_button(button_text, 1, i)

# Create 5 buttons in the second row
for i, button_text in enumerate(list(html_codes.keys())[5:], start=5):
    create_button(button_text, 2, i - 5)

root.mainloop()
