def chatbot():
    # Define lists for countries and their famous foods with detailed descriptions
    countries = [
        "italy",
        "france",
        "mexico",
        "japan",
        "china",
        "india",
        "thailand",
        "greece",
        "turkey",
        "spain",
        "germany",
        "argentina",
        "usa",
        "brazil",
        "egypt",
        "morocco",
        "vietnam",
        "south korea",
        "russia",
        "australia",
        "canada",
        "peru",
        "iran",
        "saudi arabia",
        "nigeria",
    ]

    famous_foods = [
        "Pizza, especially from Naples, is a globally loved dish made from a flatbread base topped with tomato sauce, cheese, and various toppings such as meats, vegetables, and herbs.",
        "The Croissant is a buttery, flaky pastry enjoyed by the French during breakfast, made with layers of dough and butter rolled into a crescent shape.",
        "Tacos are a staple of Mexican cuisine, consisting of a corn or wheat tortilla folded around fillings like seasoned meat, vegetables, cheese, and salsa.",
        "Sushi is a traditional Japanese dish featuring vinegared rice, often accompanied by raw fish, seaweed, and vegetables, carefully rolled or pressed into various forms.",
        "Peking Duck is a famous Chinese dish where duck is roasted until crispy and served with thin pancakes, hoisin sauce, and scallions for a perfect bite.",
        "Biryani is a rich and flavorful rice dish from India, typically prepared with fragrant basmati rice, aromatic spices, and tender meat such as chicken or lamb.",
        "Pad Thai is a stir-fried noodle dish from Thailand, combining rice noodles, shrimp or chicken, tofu, peanuts, and bean sprouts with a tangy tamarind sauce.",
        "Moussaka is a classic Greek casserole made with layers of sautéed eggplant, minced meat, tomatoes, and topped with a creamy béchamel sauce before being baked.",
        "Kebab is a popular dish from Turkey, typically made of grilled or skewered meat, often lamb or chicken, served with flatbread, rice, and salad.",
        "Paella is a famous Spanish rice dish originating from Valencia, made with saffron-infused rice, seafood, chicken, and a variety of vegetables and spices.",
        "Bratwurst is a traditional German sausage made from pork, beef, or veal, often grilled and served with sauerkraut and mustard in a bun or on a plate.",
        "Asado is the national dish of Argentina, a barbecue of various cuts of beef, pork, and chicken, slowly grilled over an open flame and served with chimichurri.",
        "Hamburger is a classic American fast food, consisting of a grilled beef patty placed in a soft bun and topped with lettuce, tomato, cheese, and condiments.",
        "Feijoada is a hearty Brazilian stew made from black beans, pork, and beef, often served with rice, collard greens, and orange slices for a balance of flavors.",
        "Koshari is a popular Egyptian street food, made from rice, lentils, chickpeas, and macaroni, topped with a spicy tomato sauce and crispy fried onions.",
        "Tagine is a traditional Moroccan stew named after the clay pot in which it is cooked, combining meat, vegetables, and spices like saffron and cinnamon.",
        "Pho is a Vietnamese soup made from a rich broth simmered with beef bones, rice noodles, herbs, and thinly sliced beef or chicken, garnished with lime and chili.",
        "Kimchi is a staple of Korean cuisine, a fermented cabbage dish mixed with chili peppers, garlic, and other spices, served as a side dish with almost every meal.",
        "Borscht is a sour soup of Ukrainian origin, made with beetroot as the main ingredient, giving it a distinctive red color, often served with sour cream.",
        "Vegemite is a popular Australian spread made from brewer’s yeast extract, known for its salty, umami flavor, and typically spread on toast with butter.",
        "Poutine is a Canadian dish consisting of french fries topped with cheese curds and smothered in gravy, creating a rich and indulgent comfort food.",
        "Ceviche is a traditional Peruvian dish made from raw fish marinated in citrus juices like lime, mixed with onions, cilantro, and spicy chili peppers.",
        "Kebab, originating from Iran, is a skewered meat dish, typically made with lamb or chicken, seasoned with spices and grilled over an open flame.",
        "Kabsa is a Saudi Arabian dish of spiced rice and meat, typically lamb or chicken, cooked together in one pot with a blend of aromatic spices and served with nuts.",
        "Jollof Rice is a beloved West African dish, particularly in Nigeria, made with rice, tomatoes, onions, and a blend of spices, often served with grilled meats.",
    ]

    # Taking user input for the favorite country
    country = input("\n \n Enter your favourite country name: ").lower()

    # Checking if the country is in the list
    if country in countries:
        index = countries.index(country)
        print(f"\n \nGreat Choice! {famous_foods[index]} \n \n ")
    else:
        print("We do not have data about your selected country.")


# Call the function to run the chatbot
chatbot()
