# -*- coding: utf-8 -*-


def car_info(name, maker, **car_info):
    info = {}
    info['Название: '] = name
    info['Производитель: '] = maker
    for key, value in car_info.items():
        info[key] = value
    return info


example = car_info('audi', 'audi enc.', color='blue', tow_package='True')
print(example)

