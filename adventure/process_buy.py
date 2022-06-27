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
        print('adding to bag')
        backpack[item] = freelancers[item]
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
        print('adding to bag')
        backpack[item] = antiques[item]
        print('--------------------------------')