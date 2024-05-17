'''Tropical Airline Program'''
'''By Soe Htet Naung'''


#===========================================================================================================================================   
'''Main Function'''

def main():
    '''Making it global variable, so I can access it from the other functions'''
    global userName 
    finalTotal = []
    Output = []
    finalCost = 0
    mainMenuExit = False

    
    userName = input("What is Your Name? : ")
    
    '''Check if the user didn't input anything(blanks)
    This will check the "enter", and from "one space" up to "3 spaces" and "one tab"
    '''
    
    while userName == "" or userName == " " or userName == "  " or userName =="   " or userName == "\t":
        print('\n'+"You must enter your name for the program to proceed")
        userName = input("Please Enter Your Name : ")
    print('\n'+"Welcome To Tropical Airline Program,", userName)

    while mainMenuExit == False:
        
        menuOutput = '\n'+"Tropical Airlines Ticket Ordering System : "+'\n'+"(I)nformation"+'\n'+"(O)rder"+'\n'+"(E)xit"
        info = '\n'+'\t'+"Thank you for choosing Tropical Airlines for your air travel needs. You will be asked questions regarding what type of ticket you would like to purchase as well as destination information. We also offer 50% discounted fares for children."
        exitMessage = userName + ", No Tickets were Purchased! Thank you for visiting Tropical Airlines!"
        
        print(menuOutput)
        userMainInput = input("Please retype the letter in the bracket to proceed with the Program : ")
        if userMainInput.lower() == "i":
            print(info)
            
        elif userMainInput.lower() == "o":
            OrderSystem()
            finalTotal.append(total)
            
        elif userMainInput.lower() == "e":
            '''
            at this point, it is clear that the user is exiting the program
            There are 3 possible situations where the user quit the program
            1: Quitting without ordering a single ticket
            2: Quitting with one ordered ticket
            3: Quitting with multiple ordered tickets
            So They are divided into 3parts and varies the output
            
            '''
            '''1: Quitting without ordering a single ticket:
                if there is nothing in Final total list that means no order was made
                if there is one value in Final total list, one order was made
                if there is more than one vlaue in final total list, multiple orders were made
            '''
            if len(finalTotal) == 0:
                print(exitMessage)
                mainMenuExit = True

            elif len(finalTotal) == 1:

                for i in finalTotal:
                    '''
                    Here, the int values from the Final total list will be formatted into string values and stored in another list called Output
                    '''
                    Output.append(CurrencyFormat(i))
                    finalCost = i
                '''
                The *Output represents all the elements in list(array) which is not very suitable here
                But I found out about this on stack over flow, so I tried using it
                '''
                print(userName + ", Your Order is:",*Output,end=".")
                
                print("Your Final Total Cost is : " + CurrencyFormat(finalCost), end=".")
                print("Thank You for visiting Tropical Airlines!")
                mainMenuExit = True

            elif len(finalTotal) > 1:
                
                for y in finalTotal:
                    
                    Output.append(CurrencyFormat(y))
                    finalCost = finalCost + y
                '''
                All The multiple string values(elements) from Output(list/array) will be taken out and mapped with "and" to join them.
                '''
                print( userName + ", Your Orders are:", " and ".join(map(str,Output)), end = ".")
                print("Your Final Total Cost is : " + CurrencyFormat(finalCost), end=".")
                print("Thank You for visiting Tropical Airlines!")
                mainMenuExit = True
                    
        else :
            print("Error : Invalid Choice")
        
        

