# get two integer parameters
# return sum
def plus(x, y):
    return x+y

# main function
def main():
    print("Welcome to calcuator")
    while True:        
        print("0: exit, 1: plus")
        check = input()
        if check == "1":
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", plus(x,y))
        elif check == "0":
            print("Thank you")
	    break
        else:
            print("Please enter number")

if __name__ == "__main__":
    main()
