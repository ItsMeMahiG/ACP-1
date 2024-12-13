try :
    age=int(input("plese enter your age : "))
    if age % 2 == 0:
        print("your age is an even number")
    else :
        print("your age is an odd number")
except ValueError :
    print("please enter numbers only..")
except :
    print ("an error has occured, please try again")