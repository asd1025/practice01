# 문제9.
# 주어진 if 문을 dict를 사용해서 수정하세요.

menu = input('메뉴: ')

menus = {'오뎅':300,'순대':400,'만두':500}
if menu  not in menus.keys() :
    price = 0
else :
    price = menus[menu]
print('가격: {0}'.format(price))
