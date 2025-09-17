import tkinter as tk

currentdataindex = 0
currenttotalpemasukan = 0
currenttotalpengeluaran = 0
data_pemasukan = []
data_pengeluaran = []

def pemasukanHandler():
    global currentdataindex
    global currenttotalpemasukan
    global data_pemasukan
    getlabel = name_input.get()
    getrp = float(maininput.get())
    print("Data didapatkan", getlabel)
    print("Data didapatkan", getrp)
    formatedrp = "Rp. " + str(getrp)
    data_pemasukan.append(getrp)
    listbox_name.insert(currentdataindex, getlabel)
    listbox_pemasukan.insert(currentdataindex, formatedrp)
    listbox_pengeluaran.insert(currentdataindex, 0)
    name_input.delete(0, tk.END)
    maininput.delete(0, tk.END)
    currentdataindex+=1
    for i in data_pemasukan:
        currenttotalpemasukan = currenttotalpemasukan + i
    labeltotalpemasukan["text"] = currenttotalpemasukan

def pengeluaranHandler():
    global currentdataindex
    global currenttotalpengeluaran
    global data_pengeluaran
    getlabel = name_input.get()
    getrp = float(maininput.get())
    print("Data didapatkan", getlabel)
    print("Data didapatkan", getrp)
    formatedrp = "Rp. " + str(getrp)
    data_pengeluaran.append(getrp)
    listbox_name.insert(currentdataindex, getlabel)
    listbox_pemasukan.insert(currentdataindex, 0)
    listbox_pengeluaran.insert(currentdataindex, formatedrp)
    name_input.delete(0, tk.END)
    maininput.delete(0, tk.END)
    currentdataindex+=1

    for i in data_pengeluaran:
        currenttotalpengeluaran = currenttotalpengeluaran + i
    labeltotalpengeluaran["text"] = currenttotalpengeluaran


window = tk.Tk()
window.title("manageME")
window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

frame_atas = tk.Frame(master=window, )
tittle_top = tk.Label(master=frame_atas, text="ManageME")
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


# frame_input.columnconfigure(1, weight=1)currentdataindex



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
    window.mainloop();