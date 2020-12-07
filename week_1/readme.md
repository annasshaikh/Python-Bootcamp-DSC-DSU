# Week 1 Assignments

Here the Week 1 Assignment from the Python Bootcamp DSC-DSU

## Assignment #1

Questain: Define a function to print a string diagonally

```python

def  cross_print(name): #Printing a function
    space = 0 
    a=1
    for i in name: #Loop For the number of carracter
        if len(name)-(2*space) > 0 : #len(name)-(2*space) Difference th String Lenght and Spaces to be add in end
            print(" "*space + i + " "*(len(name)-(2*space)) + i)
        else:
            print(" "*(1+space-2*a) + i + " "*((2*a)-1) + i)
            a += 1
        space += 1

def main():
     cross_print(input("Enter The String: "))
    

if __name__ == '__main__':
	main() #Calling Main Function

```
Output:

<a href="https://imgbb.com/"><img src="https://i.ibb.co/3W38ZkG/Output-Assissgment-1.png" alt="Output-Assissgment-1" border="0"></a>

## Assignment #2

Questain: Create a program to take as input 5 student records in the following format:

```
**roll_num** | **name** | **age** | **marks**(out of 100)
```

And then output the records in a tabular form with class average, class highest and class lowest at end in the following format.

- Use dictionaries (list of dictionaries in exact)
- Insert atleast 5 records
- Input must be user-given
- (Optional) validate the user input, i.e marks aren't greater 100 and other such validations you think there might be

Well Here Is My Approch:
```python
data2 = {'roll_number' : ['','','','',''],
         'name' : ['','','','',''],
         'mark' : ['','','','',''],
         'age' : ['','','','','']} #Empyt Dictionary With List 
highest , avg , lowest , a , b = 0 , 0 , 100 , 0 , 0
for i in range(5):
    data2["roll_number"][i] = input(f"Enter The Student {i+1} Roll Number: ")
    data2["name"][i] = input(f"Enter The Student {i+1} Name: ")
    data2["mark"][i] = int(input(f"Enter The Student {i+1} marks: "))#inputs for list
    if (data2["mark"][i] > highest):
        highest = data2["mark"][i]    #Get Current Highest
        a = i                         #Get its Index
    if (data2["mark"][i] < lowest):
        lowest = data2["mark"][i]     #Get Current Lowest
        b = i                         #Get its Index
    avg += data2["mark"][i]           #totaling Marks
    data2["age"][i] = int(input(f"Enter The Student {i+1} age: "))
    print("")
#Printing Every thing in Cell Form
print("Type\tRN\tName\tAge\tMarks")
print(f"Lowest\t{data2['roll_number'][b]}\t{data2['name'][b]}\t{data2['age'][b]}\t{data2['mark'][b]}")
print(f"Highest\t{data2['roll_number'][a]}\t{data2['name'][a]}\t{data2['age'][a]}\t{data2['mark'][a]}")
print("")
print(f"Class Average = {avg/5}" )

```
Output:

<a href="https://imgbb.com/"><img src="https://i.ibb.co/gDDjYhy/Output-Assissgment-2.png" alt="Output-Assissgment-2" border="0"></a>

## Assignment #3

Questain: A function that will print lyrics of given song with 1 second delay between each line.

   - Use time.sleep()
   - Use split() function of string

My Approch:

```python

import time #Imported For Function time.sleep()
anthum = "Pak sarzameen shad bad,Kishwar-e-Haseen shad bad ,Tou Nishaan-e-Azm-e-aali shan ,Arz-e-Pakistan ,Markaz-e-yaqeen Shad bad,Pak sarzameen ka nizaam Qouwat-e-Akhouwat-e-Awam ,Qaum mulk saltanat ,Painda tabinda bad Shad bad Manzil-e-murad ,Parcham-e-Sitara-o-Hilall ,Rahbar-e-Tarakkeey-o-Kamal ,Tarjuman-e-mazee-shaan-e-Hal Jan-e-Istaqbal ,Saaya-e-Khuda-e-zuljalal" #Saved The whole Anthum in string
x = anthum.split(",") #Break into string to list with divider,
for i in range(0,len(x),1): #Print 1 Line a time with 1 sec delay
    print(x[i])
    time.sleep(1)

```
Output:

<a href="https://imgbb.com/"><img src="https://i.ibb.co/Wz5C3LL/Output-Assissgment-3.png" alt="Output-Assissgment-3" border="0"></a>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

