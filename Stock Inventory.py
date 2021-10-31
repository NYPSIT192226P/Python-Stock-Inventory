#Dominic Fu Ming Jun, 192226P, IT2153
#A dictionary to list the product deails to the product SKU
ProductDict = [{'sku':1,"name":"Bread","description":"Soft, fluffy white bread","selling price": 5.50,"buying price":3.50,"stock level": 40, "country": "Singapore"},
               {'sku':2,"name":"Milk","description":"Creamy Milk","selling price": 3.50,"buying price":1.50,"stock level": 260,"country": "Malaysia"},
               {'sku':3,"name":"Cheese","description":"Hard cheese","selling price": 4.50,"buying price":2.50,"stock level": 150,"country": "Thailand"},
               {'sku':4,"name":"Apple","description":"Sweet apples","selling price": 2.00,"buying price":1.50,"stock level": 470,"country": "Indonesia"},
               {'sku':5,"name":"Butter","description":"Savory Butter","selling price": 6.50,"buying price":4.50,"stock level": 390,"country": "China"},
               {'sku':6,"name":"Orange","description":"Juicy orange","selling price": 5.00,"buying price":3.50,"stock level": 260,"country": "Malaysia"},
               {'sku':7,"name":"Grape","description":"Many big grapes","selling price": 4.00,"buying price":1.20,"stock level": 100,"country": "Indonesia"},
               {'sku':8,"name":"Pear","description":"Crunchy pear","selling price": 5.00,"buying price":2.70,"stock level": 110,"country": "Indonesia"},
               {'sku':9,"name":"Peach","description":"Tangy peach","selling price": 4.00,"buying price":2.50,"stock level": 10,"country": "China"},
               {'sku':10,"name":"Banana","description":"Large and soft bananas","selling price": 9.45,"buying price":5.55,"stock level": 20,"country": "Singapore"},
               {'sku':11,"name":"Bread","description":"WholeGrain Bread","selling price": 3.73,"buying price":1.70,"stock level": 100,"country": "Thailand"},
               {'sku':12,"name":"Apple","description":"Crunchy Apples","selling price": 2.95,"buying price":1.90,"stock level": 530,"country": "Malaysia"},
               {'sku':13,"name":"Peach","description":"Sweet, juicy, fuzzy Peaches","selling price": 3.50,"buying price":2.45,"stock level": 210,"country": "Singapore"},
               {'sku':14,"name":"Banana","description":"Sweet, delicious bananas","selling price": 4.00,"buying price":2.50,"stock level": 390,"country": "Indonesia"},
               {'sku':15,"name":"Beef","description":"Big and juicy Beef ","selling price": 15.95,"buying price":12.75,"stock level": 70,"country": "China"},
               {'sku':16,"name":"Chili","description":"Super spicy chili","selling price": 5.55,"buying price":2.75,"stock level": 100,"country": "Malaysia"},
               {'sku':17,"name":"Beer","description":"6-pack beer","selling price": 7.45,"buying price":4.75,"stock level": 70,"country": "Indonesia"},
               {'sku':18,"name":"Mango","description":"Juicy mangos","selling price": 3.95,"buying price":1.75,"stock level": 70,"country": "Thailand"},
               {'sku':19,"name":"Ham","description":"Huge, delicious ham","selling price": 8.25,"buying price":4.60,"stock level": 70,"country": "Singapore"},
               {'sku':20,"name":"Ham","description":"Sweet and succulent bacon ham","selling price": 9.90,"buying price":7.70,"stock level": 1900,"country": "China"},
               {'sku':21,"name":"Carrots","description":"Crunchy and big carrots","selling price": 5.95,"buying price":2.75,"stock level": 890,"country": "Singapore"},
               {'sku':22,"name":"Beets","description":"Delicious beets","selling price": 4.45,"buying price": 2.35,"stock level": 170,"country": "Thailand"},
               {'sku':23,"name":"Avogadro","description":"Flavourful and sweet avogadro","selling price": 3.95,"buying price":1.75,"stock level": 180,"country": "Malaysia"},
               {'sku':24,"name":"Watermelon ","description":"Sweet and juicy watermellon","selling price": 14.45,"buying price": 12.75,"stock level": 350,"country": "Indonesia"},
               {'sku':25,"name":"Melon","description":"Big and sweet melon","selling price": 9.35,"buying price":5.75,"stock level": 240,"country": "Malaysia"},
               {'sku':26,"name":"Fish","description":"30 pound salmon","selling price": 11.35,"buying price":8.65,"stock level": 130,"country": "Singapore"},
               {'sku':27,"name":"Eggs","description":"A dozen fresh eggs","selling price": 12.70,"buying price":10.40,"stock level": 200,"country": "Indonesia"},
               {'sku':28,"name":"Soap","description":"Sakura scented body soap","selling price": 10.35,"buying price":8.75,"stock level": 30,"country": "Thailand"},
               {'sku':29,"name":"Cucumber","description":"Long, crunchy and bitter cucumber","selling price": 3.35,"buying price":1.25,"stock level": 300,"country": "China"},
               {'sku':30,"name":"Butter","description":"Long stick of creamy goat butter","selling price": 4.35,"buying price":2.25,"stock level": 430,"country": "Malaysia"},
               {'sku':31,"name":"Bread","description":"Sunshine All-Natural California Raisin Bread","selling price": 3.35,"buying price":1.95,"stock level": 530,"country": "Singapore"},
               {'sku':32,"name":"Apple","description":"Small, crunchy, green apples","selling price": 4.35,"buying price":2.25,"stock level": 410,"country": "Indonesia"},
               {'sku':33,"name":"Chocolate","description":"Cadbury light chocolate","selling price": 3.55,"buying price":1.25,"stock level": 30,"country": "Malaysia"},
               {'sku':34,"name":"Tomato","description":"Large tomato","selling price": 1.35,"buying price":0.75,"stock level": 250,"country": "Thailand"},
               {'sku':35,"name":"Sauce","description":"Light Soya Sauce","selling price": 3.65,"buying price":2.05,"stock level": 453,"country": "China"},
               {'sku':36,"name":"Milo","description":"Powdered Malt drink","selling price": 3.95,"buying price":1.25,"stock level": 370,"country": "Malaysia"},
               {'sku':37,"name":"Noodles","description":"Maggie Instant noodles","selling price": 4.05,"buying price":2.55,"stock level": 40,"country": "Singapore"},
               {'sku':38,"name":"Chips","description":"Lightly salted potato chip","selling price": 3.65,"buying price":2.05,"stock level": 240,"country": "Malaysia"},
               {'sku':39,"name":"Biscuit","description":"Kraft Oreo Sandwich Biscuits - Regular (Pack of 9)","selling price": 5.05,"buying price":3.25,"stock level": 270,"country": "Thailand"},
               {'sku':40,"name":"Juice","description":"Marigold 100% Packet Apple Juice","selling price": 4.65,"buying price":3.05,"stock level": 795,"country": "Singapore"},
               {'sku':41,"name":"Coca-Cola","description":"Sweet and slightly astringent caramelized sugar, with hints of nutmeg and cinnamon.","selling price": 5.95,"buying price":4.35,"stock level": 563,"country": "Indonesia"},
               {'sku':42,"name":"Chips","description":"California Creamery Nacho Cheese Sauce","selling price": 3.85,"buying price":1.75,"stock level": 180,"country": "Indonesia"},
               {'sku':43,"name":"Tea","description":"Pokka Oolong natural and caffeine-free green tea","selling price": 6.35,"buying price":4.35,"stock level": 894,"country": "Singapore"},
               {'sku':44,"name":"Fish","description":"Mouth-watering Ayam Brand Sardines in Spring Water","selling price": 8.15,"buying price":5.45,"stock level": 256,"country": "China"},
               {'sku':45,"name":"Juice","description":"Fresh, delectable orange juice","selling price": 5.45,"buying price":3.45,"stock level": 103,"country": "Malaysia"},
               {'sku':46,"name":"Mask","description":"3 ply Surgical Mask 4 ply KN95 Masks CE Approved Disposable","selling price": 4.50,"buying price":3.45,"stock level": 20,"country": "Thailand"},
               {'sku':47,"name":"Shampoo","description":"Palmolive Healthy and Smooth Naturals Shampoo","selling price": 19.85,"buying price":13.60,"stock level": 150,"country": "Singapore"},
               {'sku':48,"name":"Cereal","description":"Nestlé Honey Stars Cereal with Whole Grain","selling price": 5.90,"buying price":4.30,"stock level": 230,"country": "Indonesia"},
               {'sku':49,"name":"Hand Sanitizer","description":"Germ-X Moisturizing Original Hand Sanitizer","selling price": 5.40,"buying price":3.30,"stock level": 19,"country": "Singapore"},
               {'sku':50,"name":"Coffee","description":"Old Town 3 in 1 Instant White Coffee - Hazelnut","selling price": 2.85,"buying price":1.25,"stock level": 430,"country": "Malaysia"},
               {'sku':51,"name":"Battery","description":"Panasonic Alkaline Battery -AAA","selling price": 7.90,"buying price":4.50,"stock level": 523,"country": "China"},
               {'sku':52,"name":"Potatos","description":"Nature's Best Brastagi Potatoes - Granola (Washed)","selling price": 3.95,"buying price":1.25,"stock level": 264,"country": "Indonesia"},
               {'sku':53,"name":"Rice","description":"Royal Umbrella Thai Hom Mali Rice","selling price": 17.90,"buying price":12.45,"stock level": 540,"country": "Thailand"},
               {'sku':54,"name":"Oil","description":"Naturel Cooking Oil - Premium Blend of Canola & Sunflower","selling price": 10.80,"buying price":8.30,"stock level": 248,"country": "Malaysia"},
               {'sku':55,"name":"Tissue","description":"FairPrice Anti-Bacterial Wet Wipes","selling price": 3.10,"buying price":2.60,"stock level": 7,"country": "China"}]
