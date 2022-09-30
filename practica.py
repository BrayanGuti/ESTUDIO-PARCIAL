class Nodo:
    def __init__(self, coef, expo):
        self.coef = coef
        self.expo = expo
        self.next = None
        
    def __repr__(self):
        return str(f"{self.coef}x^{self.expo[0]}y^{self.expo[1]}z^{self.expo[2]}")
class linkedList:
    def __init__(self) -> None:
        self.PTR = None
        self.last = None
    def addNode(self, data1, data2):
        p = Nodo(coef = data1, expo = data2)
        if (self.PTR== None):
            self.PTR=p
            self.last=p
        else:
            self.last.next=p
            self.last=p #en caso de que sea simple
        self.last.next=self.PTR #en caso de que sea circular
    def recorrer(self):
        p = self.PTR
        
        while(p.next != self.PTR):
            if(p.next.coef > 0):
                print(p, end="+")
            p = p.next
        
        print(p)
        
        print("")
    
    def sumar (self, lista):
        t = lista.PTR
        self.sumar_ter(t)
        t = t.next
        while (t != lista.PTR):
            self.sumar_ter(t)
            t = t.next
    

    def sumar_ter (self, term):
        p = self.PTR
        otro = True
        if (term.expo == p.expo):
            p.coef = p.coef + term.coef
            otro = False
        p = p.next

        while (p != self.PTR):
            if (term.expo == p.expo):
                p.coef = p.coef + term.coef
                otro = False
            p = p.next
            
        if (otro == True):
            self.addNode(term.coef, term.expo) 

