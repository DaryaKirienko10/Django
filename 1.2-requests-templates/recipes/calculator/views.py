from django.http import Http404, JsonResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipes(request, recipe_name):
    recipe_name = recipe_name.lower()

    if recipe_name in DATA:
        recipe = DATA[recipe_name]
        servings = request.GET.get('servings')

        if servings is not None:
            try:
                servings = int(servings)
                if servings <= 0:
                    raise ValueError
            except ValueError:
                return JsonResponse({'error':'Параметр servings должен быть положительным целым числом'}, status = 400)
        else:
            servings = 1

        mod_recipe = {ingredient: round(amount * servings, 2) for ingredient, amount in recipe.items()}
        context = {
            'recipe': mod_recipe
        }
        return render(request, 'calculator/index.html', context)
    else:
        raise Http404("Рецепт не найден")