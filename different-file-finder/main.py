import sys
import os
import hashlib

file_ext=['js','css','jpg','jpeg','png','gif']

def main(dirname1,dirname2):
    fileSet1=set(os.listdir(dirname1))
    fileSet2=set(os.listdir(dirname2))
    unionSet=fileSet1.union(fileSet2)
    if unionSet==fileSet1 and unionSet==fileSet2:
        for i in unionSet:
            newdirname1=os.path.join(dirname1,i)
            newdirname2=os.path.join(dirname2,i)
            if os.path.isdir(newdirname1) and os.path.isdir(newdirname2):
                main(newdirname1,newdirname2)
            elif os.path.isfile(newdirname1) and os.path.isfile(newdirname2):
                if(get_md5(newdirname1)!=get_md5(newdirname2)):
                    if newdirname1.split(".")[-1].lower() in file_ext:
                        print("file different:"+newdirname1+" and "+newdirname2+"(which is likely to be visited)")
                    else:
                        print("file different:"+newdirname1+" and "+newdirname2)
            else:
                print("{} or {} is a dir while the other is a file".format(newdirname1,newdirname2))
    else:
        if unionSet-fileSet1:
            print(dirname1+'new: '+','.join(unionSet-fileSet1))
        if unionSet-fileSet2:
            print(dirname2+'new: '+','.join(unionSet-fileSet2))


def get_md5(filename):
    with open(filename,'rb') as f:
        filemd5=hashlib.md5(f.read()).hexdigest()
    return filemd5
if __name__=="__main__":
    dirname1=sys.argv[1]
    dirname2=sys.argv[2]
    main(dirname1,dirname2)