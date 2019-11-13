import json

def saveToJson(clickedList, nameAG, projectsPath, ulyssesPID, nameOfExcelTable):
    
    data = [
        clickedList,
        nameAG,
        projectsPath,
        ulyssesPID,
        nameOfExcelTable
    ]

    with open(nameAG + '_data.txt', 'w') as outfile:
        json.dump(data,outfile) 


def readFromJson(nameAG):
    data = []
    with open(nameAG + '_data.txt') as json_file:
        data = json.load(json_file)
        #for p in data['clicks']:
        #    print(p)
    return data