LowStockList = []
#Asking for a search key for Binary Search
def ask():
    print("Keys to search for: SKU, Name, Description, Selling Price, Buying Price, Stock Level, Country ")
    searchKey= input("Search for key:")
    #If the search key is sku or stock level, the search value would be a integer type
    if searchKey.lower() == 'sku' or searchKey.lower() == 'stock level':
        searchValue = int(input("Search for value:"))
        return searchKey.lower(), searchValue
    #If the search key is selling price or buying price, the search value would be a float type
    elif searchKey.lower() == 'selling price'or searchKey.lower() == 'buying price':
        searchValue = float(input("Search for value:"))
        return searchKey.lower(), searchValue
    #If the search key is name, description or country, the search value would be a string type
    elif searchKey.lower() == 'name' or searchKey.lower() == 'description' or searchKey.lower() == 'country':
        searchValue = str(input("Search for value:"))
        return searchKey.lower(), searchValue
    # Recursion is used here if there is an invalid input
    else:
        print("Invalid input. Please try again")
        ask()
#Conducting Binary Searching for Phase 2
def binarySearch( theValues, targetKey, targetValue ):
    # Created a new temp list which will be used in the algorithm
    tempDict = []
    #Adding items from the original list into the temporary list.
    for i in theValues:
        tempDict.append(i)
    #Conduct a bubble sort to sort the temporary list using bubble sort
    bubbleSort(tempDict,'a',targetKey)
    #Hold all of the products with the same value as the targetValue
    list = []
    low = 0
    high = len(tempDict) - 1
    # Repeatedly subdivide the sequence in half
    # until the target is found
    while low <= high:
        # Find the midpoint of the sequence
        mid = (low + high)//2
    # Does the midpoint contain the target?
    # If yes, return midpoint (i.e. index of the list)
        if tempDict[mid][targetKey] == targetValue:
            #Add the product with the same value as the targetValue to the list
            list.append(tempDict[mid])
            #Remove the product from the temporary list of product and continue to
            # search the temporary list for other products with the same value
            # as the targetValue
            tempDict.remove(tempDict[mid])
            # Or is the target before the midpoint?
        elif targetValue < tempDict[mid][targetKey]:
            high = mid - 1
            # Or is the target after the midpoint?
        else:
            low = mid + 1
            # If the sequence cannot be subdivided further,
            # There are no more items in the temp list which has the target value
    # Return the list of items that was select to have the same value as the target value
    return list
