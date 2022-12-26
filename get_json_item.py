import json


def getJsonItem():
    with open("DatSanta.json") as jsonFile:
        jsonObjects = json.load(jsonFile)


    gifts = jsonObjects["gifts"]
    newGifts = [list(gift.values()) for gift in gifts]

    children = jsonObjects["children"]
    newChildren = [list(child.values()) for child in children]

    # return snowAreas, gifts, childrens
    return newGifts, newChildren

    print(jsonObjects)