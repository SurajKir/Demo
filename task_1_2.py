class inst():
    __count = 0
    @staticmethod
    def getInstance():
        if(inst.__count<10):
            inst()
        else:
            raise Exception('Object limit exceeded') 
        return inst.__count
        
    def __init__(self):
        if(inst.__count<10):
            inst.__count += 1
            self.self = self
        else:
            raise Exception('Object limit exceeded')
            


for i in range(0,100):
    ins = inst.getInstance()
    