#Recursion function to ask users if they want to add another product
def addAnotherPro():
    print("Enter yes or y if you want to add another product")
    print("Enter no or n to return to the main")
    AddAnother = input("Yes or No:")
    if AddAnother.lower() == "yes" or AddAnother.lower() == "y":
        #If yes or y is inputed, the function is repeated
        NewSKU = int(input("Enter the item SKU: "))
        write(NewSKU)
    elif AddAnother.lower() == "no" or AddAnother.lower() == "n":
        #If No or n is inputed, the function will end and it will return to the main menu
        print("Returning to main menu")
    else:
        #If the input is invalid, the function is repeated
        print("Invalid input. Please try again")
        input("Press Enter to continue")
        addAnotherPro()
# Add a new item into the stock inventory for phase 1
def write(SKU):
    for i in ProductDict:
        #Check if the product exists in the stock inventory
        if i["sku"] == SKU:
            print("The product exists")
            print("SKU:%s, Product name:%s, Product description:%s, Product Selling Price:%.2f, Product buying price:%.2f, Product Stock Level:%d, Country of Origin: %s"
              %(i["sku"], i["name"], i["description"], i["selling price"],i["buying price"], i["stock level"], i["country"]))
            #Recursion to add another product till user types No or n when prompted
            addAnotherPro()
            break
    if i["sku"] != SKU:
        Pname = str(input("Enter item name:"))
        description = str(input("Enter item description: "))
        #Selling price must be a float with 2 d.p.
        sellingPrice = float(input("Enter item selling price: "))
        #Buying price must be a float with 2 d.p.
        buyingPrice = float(input("Enter item buying price: "))
        #Stock level must be an integer
        stockLevel = int(input("Enter number of items being added: "))
        #5 countries: Singapore, China, Malaysia, Thailand, Indonesia
        Country = str(input("Enter the country of origin of the product: "))
        #Assign the values to their respective key for each product
        ProductDetails = {'sku':SKU,"name":Pname,"description":description,"selling price": sellingPrice,"buying price":buyingPrice,"stock level": stockLevel,"country":Country}
        #Add the product details to the stock inventory
        ProductDict.append(ProductDetails)
        #Recursion to add another product till user types No or n when prompted
        addAnotherPro()

