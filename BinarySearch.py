#Creating a class Binary Search
class BS:
    try:
        #method takes a list and which element to search and return index
        def get_index(self,l,elem):
            #getting the left and right most index of list
            left = 0
            right = len(l)
            while(left<=right):
                mid = int((left + right)/2)
                list_elem = l[mid]
                #if the element at mid return else choose one side to search 
                if list_elem == elem:
                    return mid
                if list_elem < elem:
                    left = mid +1
                if list_elem > elem:
                    right = mid -1
            return -1
    except Exception as e:
        print(e)

obj = BS()
res = obj.get_index([1,2,6,9,11,15,27,32,86],19)
if res == -1:
    print("Not Found")
else:
    print("Element at index:",res)