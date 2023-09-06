class Counter:
    def __init__(self, value=0):
        if value < 0:
            self.value = 0
        else:
            self.value = value

            
    def inc(self, num=1):
        self.value += num
        return self
    
    def dec(self, num=1):
        self.value -= num
        if self.value < 0:
            self.value = 0
        return self

c = Counter()
print(c.inc().inc(5).dec(2).value)