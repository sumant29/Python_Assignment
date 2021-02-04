class array:
    try:
        def __init__(self,i,j,k):
            self.arr = [[[0 for x in range(k)]for y in range(j)]for z in range(i)]
            print(self.arr)
    except Exception as e:
        print(e)


obj = array(3,5,8)