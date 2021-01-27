
def countingsentence():
    sentencecount=-1
    filesentence = filenames.split(".")
    for elements in filesentence:
        sentencecount=sentencecount+1
    print (sentencecount)

def countingwords():
    wordcount=0
    filelist = filenames.split()
    print(filelist)
    for elements in  filelist:
        wordcount = wordcount+1
    print (wordcount)

filename = input("Enter the File's Path :")
print(filename)
file1 = open(filename)
filenames = file1.read()
choice = input("Press W for Wordcount or S for Sentencecount")
if(choice == "S"):
    countingsentence()
elif(choice == "W"):
    countingwords()
else:
    print("Please Enter a Proper Key")


 
 

     