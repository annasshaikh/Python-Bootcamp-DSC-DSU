data2 = {'roll_number' : ['','','','',''],
         'name' : ['','','','',''],
         'mark' : ['','','','',''],
         'age' : ['','','','','']}
highest , avg , lowest , a , b = 0 , 0 , 100 , 0 , 0
for i in range(5):
    data2["roll_number"][i] = input(f"Enter The Student {i+1} Roll Number: ")
    data2["name"][i] = input(f"Enter The Student {i+1} Name: ")
    data2["mark"][i] = int(input(f"Enter The Student {i+1} marks: "))
    if (data2["mark"][i] > highest):
        highest = data2["mark"][i]
        a = i
    if (data2["mark"][i] < lowest):
        lowest = data2["mark"][i]
        b = i
    avg += data2["mark"][i]
    data2["age"][i] = int(input(f"Enter The Student {i+1} age: "))
    print("")

print("Type\tRN\tName\tAge\tMarks")
print(f"Lowest\t{data2['roll_number'][b]}\t{data2['name'][b]}\t{data2['age'][b]}\t{data2['mark'][b]}")
print(f"Highest\t{data2['roll_number'][a]}\t{data2['name'][a]}\t{data2['age'][a]}\t{data2['mark'][a]}")
print("")
print(f"Class Average = {avg/5}" )
