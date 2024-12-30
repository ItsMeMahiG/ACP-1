test={'science': 17,'math': 19,'english': 17,'hindi': 17,'kannada':17,'social':19}
print("the original dictionary: ",str(test))
tval=int(input("which number's occurences would you like to check? : "))
count=0
for key in test :
    if test[key]==tval :
        count=count+1

print("number of occurrences of the value u asked for : "+str(count))