recipes = "recipes.txt"

def get_list_by_dishes(dishes, person_count):
    result = {}

    for dish in dishes:
        with open(recipes, encoding="utf-8") as f:
         for line in f:
            if dish == line.strip():
                ingredients_count = int(f.readline())
                for i in range(ingredients_count):
                    ingredients_info = f.readline().strip().split(" | ")
                    result.update({
                        ingredients_info[0]: {"measure": ingredients_info[2], "quantity": int(ingredients_info[1]) * person_count}
                    })

    print(result)


if __name__ == "__main__":
    get_list_by_dishes(["Запеченный картофель", "Омлет"], 2)