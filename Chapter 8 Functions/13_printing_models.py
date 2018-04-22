# -*- coding: utf-8 -*-


def print_models(unprinted_models, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_models:
        current_design = unprinted_models.pop()

        # Имитация печати на 3D принтере.
        print("Печатается: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """ Выводит информацию обо всех напечатанных моделях. """
    print("\nСледующие модели были напечатаны: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_design = ["iphone case", "robot", "dragon"]
completed_models = []

print_models(unprinted_design, completed_models)
show_completed_models(completed_models)
