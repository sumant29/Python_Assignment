class Square:
    try:
        def mapping(self,n):
            l = []
            for i in range(1,int(n)+1):
                l.append(i)
            return list(map(lambda x:x*x,l))
    except Exception as e:
        print(e)
obj = Square()
print(obj.mapping(20))
