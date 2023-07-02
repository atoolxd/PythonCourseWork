import info
import buyBill

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
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("-----------------------------------------------------------------------Error!!Invalid Input!!-----------------------------------------------------------------------------")
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print()
        if sno>0 and sno<=len(mainData):
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("                                                                 Your laptop is available to be bought                                                                       ")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print()
            validInputLoop = True
        else:
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("----------------------------------------------------------------------------Error!!Invalid Input!!----------------------------------------------------------------------------")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print()
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
                inputQuantity = int(input("Amount you would like to buy: "))
                exceptionLoop =False
            except:
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("--------------------------------------------------------------------------Error!!Invalid Input!!--------------------------------------------------------------------------")
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print()
        if inputQuantity >0 :
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Laptop has been bought sucessfully!!")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print()
            validInputLoop = True
        else:
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("-------------------------------------------------------------------------------Error!!Invalid Input!!-------------------------------------------------------------------------")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print()
    return inputQuantity


def buying():
    boughtItems = []
    continueLoop = True
    while continueLoop == True:
        info.laptopInfo()
        print()
        validID = idValidation()
        available = quantityValidation(validID)
        fileInfo = info.getFileInfo()
        mainData = info.getDictInfo(fileInfo)
            
        mainData[validID][3] = str(int(mainData[validID][3]) + available)

        file = open("laptop.txt","w")
        for value in mainData.values():
            rewriteData = value[0]+","+value[1]+","+value[2]+","+value[3]+","+value[4]+","+value[5]+"\n"
            file.write(rewriteData)
        file.close()

        boughtItems.append([validID,mainData[validID][0],available])
        
        x = False
        while x == False:
            exceptionLoop =True
            while exceptionLoop == True:
                try:
                    repeat = input("Would you like to sell more(N/n to cancel)(Press any other button to continue): ")
                    exceptionLoop = False
                except:
                    print()
                    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("-------------------------------------------------------------------------------Error!!Invalid Input!!-------------------------------------------------------------------------")
                    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

                if repeat.lower() == "n":
                    print()
                    manafacName = input("Enter manafacturer name: ")
                    manafacContact = input("Phone no: ")
                    print()
                    buyBill.generateBill(manafacName,manafacContact,boughtItems)
                    continueLoop = False
                    x = True
                else:
                    continueLoop = True
                    x = True
