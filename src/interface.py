import tkinter as tk
from tkinter import filedialog as fd
from afd import AFD
from afn import AFN
from read import read_AFD

class INTERFACE:

    def __init__(self, window):
        self.afd = 0
        self.afn = 0
        self.frame = window

    def create_afd(self):
        sigma = entry_sigma.get()
        Q = entry_Q.get().split(",")
        q0 = entry_q0.get()
        qf = entry_qf.get().split(",")

        delta = {}
        for entry in entry_delta.get("1.0", tk.END).split("\n"):
            if entry:
                values = entry.split(",")
                delta[(values[0], values[1])] = values[2]
        
        self.afd = AFD(sigma, Q, delta, q0, qf)
        lbl_automaton.config(text="AFD is ready!")

    def create_afn(self):
        sigma = entry_sigma.get()
        Q = entry_Q.get().split(",")
        q0 = set(entry_q0.get())
        qf = set(entry_qf.get().split(","))

        delta = {}
        for entry in entry_delta.get("1.0", tk.END).split("\n"):
            if entry:
                values = entry.split(",")
                delta[(values[0], values[1])] = set(values[2:])

        self.afn = AFN(sigma, Q, delta, q0, qf)
        lbl_automaton.config(text="AFN is ready!")

    def select_file_AFD(self):
        filename = fd.askopenfilename()
        self.afd = read_AFD(filename)
        lbl_automaton.config(text="AFD is ready!")

    def select_file_AFN(self):
        filename = fd.askopenfilename()
        lbl_automaton.config(text="AFN is ready!")

    def run_afd(self):
        lbl_result.config(text=str(self.afd.run(entry_word.get())))

    def run_afn(self):
        lbl_result.config(text=str(self.afn.run(entry_word.get())))

# Create the main window
window = INTERFACE(tk.Tk())
window.frame.title("Automaton Interface")

# Create labels and entry fields
lbl_sigma = tk.Label(window.frame, text="Sigma:").grid(row=1, column=1, sticky="W", pady=3, padx=5)
entry_sigma = tk.Entry(window.frame, width=30)
entry_sigma.grid(row=1, column=2, pady=3, padx=5)

lbl_Q = tk.Label(window.frame, text="Q:").grid(row=2, column=1, sticky="W",pady=3, padx=5)
entry_Q = tk.Entry(window.frame, width=30)
entry_Q.grid(row=2, column=2, pady=3, padx=5)

lbl_delta = tk.Label(window.frame, text="Delta:").grid(row=3, column=1, sticky="W",pady=3, padx=5)
entry_delta = tk.Text(window.frame, height=5, width=30)
entry_delta.grid(row=3, column=2, pady=3, padx=5)

lbl_q0 = tk.Label(window.frame, text="q0:").grid(row=8, column=1, sticky="W", pady=3, padx=5)
entry_q0 = tk.Entry(window.frame, width=30)
entry_q0.grid(row=8, column=2, pady=3, padx=5)

lbl_qf = tk.Label(window.frame, text="qf:").grid(row=9, column=1, sticky="W", pady=3, padx=5)
entry_qf = tk.Entry(window.frame, width=30)
entry_qf.grid(row=9, column=2, pady=3, padx=5)

lbl_word = tk.Label(window.frame, text="Word:").grid(row=10, column=1, sticky="W", pady=3, padx=5)
entry_word = tk.Entry(window.frame, width=30)
entry_word.grid(row=10, column=2, pady=3, padx=5)

# In case user wants to import AFD or AFN as a file
btn_open_file_afd = tk.Button(window.frame, text="Select AFD File", command=window.select_file_AFD).grid(row=11, column=1, pady=3, padx=5)
btn_open_file_afn = tk.Button(window.frame, text="Select AFN File", command=window.select_file_AFN).grid(row=11, column=2, pady=3, padx=5)

# Generate an automaton
btn_create_afd = tk.Button(window.frame, text="Create AFD", command=window.create_afd).grid(row=12, column=1, pady=3, padx=5)
btn_create_afn = tk.Button(window.frame, text="Create AFN", command=window.create_afn).grid(row=12, column=2, pady=3, padx=5)
lbl_automaton = tk.Label(window.frame, text="")
lbl_automaton.grid(row=12, column=3, pady=3, padx=5)

# Create the run button
btn_run_as_afd = tk.Button(window.frame, text="Run as AFD", command=window.run_afd).grid(row=14, column=1, pady=3, padx=5)
btn_run_as_afn = tk.Button(window.frame, text="Run as AFN", command=window.run_afn).grid(row=14, column=2, pady=3, padx=5)

# Plot the automaton as a oriented graph
#btn_generate_graph = tk.Button(window.frame, text="Plot Automaton", command=show_automaton).grid(row=11, column=2, pady=3, padx=5)
#image_automaton = tk.Image(imgtype=)

# Create the result label
lbl_result = tk.Label(window.frame, text="")
lbl_result.grid(row=14, column=3, pady=3, padx=5)

# Run the main loop
window.frame.mainloop()