#================================================================================================================================================================================== 
'''OrderSystem Function
This function will handle most parts of selections by getting inputs from users throughout the process and respond accordingly 
'''
def OrderSystem():

    '''Declaring as Global Variables so that I can access them from another function'''
    global total
    '''
    ###CONSTANT VARIABLES FOR PRICES###
    These are also being declared as global since it is required to reuse in the price list outputs
    '''
    global ONEWAY_CAIRNS_PRICE
    ONEWAY_CAIRNS_PRICE = 250
    global ONEWAY_SYDNEY_PRICE
    ONEWAY_SYDNEY_PRICE = 420
    global ONEWAY_PERTH_PRICE
    ONEWAY_PERTH_PRICE = 510
    global TWOWAY_CAIRNS_PRICE
    TWOWAY_CAIRNS_PRICE = 400
    global TWOWAY_SYDNEY_PRICE
    TWOWAY_SYDNEY_PRICE = 575
    global TWOWAY_PERTH_PRICE
    TWOWAY_PERTH_PRICE = 700
    global BUSINESS_FARE_PRICE
    BUSINESS_FARE_PRICE = 275
    global ECONOMY_FARE_PRICE
    ECONOMY_FARE_PRICE = 25
    global FRUGAL_FARE_PRICE
    FRUGAL_FARE_PRICE = 0
    global WINDOW_SEAT_PRICE
    WINDOW_SEAT_PRICE = 75
    global AISLE_SEAT_PRICE
    AISLE_SEAT_PRICE = 50
    global MIDDLE_SEAT_PRICE
    MIDDLE_SEAT_PRICE = -25
    global NO_SEAT_PRICE
    NO_SEAT_PRICE = 0

    '''
    Menu Outputs
    '''
    welcomeMessage = "Hello, " + userName + '\n' + "Who are you ordering Ticket For ? : " +'\n' +"(Y)ou" + '\n' + "(S)omeone else"
    ticketTypeMessage = "The ticket type is : " +'\n'+ "(O)neway Trip" + '\n' + "(R)eturn[Round Trip]"
    OnewaydestinationMessage = '\n'+"Please select the destination for your return trip. Fare prices are listed below. : " + '\n'+ "[C]airns " + CurrencyFormat(ONEWAY_CAIRNS_PRICE) + '\n'+ "[S]ydney "+ CurrencyFormat(ONEWAY_SYDNEY_PRICE) + '\n' + "[P]erth " + CurrencyFormat(ONEWAY_PERTH_PRICE)
    TwowaydestinationMessage = '\n'+"Please select the destination for your return trip. Fare prices are listed below. : " + '\n'+ "[C]airns " + CurrencyFormat(TWOWAY_CAIRNS_PRICE) + '\n'+ "[S]ydney "+ CurrencyFormat(TWOWAY_SYDNEY_PRICE) + '\n' + "[P]erth " + CurrencyFormat(TWOWAY_PERTH_PRICE)
    fareMessage = '\n'+"Please choose the type of fare. Fees are displayed below and are in addition to the basic fare." + '\n'+ "[B]usiness " + CurrencyFormat(BUSINESS_FARE_PRICE) + '\n'+ "[E]conomy " + CurrencyFormat(ECONOMY_FARE_PRICE) + '\n'+ "[F]rugal "+ CurrencyFormat(FRUGAL_FARE_PRICE) + '\n' + "***Please note choosing Frugal fare means you will not be offered a seat choice.***"
    seatMessage = '\n'+"Please choose the seat type." + '\n'+ "[W]indow "+ CurrencyFormat(WINDOW_SEAT_PRICE) + '\n'+ "[A]isle "+ CurrencyFormat(AISLE_SEAT_PRICE) + '\n'+ "[M]iddle " + CurrencyFormat(MIDDLE_SEAT_PRICE) + '\n'+"Choosing the middle seat will deduct 25 from the total fare."
    
    '''Ticket Owner'''
    ticketOwnerChoosen = False
    while ticketOwnerChoosen == False:
        print('\n'+"Order Menu : ")
        print(welcomeMessage)
        ticketOwnerChoice = input('\n'+"The Ticket is for : ")
        if ticketOwnerChoice.lower() == "y":
            ticketOwner = userName
            ticketOwnerChoosen = True
        elif ticketOwnerChoice.lower() == "s":
            ticketOwner = input('\n'+"I'm buying the Ticket for : ")
            while ticketOwner == "":
                print("Error : Name shouldn't be blank please type in the name for the ticker holder to continue ordering ticket")
                ticketOwner = input('\n'+"I'm buying the Ticket for : ")
            ticketOwnerChoosen = True    
        else:
            print("Error : Invalid Choice")
        
    '''Ticket Type'''
    
    ticketTypeChoosen = False
    while ticketTypeChoosen == False:
        print(ticketTypeMessage)    
        ticketType = input('\n'+"Enter Ticket Type : ")
        if ticketType.lower() == "o":
            ticketType = "OneWay"
            ticketID = 1
            ticketTypeChoosen = True
        elif ticketType.lower() == "r":
            ticketType = "Return/RoundTrip"
            ticketID = 2
            ticketTypeChoosen = True
        else:
            print("Error: Invalid Choice")

    '''Destination'''
    '''To change the message output(varies prices)'''
    if ticketID == 1:
        destinationMessage = OnewaydestinationMessage
    elif ticketID == 2:
        destinationMessage = TwowaydestinationMessage
        
    destinationID = ThreeMenuChoices(destinationMessage,"Cairns","Sydney ","Perth")
    destination = CheckID(destinationID,"Cairns","Sydney ","Perth")


    '''Type Of Fare'''
    fareID = ThreeMenuChoices(fareMessage,"Business","Economy","Frugal")
    fareType = CheckID(fareID,"Business","Economy","Frugal")


    '''Type Of Seat'''
    if fareID != 3:
        seatID = ThreeMenuChoices(seatMessage,"Window","Aisle","Middle")
        seatType = CheckID(seatID,"Window","Aisle","Middle")

    if fareID == 3:
        print("This Fare Type is not eligible to choose Seat Type")
        seatID = 0
        seatType = "None"
    
    '''Calculate'''
    total = CalculateTotal(ticketID, destinationID, fareID, seatID)

    '''Print Out Ticket Details'''
    print('\n'+"Calculating Fare...")
    print("Ticket for :" + '\t'+'\t'+ ticketOwner)
    print(destination+"("+ticketType+")" +"-"+'\t' +CurrencyFormat(dCost))
    print(fareType+ "-" + '\t'+ '\t' + CurrencyFormat(fCost))
    print(seatType + "-" + '\t' +'\t'+ '\t' + CurrencyFormat(sCost))
    print("Age-" + '\t'+'\t'+ '\t' + str(age)+ eligibleText)
    print('\n'+"Total Price :"+ '\t'+'\t'+CurrencyFormat(total))
    
    
