# I. Jenny's secret message

# Jenny has written a function that returns a greeting for a user.
# However, she's in love with Johnny, and would like to greet him slightly different.
# She added a special case to her function, but she made a mistake.

def greats ():
    name = input("Your name: ")
    if name == 'John':
     print ("Hello my dear,",name)
    else:
        print ("Hello,",name,".")
greats()

