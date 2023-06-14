import tkinter as tk
from tkinter import filedialog as fd
from functools import partial
from afd import AFD
from afn import AFN
from read import read_AFD

def create_afd(automaton):
    sigma = entry_sigma.get()
    Q = entry_Q.get().split(",")
    q0 = entry_q0.get()
    qf = entry_qf.get().split(",")
    
    delta = {}
    for entry in entry_delta.get("1.0", tk.END).split("\n"):
        if entry:
            values = entry.split(",")
            delta[(values[0], values[1])] = values[2]
    
    automaton = AFD(sigma, Q, delta, q0, qf)
    #lbl_result.config(text=str(automaton.run(entry_word.get())))

def create_afn(automaton):
    sigma = entry_sigma.get()
    Q = entry_Q.get().split(",")
    q0 = entry_q0.get()
    qf = entry_qf.get().split(",")

    delta = {}
    for entry in entry_delta.get("1.0", tk.END).split("\n"):
        if entry:
            values = entry.split(",")
            delta[(values[0], values[1])] = values[2]

    automaton = AFN(sigma, Q, delta, q0, qf)
    #lbl_result.config(text=str(automaton.run(entry_word.get())))

def select_file(automaton):
    filename = fd.askopenfilename()
    automaton = read_AFD(filename)
    #lbl_result.config(text=str(automaton.run(entry_word.get())))

def run_automaton(automaton):
    lbl_result.config(text=str(automaton.run(entry_word.get())))

# Create the main window
window = tk.Tk()
window.title("Automaton Interface")

# Create labels and entry fields
lbl_sigma = tk.Label(window, text="Sigma:").grid(row=1, column=1, sticky="W", pady=3, padx=5)
entry_sigma = tk.Entry(window, width=30)
entry_sigma.grid(row=1, column=2, pady=3, padx=5)

lbl_Q = tk.Label(window, text="Q:").grid(row=2, column=1, sticky="W",pady=3, padx=5)
entry_Q = tk.Entry(window, width=30)
entry_Q.grid(row=2, column=2, pady=3, padx=5)

lbl_delta = tk.Label(window, text="Delta:").grid(row=3, column=1, sticky="W",pady=3, padx=5)
entry_delta = tk.Text(window, height=5, width=30)
entry_delta.grid(row=3, column=2, pady=3, padx=5)

lbl_q0 = tk.Label(window, text="q0:").grid(row=8, column=1, sticky="W", pady=3, padx=5)
entry_q0 = tk.Entry(window, width=30)
entry_q0.grid(row=8, column=2, pady=3, padx=5)

lbl_qf = tk.Label(window, text="qf:").grid(row=9, column=1, sticky="W", pady=3, padx=5)
entry_qf = tk.Entry(window, width=30)
entry_qf.grid(row=9, column=2, pady=3, padx=5)

lbl_word = tk.Label(window, text="Word:").grid(row=10, column=1, sticky="W", pady=3, padx=5)
entry_word = tk.Entry(window, width=30)
entry_word.grid(row=10, column=2, pady=3, padx=5)

# just to create something
automaton = 0

# Create automaton button
afd_with_arg = partial(create_afd, automaton)
create_as_afd = tk.Button(window, text="Create AFD", command=afd_with_arg).grid(row=12, column=1, pady=3, padx=5)

afn_with_arg = partial(create_afn, automaton)
create_as_afn = tk.Button(window, text="Create AFN", command=afn_with_arg).grid(row=12, column=2, pady=3, padx=5)

# In case user wants to import AFD or AFN as a file
file_with_arg = partial(select_file, automaton)
create_as_file = tk.Button(window, text="Select File", command=file_with_arg).grid(row=12, column=3, pady=3, padx=5)

# Run automaton

run_with_arg = partial(run_automaton, automaton)
btn_run_automaton = tk.Button(window, text="Run automaton", command=run_with_arg).grid(row=13, column=1, pady=3, padx=5)

# Create the result label
lbl_result = tk.Label(window, text=" ")
lbl_result.grid(row=12, column=3, pady=3, padx=5)

# Run the main loop
window.mainloop()
