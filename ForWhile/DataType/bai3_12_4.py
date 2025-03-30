import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from Crypto.Cipher import DES, DES3, AES
from Crypto.Util.Padding import pad, unpad
import binascii
import base64


class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mã hóa & Giải mã File")
        self.root.geometry("500x350")

        ttk.Label(root, text="Thuật toán:").grid(row=0, column=0, padx=10, pady=5)
        self.algorithm = ttk.Combobox(root, values=["DES", "TripleDES", "AES"], state="readonly")
        self.algorithm.grid(row=0, column=1, padx=10, pady=5)
        self.algorithm.current(0)

        ttk.Label(root, text="Tệp dữ liệu:").grid(row=1, column=0, padx=10, pady=5)
        self.input_file = ttk.Entry(root, width=40)
        self.input_file.grid(row=1, column=1, padx=10, pady=5)
        ttk.Button(root, text="Chọn", command=self.browse_input).grid(row=1, column=2, padx=5)

        ttk.Label(root, text="Khóa (hex):").grid(row=2, column=0, padx=10, pady=5)
        self.key_entry = ttk.Entry(root, width=40)
        self.key_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(root, text="Mã hóa", command=self.encrypt_file).grid(row=3, column=0, padx=10, pady=10)
        ttk.Button(root, text="Giải mã", command=self.decrypt_file).grid(row=3, column=1, padx=10, pady=10)

    def browse_input(self):
        file_path = filedialog.askopenfilename()
        self.input_file.delete(0, tk.END)
        self.input_file.insert(0, file_path)

    def get_key(self):
        try:
            key_hex = self.key_entry.get().strip()
            key = binascii.unhexlify(key_hex)

            algo = self.algorithm.get()
            if algo == "DES" and len(key) != 8:
                raise ValueError("Khóa DES phải có đúng 8 byte!")
            elif algo == "TripleDES" and len(key) not in [16, 24]:
                raise ValueError("Khóa TripleDES phải có 16 hoặc 24 byte!")
            elif algo == "AES" and len(key) not in [16, 24, 32]:
                raise ValueError("Khóa AES phải có 16, 24 hoặc 32 byte!")

            return key
        except Exception as e:
            messagebox.showerror("Lỗi", f"Khóa không hợp lệ: {e}")
            return None

    def encrypt_file(self):
        self.process_file(encrypt=True)

    def decrypt_file(self):
        self.process_file(encrypt=False)

    def process_file(self, encrypt=True):
        algo = self.algorithm.get()
        key = self.get_key()
        if not key:
            return

        try:
            with open(self.input_file.get(), 'rb') as file:
                data = file.read()

            iv = b'12345678' if algo != "AES" else b'1234567890123456'
            if algo == "DES":
                cipher = DES.new(key, DES.MODE_CBC, iv=iv)
            elif algo == "TripleDES":
                cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)
            elif algo == "AES":
                cipher = AES.new(key, AES.MODE_CBC, iv=iv)
            else:
                messagebox.showerror("Lỗi", "Thuật toán không hợp lệ!")
                return

            if encrypt:
                encrypted_data = cipher.encrypt(pad(data, cipher.block_size))
                encoded_data = base64.b64encode(encrypted_data)  # Chuyển thành Base64
                output_file = self.input_file.get() + ".enc"
                with open(output_file, 'wb') as file:
                    file.write(encoded_data)
            else:
                decoded_data = base64.b64decode(data)  # Giải mã Base64
                decrypted_data = unpad(cipher.decrypt(decoded_data), cipher.block_size)
                output_file = self.input_file.get().replace(".enc", ".dec")
                with open(output_file, 'wb') as file:
                    file.write(decrypted_data)

            messagebox.showinfo("Thành công", f"{('Mã hóa' if encrypt else 'Giải mã')} thành công! File: {output_file}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xử lý file: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()