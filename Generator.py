class SimpleGenerator:
    def generate(self,n):
        for i in range(int(n)+1):
            yield i

n = input('Enter the number: ')
obj = SimpleGenerator()
ans = obj.generate(n)
l = []
for i in ans:
    if i % 7 == 0 and i % 5 == 0:
        l.append(i)
print(l)