class AFN:
    def __init__(self,sigma,Q,delta,q0,qf):

        self.sigma = sigma # alfabeto
        self.Q = Q # conjunto de estados
        self.delta = delta # conjunto de transições
        self.q0 = q0 #estado inicial S
        self.qf = qf #estado final 
    
    def do_delta(self, q, x):
        try:
            return self.delta[(q,x)]
        except KeyError:
            return set({})
        
    def run(self,w):
        P = self.q0
        while w!="":
            Pnew = set({})
            for q in P:
                Pnew = Pnew | self.do_delta(q, w[0])
            w = w[1:]
            P = Pnew
        return (P & self.qf) != set({})
    
#N0 = AFN({"0","1"},{0,1,2},{(0,"0"):{0},(0,"1"):{0,1},(1,"0"):{2},(1,"1"):{2}},{0},{2})

#print(N0.run("11"))#true
#print(N0.run("01"))#false
#print(N0.run("10"))#true
#print(N0.run("00"))#false
#print(N0.run("11"))#true
