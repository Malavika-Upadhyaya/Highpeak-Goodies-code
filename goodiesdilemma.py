file1=open(r'C:\Users\Malavika Upadhyaya\Desktop\goodies\input.txt','r')
lines=file1.readlines()
goodies=[]
employee_count=int(lines[0][-2])
for i in range(4,len(lines)):
    l=lines[i].split(":")
    goodies.append([l[0],int(l[1])])
goodies=sorted(goodies,key=lambda x:x[1])
min_diff=float('inf')
for i in range(0,len(goodies)-employee_count+1):
    difference=goodies[i+employee_count-1][1]-goodies[i][1]
    if difference<min_diff:
        min_index=i
        min_diff=difference
file1.close()
file2=open(r'C:\Users\Malavika Upadhyaya\Desktop\goodies\output.txt','w')
file2.write("The goodies selected for distribution are:\n")
file2.write("\n")
for i in range(min_index,min_index+employee_count):
    file2.write(goodies[i][0]+":"+str(goodies[i][1])+"\n")
file2.write("\n")
file2.write("And the difference between the chosen goodie with highest price and the lowest price is "+ str(min_diff))
file2.close()
