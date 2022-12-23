# This is a sample Python script.
import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def getJsonItem():
    with open("response.json") as jsonFile:
        jsonObjects = json.load(jsonFile)

    snowAreas = jsonObjects["snowAreas"]
    newSnowAreas  = [list(snowArea.values()) for snowArea in snowAreas]

    gifts = jsonObjects["gifts"]
    newGifts = [list(gift.values()) for gift in gifts]

    children = jsonObjects["children"]
    newChildren = [list(child.values()) for child in children]

    # return snowAreas, gifts, childrens
    return newSnowAreas, newGifts, newChildren

    print(jsonObjects)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    snowAreas, gifts, children = getJsonItem()
    print(f"{snowAreas=}", f"{gifts=}", f"{children=}", sep='\n')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
