import tkinter as tk
from tkinter import ttk, scrolledtext
import collections
import string


def frequency_analysis(text):
    text = text.upper()
    counter = collections.Counter(text)
    total = sum(counter.values())

    result = "Tần suất chữ cái:\n"
    for char, freq in sorted(counter.items(), key=lambda x: -x[1]):
        if char in string.ascii_uppercase:
            result += f"{char}: {freq} ({freq / total:.2%})\n"
    return result


def digram_analysis(text):
    text = text.upper()
    digrams = collections.Counter([text[i:i + 2] for i in range(len(text) - 1)])

    result = "\nTần suất digram:\n"
    for pair, freq in digrams.most_common(10):
        result += f"{pair}: {freq}\n"
    return result


def substitute(text, mapping):
    text = text.upper()
    return "".join(mapping.get(char, char) for char in text)


def analyze_text():
    cipher_text = input_text.get("1.0", tk.END).strip().upper()
    analysis_result = frequency_analysis(cipher_text) + digram_analysis(cipher_text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, analysis_result)


def decrypt_text():
    cipher_text = input_text.get("1.0", tk.END).strip().upper()
    update_mapping()
    decrypted_text = substitute(cipher_text, substitution_table)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)


def update_mapping():
    global substitution_table
    substitution_table = {
        entry[0]: entry[1].get().upper() if entry[1].get().strip() else entry[0]
        for entry in table_entries
    }


def setup_gui():
    global input_text, output_text, table_entries
    root = tk.Tk()
    root.title("Phá mã thay thế đơn bảng")
    root.geometry("800x700")

    ttk.Label(root, text="Văn bản mã hóa:").pack(anchor='w', padx=10, pady=5)
    input_text = scrolledtext.ScrolledText(root, height=10, width=80)
    input_text.pack(padx=10, pady=10)

    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=5)
    ttk.Button(btn_frame, text="Phân tích", command=analyze_text).pack(side=tk.LEFT, padx=10)
    ttk.Button(btn_frame, text="Giải mã", command=decrypt_text).pack(side=tk.LEFT, padx=10)

    ttk.Label(root, text="Kết quả:").pack(anchor='w', padx=10, pady=5)
    output_text = scrolledtext.ScrolledText(root, height=10, width=80)
    output_text.pack(padx=10, pady=10)

    ttk.Label(root, text="Bảng thay thế (Ký tự - Thay thế):").pack(anchor='w', padx=10, pady=5)
    table_frame = ttk.Frame(root)
    table_frame.pack()

    table_entries = []
    letters = string.ascii_uppercase

    for i in range(13):
        for j in range(2):
            index = i + j * 13
            if index < len(letters):
                letter = letters[index]
                lbl = ttk.Label(table_frame, text=letter, width=3, anchor="center")
                lbl.grid(row=i, column=j * 2, padx=5, sticky="w")

                entry = ttk.Entry(table_frame, width=5)
                entry.grid(row=i, column=j * 2 + 1, padx=5, sticky="w")

                table_entries.append((letter, entry))

    root.mainloop()


substitution_table = {chr(i): chr(i) for i in range(65, 91)}

setup_gui()