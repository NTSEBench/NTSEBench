import fitz  # PyMuPDF
import sys
import os
import shutil
import json
from PIL import Image


# change this before running
checking=False
# format 1
optionNames=["(1)","(2)","(3)","(4)"]
# format 2
# optionNames=["(a)","(b)","(c)","(d)"]
# format 3
# optionNames=["(A)","(B)","(C)","(D)"]
sourceName="2016Gujarat_NTSE"
idPrefix="ntse2016-gujarat"
source="Resonance"
solnSource="Resonance"
solString="Sol."
isSolAns=True
stage=1
#
def myinput(prompt):
    while True:
        try:
            out = input(prompt)
            print(out)
            return out
        except :
            print("Please enter a valid input")
            continue
        # out = input(prompt)
        # print(out)
        # # return input(prompt)
        # return out

def getOptionNameMap():
    dict={}
    for i in range(len(optionNames)):
        opt=optionNames[i][1:-1]
        dict[opt]=i+1
    return dict
optNameMap=getOptionNameMap()

def processOptionsList(options):
    optionTextDict={1:"",2:"",3:"",4:""}
    optionImagesDict={1:[],2:[],3:[],4:[]}
    i=0
    j=0
    
    while(j<len(optionNames)):
        # check remnant
        if(j!=0):
            si=options[i].find(optionNames[j])
            if(si!=0):
                optionTextDict[j]+=options[i][0:si]
                options[i]=options[i][si:]
        
        si=options[i].find(optionNames[j])
        options[i]=options[i][si+len(optionNames[j]):]
        
        while(i<len(options) and (isinstance(options[i],Image.Image) or (j==(len(optionNames)-1)) or (optionNames[j+1] not in options[i]))):
            if(isinstance(options[i],Image.Image)):
                optionImagesDict[j+1].append(options[i])
            else:
                optionTextDict[j+1]+=options[i]
            i+=1    
        j+=1
    
    for i in range(len(optionNames)):
        if(optionTextDict[i+1].isspace()):
            optionTextDict[i+1]=""
    
    # print(f"options: {ops}")
    return optionTextDict,optionImagesDict

def getAnswerOption(answerString):
    temp=answerString.split("(")[1]
    option=(temp.split(")")[0])
    # in case of multiple correct options
    option=option.split(",")
    ansOption=[]
    for op in option:
        curr="".join(op.split())
        if(curr!="NA"):
            ansOption.append(optNameMap[curr])
    return ansOption

def seperateQuestion(question,question_parsed,currQuesNum):
    # current idea: quesNum,text prompt(can contain a combination of direction as well as problem text),
    # quesImage, quesImageCaption, (can have a combination of direction images as well)
    # option1Text, option1Image, option2Text, option2Image, option3Text, option3Image, option4Text, option4Image,
    # Answer_option,
    # SolutionText, SolutionImage
    # issues: cases where solution contains text and images interleaved(should be fine if we call solution as something after answer and before next direction or next ques number => so for us anything after answer is the solution)
    print(question)
    print(question_parsed)
    print(currQuesNum)
    # print(question)
    # print(question_parsed)
    textPrompt=""
    quesImages=[]
    solnImages=[]
    solnText=""
    options=[]
    i=0
    # TODO check remnant of i=0
    startString=f"{currQuesNum}."
    si=question[i].find(startString)
    if(si+len(startString)<len(question[i])):
        textPrompt+=question[i][si+len(startString):]
    i+=1
    # anything before options is either question images or question text prompt
    while(isinstance(question[i],Image.Image) or optionNames[0] not in question[i]):
        if(isinstance(question[i],Image.Image)):
            quesImages.append(question[i])
        else:
            textPrompt+=question[i]
        i+=1
    
    # check remnant
    if(isinstance(question[i],Image.Image)==False):
        si=question[i].find(optionNames[0])
        if(si!=0):
            textPrompt+=question[i][0:si]
            question[i]=question[i][si:]
    
    while(isinstance(question[i],Image.Image) or (not isSolAns and "Ans." not in question[i]) or (isSolAns and solString not in question[i])):
        options.append(question[i])
        i+=1
    print(question[i])
    # check remnant 
    if(isinstance(question[i],Image.Image)==False and not isSolAns):
        si=question[i].find("Ans.")
        # print(si)
        if(si!=0):
            options.append(question[i][0:si])
            question[i]=question[i][si:]
    
    answerString=""
    print(i, question[i])
    while("Sol." not in question[i]):
        # print(i, question[i])
        answerString+=question[i]
        i+=1
    
    # check remnant
    if(isinstance(question[i],Image.Image)==False):
        si=question[i].find("Sol.")
        if(si!=0):
            answerString+=question[i][0:si]
            question[i]=question[i][si:]
    
        # remove Sol. from string
        question[i]=question[i][len("Sol."):]
        if(isSolAns):
            answerString=question[i]
        
    # answer option processing
    # check if the answerstring contains word bonus in it in any case upper or lower
    # skipquestion = False
    if("bonus" in answerString.lower()):
        return None
        # skipquestion = True
        # answerOption = [-1]
    else: 
        answerOption=getAnswerOption(answerString)
    
    # options processing
    optionTextDict,optionImagesDict = processOptionsList(options)
    
    # now comes the solution
    while(i<len(question)):
        if(isinstance(question[i],Image.Image)):
            solnImages.append(question[i])
        else:
            solnText+=question[i]
        i+=1
    
    # checking
    # print(currQuesNum)
    # if(question_parsed!=None and "direction" in question_parsed.keys()):
    #     print(f'DirectionText: {question_parsed["direction"]}')
    # else:
    #     print(f'Direction text: -')
    # if(question_parsed!=None and "directionImages" in question_parsed.keys()):
    #     print(f'DirectionImages: {question_parsed["directionImages"]}')
    # else:
    #     print(f'DirectionImages: -') 
    # print(f"textPrompt: {textPrompt}")
    # print(f"quesImages: {quesImages}")
    # print(f"optionText: {optionTextDict}")
    # print(f"optionImages: {optionImagesDict}")
    # print(f"answer: {answerOption}")
    # print(f"solnImages: {solnImages}")
    # print(f"solnText: {solnText}")
    
    output={"currQuesNum":currQuesNum}
    output["id"]=idPrefix+str(currQuesNum)
    if(question_parsed!=None):
        output["hasDirn"]=True
        output["directionModeRange"]=question_parsed["directionModeRange"]
        output["category"]=question_parsed["questionCategories"]
    else:
        output["hasDirn"]=False
        output["category"]="N/A"
        
    if(question_parsed!=None and "direction" in question_parsed.keys()):
        output['directionText']= question_parsed["direction"]
    else:
        output['directionText']=None

    if(question_parsed!=None and "directionImages" in question_parsed.keys()):
        output['directionImages']=question_parsed["directionImages"]
    else:
        output['directionImages']=None 
    output["textPrompt"]= textPrompt
    output["quesImages"]= quesImages
    output["optionText"]= optionTextDict
    output["optionImages"]= optionImagesDict
    output["answer"]= answerOption
    output["solnImages"]= solnImages
    output["solnText"]= solnText
    
    # below is fixed for a file
    output["difficulty"]="N/A"
    output["source"]=source
    output["solnSource"]=solnSource
    output["stage"]=stage
    
    return output

