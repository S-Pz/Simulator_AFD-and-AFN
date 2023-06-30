import tkinter as tk
import InterAFDandAFN
import InterPilha

window = tk.Tk()
window.title("Escolha o tipo de automato")
window.geometry("350x150")

# AFD and AFN
btn_AfnAfd = tk.Button(text="AFD ou AFN", command = InterAFDandAFN.openInterface)
btn_AfnAfd.place(height=40, x=75, y=20)
#btn_AfnAfd.grid(row=0, column=0, padx=75, pady=20)

pushdown= tk.Button(text="Automanto de Pilha", command= InterPilha.openInterface)
pushdown.place(height=40,x=75, y=60)

#btn_AfnAfd.pack()
#pushdown.pack()

window.mainloop()