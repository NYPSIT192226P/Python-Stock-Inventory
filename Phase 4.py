#Dominic Fu Ming Jun, 192226P, IT2153
SEQ = [2,3,5,7,8,10,15,16,23,28]
def binarySearch( theValues, target):
        #This is to go through the numbers in the list for the first number, X.
        for i in theValues:
            #This is to find the number that have to be added to X to get Z, which is Y
            SecNum = target - i
            # Start with the entire sequence of elements
            low = 0
            high = len(theValues) - 1
            # Repeatedly subdivide the sequence in half
            # until the target is found
            #This binary search is used to search for the second number Y to add with X
            # to get the value stated in Z
            while low <= high:
                # Find the midpoint of the sequence
                mid = (low + high)//2
                # Does the midpoint contain the target?
                # If yes, return midpoint (i.e. index of the list)
                #This is to check if the second number Y equals to the midpoint
                if theValues[mid] == SecNum:
                    #To check if both X and Y are the same value
                    #If they are not the same value,
                    if i != SecNum:
                        print("X = %d"%i)
                        print("Y = %d"%SecNum)
                        return True
                    #If they are the same value, then the loop breaks
                    else:
                        break
                # Or is the target before the midpoint?
                elif SecNum < theValues[mid]:
                    high = mid - 1
                    # Or is the target after the midpoint?
                else:
                    low = mid + 1
                    # If the sequence cannot be subdivided further,
                    # target is not in the list of values
        print("X = not found")
        print("Y = not found")
        return False # If not found, return False

testZ = int(input("Z: "))
print(binarySearch(SEQ,testZ))
