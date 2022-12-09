recipes = "recipes.txt"

def recipes_dict():
    cook_book = {}

    with open(recipes, encoding="utf-8") as f:
        for line in f:
            dish_name = line.strip()
            ingredients_count = int(f.readline())

            cook_book[dish_name] = []

            for i in range(ingredients_count):
                ingredient_info = f.readline().strip().split(" | ")
                cook_book[dish_name].append({
                    "ingredient_name": ingredient_info[0],
                    "quantity": ingredient_info[1],
                    "measure": ingredient_info[2]
                })
            f.readline()

    print(cook_book)


if __name__ == "__main__":
    recipes_dict()