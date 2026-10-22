def createuser():
    uname = input("Enter the UserName:")
    fname = open(uname+".txt","w")
    fname.write("welcome to user ...."+uname)
    fname.write("\n I am very dengerous...")
    fname.close()
def getFileData(f):
    try:
        f1=open(f)
        print(f1.read())
        f1.close()
    except FileNotFoundError as f:
        print(f,"ide error")