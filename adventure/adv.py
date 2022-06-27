
def view_items_in_backpack():
    print('--------------------------------')
    print("unzipping...")
    print(backpack)


def process_buy(storeNumber):
    print('--------------------------------')
    if storeNumber == '1':
        print('--------------------------------')
        print("choose an item from", freelancers['name'] + "...\n")
        for key, value in freelancers.items():
            if key != 'name':
                print(f"{key}, ${value}")
        print('enter exit to leave')
        item = input("--> ")
        if item == 'exit':
            return
        if item not in freelancers:
            print("item does not exist/out of stock")
            return
        print('adding to bag')
        backpack[item] = freelancers[item]
        del freelancers[item]
        print('--------------------------------')
    elif storeNumber == '2':
        print('--------------------------------')
        print('choose an item from', antiques['name'])
        for key, value in antiques.items():
            if key != 'name':
                print(f"{key}, ${value}")
        print('enter exit to leave')
        item = input("--> ")
        if item == "exit":
            return
        # check is the inputted item exists in the antique store
        if item not in antiques:
            print("item does not exist/out of stock")
            return

        print('adding to bag')
        backpack[item] = antiques[item]
        del antiques[item]

        print('--------------------------------')


# create stores (numbered 1, 2, 3)
freelancers = {'name': 'freelancing Shop', 'brian': 70, 'black knight': 20,
               'biccus diccus': 100, 'grim reaper': 500, 'minstrel': -15}
antiques = {'name': 'Antique Shop', 'french castle': 400,
            'wooden grail': 3, 'scythe': 150, 'catapult': 75, 'german joke': 5}
pet_shop = {'name': 'Pet Shop', 'blue parrot': 10,
            'white rabbit': 5, 'newt': 2}

backpack = {}


def game_loop():
    go = True
    while (go != False):
        print("Enter 0 to stop buying")
        print(f"Enter 1 to go to {freelancers['name']}")
        print(f"Enter 2 to go to {antiques['name']}")
        print(f"Enter 3 to go to {pet_shop['name']}")
        print("Enter 4 to view items in your backpack")

        choice = input()
        if choice == '0':
            go = False
        elif int(choice) > 0 and int(choice) < 4:
            process_buy(choice)
        elif choice == '4':
            view_items_in_backpack()


game_loop()
