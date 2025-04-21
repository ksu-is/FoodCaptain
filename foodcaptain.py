while True:
    location = input("What city would you like to eat in?").strip()
    cuisine = input("what cusisine would you like to eat?").strip()
    budget = input("What's your budget? ($, $$, $$$) ").strip()

    search_result = search_yelp(location, cuisine, budget)

    if not search_result:
        print("There are no options for that in your area. Please try again.")
        continue

    while True:
        choice = random.choice(search_result) 

        print("\n Here's where I suggest:")
        print("---------------------------------------")
        print(f" Name: {choice['name']}")
        print(f" Rating: {choice['rating']} stars")
        print(f" Price Range: {choice['price']}")
        print(f" Location: {choice['location']}")
        print("---------------------------------------")
    
        while True:
            redo = input("Would you like another suggestion from the list? (yes/no): ").strip().lower()
            if redo == "no":
                print("Enjoy your meal.")
                exit()
            elif redo == "yes":
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")