#Displaying how many products are in the Product Inventory
def InventoryCount():
    #Checks if there is only 1 product in the Product Inventory
    if len(ProductDict) == 1:
        print("There is 1 product in the inventory." )
    #Checks if there is only 1 product in the Product Inventory
    elif len(ProductDict) == 0:
        print("There is no product in the inventory.")
    #States how many products is in the inventory
    else:
        print("There are %d products in the inventory." %len(ProductDict))
    input("Press enter to continue ")

#Display the objects in the stock inventory for Phase 1
def read(firstNum, lastNum, count):
    readItemCount = count
    #If the count is less than the number of products
    if readItemCount < len(ProductDict):
        #Display the products in intervals of 10 items at a time
        for i in ProductDict[firstNum:lastNum]:
            print("SKU:%s, Product name:%s, Product description:%s, Product Selling Price:%.2f, Product buying price:%.2f, Product Stock Level:%d, Country of Origin: %s"
              %(i["sku"], i["name"], i["description"], i["selling price"],i["buying price"], i["stock level"], i["country"]))
            #Increases the count by 1
            readItemCount += 1
        #Run the readNext function after displaying the page
        readNext(lastNum,readItemCount)
    #If the user try to access the next page and the count has exceed number of products, then they will return to the main menu
    else:
        print("There are no more items to display")
        print("Returning to main menu")
        input("Press enter to continue ")

