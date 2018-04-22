# -*- coding: utf-8 -*-


def build_profile(first, last, **user_info):
    profile = {}
    profile['Имя:'] = first
    profile['Фамилия:'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('алексей', 'кочетов',
                             location='санкт-петербург',
                             field='программист', age='30',
                             weight='70', height='186')

print(user_profile)



