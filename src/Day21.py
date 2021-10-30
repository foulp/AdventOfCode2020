from pathlib import Path


if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        foods = f.read().split('\n')

    allergens_links = {}
    ingredients_all = []
    for food in foods:
        ingredients, allergens = food.split('(contains ')
        ingredients = ingredients.strip().split()
        ingredients_all.extend(ingredients)
        allergens = allergens.strip(')').split(', ')
        for a in allergens:
            if a in allergens_links:
                allergens_links[a] = allergens_links[a].intersection(ingredients)
            else:
                allergens_links[a] = set(ingredients)

    impossible_ingredients = set(ingredients_all) - set.union(*(allergens_links[a] for a in allergens_links))
    print(f"The result of first star is {sum(ingredients_all.count(i) for i in impossible_ingredients)}.")

    found_ingredients = {a: i.pop() for a, i in allergens_links.items() if len(i) == 1}
    while any(len(allergens_links[a]) > 1 for a in allergens_links):
        for a in allergens_links:
            allergens_links[a] = allergens_links[a] - set(found_ingredients.values())
            if len(allergens_links[a]) == 1:
                found_ingredients[a] = allergens_links[a].pop()

    print(f"The result of second star is {','.join(found_ingredients[a] for a in sorted(found_ingredients.keys()))}.")
