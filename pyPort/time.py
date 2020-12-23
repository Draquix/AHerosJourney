class widget:
    def __init__(self):
        self.socket = []

    def plugIn(self, plug):
        self.socket.append(plug)

class woozle:
    def __init__(self,ident):
        self.ident = ident
        self.quantity = 1

draq = widget()
vitamin = woozle("iron")
draq.plugIn(vitamin)
pill = woozle("iron")
draq.plugIn(pill)
pill = woozle("iron"
draq.plugIn(pill)
print(draq.socket)


