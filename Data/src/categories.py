import json
import os

folderName=sourceName="2016Gujarat_NTSE"
createCatFile=True
addToJson=True

# map from category numeber to category
categoryNumToName={
    1:"Series",
    2:"Alphabet Test",
    3:"Odd one out",
    4:"Analogy",
    5:"Coding-Decoding",
    6:"Number and Ranking",
    7:"Blood Relation",
    8:"Mathematical Operations",
    9:"Direction Sense",
    10:"Venn Diagrams",
    11:"Time and Clock",
    12:"Missing Character",
    13:"Non-Verbal Series",
    14:"Non-Verbal odd one out",
    15:"Non-Verbal Analogy",
    16:"Incomplete Figure",
    17:"Mirror, Water and Images",
    18:"Cube and Dice",
    19:"Paper Folding & Cutting",
    20:"Embedded Figure",
    21:"Puzzle Test",
    22:"Figure Partition",
    23:"Dot Problem",
    24:"Cryptography",
    25:"Syllogisms",
    26:"Statement & Conclusions",
    27:"Data Sufficiency",
}

def addCategoriesToJson(folderName,sourceName):
    f1=open(folderName+f"/{sourceName}_data.json")
    f2=open(folderName+f"/{sourceName}_QwiseCategories.json")
    data=json.load(f1)
    catDict=json.load(f2)
    
    for i in range(len(data)):
        category= catDict[data[i]['id']]
        data[i]["category"]=category
    json_object = json.dumps(data, indent=4)
    
    with open(folderName+f"/{sourceName}_data_cat.json", "w") as outfile:
        outfile.write(json_object)

def addQuestionWiseCategories(folderName,sourceName):
    f1=open(folderName+f"/{sourceName}_data.json")
        
    data=json.load(f1)
    catDict={}
    if folderName+f"/{sourceName}_QwiseCategories.json" in os.listdir(folderName):
        f2=open(folderName+f"/{sourceName}_QwiseCategories.json")
        catDict=json.load(f2)
    for i in range(len(data)):
        if(str(data[i]["category"])=="N/A" and catDict.get(data[i]['id'])==None):
            category=int(input(f"Enter the category number of {data[i]['id']}: "))
            print(f"setting category of {data[i]['id']} to {categoryNumToName[category]}")
        else:
            category=data[i]["category"]
            print(f"already set category of {data[i]['id']} to {categoryNumToName[category]}")
            change = input("Do you want to change the category? (y/n): ")
            if(change=="y"):
                category=int(input(f"Enter the category number of {data[i]['id']}: "))
                print(f"setting category of {data[i]['id']} to {categoryNumToName[category]}")
        catDict[data[i]['id']]=category
        json_object = json.dumps(catDict, indent=4)
    
        with open(folderName+f"/{sourceName}_QwiseCategories.json", "w") as outfile:
            outfile.write(json_object)



if(createCatFile):
    addQuestionWiseCategories(folderName,sourceName)
if(addToJson):
    addCategoriesToJson(folderName,sourceName)