import math


# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland: str = ('"Would you tell me, please, which way I ought to go from here?"\n'\
                            '"That depends a good deal on where you want to get to," said the Cat.\n'\
                            '"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n'\
                            '"—— so long as I get somewhere," Alice added as an explanation.\n'\
                            '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\n'
                            )


# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
print(f"Одинарні лапки: {' '.join([char for char in alice_in_wonderland if char == "'"])}\n"
      f"________________________________________\n"
      )

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(f"{alice_in_wonderland}"
      f"________________________________________\n"
      )

# task 04

area_blacksea = int (436402)
area_azovsea = int (73800)
area_total = int (area_azovsea + area_blacksea)
print(f"Площа Чорного моря становить {area_blacksea} км2, а площа Азовського моря становить {area_azovsea} км2.\n"
    f"Яку площу займають Чорне та Азовське моря разом?\n"
    f"Загальная полща: {area_total} км2\n"
    f"________________________________________\n"
    )

# task 05

storage_total: int = 375291
storage_01_and_02: int = 250449
storage_02_and_03: int = 222950
storage_01: int = storage_total - storage_02_and_03
storage_03: int = storage_total - storage_01_and_02
storage_02: int = storage_total - storage_01 - storage_03

print(f"Мережа супермаркетів має 3 склади, де всього розміщено\n"
    f"{storage_total} товар. На першому та другому складах перебуває\n"
    f"{storage_01_and_02} товарів. На другому та третьому – {storage_02_and_03} товарів.\n" 
    f"Знайдіть кількість товарів, що розміщені на кожному складі.\n" \
    f"На першому складі: {storage_01:,.0f}".replace(",", " ") + " товарів\n" 
    f"На другому складі: {storage_02:,.0f}".replace(",", " ") + " товарів\n" 
    f"На третьому складі: {storage_03:,.0f}".replace(",", " ") + " товарів\n"
    f"________________________________________\n"
    )

# task 06

pay_01: int = 1179
month: int = 18
total_pay: int = pay_01 * month

print(f"Михайло разом з батьками вирішили купити комп’ютер, скориставшись\n"
    f"послугою «Оплата частинами». Відомо, що сплачувати\n"
    f"необхідно буде {month} місяців по {pay_01} грн/місяць.\n"
    f"Обчисліть вартість комп’ютера.\n"
    f"Вартість комп'ютера: {total_pay:,.0f} грн\n"
    f"________________________________________\n"
    )

# task 07

a, d = 8019, 7248
b, e = 9907, 7128
c, f = 2789, 19224

div_a, div_d = 8, 6
div_b, div_e = 9, 5
div_c, div_f = 5, 9

remainder_a = a % div_a
remainder_b = b % div_b
remainder_c = c % div_c
remainder_d = d % div_d
remainder_e = e % div_e
remainder_f = f % div_f

print(f"Знайди остачу від діленя чисел:\n"
    f"a) {a} : {div_a}     d) {d} : {div_d}\n"
    f"b) {b} : {div_b}     e) {e} : {div_e}\n"
    f"c) {c} : {div_c}     f) {f} : {div_f}\n\n"  
      
    f"Остача від ділення:\n"
    f"a) {remainder_a}      d) {remainder_d}\n"
    f"b) {remainder_b}      e) {remainder_e}\n"
    f"c) {remainder_c}      f) {remainder_f}\n"
    f"________________________________________\n"
    )

# task 08

pizza_large_qty, pizza_large_price = 4, 274
pizza_medium_qty, pizza_medium_price = 2, 218
juice_qty, juice_price = 4, 35
cake_qty, cake_price = 1, 350
water_qty, water_price = 3, 21

print(f"Іринка, готуючись до свого дня народження, склала список того, що їй потрібно замовити:\n"
      f"Піца велика: {pizza_large_qty} шт. по {pizza_large_price} грн\n"
      f"Піца середня: {pizza_medium_qty} шт. по {pizza_medium_price} грн\n"
      f"Сік: {juice_qty} шт. по {juice_price} грн\n"
      f"Торт: {cake_qty} шт. за {cake_price} грн\n"
      f"Вода: {water_qty} шт. по {water_price} грн"
    )

order = {
    "Піца велика": (4, 274),
    "Піца середня": (2, 218),
    "Сік": (4, 35),
    "Торт": (1, 350),
    "Вода": (3, 21)
}
total_cost = sum(quantity * price for quantity, price in order.values())
print(f"Всього знадобиться {total_cost:,} грн для замовлення\n"
      f"________________________________________\n"
      .replace(",", " ")
      )

# task 09

total_photo = 232
photo_per_page = 8
total_page = math.ceil(total_photo / photo_per_page)
print(f"Ігор займається фотографією. Він вирішив зібрати всі свої {total_photo}\n"
    f"фотографії та вклеїти в альбом. На одній сторінці може бути\n"
    f"розміщено щонайбільше {photo_per_page} фото. Скільки сторінок знадобиться\n"
    f"Ігорю, щоб вклеїти всі фото?\n"
    f"Ігорю знадобиться {total_page} сторінок\n"
    f"________________________________________\n"
      )

# task 10

distance = 1600
fuel_per_100km = 9
fuel_tank = 48
total_fuel_need = (distance / 100) * fuel_per_100km
refuel_times = math.ceil(total_fuel_need / fuel_tank)

print(f"Родина зібралася в автомобільну подорож із Харкова в Будапешт.\n"
    f"Відстань між цими містами становить 1600 км.\n"
    f"Відомо, що на кожні 100 км необхідно {fuel_per_100km} літрів бензину.\n" 
    f"Місткість баку становить 48 літрів.\n"
    f"1) Скільки літрів бензину знадобиться для такої подорожі?\n"
    f"2) Скільки щонайменше разів родині необхідно заїхати на заправку\n"
    f"під час цієї подорожі, кожного разу заправляючи повний бак?\n \n"
    
    
    f"""Для подорожі потрібно {total_fuel_need:.1f}л бензину.
Потрібно заїхати на заправку щонайменше {refuel_times} рази.""")