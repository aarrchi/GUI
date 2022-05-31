import sys
import datetime as dt

def OpeningMessage():
    """Creating function to show initial message"""
    print("\n" + "***************************************************************************")
    print("\nHello you are welcomed to INGCollege Library Management System.\n")
    print("****************************************************************************")




def takingInput():
    """Creating function to take the input from user"""
    print ("\n\nPlease enter '1', if you want to borrow book")#Printing userOptions
    print ("Please enter '2', if you want to return the book")
    print ("Please enter '3', if you want to exit")
    
    while True:
        try: #Implementing try and catch 
            
            userChoice = int(input("\nPleasw enter the value (1, 2, or 3): "))#Taking input from user
            break

        except:
            print("\n\n" +"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Invalid input! Please enter number values")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            


    if userChoice == 1:
        borrowMessage()
            
    elif userChoice == 2:
        returningMessage()
            
    elif userChoice == 3:
        print("\n\n" + "***********************************************")
        print("\nThank you for using our library. Have a nice day\n")
        print("************************************************" + "\n")
        sys.exit()


   
    else:
        print("\n" + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Invalid input! Please enter the valid input")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + "\n")
    

def readFile():
    """Creating function to read the textfile"""

    file = open("Book.txt","r")
    file.read()
    file.close


def dictionaryFile():
    """Creating function to create dictionary"""
    file = open("Book.txt","r")
    storeInDictionary = {} #Initializing dictionary
    keyBookID = 1

    for line in file:
        line = line.replace("\n", "")
        valueList = (line.split(","))
        storeInDictionary[keyBookID] = valueList #Creating dictionary key value pair 
        keyBookID +=1
       
    file.close()
    return storeInDictionary


def listOfKey():
    """Creating function to store keys"""
    keyData=dictionaryFile()
    keyContainer = []

    for key in keyData.keys():
        keyContainer.append(key) #Storing keys in keyContainer
    return keyContainer
          

def bookInfoTable():
    """Creating function to create table containing book info"""
    dictionaryData = dictionaryFile()
    print("\n\n" + "-" * 80)
    print("Book-ID\t | Name\t\t|    Author\t\t|  Quantity\t| Price \t|")
    print("-" * 80)

    for key, value in dictionaryData.items():

        print(str(key), "\t|  " + value[0] + "\t| " + value[1]+ "\t\t|    " +  value[2]+ "\t\t|   " +   value[3] + "    \t|" + "\n") #Presenting data in tabular form
    print("-" * 80)


def borrowMessage():
    """Creating function to display the borrowMessage"""
    global borrowerName
    
    print("\n\n" + "-" * 50)
    print("\nYou will be borrowing book now\n")
    print("-" * 50 + "\n\n")
    
    borrowerName = input("Enter the name of the person who is borrowing the book: ")
    borrowingBook()
    
   
def borrowingBook():
    """Creating function to borrow the book"""
    global borrowBookID, bookIdList
   
    dictionaryType = dictionaryFile()
    keyHouse = listOfKey()
    bookIdList = []
       
    
    while True:
        bookInfoTable()
        while True:
            try:
                borrowBookID = int(input("\n\nEnter the ID of the book you wanted to borrow: "))
                break
            except:
                print("\n\n" +"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Invalid input! Please enter number values")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+ "\n")
            

        if int(borrowBookID) not in keyHouse:  #Checking if borrowID is not in keyHouse printing respective message
            print("\n\n" +"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Sorry! Please enter valid bookID")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+ "\n\n")

        elif int(dictionaryType[int(borrowBookID)][2])<= 0:  #Checking if the quantity of the book is 0 and displaying respective message
             print("\n\n" +"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
             print("Sorry! This book is not available")
             print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + "\n\n")

        else:
           
            bookIdList.append(borrowBookID)  #Adding borrowBookID in list
           
            print("\n\n" +"*********************************************")
            print("You have succesfully borrowed book")
            print("*********************************************" + "\n\n")
            print("The price of the book is:", dictionaryType[int(borrowBookID)][3]) #Printing price of the book
            
            bookQuantity()
            

        continueBorrow = input("\nBorrow another books?Yes/no: ").lower()
        if continueBorrow == "no":
            displayBill()
            writeborrowedFile()
            break



    
                        
def bookQuantity():
    """Creating function to update the quantity of book"""

    quantityDict = dictionaryFile()
    keyList =listOfKey()
    bookFile = open("Book.txt", "w")

   
    for key, value in quantityDict.items():

        #Updating the book quantity
        changedQuantity = int(value[2])-1 #Updatting quantity of the book when they are borrowed

        if str(key) in str(bookIdList[-1]): #Checking keys in last index of bookIdList
            update = value[0] + "," + value[1] + "," + str(changedQuantity) + "," + value[3] + "\n"
            bookFile.write(update) #Writing updated value in bookFile
        else:
            
            update = value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n"
            bookFile.write(update)
    

    bookFile.close()


    


def totalAmount():
    """Creating function to calculate the total cost of the book"""
    priceDictionary = dictionaryFile()
    totalPrice = 0
  
    for key in bookIdList:
       
        totalPrice += float(priceDictionary[int(key)][3].replace("$", ""))#Calculating the totalPrice
    addDollar = "$" + str(totalPrice)
    return addDollar
    

def dateTime():
    """Creating function to display dateTime"""
    currentDateTime = str(dt.datetime.now()).split(".")[0]
    return currentDateTime
    
