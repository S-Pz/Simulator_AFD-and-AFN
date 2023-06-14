class AFD:

    def __init__(self,sigma,Q,delta,q0,qf):

        self.sigma = sigma # alfabeto
        self.Q = Q # conjunto de estados
        self.delta = delta # conjunto de transições
        self.q0 = q0 #estado inicial
        self.qf = qf #estado final

    #def __repr__(self):
    #    return f"AFD({self.sigma},\n\t{self.Q},\n\t{self.delta},\n\t{self.q0},\n\t{self.qf}\n)"
    
    def run(self, w):
        q = self.q0
    
        while w!="":
            q = self.delta[(q,w[0])]
            w = w[1:]
        return q in self.qf
    
D0 = AFD({"a","b"},{0,1,2},{(0,"a"):0,(0,"b"):1,(1,"a"):2,(1,"b"):1,(2,"a"):2,(2,"b"):2}, 0, {0,1})
#D0.run("ab")
#print(D0.run("bba"))
