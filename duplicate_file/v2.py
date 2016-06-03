import hashlib
import os
from stat import *


class Node:

    def __init__(self,hash):
        self.hash =hash
        self.files=list()
        self.next_node = None


    def get_hash(self):
        return self.hash

    def get_files(self):
        return self.files

    def get_file_index(self,index):
        return self.files[index]

    def set_files(self,file):
        self.files.append(file)

    def get_next(self):
        return self.next_node


    def set_next(self, new_next):
        self.next_node = new_next



class DuplicateChecker:


    def __init__(self):
        self.head=None
    
    def insert(self,hash): 
        n = Node(hash)
        if self.head is None:
            self.head=n
        else:
            n.set_next(self.head)
            self.head = n


    def search_hash(self,hash):
        current = self.head
        found = False
        while current and found is False:
            if current.get_hash() == hash:
                found = True
            else:
                current = current.get_next()
        return current

    def hashchecker(self,file,blocksize=65535):
        afile = open(file, 'rb')
        hasher = hashlib.md5()
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)    
        afile.close()
        return hasher.hexdigest()


                    
    def duplicate(self,Dir):
        
        
        for dirpath, dirnames, filenames in os.walk(Dir):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                statmode=os.stat(full_path).st_mode
                if not S_ISDIR(statmode):
                    hash=self.hashchecker(full_path)
                    current=self.search_hash(hash)
                    if  current is None:
                        self.insert(hash)
                        self.head.set_files(full_path)
                    else:
                        current.set_files(full_path)
                
                    

    def printfiles(self):
        current = self.head
        if current is not None:
            while current is not None:
                print("============================\n")
                print(current.get_hash())
                count=0
                for i in current.get_files():
                    print(current.get_file_index(count))
                    count=count+1
                print("============================\n")
                current = current.get_next()

    def delete(self,nodeindex,fileindex):
        print("In delete")
        print (fileindex)
        current=self.head
        for i in range(0,int(nodeindex)):
            current=current.get_next()

        file=current.get_file_index(int(fileindex))
        os.remove(file)
            
                    
        

dc=DuplicateChecker()
dc.duplicate("/home/kbw/Desktop/tecmint") 
dc.printfiles()

choice=raw_input("1.Delete File\n 2.Exit")

if int(choice)==1:
    nodeindex=raw_input("Enter Node Index In which file Exist\n")
    fileindex=raw_input("Enter File Index in above specified Node\n")

    dc.delete(int(nodeindex),int(fileindex))
    print("File Deleted Successfully")

dc.printfiles()





    