import tkinter as tk # import library tkinter
currentdataindex = 0 # untuk menyimpan posisi data sekarang
currenttotalpemasukan = 0 # variable untuk menyimpan total pemasukan
currenttotalpengeluaran = 0 # variable untuk menyimpan total pengeluaran
data_pemasukan = [] # list untuk menyimpan data pemasukan
data_pengeluaran = [] # list untuk menyimpan data pemasukan

def pemasukanHandler(): # Function untuk tombol pemaskan
    global currentdataindex # syntax untuk menggunakan global variable 
    global currenttotalpemasukan # syntax untuk menggunakan global variable
    global data_pemasukan # syntax untuk menggunakan global variable
    getlabel = name_input.get() # mendapatkan input label
    getrp = float(maininput.get()) # mendapatkan input nilai uang
    print("Data didapatkan", getlabel) # print ke terminal data yang telah di dapatkan
    print("Data didapatkan", getrp) # print ke terminal data yang telah di dapatkan
    formatedrp = "Rp. " + str(getrp) # format input rp menjadi string yang bagus
    data_pemasukan.append(getrp) # masukkan data uang
    listbox_name.insert(currentdataindex, getlabel) # tambahkan / catat label ke listbox
    listbox_pemasukan.insert(currentdataindex, formatedrp) # tambahkan / catat input uang ke listbox
    listbox_pengeluaran.insert(currentdataindex, 0) # tambahkan / catat input uang ke listbox
    name_input.delete(0, tk.END) # clear input box
    maininput.delete(0, tk.END) # clear input box
    currentdataindex+=1 # incremen posisi data sekarang
    for i in data_pemasukan: # pengulangan untuk menjumlahkan total uang ke total pemasukan
        currenttotalpemasukan = currenttotalpemasukan + i # logika untuk menambahkan data yang tersimpan ke total data
    labeltotalpemasukan["text"] = currenttotalpemasukan # tampilkan total data

def pengeluaranHandler(): # Function untuk tombol pemaskan
    global currentdataindex # syntax untuk menggunakan global variable
    global currenttotalpengeluaran # syntax untuk menggunakan global variable
    global data_pengeluaran # syntax untuk menggunakan global variable
    getlabel = name_input.get() # mendapatkan input label
    getrp = float(maininput.get()) # mendapatkan input nilai uang
    print("Data didapatkan", getlabel) # print ke terminal data yang telah di dapatkan
    print("Data didapatkan", getrp) # print ke terminal data yang telah di dapatkan
    formatedrp = "Rp. " + str(getrp) # format input rp menjadi string yang bagus
    data_pengeluaran.append(getrp) # masukkan data uang
    listbox_name.insert(currentdataindex, getlabel) # tambahkan / catat label ke listbox
    listbox_pemasukan.insert(currentdataindex, 0) # tambahkan / catat input uang ke listbox
    listbox_pengeluaran.insert(currentdataindex, formatedrp) # tambahkan / catat input uang ke listbox
    name_input.delete(0, tk.END) # clear input box
    maininput.delete(0, tk.END) # clear input box
    currentdataindex+=1 # incremen posisi data sekarang
    for i in data_pengeluaran: # pengulangan untuk menjumlahkan total uang ke total pemasukan
        currenttotalpengeluaran = currenttotalpengeluaran + i # logika untuk menambahkan data yang tersimpan ke total data
    labeltotalpengeluaran["text"] = currenttotalpengeluaran # tampilkan total data


window = tk.Tk() # inisiasi window dasar
window.title("manageME") # set window title

frame_atas = tk.Frame(master=window) # buat frame untuk bagian atas
tittle_top = tk.Label(master=frame_atas, text="ManageME") # buat title label
desc = tk.Label(master=frame_atas, text="Silahkan ketik Pengeluaran / Pemasukan mu!")

frame_input = tk.Frame(master=frame_atas)
labelName = tk.Label(master=frame_input, text="Label: ")
name_input = tk.Entry(master=frame_input, width=35)
labelRP = tk.Label(master=frame_input, text="Rp.")
maininput = tk.Entry(master=frame_input, width=35)
frame_2button = tk.Frame(master=frame_atas)
label_button = tk.Label(master=frame_2button, text="Catat sebagai: ")

button_pengeluaran = tk.Button(master=frame_2button, text="Pengeluaran",command=pengeluaranHandler)
button_pemasukan = tk.Button(master=frame_2button, text="Pemasukan", command=pemasukanHandler)

labelRP.grid(row=0, column=0,sticky=tk.E)
maininput.grid(row=0, column=1,sticky=tk.E)
labelName.grid(row=1, column=0)
name_input.grid(row=1, column=1,sticky=tk.E)

label_button.grid(row=0, column=0)
button_pengeluaran.grid(row=0, column=1)
button_pemasukan.grid(row=0, column=2)

tittle_top.pack()
desc.pack()
frame_input.pack()
frame_2button.pack(fill=tk.X)

frame_data = tk.Frame(master=window)
label_identifier = tk.Label(master=frame_data, text="Label")
label_pengeluaran = tk.Label(master=frame_data, text="Pengeluaran")
label_pemasukan = tk.Label(master=frame_data, text="Pemasukan") 

listbox_name = tk.Listbox(master=frame_data, width=30)
listbox_pengeluaran = tk.Listbox(master=frame_data, width=15)
listbox_pemasukan = tk.Listbox(master=frame_data, width=15)

label_identifier.grid(row=0, column=0)
label_pengeluaran.grid(row=0, column=1)
label_pemasukan.grid(row=0, column=2)
listbox_name.grid(row=1, column=0)
listbox_pengeluaran.grid(row=1, column=1)
listbox_pemasukan.grid(row=1, column=2)

frame_bawah = tk.Frame(master=window)
titletotalpengeluaran = tk.Label(master=frame_bawah, text="Total Pengeluaran: ")
titletotalpemasukan = tk.Label(master=frame_bawah, text="Total Pemasukan: ")
spacerbwh = tk.Label(master=frame_bawah, text="|")
labeltotalpengeluaran = tk.Label(master=frame_bawah, text=currenttotalpengeluaran)
labeltotalpemasukan = tk.Label(master=frame_bawah, text=currenttotalpemasukan)
titletotalpengeluaran.grid(row=0, column=0)
titletotalpemasukan.grid(row=0, column=3)
spacerbwh.grid(row=0,column=2)
labeltotalpengeluaran.grid(row=0, column=1)
labeltotalpemasukan.grid(row=0, column=4)

frame_atas.pack()
frame_data.pack()
frame_bawah.pack()

if __name__ == "__main__":
    window.mainloop()