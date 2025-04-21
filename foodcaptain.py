while True:
    location = input("What city would you like to eat in?")
    cuisine = input("what cusisine would you like to eat?")

    search_result = search_yelp(location, cuisine)

    if not search_result:
        print("There are no options for that in your area. Please try again.")
        continue

    print(f"Here are some {cuisine} options in {location}:")
    for business in search_result:
        print("-", business)
    break