#To ask the user if they wish to continue to display the next 10 products/page
#or to return to the main menu
def readNext(LastNum, ReadItemCount):
    input("Press enter to continue ")
    print("1. Next page.")
    print("0. Return to main menu")
    readNextPage = input("Enter your input (0/1): ")
    if readNextPage == "1":
        #Start from where it last element off, end at 10 elements later, count starts from where it left off
        read(LastNum,LastNum+10,ReadItemCount)
    #Return to the main menu
    elif readNextPage == "0":
        print("Returning to main menu")
        input("Press enter to continue ")
    #Invalid inputs causes the function to run again
    else:
        print("Invalid input. Please try again")
        readNext(LastNum,ReadItemCount)

#The function if the user want to delete something after the first delete function
def deleteRetry(RetryQ):
    if RetryQ.lower() == "yes" or RetryQ.lower() == "y":
        #If yes or y is inputed, the function is repeated
        SKUdelete = int(input("Enter the item SKU: "))
        delete(SKUdelete)
    elif RetryQ.lower() == "no" or RetryQ.lower() == "n":
        #If No or n is inputed, the function will end and it will return to the main menu
        print("Returning to main menu")
        input("Press enter to continue")
    else:
        #If the input is invalid, the function is repeated using recursion
        print("Invalid input. Please try again")
        print("Enter yes or y to retry")
        print("Enter no or n to return to the main")
        Retry = input("Yes or No:")
        deleteRetry(Retry)

#Delete the object in the file for Phase 1
def delete(SKU):
        i = 0
        #Checks if the product
        while i < len(ProductDict):
            if ProductDict[i]["sku"] == SKU:
                #Displays the product that is to be removed
                print("Product to be removed:")
                print(ProductDict[i])
                #Confirming if the user wants to delete the product
                ConfirmDelete = input("Do you want to remove this product (Y/N):")
                if ConfirmDelete.lower() == 'y':
                    #Removing the product
                    print("The product %s with the SKU of %d has been removed."%(ProductDict[i]["name"],ProductDict[i]["sku"]))
                    ProductDict.remove(ProductDict[i])
                    print("Enter yes or y if you want to delete another product")
                    print("Enter no or n to return to the main")
                    retry = input("Yes or No:")
                    deleteRetry(retry)
                    break
                elif ConfirmDelete.lower() == 'n':
                    #Cancel the removal of the product
                    print("The removal of the product %s has been cancelled."%ProductDict[i]["name"])
                    print("Enter yes or y if you want to delete another product")
                    print("Enter no or n to return to the main")
                    retry = input("Yes or No:")
                    deleteRetry(retry)
                    break
                else:
                    print("Invalid input.")
            else:
                i += 1
        if i > len(ProductDict)-1:
            print("There is no product with the SKU %s."%(SKU))
            print("Enter yes or y to retry")
            print("Enter no or n to return to the main")
            retry = input("Yes or No:")
            deleteRetry(retry)
# This would determine if the User would want the total Stock Level or the Average Stock Level.
def option4Question(StockType):
    # If 1 is inputed, then the function to find the inventory total stock level is activated
    if StockType.lower() == "1":
        totalStockLevel(ProductDict)
    # If 2 is inputed, then the function to find the inventory average stock level is activated
    elif StockType.lower() == "2":
        averageStockLevel(ProductDict)
    elif StockType.lower() == "0":
        print("Returning to main menu")
    else:
        #If an invalid input is placed, then the function is asked again.
        print("Invalid input. Please try again.")
        print("1. Display the total stock level of inventory")
        print("2. Display the average stock level of inventory")
        print("0. Return to main menu")
        StockType2 = input("Please enter your choice(1/2):")
        option4Question(StockType2)
#Calculate the total stock level for all of the items in the stock inventory for Phase 2
def totalStockLevel(ProductDict):
    total = 0
    for i in ProductDict:
        #Adding the total stock level of all of the inventory
        total += i["stock level"]
    print("There are %d stock in the inventory with %d products." %(total,len(ProductDict)))

#Calculate the average stock level for all of the items in the stock inventory for Phase 2
def averageStockLevel(ProductDict):
    total = 0
    for i in ProductDict:
        #Adding the total stock level of all of the inventory
        total += i["stock level"]
    #Getting the average stock level of all of the inventory
    average = total//len(ProductDict)
    print("There ia an average of %d stock in the inventory with %d products." %(average,len(ProductDict)))