def saveImages(parsedQues,folderName,directionImagesFolder,problemImagesFolder,optionImagesFolder,solutionImagesFolder):
    # this function saves the images and changes the image arrays to contain the names of the images
    if(parsedQues["hasDirn"] and "directionImages" in parsedQues.keys()):
        # direction image may need to be stored but the names must be returned
        imageNames=[]
        prefix=f"{sourceName}_{parsedQues['currQuesNum']}_Direction_{parsedQues['directionModeRange'][0]}_{parsedQues['directionModeRange'][-1]}_"
        for i in range(len(parsedQues["directionImages"])):
            fname=prefix+str(i)
            if(parsedQues["directionModeRange"][0]==parsedQues["currQuesNum"]):
                # it must be saved
                parsedQues["directionImages"][i].save(directionImagesFolder+fname+".png")
            imageNames.append(fname)
        # now change the lists to contain the names
        parsedQues['directionImages']=imageNames
    
    # save the problem images, if any
    if(len(parsedQues["quesImages"])!=0):
        imageNames=[]
        prefix=f"{sourceName}_{parsedQues['currQuesNum']}_Problem_"
        for i in range(len(parsedQues["quesImages"])):
            fname=prefix+str(i)
            parsedQues["quesImages"][i].save(problemImagesFolder+fname+".png")
            imageNames.append(fname)
        # now change the lists to contain the names
        parsedQues['quesImages']=imageNames
            
    # save the option images, if any
    for j in range(1,5):
        imgList=parsedQues["optionImages"][j]
        if(len(imgList)!=0):
            imageNames=[]
            prefix=f"{sourceName}_{parsedQues['currQuesNum']}_Option_{j}_"
            for i in range(len(imgList)):
                fname=prefix+str(i)
                imgList[i].save(optionImagesFolder+fname+".png")
                imageNames.append(fname)
            # now change the lists to contain the names
            parsedQues['optionImages'][j]=imageNames
    
    # save the option solution images, if any
    if(len(parsedQues["solnImages"])!=0):
        imageNames=[]
        prefix=f"{sourceName}_{parsedQues['currQuesNum']}_Solution_"
        for i in range(len(parsedQues["solnImages"])):
            fname=prefix+str(i)
            parsedQues["solnImages"][i].save(solutionImagesFolder+fname+".png")
            imageNames.append(fname)
        # now change the lists to contain the names
        parsedQues['solnImages']=imageNames
    