def displayBill():
    """Creating function to display display the bill"""
    bookDict = dictionaryFile()
    print("\n\n" + "-" * 40)
    print("\nCustomer borrow details\n")
    print("-" * 40  + "\n" )
    print("The person who borrowed the book is: ", borrowerName)
    print("The total price of the book is ", totalAmount() )
    print("The book borrowed date and time: ",dateTime())
   

    print("The books borrowed are: " )
    for i in bookIdList: #Printing the books borrowed
        print(bookDict[int(i)][0], "\n")


def writeborrowedFile():
    """Creating function to write the borrowed file"""
    bookDict = dictionaryFile()
    minute = str(dt.datetime.now().minute) 
    second = str(dt.datetime.now().second)
    microSecond = str(dt.datetime.now().microsecond)
    fileName = borrowerName + minute + second + microSecond #Setting name for the file


    file = open(fileName + ".txt", "w")
    
    
    file.write("\n\n" + "-" * 40)
    file.write("\nCustomer borrow details\n")#Writing all the borrow details in textfile
    file.write("-" * 40  + "\n" )
    file.write("The person who borrowed the book is: " + borrowerName)
    file.write("\nThe total price of the book is " + totalAmount() )
    file.write("\nThe book borrowed date and time: " + dateTime())
   

    file.write("\nThe books borrowed are: " )
    for i in bookIdList:
        file.write("\n")
        file.write(bookDict[int(i)][0])
        file.write("\n")
    file.close()




def returningMessage():
    """Creating function to returning Message"""
    global returnerName
    print("\n\n" + "-" * 50)
    print("\nYou will be returning book now\n")
    print("-" * 50 + "\n\n")
    
    returnerName = input("Enter the name of the person who is returning the book: ")
    returningBook()



def returningBook():
    """Creating function to return the book"""
    global returnIdList, borrowedDaysList
    
    returnDictionary = dictionaryFile()
    storeKey = listOfKey()
    returnIdList = []
    borrowedDaysList = []
    while True:
        bookInfoTable()
        
        while True:
            try: #Imjplementing try and catch
                returnBookID = int(input("\nEnter the ID of the book you wanted to return: "))
                break
            except:
                print("\n\n" +"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Invalid input! Please enter number value")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+ "\n\n")
            
            
        if int(returnBookID) in storeKey: #Checking if the the returnBookId is in list of keys
            
            returnIdList.append(returnBookID) #Adding returnBookID in returnIdList
            borrowedDays()
            updateQuantity()
            
            print("\n\n" +"*********************************************")
            print("Thank you for returning the book")
            print("*********************************************"+ "\n\n")

            
        else:
            print("\n\n" +"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Sorry! Please enter valid bookID")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+ "\n\n")

        continueReturn = input("Do you want to return another books?Yes/no: ").lower()
        if continueReturn == "no":
            
            returnBill()
            writeReturnFile()
            
            break



def borrowedDays():
    """Creating function to ask borrowed days"""
    
    while True:
        try:
            bookBorrowedDays = int(input("\nHow many days you kept the book?: "))
            borrowedDaysList.append(bookBorrowedDays)
            break
        
        except:
            print("\n\n" +"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Invalid input! Please enter number values")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+ "\n\n")


def updateQuantity():
    """Creating function to read the textfile"""
    quantityDict = dictionaryFile()
    
    bookFile = open("Book.txt", "w")

   
    for key, value in quantityDict.items():
            
        changedQuantity = int(value[2])+1

        if str(key) in str(returnIdList[-1]): #Checking keys in last index of bookIdList
            update = value[0] + "," + value[1] + "," + str(changedQuantity) + "," + value[3] + "\n"
            bookFile.write(update)
        else:
            update = value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n"
            bookFile.write(update)
    
    bookFile.close()


    

def fineCharging():
    """ Creating function to calculate fine"""
    fineDictionary = dictionaryFile()
    
    lendingDuration = 10
    totalFine = 0
    j = 0

    for key in returnIdList:
        days = borrowedDaysList[j]
        if days> lendingDuration: #Charging fine if the borrowed days exceed than 10 days
            fine = 0.3
            totalFine += fine
        else:
            fine = 0
            totalFine += fine
        j += 1

    bookFine  = str(round(totalFine, 2)) #Rounding up the fine value
    return bookFine


def returnBill():
    billDictionary = dictionaryFile()
    print("\n\n" + "-" * 40)
    print("\nCustomer book return details\n") 
    print("-" * 40  + "\n" )
    print("The person who returned the book is: ", returnerName)
    print("The total fine of the book is: ", fineCharging())
    print("The book returned date and time: ", dt.datetime.now())
    print("The books returned are: " )
    for i in returnIdList:
        print(billDictionary[int(i)][0])
        

    
def writeReturnFile():
    returnDict = dictionaryFile()
    minute = str(dt.datetime.now().minute) 
    second = str(dt.datetime.now().second)
    microSecond = str(dt.datetime.now().microsecond)
    fileName = returnerName + minute + second + microSecond


    file = open(fileName + ".txt", "w")
    
    
    file.write("\n\n" + "-" * 40)
    file.write("\nCustomer book return details\n") #Writing all the retun book details in file
    file.write("-" * 40  + "\n" )
    file.write("The person who returned the book is: " + returnerName)
    file.write("\nThe total fine of the book is " + fineCharging() )
    file.write("\nThe book returned date and time: " + str(dt.datetime.now()))
   

    file.write("\nThe books borrowed are: " )
    for i in returnIdList:
        file.write("\n")
        file.write(returnDict[int(i)][0])
        file.write("\n")
        

    file.close()

   


    
    
