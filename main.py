import json
from make_packages import makePackages
from get_json_item import getJsonItem



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example usage
    gifts, children = getJsonItem()
    total_gifts_price = 0
    for i in gifts:
        total_gifts_price += i[2]
    print(total_gifts_price)
    print()





