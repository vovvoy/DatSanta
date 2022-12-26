import json
from make_packages import makePackages
from get_json_item import getJsonItem

def select_gifts(children, budget, catalog):
  gifts = {}

  # Determine the budget for each child
  budget_per_child = budget / len(children)
  cnt = 0
  for child in children:
    # budget_per_child = budget / len(children) - cnt
    age = child[2]
    gender = child[1]
    # interests = child["interests"]
    # Конструкторы[constructors]
    # Куклы[dolls]
    # Радиоуправляемые
    # игрушки[radio_controlled_toys]
    # Игрушечный
    # транспорт[toy_vehicles]
    # Настольные
    # игры[board_games]
    # Подвижные
    # игры[outdoor_games]
    # Игровая
    # площадка[playground]
    # Мягкие
    # игрушки[soft_toys]
    # Компьютерные
    # игры[computer_games]
    # Сладости[sweets]
    # Книги[books]
    # Домашнее
    # животное[pet]
    # Одежда(сумочки, заколки, платья, рюкзаки)[clothes]
    # Create a list of potential gift categories based on age and gender
    potential_categories = []
    if age < 6 and gender == "female":
      potential_categories += ["dolls", "soft_toys", "board_games", "outdoor_games", "playground", "sweets", "pet"]
    elif age < 6 and gender == "male":
      potential_categories += ["constructors", "toy_vehicles", "board_games", "outdoor_games", "playground", "sweets", "pet", "soft_toys"]
    elif age < 11 and gender == "female":
      potential_categories += ["dolls", "soft_toys", "sweets", "books", "clothes", "pet"]
    elif age < 11 and gender == "male":
      potential_categories += ["computer_games", "radio_controlled_toys", "toy_vehicles", "books", "outdoor_games",]
    # else:
    #   potential_categories += ["constructors", "radio_controlled_toys", "toy_vehicles", "computer_games", "books"]
    # if gender == "female":
    #   potential_categories += ["dolls", "soft_toys", "clothes"]
    # elif gender == "male":
    #   potential_categories += ["toy_vehicles", "radio_controlled_toys"]

    # Consider the child's interests and hobbies
    # for interest in interests:
    #   if interest in catalog:
    #     potential_categories += [interest]

    # Select the gift that will bring the most happiness to the child within the budget allocated for that child
    selected_gift = None
    max_happiness = 0
    for gift in catalog:
      if gift[1] in potential_categories and gift[2] <= budget_per_child:
        # Calculate the happiness of the gift based on gender and price
        happiness = gift[2]
        if gender == "female" and gift[1] in ["dolls", "soft_toys", "clothes"]:
          happiness += 5
        elif gender == "male" and gift[1] in ["toy_vehicles", "radio_controlled_toys", "computer_games"]:
          happiness += 3
        if happiness > max_happiness:
          selected_gift = gift
          max_happiness = happiness
          # budget -= selected_gift[2]
          # budget_per_child = budget / len(children) - cnt



    # Add the selected gift to the list of gifts for this child

    try:
        gifts[child[0]] = selected_gift
        budget -= selected_gift[2]
        cnt += 1
        if cnt < 1000:
            budget_per_child = budget / (len(children) - cnt)
        catalog.remove(selected_gift)
    except TypeError:
        print(selected_gift)


  return gifts



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gifts, children = getJsonItem()
    children.sort(key=lambda x:x[2], reverse=True)
    gifts.sort(key=lambda x:x[2], reverse=True)
    new_result = select_gifts(children, 100000, gifts)
    total_spend_money = 0
    presentingGifts = []
    for key, value in new_result.items():
        presentingGifts.append({"giftID":value[0], "childID":key})


    summ = 0
    for i, j in new_result.items():
        summ += j[2]
    print(summ)
    print()


    bizim_return = {}
    bizim_return['mapID']  = 'a8e01288-28f8-45ee-9db4-f74fc4ff02c8'
    bizim_return['presentingGifts'] = presentingGifts

    json_object = json.dumps(bizim_return, indent=4)

    with open("route4.json", "w") as outfile:
        outfile.write(json_object)






