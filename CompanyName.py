class Name:
    def getname(self,str):
        char = ''
        c_name = ""
        for c in str:
            if c == '.':
                break
            if c == '@':
                char = c
            elif char == '@':
                c_name += c
        return c_name

str = input('Enter email:')
obj = Name()
print("Comapany Name:",obj.getname(str))