tuple = ('apple', 'orange', 'banana', 'burger', 'fries' , 'cheese' , 'onions' , 'melon' , 'stawberry' )

print("There are: " + str(len(tuple)) + " items in the cart" )


for i in range(len(tuple)):
    print("This is item number " + str(i + 1)  + ": " +  str(tuple[i]) + ".")
    i = i+1
