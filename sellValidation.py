import info
import sellBill

def idValidation():
    fileInfo = info.getFileInfo()
    mainData = info.getDictInfo(fileInfo)
    validInputLoop = False
    while validInputLoop == False:
        exceptionLoop =True
        while  exceptionLoop == True:
            try:
                sno = int(input("LAPTOP ID needed: "))
                exceptionLoop = False
            except:
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("--------------------------------------------------------------------Error!!Invalid Input!!-------------------------------------------------------------------------------")
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print()
        if sno>0 and sno<=len(mainData):
            if  int(mainData[sno][3]) == 0:
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("                                                                   This laptop is out of Stock                                                                              ")
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print()
                validInputLoop = False
            else:
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("                                                                Your laptop is available to be sold.                                                                      ")
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print()
                validInputLoop = True
        else:
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("-----------------------------------------------------------------------Error!!Invalid Input!!-----------------------------------------------------------------------------")
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print()
                validInputLoop = False
    return sno

def quantityValidation(validID):
    fileInfo = info.getFileInfo()
    mainData = info.getDictInfo(fileInfo)
    quantity = int(mainData[validID][3])
    validInputLoop = False
    while validInputLoop == False:
        exceptionLoop =True
        while  exceptionLoop == True:
            try:
                inputQuantity = int(input("Amount you would like to sell: "))
                exceptionLoop =False
            except:
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("-------------------------------------------------------------------------------Error!!Invalid Input!!---------------------------------------------------------------------")
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print()
        if inputQuantity >0 and inputQuantity <=quantity:
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("                                                                                Laptop has been sold sucessfully!!                                                            ")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print()
            validInputLoop = True
        else:
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------Error!!Invalid Input!!-----------------------------------------------------------------------")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print()
    return inputQuantity
    

 
def selling():
    grandTotal = 0
    price  = 0
    soldItems = []
    continueLoop = True
    while continueLoop == True:
        info.laptopInfo()
        print()
        validID = idValidation()
        available = quantityValidation(validID)
        fileInfo = info.getFileInfo()
        mainData = info.getDictInfo(fileInfo)
        no = mainData[validID][2].replace("$","")
        price = float(no)*int(available)
        grandTotal += float(price)
        mainData[validID][3] = str(int(mainData[validID][3]) - available)

        file = open("laptop.txt","w")
        for value in mainData.values():
            rewriteData = value[0]+","+value[1]+","+value[2]+","+value[3]+","+value[4]+","+value[5]+"\n"
            file.write(rewriteData)
        file.close()

        soldItems.append([validID,mainData[validID][0],available])
            
        x = False
        while x == False:
                repeat = input("Would you like to sell more(N/n to cancel)(Press any other button to continue): ")

                if repeat.lower() == "n":
                    print()
                    customerName = input("Enter your name: ")
                    customerContact = input ("Phone no: ")
                    print()
                    sellBill.billForCustomers(customerName,customerContact,grandTotal,soldItems)
                    print()
                    sellBill.generateBill(customerName, customerContact,grandTotal,soldItems)
                    continueLoop = False
                    x = True
                else:
                    continueLoop = True
                    x = True