#===========================================================================================================================================    
'''ReadyMade Functions:
    The template functions for choosing 3 options menus:
    Including: Choosing Destinations,type of fares and type of seats,
'''
#............................................................................................................    
def ThreeMenuChoices(message, optionOne, optionTwo, optionThree):
    '''
    This Function will take in the message to output the menu, followed by the three Choices
    to check the input. The input here will be changed into lowercase and will be checked by
    lowering the case of the choices in parameter as well. It is not necessarily needed to be done
    I just wanted to alternative ways and practice myself while working on this assignment
    This function will return the ID of the options.
    '''
    chosen = False
    while chosen == False:
        print(message)
        option = input("Type the initial letter of option you want: ")
        if option.lower() == optionOne[0].lower():
            choice = 1
            chosen = True
        elif option.lower() == optionTwo[0].lower():
            choice = 2
            chosen = True
        elif option.lower() == optionThree[0].lower():
            choice = 3
            chosen = True
        else:
            print("Error : Invalid Choice")
    return choice

#===========================================================================================================================================

def CheckID(chosenID,optionOne, optionTwo, optionThree):
    '''
    This function will again takein 3 options plus the ID stored from ealier functon
    In this function, the ID will be checked and return the string (3options' values)
    '''
    if chosenID == 1:
        choice = optionOne
    elif chosenID == 2:
        choice = optionTwo
    elif chosenID == 3:
        choice = optionThree
    else:
        print("Error : !!!!")
    return choice
#...............................................................................................................
#===========================================================================================================================================

'''Calculation Funciton'''
def CalculateTotal(tID, dID, fID, sID):
    '''
    This function will take in the IDs of the choices,
    determine the prices
    calulate total
    and check whether the ticket owner is eligible for discounnt or not................
    '''
    '''Declaring as Global Variables so that I can access them from another function'''
    global dCost
    global fCost
    global sCost
    global eligibleText
    global age
    
       
    '''Destination Cost According to the Trip Type'''
    
    '''OneWayPrices'''
    if tID == 1:
        
        if dID == 1:
            dCost = ONEWAY_CAIRNS_PRICE
        elif dID == 2:
            dCost = ONEWAY_SYDNEY_PRICE
        elif dID == 3:
            dCost = ONEWAY_PERTH_PRICE
        else:
            print("Error")
        
    '''TwoPrices'''  
    if tID == 2:
        
        if dID == 1:
            dCost = TWOWAY_CAIRNS_PRICE
        elif dID == 2:
            dCost = TWOWAY_SYDNEY_PRICE
        elif dID == 3:
            dCost = TWOWAY_PERTH_PRICE
        else:
            print("Error")
    '''
    Common Prices(Not affected by the Oneway or Twoway)
    '''
    '''Fare Cost'''
    if fID == 1:
        fCost = BUSINESS_FARE_PRICE
    elif fID == 2:
        fCost = ECONOMY_FARE_PRICE
    elif fID == 3:
        fCost = FRUGAL_FARE_PRICE
    else:
        print("Error")
            
    '''Seat Cost'''
    if sID == 1:
        sCost = WINDOW_SEAT_PRICE
    elif sID == 2:
        sCost = AISLE_SEAT_PRICE
    elif sID == 3:
        sCost = MIDDLE_SEAT_PRICE
    elif sID == 0:
        sCost = NO_SEAT_PRICE
    else:
        print("Error")
        
    '''Checking Error Just In Case'''
    if tID == 0 or tID >= 3 :
        print("Error!!")
        
    Ctotal = dCost + fCost + sCost
    
    '''For Child Fare Price'''
    '''Making the variables CONSTANT so we can change it easily'''
    discountPercentage = 50
    discount = discountPercentage/100
    max_EligibleAge = 16
    
    print('\n',"How old is the person travelling? Travellers under 16 years old will receive a 50% discount for the child fare.")
    
    age = int(input("Please Enter Age : "))
    '''
    ERROR CHECKING for INVALID INPUT
    '''
    while age <= 0 or age >= 105:
        print("Error: Impossible Age, Please Try again")
        age = int(input("Please Enter Age : "))
    if age <= max_EligibleAge:
        eligibleText = "(eligible for child ticket, 50% discount applied)"
        Ctotal = Ctotal - (Ctotal * discount)
        
    if age > max_EligibleAge:
        eligibleText = "(not eligible for child ticket, no discount applied)"
        Ctotal = Ctotal
        
    return Ctotal

#===========================================================================================================================================      
'''Format
    To format the prices and return as a string.....
'''

def CurrencyFormat(amount):
    '''
    First format it into 2decimal places
    Didn't do round method since round will also round up the 2nd decimal if it is 0(zero),which will make it looks like only one decimal
    then format it into string and add "$" sign in front
    '''
    amount = format(amount, '.2f')
    output = "${}".format(amount)
    return output
   
#===========================================================================================================================================   

main()
