import math

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
""""Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
"""
)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
single_quotes = ' '.join([char for char in alice_in_wonderland if char == "'"])
print("Одинарні лапки:", single_quotes)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_blacksea = int (436402)
area_azovsea = int (73800)
area_total = int (area_azovsea + area_blacksea)
print(f'Загальная полща: {area_total} км2\n')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
storage_total = 375291
storage_01_and_02 = 250449
storage_02_and_03 = 222950
storage_01 = storage_total - storage_02_and_03
storage_03 = storage_total - storage_01_and_02
storage_02 = storage_total - storage_01 - storage_03

print(f"На першому складі: {storage_01:,.0f}".replace(",", " ") + " товарів\n"
f"На другому складі: {storage_02:,.0f}".replace(",", " ") + " товарів\n"
f"На третьому складі: {storage_03:,.0f}".replace(",", " ") + " товарів\n"
)
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

pay_01 = 1179
month = 18
total_pay = pay_01 * month
print(f"Вартість комп'ютера: {total_pay:,.0f} грн\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
remainder_a = 8019 % 8
remainder_b = 9908 % 9
remainder_c = 2789 % 5
remainder_d = 7248 % 6
remainder_e = 7128 % 5
remainder_f = 19224 % 9

print(f"""Остача від ділення:
a) 8019 : 8 = {remainder_a}
b) 9907 : 9 = {remainder_b}
c) 2789 : 5 = {remainder_c}
d) 7248 : 6 = {remainder_d}
e) 7128 : 5 = {remainder_e}
f) 19224 : 9 = {remainder_f}\n"""
      )
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
order = {
    "Піца велика": (4, 274),
    "Піца середня": (2, 218),
    "Сік": (4, 35),
    "Торт": (1, 350),
    "Вода": (3, 21)
}
total_cost = sum(quantity * price for quantity, price in order.values())
print(f"Всього знадобиться {total_cost:,} грн для замовлення\n".replace(",", " "))

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_photo = 232
photo_per_page = 8
total_page = math.ceil(total_photo / photo_per_page)
print(f"Знадобиться {total_page} сторінок")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
fuel_per_100km = 9
fuel_tank = 48
total_fuel_need = (distance / 100) * fuel_per_100km
refuel_times = math.ceil(total_fuel_need / fuel_tank)

print(f"""Для подорожі потрібно {total_fuel_need:.1f}л бензину.
Потрібно заїхати на заправку щонайменше {refuel_times} рази.""")