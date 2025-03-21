
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""


adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.splitlines())

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_count = adwentures_of_tom_sawer.count('h')
print(f"\nЛітера 'h' встречается в тексте {h_count} раз.")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
capitalized_words = [word for word in adwentures_of_tom_sawer.split()
                     if word[0].isupper()]
print(f"\nКількість слів які починаються з великої літери: {len(capitalized_words)}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
tom_positions = [i for i, word in enumerate(adwentures_of_tom_sawer.split()) if word == "Tom"]
if len(tom_positions) > 1:
    print(f"\nДруге входження слова 'Tom' знаходиться на позиції: {tom_positions[1]}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = [sentence.strip() + '.' for sentence in adwentures_of_tom_sawer.split('.') if sentence]
print(f"\nРозділений текст на речення: {adwentures_of_tom_sawer_sentences}")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_4 = adwentures_of_tom_sawer_sentences[4]

print(f"\n{adwentures_of_tom_sawer_4.lower()}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

is_start_adwentures: bool = any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)

print(f"\n{is_start_adwentures}:")  # True (если есть хотя бы одно предложение, иначе False)

for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        print(sentence)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_counnt = len(last_sentence.split())
print(f"\nКількість слів останнього речення: {word_counnt}")
