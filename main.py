import tkinter as tk

window = tk.Tk();
window.title("manageME");


frame_atas = tk.Frame(master=window, )
tittle_top = tk.Label(master=frame_atas, text="ManageME")
desc = tk.Label(master=frame_atas, text="Silahkan ketik Pengeluaran / Pemasukan mu!")
tittle_top.pack()
desc.pack()

frame_bawah = tk.Frame(master=window, )
    

frame_atas.pack()
frame_bawah.pack()

if __name__ == "__main__":
    window.mainloop();