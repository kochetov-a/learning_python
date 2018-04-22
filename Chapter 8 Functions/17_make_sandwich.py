# -*- coding: utf-8 -*-


def make_sandwich(*components):
    """Выводим информацию о сендвиче"""
    print("\nГотовим сендвич со следующим составом:")
    for component in components:
        print(component)


make_sandwich('хлеб', 'колбаса', "помидор")
make_sandwich('сыр', 'булка', "лук")
make_sandwich('хлеб', 'колбаса', 'помидор','хлеб', 'горчица', "помидор")
