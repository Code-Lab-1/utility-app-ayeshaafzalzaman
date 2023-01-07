# catagorizing items in different catagory
items = {
    "Drinks": {
        "1": {"item": "Coke", "price":4, "stock": 20},
        "2": {"item": "Sprite", "price": 5, "stock": 40},
        "3": {"item": "cocktail juice", "price": 3, "stock": 35},
        "4": {"item": "water", "price": 3, "stock": 34},
    },
    "Snacks": {
        "5": {"item": "lays", "price": 6, "stock": 25},
        "6": {"item": "salted peanuts", "price": 4, "stock": 30},
        "7": {"item": "hershey's cookie", "price": 3, "stock": 5},
        "8": {"item": "oreo bisciut", "price": 3, "stock": 14},
        '9':{'item':"cheetos",'price':5,'stock':5},
        '10':{'item':'popcorn','price':4,'stock':4}
    },
    "chocolate": {
        "11": {"item": "kitkat", "price": 3, "stock": 25},
        "12": {"item": "twix", "price": 4, "stock": 13},
        "13": {"item": "dairy milk", "price": 3, "stock": 5},
        "14": {"item": "galaxy", "price": 3, "stock": 14},
        '15':{'item':"milky way",'price':5,'stock':5},
        '16':{'item':'bounty','price':4,'stock':4}
    },
    "coffee": {
        "17": {"item": "milk coffee", "price": 3, "stock": 25},
        "18": {"item": "mocha", "price": 7, "stock": 13},
        "19": {"item": "latte", "price": 15, "stock": 5},
        "20": {"item": "cold coffee", "price": 9, "stock": 14},
        '21':{'item':"black coffee",'price':9,'stock':5},
        '22':{'item':'cappucino','price':10,'stock':4}
    },

}
# function to print menu of items
def print_menu(item):
    print("Menu:\n")
    for category, category_items in item.items():
        print(category + ":")
        for code, item in category_items.items():
            print(f'{code}: {item["item"]} ({item["price"]:.2f} dhs)')
        print()


# function to get valid code from user
def get_code(item):
    while True:
        code = input("Enter code: ")
        # check if code is valid
        for category, category_items in item.items():
            if code in category_items:
                return code
        print("Invalid code. Please try again.")


# function to get valid amount of money from user
def get_money(item, code):
    # search for item in Drinks , Snacks,chocolate and coffee dictionaries
    for category, category_items in item.items():
        if code in category_items:
            item = category_items[code]
            break
    else:
        print(f'Invalid code "{code}".')
        return

    while True:
        money = float(input("Enter money: "))
        # check if the amount was enough
        if money > item["price"] or money==item["price"]:
            return money
            dispense_item(item, code,money)
        print(
            f'Not enough money. Please insert {item["price"] - money:.2f} dhs more.'
        )


# function to dispense item and calculate change
def dispense_item(item, code, money):
    # search for item in Drinks ,Snacks,chocolates and coffee dictionaries
    for category, category_items in items.items():
        if code in category_items:
            item = category_items[code]
            break
    else:
        print(f'Invalid code "{code}".')
        return

    # check if item is in stock
    if item["stock"] > 0:
        #dispense item and calculate change
        print(f'\nDispensing {item["item"]}...')
        change = money - item["price"]
        item["stock"] -= 1
        print(f"Returning {change:.2f} DHS...\n")
    else:
        print(f'\nError: {item["name"]} is out of stock.')


# function to suggest additional purchase based on previous purchase
def suggest_purchase(item, code):
    if code in items["Drinks"]:
        print("You might also like:")
        for code, item in items["Snacks"].items():
            print(f'{code}: {item["item"]} ({item["price"]:.2f}dhs)')
    elif code in items["coffee"]:
        print("You might also like:")
        for code, item in items["chocolate"].items():
            print(f'{code}: {item["item"]} ({item["price"]:.2f}dhs)')



# main program
while True:
    # print menu of items
    print_menu(items)
    # get valid code from user
    code = get_code(items)
    # get valid amount of money from user
    money = get_money(items, code)
    #dispense item and calculate change
    dispense_item(items, code, money)
    # suggest additional purchase based on previous purchase
    suggest_purchase(items, code)
    # prompt user to continue or exit
    while True:
        response = input("\nWould you like to make another purchase? (y/n) ")
        if response.lower() == "y":
            break
        elif response.lower() == "n":
            print("Thank you for using the vending machine!")
            exit()
        else:
            print("Invalid response. Please try again.")