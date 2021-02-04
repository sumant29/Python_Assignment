class Rev_iterator:
    def __init__(self,l):
        self.x = l[::-1]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.x):
            i = self.i
            self.i+=1
            return self.x[i]
        else:
            raise StopIteration()
    def next(self):
        return self.__next__()

obj = Rev_iterator([1,2,3,4,5,6,7,8,9,10])
while True:
    try:
        print(obj.next())
    except StopIteration:
        break

