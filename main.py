
# Importing
import tkinter as tk # import library tkinter


# Define Global Variable
currentdataindex = 0 # untuk menyimpan posisi data sekarang
currenttotalpemasukan = 0 # variable untuk menyimpan total pemasukan
currenttotalpengeluaran = 0 # variable untuk menyimpan total pengeluaran
data_pemasukan = [] # list untuk menyimpan data pemasukan
data_pengeluaran = [] # list untuk menyimpan data pengeluaran

# Function
def pemasukanHandler(): # Function untuk tombol pemasukan
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

def pengeluaranHandler(): # Function untuk tombol ppengeluaran
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
    for i in data_pengeluaran: # pengulangan untuk menjumlahkan total uang ke total pengeluaran
        currenttotalpengeluaran = currenttotalpengeluaran + i # logika untuk menambahkan data yang tersimpan ke total data
    labeltotalpengeluaran["text"] = currenttotalpengeluaran # tampilkan total data

# Main WIndow
window = tk.Tk() # inisiasi window dasar
window.title("manageME") # set window title

frame_atas = tk.Frame(master=window) # buat frame untuk bagian atas
tittle_top = tk.Label(master=frame_atas, text="ManageME") # buat title label
desc = tk.Label(master=frame_atas, text="Silahkan ketik Pengeluaran / Pemasukan mu!") # buat label deskripsi

frame_input = tk.Frame(master=frame_atas) # buat frame untuk bagian atas
labelName = tk.Label(master=frame_input, text="Label: ") # buat labe disamping input label
name_input = tk.Entry(master=frame_input, width=35) # buat kolom input label
labelRP = tk.Label(master=frame_input, text="Rp.") # buat label di samping input uang
maininput = tk.Entry(master=frame_input, width=35) # buat kolom input uang
frame_2button = tk.Frame(master=frame_atas) # buat frame untuk bagian tombol
label_button = tk.Label(master=frame_2button, text="Catat sebagai: ") # buat label disamping tombol

button_pengeluaran = tk.Button(master=frame_2button, text="Pengeluaran",command=pengeluaranHandler) # buat button pengeluaran
button_pemasukan = tk.Button(master=frame_2button, text="Pemasukan", command=pemasukanHandler) # buat button pemasukan

labelRP.grid(row=0, column=0,sticky=tk.E) # tampilkan labelrp dengan methode grid pada row 1 col 1
maininput.grid(row=0, column=1,sticky=tk.E) # tampilkan kolom input uang dengan methode grid pada row 1 col 2
labelName.grid(row=1, column=0) # tampilkan labelname dengan methode grid pada row 2 col 1
name_input.grid(row=1, column=1,sticky=tk.E) # tampilkan kolom input label dengan methode grid pada row 2 col 2

label_button.grid(row=0, column=0) # tampilkan tulisan button dengan methode grid pada row 1 col 1
button_pengeluaran.grid(row=0, column=1) # tampilkan tombol pengeluaran dengan methode grid pada row 1 col 2
button_pemasukan.grid(row=0, column=2) # tampilkan tombol pemasukan dengan methode grid pada row 1 col 0

tittle_top.pack() # tampilkan label judul dengan methode pack
desc.pack() # tampilkan label deskripsi dengan methode pack
frame_input.pack() # tampilkan frame input judul dengan methode pack
frame_2button.pack(fill=tk.X) # tampilkan frame button dengan methode pack lalu ratakan posisi x

frame_data = tk.Frame(master=window) # buat frame data
label_identifier = tk.Label(master=frame_data, text="Label") # buat label label
label_pengeluaran = tk.Label(master=frame_data, text="Pengeluaran") # buat label pengeluaran
label_pemasukan = tk.Label(master=frame_data, text="Pemasukan")  # buat label pemasukan

listbox_name = tk.Listbox(master=frame_data, width=30) # buat listbox label
listbox_pengeluaran = tk.Listbox(master=frame_data, width=15) # buat listbox pengeluaran
listbox_pemasukan = tk.Listbox(master=frame_data, width=15) # buat listbox pemasukan

label_identifier.grid(row=0, column=0) # tampilkan label label dengan methode grid pada row 1 col 1
label_pengeluaran.grid(row=0, column=1) # tampilkan label pengeluaran dengan methode grid pada row 1 col 2
label_pemasukan.grid(row=0, column=2) # tampilkan label pemasukan dengan methode grid pada row 1 col 3
listbox_name.grid(row=1, column=0) # tampilkan listbox label dengan methode grid pada row 2 col 1
listbox_pengeluaran.grid(row=1, column=1) # tampilkan listbox pengeluaran dengan methode grid pada row 2 col 2
listbox_pemasukan.grid(row=1, column=2) # tampilkan listbox pemasukan dengan methode grid pada row 2 col 3

frame_bawah = tk.Frame(master=window) # buat frame untuk bagian bawah
titletotalpengeluaran = tk.Label(master=frame_bawah, text="Total Pengeluaran: ") # buat label total pengeluaran
titletotalpemasukan = tk.Label(master=frame_bawah, text="Total Pemasukan: ") # buat label total pengeluaran
spacerbwh = tk.Label(master=frame_bawah, text="|") # buat label spacer
labeltotalpengeluaran = tk.Label(master=frame_bawah, text=currenttotalpengeluaran) # buat label angka total pengeluaran
labeltotalpemasukan = tk.Label(master=frame_bawah, text=currenttotalpemasukan) # buat label angka total pemasukan
titletotalpengeluaran.grid(row=0, column=0) # tampilkan label total pengeluaran dengan methode grid pada row 1 col 1
titletotalpemasukan.grid(row=0, column=3) # tampilkan label total pemasukan dengan methode grid pada row 1 col 4
spacerbwh.grid(row=0,column=2) # tampilkan label spacer dengan methode grid pada row 1 col 3
labeltotalpengeluaran.grid(row=0, column=1) # tampilkan total pengeluaran dengan methode grid pada row 1 col 2
labeltotalpemasukan.grid(row=0, column=4) # tampilkan total pemasukan dengan methode grid pada row 1 col 5

frame_atas.pack() # tampilkan frame atas dengan methode pack
frame_data.pack() # tampilkan frame tengah / data dengan methode pack
frame_bawah.pack() # tampilkan frame bawah dengan methode pack


# Execution
if __name__ == "__main__": # cek file ini sebagai main / file utama
    window.mainloop() # jalankan loop utama