#Conducting Bubble Sort in the stock inventory for Phase 2
def bubbleSort( theSeq , sortOrder, Type ):
    #The length of the list
    n = len( theSeq )
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Bubble the largest item to the end
        for j in range(i):
            #Check in which order should the Inventory be sorted
            if sortOrder == 'a':
                #Sort the list in ascending order
                if theSeq[j][Type] > theSeq[j + 1][Type]:
                    # Swap the j and j+1 items so that the larger value is on the left
                    # and the smaller value is on the right
                    tmp = theSeq[j]
                    theSeq[j] = theSeq[j + 1]
                    theSeq[j + 1] = tmp
            elif sortOrder == "d":
                #Sort the list in descending order
                if theSeq[j][Type] < theSeq[j + 1][Type]:
                    # Swap the j and j+1 items so that the larger value is on the right
                    # and the smaller value is on the left
                    tmp = theSeq[j]
                    theSeq[j] = theSeq[j + 1]
                    theSeq[j + 1] = tmp
    #Returns the sorted list
    return theSeq
#Conducting Insertion Sort in the stock inventory for Phase 2
def insertionSort( theSeq, sortOrder, Type ):
    n = len( theSeq )
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = theSeq[i]
        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        #Check in which order should the Inventory be sorted
        if sortOrder == 'a':
            #Sort the list in ascending order
            while pos > 0 and value[Type] < theSeq[pos - 1][Type]:
                # Shift the items to the right during the search
                theSeq[pos] = theSeq[pos-1]
                pos -= 1
            # Put the saved value into the open slot.
            theSeq[pos] = value
        elif sortOrder == 'd':
            #Sort the list in descending order
            while pos > 0 and value[Type] > theSeq[pos - 1][Type]:
                # Shift the items to the left during the search
                theSeq[pos] = theSeq[pos-1]
                pos -= 1
            # Put the saved value into the open slot.
            theSeq[pos] = value
    #Returns the sorted list
    return theSeq
#A function to activate the binary search when asked in the main menu for phase 2
def Searching():
    #Use the function ask to get a search key and a search value for the binary search to use
    search = ask()
    searchKey = search[0]
    searchValue = search[1]
    newDict = binarySearch(ProductDict, searchKey, searchValue)
    #Conduct a insertion sort to sort the results from the binary search
    insertionSort(newDict,'a','sku')
    #To check if there is anything in the list
    if len(newDict) != 0:
        j = 1
        for i in newDict:
            print("%d : %s"%(j,i))
            j = j + 1
        input("Press Enter to continue")
    while len(newDict) == 0:
        print("There is no product with the %s %s in the Stock Inventory."%(searchKey, searchValue))
        print("To retry, type Yes or Y.")
        print("To exit, type No or N.")
        Retry = input("Enter input here (Y/N):")
        if Retry.lower() == 'y':
            #If the user input y, then the searching function is called again
            Searching()
            break
        elif Retry.lower() == 'n':
            #If the user input n, then it returns to the main menu
            print("Returning to Main Menu")
            input("Press Enter to continue")
            break
        else:
            #If an invalid input is given, then the codes in the while look is asked again
            #until a valid input is given
            print("Invalid input. Please try again")
            input("Press Enter to continue")
