import os

def tree(path):
    try:
        for files in os.listdir(path):
            if path[len(path)-1 ] == '/':
                new_path = path+files
                if os.path.isdir(new_path):
                    print("Folder :",new_path)
                    tree(new_path+'/')
                else:
                    print(files)
            else:
                raise Exception("Invalid Path: 'Folder path has \'/\' at the last !'")
    except Exception as e:
        print(e)


path = 'E:/DG/Assignment/test_db-master/'
tree(path)