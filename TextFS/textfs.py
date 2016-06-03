import os,re,sys






class textfs:
    MetaFile="/home/kbw/coding/L3cube/textfs/.Textfs"

#     def __init__(self):
#          MetaFile="/home/kbw/coding/L3cube/textfs/.Textfs"
#          if not (os.path.exists(self.MeataFile)):
#              os.system("touch "+self.MetaFile)
#   
#          else:
#              print ("File Exists")


    def no_of_lines(self,file):
        Flag=False
        fp=open(file,'r')
        max_line=0
        while Flag is False:
            k=fp.readline()
            if k=="":
                break
            else:
                max_line+=1
        fp.close()
        return max_line

    def create(self,file):
        fp1=open(file,'w')

        print ("Enter File data\n")
    #fp1.write(input("Enter File Data (Press cltr+D to End Writing"))
        lines=sys.stdin.readlines()
        count=0
        for line in lines:
            count+=1
            #fp1.write(line)
        fp1.close()
        fp1=open(file,'r')
        newfile_size=self.no_of_lines(file)+1
        fp=open(self.MetaFile,'r')
        maxmetafile_size=self.no_of_lines(self.MetaFile)
        if maxmetafile_size==0:
            maxmetafile_size+=1
        
        
        Metaline=fp.readline()
        Metaline=Metaline[:-1]
        Metaline=Metaline+"[ "+file+" "+str(int(maxmetafile_size)+1)+" "+str(count)+" ]$\n"
        
        
        
        fp1=open(file,'r')
        Flag=False
        while Flag==False:
            k=fp.readline()
            if k=="":
                Flag=True
            else:
                Metaline=Metaline+k
        fp.close()
                
        for line in lines:
            Metaline=Metaline+line
        
        
        fp=open(self.MetaFile,'w')
        fp.write(Metaline)
        fp.close()
        os.system( "rm "+file)
        

    def copy(self,file,path):
        
        fp1=open(path,'r')
        lines=fp1.readlines()
        count=0
        for line in lines:
            count+=1
            #fp1.write(line)
        fp1.close()
        
        fp1=open(path,'r')
        newfile_size=self.no_of_lines(path)+1
        
        fp=open(self.MetaFile,'r')
        maxmetafile_size=self.no_of_lines(self.MetaFile)
        if maxmetafile_size==0:
            maxmetafile_size+=1
        
        
        
        Metaline=fp.readline()
        Metaline=Metaline[:-1]
        Metaline=Metaline+"[ "+file+" "+str(int(maxmetafile_size)+1)+" "+str(count)+" ]$\n"
        
        
        fp1.close()
        fp1=open(path,'r')
        Flag=False
        while Flag==False:
            k=fp.readline()
            if k=="":
                Flag=True
            else:
                Metaline=Metaline+k
        fp.close()
                
        for line in lines:
            Metaline=Metaline+line
        
        
        fp=open(self.MetaFile,'w')
        fp.write(Metaline)
        fp.close()
        

    def delete(self,Filepath):
        newmetafile=""
        fp=open(self.MetaFile,'r')
        line=fp.readline()
        
        
        if line ==None:
            print ("No file Exists in File System")
            return
        flag=False
        files=line.split("$")
        for file in files:
            if file=="\n":
                break
            
            filemetadata=file.split(" ")
            filename=filemetadata[1]
            startline=filemetadata[2]
            no_of_lines=filemetadata[3]
            
            if filename==Filepath and flag==False:
                startline_delete=filemetadata[2]
                no_of_lines_delete=filemetadata[3]
                flag=True
                
            elif flag==True:
                startline=int(startline)-int(no_of_lines_delete)
                newmetafile=newmetafile+"[ " +filename+" "+str(startline)+" "+str(no_of_lines)+" ]$"
            
            else:
                newmetafile=newmetafile+file+"$"
        if flag==False:
            print("File Not Present")
            return
                
        newmetafile+="\n"
        for i in range (2,int(startline_delete)):
            newmetafile=newmetafile+fp.readline()
          
        for i in range(0,int (no_of_lines_delete)):
            fp.readline()
        F=False
        while F == False:
            k=fp.readline()
            if k =="":
                F=True
            else:
                newmetafile=newmetafile+k
        fp.close()
        
        fp=open(self.MetaFile,'w')
        fp.write(newmetafile)
        fp.close()
          
        print("File Deleted Successfully")
        
            

    def echo(self,Filepath):
        fp=open(self.MetaFile,'r')
        line=fp.readline()
        
        
        if line ==None:
            print ("No file Exists in File System")
            return
        flag=False
        files=line.split("$")
        
        for file in files:
            if file=="\n":
                break
        
            filemetadata=file.split(" ")    
            filename=filemetadata[1]
            startline=filemetadata[2]
            no_of_lines=filemetadata[3]
        
            if filename==Filepath and flag==False:
                startline_echo=startline
                no_of_lines_echo=no_of_lines
                flag=True
        if flag==False:
            print("No File Present")
            return
                    
        for i in range(2,int(startline_echo)):
            fp.readline()       
        for i in range(0,int(no_of_lines_echo)):
            file=file+fp.readline()
    
        print (file)
                            
    def ls(self):
        fp=open(self.MetaFile,'r')
        
        metaline=fp.readline()
        
        files=metaline.split("$")
        
        for file in files:
           filename=file.split(" ")
           if filename[0]=="\n":
               break
           else:
               print(filename[1]) 


textfs=textfs()



choice=raw_input("=======MENU======\n1.Create File \n2.Copy File\n3.delete file \n4.display file data\n5.list  Files\n6.Exit\n")


while(True):
    if choice=="1":
        file=raw_input("Enter File name\n")
        textfs.create(file)
        print("File Created Successfully\n")
        sys.stdin.flush()
        choice=""   
        choice=raw_input("=======MENU======\n1.Create File \n2.Copy File\n3.delete file \n4.display file data\n5.list  Files\n6.Exit\n")
        continue
    if choice=="2":
        newfile=raw_input("Enter NewFilename\n")
        oldfile=raw_input("Enter Old File name\n")
        textfs.copy(newfile,oldfile)
        print("File copied Successfully\n")
        choice=""
        choice=raw_input("=======MENU======\n1.Create File \n2.Copy File\n3.delete file \n4.display file data\n5.list  Files\n6.Exit\n")
        continue
    if choice=="3":
        file=raw_input("Enter File name\n")
        textfs.delete(file)
        choice=""
        choice=raw_input("=======MENU======\n1.Create File \n2.Copy File\n3.delete file \n4.display file data\n5.list  Files\n6.Exit\n")
        continue
    if choice=="4":
        file=raw_input("Enter File name\n")
        textfs.echo(file)
        choice=""
        choice=raw_input("=======MENU======\n1.Create File \n2.Copy File\n3.delete file \n4.display file data\n5.list  Files\n6.Exit\n")
        continue
    if choice=="5":
        textfs.ls()
        choice=""
        choice=raw_input("=======MENU======\n1.Create File \n2.Copy File\n3.delete file \n4.display file data\n5.list  Files\n6.Exit\n")
        continue
    if choice=="6":
        print ("Thank You\n")
        break
    else:
        print("Invalid Input\n")
        choice=""
        choice=raw_input("=======MENU======\n1.Create File \n2.Copy File\n3.delete file \n4.display file data\n5.list  Files\n6.Exit\n")
        continue