#A auto order reucrsion function for phase 3
def autoOrder(lowStockList, orderCount):
    #Base case
    if len(lowStockList) == 1:
        #This would indicate how many stock is needed till the stock level of the product
        #reaches 100 stocks
        remaining = 100 - lowStockList[0]["stock level"]
        #This would calculate the profit to gain from selling one stock of the product
        profit = lowStockList[0]["selling price"] - lowStockList[0]["buying price"]
        #This would calcualte the total profit to gain from the buying the remaining stock
        #needed to have the stock level reach 100
        totalProfit = profit * remaining
        #This would calculate the cost of buying the remaining stock needed to have the
        #stock level reach 100
        cost = remaining * lowStockList[0]["buying price"]
        print("The product %d.) %s has a low stock of %d."
              %(lowStockList[0]["sku"],lowStockList[0]["name"],lowStockList[0]["stock level"]))
        print("%d more stock of %s would be needed to reach the minimum stock level of 100."
              %(remaining,lowStockList[0]["name"]))
        print("One stock of the product cost $%.2f and the profit from one stock is $%.2f."
              %(lowStockList[0]["buying price"],profit))
        print("The total cost of the order is $%.2f and the profit to be earned from this order is $%.2f."
              %(cost,totalProfit))
        while True:
            #Gives the user the option to accept the order and buy the remaining stock, or
            #to cancel the order if the store is unable to purchase the remaining stock
            print("Enter yes or y to accept the order.")
            print("Enter no or n to cancel the order.")
            orderOption = input("Enter input here (Y/N):")
            #If the user answer yes or y, then the order is accepted
            if orderOption.lower() == "yes" or orderOption.lower() == "y":
                print("Order accepted.")
                #This is to adjust the stock level of the product in the main Stock Inventory
                #to become 100
                ProductDict[lowStockList[0]['sku']-1]['stock level'] = 100
                #This removes the product from the low stock list so that when the recursion
                #occurs, the next product in the low stock list would be first until the
                #low stock list is empty
                lowStockList.remove(lowStockList[0])
                #Increases the count of the numbers of orders accepted
                orderCount += 1
                input("Press enter to continue")
                #This would print how many orders has been accepted at the end as this is in
                #the base case, so it would display the final order count
                print("%d of the orders has been accepted."%orderCount)
                return cost
            #If the user answer no or n, then the order is cancelled
            elif orderOption.lower() == "no" or orderOption.lower() == "n":
                print("Order cancelled.")
                #This removes the product from the low stock list so that when the recursion
                #occurs, the next product in the low stock list would be first until the
                #low stock list is empty
                lowStockList.remove(lowStockList[0])
                input("Press enter to continue")
                #This would print how many orders has been accepted at the end as this is in
                #the base case, so it would display the final order count
                print("%d of the orders has been accepted."%orderCount)
                return 0
            #If an invalid input is places, then the while loop would repeat
            else:
                print("Invalid input. Please try again.")
    else:
        #This would indicate how many stock is needed till the stock level of the product
        #reaches 100 stocks
        remaining = 100 - lowStockList[0]["stock level"]
        #This would calculate the profit to gain from selling one stock of the product
        profit = lowStockList[0]["selling price"] - lowStockList[0]["buying price"]
        #This would calcualte the total profit to gain from the buying the remaining stock
        #needed to have the stock level reach 100
        totalProfit = profit * remaining
        #This would calculate the cost of buying the remaining stock needed to have the
        #stock level reach 100
        cost = remaining * lowStockList[0]["buying price"]
        print("The product %d.) %s has a low stock of %d."
              %(lowStockList[0]["sku"],lowStockList[0]["name"],lowStockList[0]["stock level"]))
        print("%d more stock of %s would be needed to reach the minimum stock level of 100."
              %(remaining,lowStockList[0]["name"]))
        print("One stock of the product cost $%.2f and the profit from one stock is $%.2f."
              %(lowStockList[0]["buying price"],profit))
        print("The total cost of the order is $%.2f and the profit to be earned from this order is $%.2f."
              %(cost,totalProfit))
        while True:
            #Gives the user the option to accept the order and buy the remaining stock, or
            #to cancel the order if the store is unable to purchase the remaining stock
            print("Enter yes or y to accept the order.")
            print("Enter no or n to cancel the order.")
            orderOption = input("Enter input here (Y/N):")
            #If the user answer yes or y, then the order is accepted
            if orderOption.lower() == "yes" or orderOption.lower() == "y":
                print("Order accepted.")
                #This is to adjust the stock level of the product in the main Stock Inventory
                #to become 100
                ProductDict[lowStockList[0]['sku']-1]['stock level'] = 100
                #This removes the product from the low stock list so that when the recursion
                #occurs, the next product in the low stock list would be first until the
                #low stock list is empty
                lowStockList.remove(lowStockList[0])
                #Increases the count of the numbers of orders accepted
                orderCount += 1
                input("Press enter to continue")
                return cost + autoOrder(lowStockList,orderCount)
            #If the user answer no or n, then the order is cancelled
            elif orderOption.lower() == "no" or orderOption.lower() == "n":
                print("Order cancelled.")
                #This removes the product from the low stock list so that when the recursion
                #occurs, the next product in the low stock list would be first until the
                #low stock list is empty
                lowStockList.remove(lowStockList[0])
                input("Press enter to continue")
                return 0 + autoOrder(lowStockList,orderCount)
            #If an invalid input is places, then the while loop would repeat
            else:
                print("Invalid input. Please try again.")
