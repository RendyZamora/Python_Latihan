import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()

window.configure(bg="grey")
window.title("projek_python")
window.geometry("300x400")

frame1 = ttk.Frame(window)
frame1.pack(padx=10,pady=10,fill="x",expand=True)

nama_depan = ttk.Label(frame1,text="Nama Depan")
nama_depan.pack(padx=10,pady=3,fill="x",expand=True)
NAMA_DEPAN = tk.StringVar()
input_namadepan = ttk.Entry(frame1, textvariable= NAMA_DEPAN)
input_namadepan.pack(padx=10,pady=3,fill="x",expand=True)

nama_depan = ttk.Label(frame1,text="Nama Belakang")
nama_depan.pack(padx=10,pady=3,fill="x",expand=True)
NAMA_BELAKANG = tk.StringVar()
input_namadepan = ttk.Entry(frame1, textvariable= NAMA_BELAKANG)
input_namadepan.pack(padx=10,pady=3,fill="x",expand=True)

def pencet():
    showinfo(title="PESAN!",message= f"Selamat Datang {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}")
tombol_submit = tk.Button(frame1,text="SUBMIT",background="skyblue", command= pencet)
tombol_submit.pack(padx=15,pady=3, expand=True)

window.mainloop()