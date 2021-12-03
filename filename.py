#open function return a file object
#always open the file
#file = open(filename , mode)
f1 = open("myfile.txt","r")  

print(f1.readline())
print(f1.read(5))
#always close the file
f1.close()
