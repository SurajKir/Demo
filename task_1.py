class inst():
    count = 0
    def __init__(self, val):
        inst.count += 1
        if(inst.count<=10):
            self.val = val
        else:
            raise ValueError('Object limit exceeded')


for i in range(0,100):
    ins = inst(i)