def createQuestionwiseFolders(questionwise_dict,questionwise_parsed_dict,folderName,quesNumStart=1,quesNumEnd=100):
    # creating folders
    directionImagesFolder=folderName+"/directionImages/"
    problemImagesFolder=folderName+"/problemImages/"
    optionImagesFolder=folderName+"/optionImages/"
    solutionImagesFolder=folderName+"/solutionImages/"
    
    # to remove old one
    if os.path.exists(folderName):
        shutil.rmtree(folderName)
    
    os.mkdir(folderName) 
    os.mkdir(directionImagesFolder)
    os.mkdir(problemImagesFolder)
    os.mkdir(optionImagesFolder)
    os.mkdir(solutionImagesFolder)
    
    data=[]
    for i in range(quesNumStart,quesNumEnd+1):
        question=questionwise_dict[i]
        question_parsed=None
        if(i in questionwise_parsed_dict.keys()):
            question_parsed=questionwise_parsed_dict[i]
        output=seperateQuestion(question,question_parsed,i)
        if(output==None):
            continue
        saveImages(output,folderName,directionImagesFolder,problemImagesFolder,optionImagesFolder,solutionImagesFolder)
        
        del output["currQuesNum"]
        if(output["hasDirn"]):
            del output["directionModeRange"]
        data.append(output)
    
    # Serializing json
    json_object = json.dumps(data, indent=4)
    
    with open(folderName+f"/{sourceName}_data.json", "w") as outfile:
        outfile.write(json_object)

def extract_text_and_images(pdf_path,quesNumStart = 0,checking=False):
    currQuesNum=quesNumStart
    questionwise_dict={quesNumStart:[]}
    questionwise_parsed_dict={}
    doc = fitz.open(pdf_path)
    text = ''
    directionMode=False
    directionModeRange=None
    currentDirection=None
    directionImages=[]

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
        image_list = page.get_images()
        
        for block in page.get_text("dict",sort=True)["blocks"]:
            # print("next block")
            if(block['type']!=1):
                for line in block['lines']:
                    for span in line['spans']:
                        print(span['text'], "p", directionMode, str("Direction") in span['text'])
                        # print(span['text'])
                        # possible issue if question number x contains "x+1." as substring(pretty rare, I expect)
                        if(directionMode==False and str("Direction") in span['text']):
                            # to check whether to enable direction mode or not
                            print("Direction for a block of questions detected:")
                            print(span['text'])
                            solved=False
                            while(solved==False):
                                if(checking==True):
                                    break
                                isDirection=myinput("Is this actually direction for following set of questions(y/n)?: ")
                                if(isDirection=="y"):
                                    directionMode=True
                                    while(solved==False):
                                        print("please enter range of questions this direction covers: ")
                                        lower=int(myinput("enter lower question Number: "))
                                        higher=int(myinput("enter higher question Number: "))
                                        questionCategories=int(myinput("enter the category number of questions: "))
                                        directionModeRange=range(lower,higher+1)
                                        solved=True
                                elif(isDirection=="n"):
                                    solved=True
                                else:
                                    print("please type y/n")
                        
                        
                        if(directionMode==True):
                            # stopping condition for direction mode
                            if(str(currQuesNum+1)+"." in span['text']):
                                # TODO here we can give option to user to give there own direction after showing currentDirection
                                for i in directionModeRange:
                                    questionwise_parsed_dict[i]={"direction":currentDirection,"directionImages":directionImages,"directionModeRange":directionModeRange,"questionCategories":questionCategories}
                                directionMode=False
                                directionModeRange=None
                                questionCategories=-1
                                currentDirection=None
                                directionImages=[]
                            else:
                                if(currentDirection==None):
                                    currentDirection=span['text']
                                else:
                                    currentDirection+=span['text']
                        # print(currQuesNum+1, span['text'])
                        if(directionMode==False):
                            if(str(currQuesNum+1)+"." in span['text']):
                                currQuesNum+=1
                                questionwise_dict[currQuesNum]=[]
                                questionwise_dict[currQuesNum].append(span['text'])
                            else:
                                questionwise_dict[currQuesNum].append(span['text'])
                            
            if(block['type']==1):
                # print("image")
                img_rect = fitz.Rect(block["bbox"])  # Get the bounding box of the image block
                image = page.get_pixmap(clip=img_rect)
                # if(image.width * image.height >= min_image_size):
                pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
                
                if(directionMode==True):
                    # directionImages.append("image")
                    directionImages.append(pil_image)
                else:    
                    # questionwise_dict[currQuesNum].append("image")
                    questionwise_dict[currQuesNum].append(pil_image)
                
                # print(isinstance(pil_image,Image.Image))
                
        
    # print(questionwise_dict)
    return questionwise_dict,questionwise_parsed_dict

 
# total arguments
n = len(sys.argv)
print("Enter filename, ques start num and ques end num")
if(n!=4):
    print("Enter all arguments")
    print("Total arguments passed:", n)
    exit(0)

fileName=sys.argv[1]
startNum=int(sys.argv[2])
endNum=int(sys.argv[3])

quesNumStart=startNum-1     # give one less than quesnum
questionwise_dict, questionwise_parsed_dict = extract_text_and_images("./inputFiles/"+fileName,quesNumStart,checking)
folderName=sourceName
createQuestionwiseFolders(questionwise_dict,questionwise_parsed_dict,folderName,quesNumStart=startNum,quesNumEnd=endNum)
if(not checking):
    print("Question folder creation successful")
else:
    print("checking successful")

# TODO now we create the combined.pdf
# we basically parse the json and create a new pdf using the data just to verify the procedure worked correctly