import dateTime
import info

def generateBill(manafacName,manafacContact,boughtItems):
    fileInfo = info.getFileInfo()
    mainData = info.getDictInfo(fileInfo)
    total=[]
    file = open("buy"+"_"+dateTime.get_datetime()+"_"+manafacName+".txt","w")
    file.write("____________________________________________________________________________________________________________________________________________________________________________"+"\n")
    file.write("                                                                Laptop Buy Bill                                                                                             "+"\n")
    file.write("____________________________________________________________________________________________________________________________________________________________________________"+"\n")
    file.write("Manafacturer Name: "+manafacName+"\n")
    file.write("Contact: "+manafacContact+"\n")
    file.write("Buy Date: "+dateTime.dates()+"\n")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
    file.write("ID"+"    "+"Name"+"\t"+"            "+"Brand"+"\t"+"       "+"Quantity"+"\t"+"Processor"+"\t"+"Graphics Card"+"\t"+"Net Price"+"\t"+"VAT"+"\t"+"Gross"+"\n")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
    for index in range(len(boughtItems)):
        snoTemp = int(boughtItems[index][0])
        quantityTemp = int(boughtItems[index][2])
        modelTemp = mainData[snoTemp][0]
        brandTemp = mainData[snoTemp][1]
        priceTemp = float(mainData[snoTemp][2].replace("$","")) 
        processorTemp = mainData[snoTemp][4]
        graphicsTemp = mainData[snoTemp][5]
        file.write(str(index+1)+"\t"+modelTemp+"\t"+brandTemp+"\t"+"  "+str(quantityTemp)+"\t"+processorTemp+"\t"+graphicsTemp+"\t"+str(priceTemp)+"\t"+str(priceTemp*0.13)+"\t"+str(priceTemp+(priceTemp*0.13))+"\n")
        total.append((priceTemp+(priceTemp*0.13))*quantityTemp)
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n")
    file.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+"\n")
    grandTotal=0
    for i in range(len(total)):
        totalEach=total[i]
        grandTotal = grandTotal+totalEach
    file.write("Grand Total: $"+str(grandTotal)+"\n")
    file.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+"\n")
    file.close()

    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                                     Your Purchase Bill                                                                                               ")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Manafacturer Name: ", manafacName)
    print("Contact: ", manafacContact)
    print("Buy Date: ", dateTime.dates())
    print("List of Items Bought: ")
    for items in boughtItems:
        print(items)
    print("------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Total Price: $",grandTotal)
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
