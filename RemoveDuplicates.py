
class Rem_Duplicate:

    def remove_dup(self,l):
        try:
            self.result = list(set(l))
            lis = []
            for x in l:
                if x in self.result and x not in lis:
                    lis.append(x)
            return lis
        except Exception as e :
            print(e)


obj = Rem_Duplicate()
print(obj.remove_dup([12,24,35,24,88,120,155,88,120,155]))