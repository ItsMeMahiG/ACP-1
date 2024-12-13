def shutdown():
    confirm=input("Do you want to shut down? : ")
    if confirm=="yes" :
        print ("shutting down...")
    elif confirm=="no" :
        print("aborting shut down")
    else :
        print("please only give yes or no answers!")

shutdown()