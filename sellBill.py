import dateTime
import info


def billForCustomers(customerName,customerContact,grandTotal,soldItems):
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                                         Your Sell Bill                                                                                      ")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Customer Name: ", customerName)
    print("Contact : ",customerContact)
    print("Purchase Date: ", dateTime.dates())
    print("Your Items:")
    for items in soldItems:
        print(items)
    print("------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Grand total with $25 shipping: $",grandTotal+25)
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def generateBill(customerName,customerContact,grandTotal,soldItems):
    fileInfo = info.getFileInfo()
    mainData = info.getDictInfo(fileInfo)
    
    file = open("sell"+"_"+dateTime.get_datetime()+"_"+customerName+".txt","w")
    file.write("______________________________________________________________________________________________________________________________________________________________________"+"\n")
    file.write("                                                                                 Laptop Sell Bill                                                                     "+"\n")
    file.write("______________________________________________________________________________________________________________________________________________________________________"+"\n")
    file.write("Customer name: "+customerName+"\n")
    file.write("Contact : "+customerContact+"\n")
    file.write("Rented Date: "+dateTime.dates()+"\n")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
    file.write("ID"+"    "+"Name"+"\t""\t"+"            "+"Brand"+"\t""\t"+"       "+"Price"+"\t""\t"+"    "+"Quantity"+"\t""\t"+"Processor"+"\t""\t"+"Graphics Card"+"\n")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
    for index in range(len(soldItems)):
        snoTemp = int(soldItems[index][0])
        quantityTemp = int(soldItems[index][2])
        modelTemp = mainData[snoTemp][0]
        brandTemp = mainData[snoTemp][1]
        priceTemp = float(mainData[snoTemp][2].replace("$","")) * quantityTemp
        processorTemp = mainData[snoTemp][4]
        graphicsTemp = mainData[snoTemp][5]
        file.write(str(index+1)+"\t""\t"+modelTemp+"\t""\t"+brandTemp+"\t""\t"+"  "+str(priceTemp)+"\t""\t"+"       "+str(quantityTemp)+"\t""\t"+processorTemp+"\t""\t"+graphicsTemp+"\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
    file.write("______________________________________________________________________________________________________________________________________________________________________"+"\n")
    file.write("Grand total with $25 shipping: $"+str(grandTotal+25)+"\n")
    file.write("_______________________________________________________________________________________________________________________________________________________________________"+"\n")
    file.close()
