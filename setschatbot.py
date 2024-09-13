# ---------------
# Sets in python
# --------------


famous_foods_dict = {
    "italy": "Pizza, especially from Naples, is a globally loved dish. It's made from a flatbread base topped with tomato sauce, mozzarella cheese, and various toppings such as pepperoni, vegetables, and herbs. Naples pizza is known for its thin, soft, and slightly chewy crust cooked in a wood-fired oven.",
    "france": "The Croissant is a buttery, flaky, and crescent-shaped pastry enjoyed by the French, especially at breakfast. It's made with layers of dough and butter folded multiple times before being baked to a golden, crispy perfection. Often paired with coffee or hot chocolate.",
    "mexico": "Tacos are a versatile Mexican dish where a soft or crispy tortilla wraps around fillings like seasoned beef, pork, chicken, beans, or vegetables. Tacos are often topped with fresh salsa, guacamole, onions, cilantro, and lime, giving a rich mix of flavors in every bite.",
    "japan": "Sushi is a traditional Japanese delicacy made with vinegared rice, often accompanied by raw fish like tuna or salmon, seaweed, and vegetables. Sushi can come in different forms such as nigiri (fish over rice), maki (rolls), or sashimi (sliced raw fish).",
    "china": "Peking Duck, originating from Beijing, is a famous Chinese dish known for its crispy skin and tender meat. The duck is roasted and sliced thinly, served with pancakes, hoisin sauce, and scallions. It’s a special meal often enjoyed during celebrations.",
    "india": "Biryani is a fragrant and flavorful rice dish from India, layered with aromatic basmati rice, marinated meat (often chicken or lamb), and a mix of spices such as saffron, cumin, and cardamom. Often served with raita (yogurt sauce) or a boiled egg.",
    "thailand": "Pad Thai is a globally loved Thai stir-fried noodle dish. It combines rice noodles, shrimp, chicken, tofu, eggs, bean sprouts, peanuts, and a tangy tamarind sauce, balancing sweet, sour, salty, and spicy flavors. It's a signature dish of street food culture in Thailand.",
    "greece": "Moussaka is a baked dish with layers of sautéed eggplant, minced meat (usually lamb), tomatoes, and topped with a creamy béchamel sauce. This hearty dish is a staple in Greek households, served warm and often accompanied by a fresh salad.",
    "turkey": "Kebab is an iconic dish in Turkey, featuring skewered and grilled meats like lamb, beef, or chicken, often marinated in spices. It can be served with flatbread, rice, and salad, and is enjoyed in various forms such as shish kebab or doner kebab.",
    "spain": "Paella is a traditional Spanish rice dish from Valencia, made with saffron-infused rice cooked with a variety of ingredients like chicken, rabbit, seafood (shrimp, mussels), and vegetables. The dish is cooked slowly in a wide pan to create a crispy rice layer at the bottom.",
    "germany": "Bratwurst is a famous German sausage made from pork, beef, or veal, spiced and grilled to perfection. It is commonly served with mustard, sauerkraut, and hearty bread or as part of a larger meal with potatoes and vegetables.",
    "argentina": "Asado is more than just a meal in Argentina—it's a social event. Asado is a barbecue where beef, pork, and chicken are grilled over an open flame. The slow-cooked meat is tender and flavorful, often served with chimichurri, a green herb sauce.",
    "usa": "The Hamburger is an iconic American food, made from a grilled beef patty placed in a soft bun, topped with lettuce, tomato, cheese, and various condiments like ketchup or mustard. It's a staple of American fast food and backyard barbecues.",
    "brazil": "Feijoada is a rich and hearty Brazilian stew made from black beans, pork, and beef, slow-cooked until tender. It's traditionally served with rice, collard greens, and orange slices, creating a balance between the stew’s deep flavors and the citrus's acidity.",
    "egypt": "Koshari is a beloved Egyptian street food made from a mixture of rice, lentils, chickpeas, and macaroni, all topped with a tangy tomato sauce and crispy fried onions. It's a filling and comforting dish, often served in large portions.",
    "morocco": "Tagine is a slow-cooked Moroccan stew named after the earthenware pot it’s cooked in. The stew combines lamb or chicken with a mix of vegetables and spices such as saffron, cinnamon, and cumin. Often served with couscous or bread.",
    "vietnam": "Pho is a Vietnamese noodle soup consisting of a fragrant broth, rice noodles, herbs, and either beef or chicken. The broth is simmered for hours with bones, creating a deeply flavorful base, and the dish is garnished with lime, chili, and fresh herbs.",
    "south korea": "Kimchi is a spicy and tangy fermented cabbage dish that’s a staple in Korean cuisine. It’s made with Napa cabbage, Korean radishes, and a mix of spices including garlic, ginger, and chili peppers. It accompanies almost every meal in Korea.",
    "russia": "Borscht is a beetroot soup from Russia and Ukraine, giving it its signature red color. It's often made with beef or pork, cabbage, and potatoes, and is served hot with a dollop of sour cream on top. It's a warming dish, perfect for cold winters.",
    "australia": "Vegemite is a dark, salty spread made from yeast extract, enjoyed on toast or crackers. It's an acquired taste, often spread thinly with butter, and is considered a staple of Australian breakfasts.",
    "canada": "Poutine is a Canadian comfort food made with crispy french fries, topped with fresh cheese curds, and smothered in rich brown gravy. The combination of textures and flavors makes it a favorite in Canada, especially during colder months.",
    "peru": "Ceviche is a Peruvian dish made from fresh raw fish marinated in citrus juices like lime, combined with onions, cilantro, and spicy chili peppers. The acidity 'cooks' the fish, giving it a firm texture and refreshing taste.",
    "iran": "Kebab, originating from Iran, is a dish of skewered, grilled meats, typically made with lamb or chicken. The meat is marinated in a blend of spices and herbs, grilled over open flames, and often served with rice or flatbread.",
    "saudi arabia": "Kabsa is a Saudi Arabian rice dish cooked with aromatic spices like cardamom, cloves, and cinnamon, usually accompanied by lamb, chicken, or fish. The meat and rice are cooked together in one pot, infusing deep flavors throughout the dish.",
    "nigeria": "Jollof Rice is a popular West African dish, particularly in Nigeria, made from rice cooked with tomatoes, onions, and a variety of spices. It's often served as a main course with grilled or fried chicken, beef, or fish.",
    "malaysia": "Nasi Lemak is a Malaysian dish consisting of rice cooked in coconut milk, served with sambal (spicy chili paste), fried anchovies, boiled eggs, and cucumber. It's often eaten as breakfast and is considered the national dish of Malaysia.",
    "sweden": "Meatballs, served with lingonberry sauce and creamy mashed potatoes, are a staple in Swedish cuisine. The meatballs are made from a blend of beef and pork, seasoned with spices like allspice and cooked until tender.",
    "indonesia": "Nasi Goreng is Indonesia's take on fried rice, cooked with sweet soy sauce, garlic, shallots, and a variety of vegetables. It’s often topped with a fried egg and served with prawn crackers for added crunch.",
    "ethiopia": "Injera with Doro Wat is a popular Ethiopian dish. Injera is a spongy flatbread made from teff flour, served with Doro Wat, a spicy chicken stew made with a blend of Ethiopian spices. The injera is used to scoop up the stew.",
    "pakistan": "Nihari is a rich and spicy beef stew from Pakistan, slow-cooked with ginger, garlic, and a variety of spices like cardamom and cloves. It's traditionally eaten for breakfast with naan bread and garnished with fresh ginger and coriander.",
}


countries_set = set(famous_foods_dict.keys())
foods_set = set(famous_foods_dict.values())

print("Countries Set:", countries_set)
print("\nFoods Set:", foods_set)


def get_famous_food(country):
    country = country.lower()
    if country in famous_foods_dict:
        return f"\n \nThe famous food of {country.capitalize()} is {famous_foods_dict[country]}. \n \n"
    else:
        return "The country cannot be found."


user_input = input("\n \nPlease enter a country name to see its famous food: ").lower()
result = get_famous_food(user_input)
print(result)
