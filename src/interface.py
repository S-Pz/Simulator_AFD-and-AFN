import tkinter as tk

class AFD:
    def __init__(self, sigma, Q, delta, q0, qf):
        self.sigma = sigma
        self.Q = Q
        self.delta = delta
        self.q0 = q0
        self.qf = qf
    
    def run(self, w):
        q = self.q0
    
        while w != "":
            q = self.delta[(q, w[0])]
            w = w[1:]
        return q in self.qf

def create_afd():
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
    lbl_result.config(text=str(automaton.run(entry_word.get())))

# Create the main window
window = tk.Tk()
window.title("Automaton Interface")

# Create labels and entry fields
lbl_sigma = tk.Label(window, text="Sigma:")
lbl_sigma.pack()
entry_sigma = tk.Entry(window)
entry_sigma.pack()

lbl_Q = tk.Label(window, text="Q:")
lbl_Q.pack()
entry_Q = tk.Entry(window)
entry_Q.pack()

lbl_delta = tk.Label(window, text="Delta (comma-separated):")
lbl_delta.pack()
entry_delta = tk.Text(window, height=5, width=30)
entry_delta.pack()

lbl_q0 = tk.Label(window, text="q0:")
lbl_q0.pack()
entry_q0 = tk.Entry(window)
entry_q0.pack()

lbl_qf = tk.Label(window, text="qf (comma-separated):")
lbl_qf.pack()
entry_qf = tk.Entry(window)
entry_qf.pack()

lbl_word = tk.Label(window, text="Word:")
lbl_word.pack()
entry_word = tk.Entry(window)
entry_word.pack()

# Create the run button
btn_run = tk.Button(window, text="Run", command=create_afd)
btn_run.pack()

# Create the result label
lbl_result = tk.Label(window, text="")
lbl_result.pack()

# Run the main loop
window.mainloop()
