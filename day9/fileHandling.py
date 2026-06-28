#text file(.txt)
#CSV file (.csv)
#JSON file(.json)
#Excel file(.xlsx)

#opening a file

#syntax
#file =open(filename,mode)


#file =open("trial.txt", "r")

#content =file.read
#print(content)
#file.close()

#with open('trial.txt','r') as file:
    #data = file.read()

#print(data)    

#reading line by line
#with open('trial.txt','r') as file:
 #   for line in file:
       # print(line.strip())

#appending a file, use the sample repo.txt append

#real world example
#attendance system 
#live demo

name =input('Enter Student:')
with open('attendance.txt', 'a') as file:
    #save
    file.write(name + '\n')
print('student saved successfully')  

#work with a CSV file
#what is CSV? Comma Separated values