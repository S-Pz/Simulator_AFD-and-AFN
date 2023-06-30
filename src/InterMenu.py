import tkinter as tk
import InterAFDandAFN
import InterPilha

window = tk.Tk()
window.title("Escolha o tipo de automato")
window.geometry("300x200")

# AFD and AFN
btn_AfnAfd = tk.Button(text="AFD ou AFN", command = InterAFDandAFN.openInterface)
btn_AfnAfd.place(x=75, y=20, anchor=tk.CENTER)
#btn_AfnAfd.grid(row=0, column=0, padx=75, pady=20)

pushdown= tk.Button(text="Automanto de Pilha", command= InterPilha.openInterface)
pushdown.grid(row=1, column=0, padx=75, pady=0)

#btn_AfnAfd.pack()
#pushdown.pack()

window.mainloop()