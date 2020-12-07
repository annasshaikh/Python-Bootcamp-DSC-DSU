
def  cross_print(name):
    space = 0
    a=1
    for i in name:
        if len(name)-(2*space) > 0 :
            print(" "*space + i + " "*(len(name)-(2*space)) + i)
        else:
            print(" "*(1+space-2*a) + i + " "*((2*a)-1) + i)
            a += 1
        space += 1

def main():
     cross_print(input("Enter The String: "))
    

if __name__ == '__main__':
	main()
