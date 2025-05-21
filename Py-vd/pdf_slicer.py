import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter

def slice_pdf(input_path, start_page, end_page):
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        total_pages = len(reader.pages)
        if start_page < 1 or end_page > total_pages or start_page > end_page:
            raise ValueError(f"Pages must be between 1 and {total_pages}, and start <= end.")

        for i in range(start_page - 1, end_page):
            writer.add_page(reader.pages[i])

        base = os.path.splitext(input_path)[0]
        output_path = f"{base}_sliced_{start_page}-{end_page}.pdf"

        with open(output_path, "wb") as f:
            writer.write(f)

        messagebox.showinfo("Success", f"Created: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if filepath:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, filepath)

def run_slicer():
    path = entry_file.get()
    try:
        start = int(entry_start.get())
        end = int(entry_end.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Start and end pages must be numbers.")
        return

    if not os.path.exists(path):
        messagebox.showerror("File Error", "The selected file does not exist.")
        return

    slice_pdf(path, start, end)

# Build GUI
root = tk.Tk()
root.title("PDF Page Slicer")
root.geometry("400x200")
root.resizable(False, False)

# File selection
tk.Label(root, text="PDF File:").pack(pady=(10, 0))
entry_file = tk.Entry(root, width=40)
entry_file.pack()
tk.Button(root, text="Browse", command=browse_file).pack(pady=(0, 10))

# Page range
frame_pages = tk.Frame(root)
frame_pages.pack()

tk.Label(frame_pages, text="Start Page:").grid(row=0, column=0, padx=5)
entry_start = tk.Entry(frame_pages, width=5)
entry_start.grid(row=0, column=1)

tk.Label(frame_pages, text="End Page:").grid(row=0, column=2, padx=5)
entry_end = tk.Entry(frame_pages, width=5)
entry_end.grid(row=0, column=3)

# Slice button
tk.Button(root, text="Slice PDF", command=run_slicer, bg="darkgreen", fg="white").pack(pady=15)

root.mainloop()
