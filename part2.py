import pickle
from itertools import chain
import numpy as np



d = input("Dish type: ")
given_ingredients = input("provide ingredients: ").split(" ")


R = []
ingredients = []
for recipe in recipe_data:
    if d in recipe['title']:
        R.append(recipe)
        ingredients.append(recipe["ingredients"])
all_ingredients1 = np.unique(np.array(list(chain.from_iterable(ingredients))))

all_ingredients = []
for i in all_ingredients1:
    if i in given_ingredients:
        pass
    else:
        all_ingredients.append(i)


def P_of_xt(xt):
    count = 0
    for recipe in R:
        result = set(x in recipe['ingredients'] for x in xt)
        flag = 0
        for ans in result:
            if ans == False:
                flag=1
        if flag == 0:
            count += 1
    return count


most_likely_ingredient = ''
val = -1

for t in all_ingredients:
    x = given_ingredients + [t]
    ingredient_output = P_of_xt(x)/len(R)
    if ingredient_output > val:
        val = ingredient_output
        most_likely_ingredient = t


print("Most likely ingredient is:",most_likely_ingredient)