#Getting all of product with low stock in a list Phase 3
def findLowStock():
    for P in ProductDict:
        if P['stock level'] < 100:
            LowStockList.append(P)
        else:
            pass
while True:
    print("Welcome to the Dwarf Grocery Store inventory menu.")
    print("Select the following options to continue:")
    #Phase 1 Add items for phase 1
    print("1. Add new items to the stock inventory:")
    #Phase 1 Remove items for phase 1
    print("2. Remove item from stock inventory")
    #Phase 1 Display items for phase 1
    print("3. Display items in stock inventory")
    #Phase 2 Display total and average stock level for phase 2
    print("4. Display Inventory stock level")
    #Phase 2 Bubble sort and insertion Sort for phase 2
    print("5. Sort the product")
    #Phase 2 Binary Search for phase 2
    print("6. Search for product")
    #Phase 3 Automatic ordering system for low stock products for phase 3
    print("7. Auto order low stock items")
    #Enter 0 in the option to end the entire program
    print("0. Exit Program")
    option = input("Enter option: ")


    if option == "1":
        #Unique identifier SKU (Stock Keeping Units)
        SKU = int(input("Enter the item SKU:"))
        write(SKU)

    elif option == "2":
        SKUdelete = int(input("Enter the item SKU: "))
        delete(SKUdelete)

    elif option == "3":
        InventoryCount()
        #Start at the 1st element, end at the 10th element, start the count at 1
        read(0,10,1)


    elif option == "4":
        print("1. Display the total stock level of inventory")
        print("2. Display the average stock level of inventory")
        print("0. Return to main menu")
        StockType = input("Please enter your choice(1/2):")
        option4Question(StockType)
        input("Press Enter to return to main menu")

    elif option == "5":
        #Displays all of the possible sorting options
        print("All sorting options: Name, Selling Price, SKU, Stock Level, Buying Price, Country, Description")
        #Ask the user to sort the Stock Inventory List by what
        SortBy = str(input("Sort list by: "))
        SortOrder = str(input("Sort by ascending(A) or descending(D) order: "))
        print("Would you like to sort using 1.) Bubble sort or 2.) Insertion Sort:")
        SortType = int(input("Enter your input (1/2):"))
        if SortType == 1:
            bubbleSort(ProductDict,SortOrder.lower(),SortBy.lower())
        elif SortType == 2:
            insertionSort(ProductDict,SortOrder.lower(),SortBy.lower())
        input("Press Enter to return to main menu")


    elif option == "6":
        #This calls for the searching function
        Searching()
    #Automated process using recursion for phase 3
    elif option == "7":
        #Activate the find low stock function to search the Inventory list for
        #items with low stock
        findLowStock()
        #If the low stock lost is empty, that means that all of the products in the list
        #has at least 100 stock, so it would return to main menu.
        if len(LowStockList) == 0:
            print("There is no product in the stock inventory with low stock")
            input("Press enter to return to main menu")
        else:
            print("There are %d products with low stock."%len(LowStockList))
            totalcost = autoOrder(LowStockList,0)
            print("The total cost of the accepted orders are $%.2f."%totalcost)
            input("Press enter to continue")

    elif option == "0":
        print("Ending the program")
        break

    #If an invalid input is placed, then the while loop is repeated
    else:
        print("Invalid option.")
        print("Please try again")
        input("Press Enter to continue")



