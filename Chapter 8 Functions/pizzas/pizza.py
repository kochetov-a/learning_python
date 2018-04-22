def make_pizza(size, *toppings):
    """Выводит описание пиццы"""
    print("\nДелаем " + str(size) + "-см пиццу с следующим составом:")
    for topping in toppings:
        print("- " + topping)
