def getFileInfo():
    file = open("laptop.txt","r")
    data = file.readlines()
    file.close()
    return data

def getDictInfo(fileInfo):
    dataDict = {}
    for index in range(len(fileInfo)):
        dataDict[index+1] = fileInfo[index].replace("\n","").split(",")
    return dataDict

def laptopInfo():    
    fileInfo = getFileInfo()
    mainData = getDictInfo(fileInfo)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("ID","\t","Model","\t" ,"Brand","\t\t","Price","\t\t","Quantity","Processor","Graphics Card")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for key,value in mainData.items():
        print(key,value[0],value[1],"\t",value[2],"\t",value[3],"\t",value[4],"\t",value[5])
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
