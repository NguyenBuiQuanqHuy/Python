import tkinter as tk
from tkinter import ttk, scrolledtext
from collections import Counter

# Phân tích tần số ký tự
def frequency_analysis(text):
    text = text.upper()
    counter = Counter(c for c in text if c.isalpha())
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)

# Thay thế ký tự dựa trên bảng thay thế
def decrypt(text, substitution_table):
    return ''.join(substitution_table.get(char, char) for char in text)

# Nhấn nút giải mã
def on_decrypt():
    update_table()
    cipher_text = input_text.get("1.0", tk.END).strip().upper()
    decrypted_text = decrypt(cipher_text, substitution_table)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

# Đếm tần số ký tự
def count_character_frequency():
    cipher_text = input_text.get("1.0", tk.END).strip().upper()
    freq = frequency_analysis(cipher_text)
    freq_dict = dict(freq)
    for entry in table_entries:
        letter = entry[0]
        freq_value = freq_dict.get(letter, 0)
        entry[2].config(text=str(freq_value))

# Cập nhật bảng thay thế
def update_table():
    global substitution_table
    substitution_table = {
        entry[0]: entry[1].get().upper() if entry[1].get().strip() else entry[0]
        for entry in table_entries
    }

def setup_gui():
    global input_text, output_text, table_entries

    root = tk.Tk()
    root.title("Mã thay thế đơn bảng")
    root.geometry("800x700")

    ttk.Label(root, text="Cipher Text:").pack(anchor='w', padx=10, pady=5)
    input_text = scrolledtext.ScrolledText(root, height=10, width=80)
    input_text.pack(padx=10, pady=10)

    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=5)
    ttk.Button(btn_frame, text="Giải mã", command=on_decrypt).pack(side=tk.LEFT, padx=10)
    ttk.Button(btn_frame, text="Đếm tần số", command=count_character_frequency).pack(side=tk.LEFT, padx=10)

    ttk.Label(root, text="Plain Text:").pack(anchor='w', padx=10, pady=5)
    output_text = scrolledtext.ScrolledText(root, height=10, width=80)
    output_text.pack(padx=10, pady=10)

    ttk.Label(root, text="Bảng thay thế (Ký tự - Thay thế - Tần số):").pack(anchor='w', padx=10, pady=5)
    table_frame = ttk.Frame(root)
    table_frame.pack()

    table_entries = []
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(13):
        for j in range(2):
            index = i + j * 13
            if index < len(letters):
                letter = letters[index]
                lbl = ttk.Label(table_frame, text=letter)
                lbl.grid(row=i, column=j * 3, padx=5)

                entry = ttk.Entry(table_frame, width=5)
                entry.grid(row=i, column=j * 3 + 1, padx=5)

                freq_label = ttk.Label(table_frame, text="0")
                freq_label.grid(row=i, column=j * 3 + 2, padx=5)

                table_entries.append((letter, entry, freq_label))

    root.mainloop()

substitution_table = {chr(i): chr(i) for i in range(65, 91)}

setup_gui()
