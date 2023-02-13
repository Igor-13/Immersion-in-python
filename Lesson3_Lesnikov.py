""" Урок №3 """

# Задание 1. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

elem = [1, 1, 1, 22, 31, 31, 17, 17, 4, 21, 21, 6, 11]
result = []

for i in range(len(elem)):
    n = elem.pop()
    if n in elem:
        if n in result:
            continue
        else:
            result.append(n)
    else:
        continue

result.reverse()
print(result)

# **********************************************************************************************************************

# Задание 3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый
# вариант. *Верните все возможные варианты комплектации рюкзака.

backpack = 5.0
backpack_full = []
things = {
    'sleeping bag': 2,
    'tourist mat': 1.5,
    'lantern': 1.7,
    'thermos': 1,
    'cup': 0.5
}

for key, var in things.items():
    if backpack - var > 0:
        backpack_full.append(key)
        backpack -= var
    else:
        continue
print(f'the backpack will fit: {backpack_full}')

# **********************************************************************************************************************

# Задание 2. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не
# учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к
# языку.

text = """ Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и
автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и
его качества, а также на обеспечение переносимости написанных на нём программ. Язык является полностью
объектно-ориентированным в том плане, что всё является объектами. Необычной особенностью языка является выделение
блоков кода пробельными отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает
необходимость обращаться к документации. Сам же язык известен как интерпретируемый и используется в том числе для
написания скриптов. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление
памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C
или C++. Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное,
структурное, объектно-ориентированное программирование, метапрограммирование и функциональное программирование.
Задачи обобщённого программирования решаются за счёт динамической типизации. Аспектно-ориентированное
программирование частично поддерживается через декораторы[32], более полноценная поддержка обеспечивается
дополнительными фреймворками. Такие методики как контрактное и логическое программирование можно реализовать с
помощью библиотек или расширений. Основные архитектурные черты — динамическая типизация, автоматическое управление
памятью, полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений с глобальной
блокировкой интерпретатора (GIL), высокоуровневые структуры данных. Поддерживается разбиение программ на модули,
которые, в свою очередь, могут объединяться в пакеты. Эталонной реализацией Python является интерпретатор CPython,
который поддерживает большинство активно используемых платформ и являющийся стандартом де-факто языка. Он
распространяется под свободной лицензией Python Software Foundation License, позволяющей использовать его без
ограничений в любых приложениях, включая проприетарные. CPython компилирует исходные тексты в высокоуровневый
байт-код, который исполняется в стековой виртуальной машине. К другим трём основным реализациям языка относятся
Jython (для JVM), IronPython (для CLR/.NET) и PyPy. PyPy написан на подмножестве языка Python (RPython) и
разрабатывался как альтернатива CPython с целью повышения скорости исполнения программ, в том числе за счёт
использования JIT-компиляции. Поддержка версии Python 2 закончилась в 2020 году. На текущий момент активно
развивается версия языка Python 3. Разработка языка ведётся через предложения по расширению языка PEP (англ. Python
Enhancement Proposal), в которых описываются нововведения, делаются корректировки согласно обратной связи от
сообщества и документируются итоговые решения. Стандартная библиотека включает большой набор полезных переносимых
функций, начиная с возможностей для работы с текстом и заканчивая средствами для написания сетевых приложений.
Дополнительные возможности, такие как математическое моделирование, работа с оборудованием, написание
веб-приложений или разработка игр, могут реализовываться посредством обширного количества сторонних библиотек,
а также интеграцией библиотек, написанных на Си или C++, при этом и сам интерпретатор Python может интегрироваться
в проекты, написанные на этих языках. Существует и специализированный репозиторий программного обеспечения,
написанного на Python, — PyPI. Данный репозиторий предоставляет средства для простой установки пакетов в
операционную систему и стал стандартом де-факто для Python. По состоянию на 2019 год в нём содержалось более 175
тысяч пакетов[45]. Python стал одним из самых популярных языков, он используется в анализе данных,
машинном обучении, DevOps и веб-разработке, а также в других сферах, включая разработку игр. За счёт читабельности,
простого синтаксиса и отсутствия необходимости в компиляции язык хорошо подходит для обучения программированию,
позволяя концентрироваться на изучении алгоритмов, концептов и парадигм. Отладка же и экспериментирование в
значительной степени облегчаются тем фактом, что язык является интерпретируемым. Применяется язык многими крупными
компаниями, такими как Google или Facebook. По состоянию на сентябрь 2022 года Python занимает первое место в
рейтинге TIOBE популярности языков программирования с показателем 15,74%. «Языком года» по версии TIOBE Python
объявлялся в 2007, 2010, 2018, 2020 и 2021 годах. """

text_list = text.split()
dictionary_words = {}
sorted_dict_words = {}
for i in text_list:
    if len(i) > 1:
        if i in dictionary_words:
            continue
        else:
            var = text_list.count(i)
            dictionary_words[i] = var
    else:
        continue

sorted_val = sorted(dictionary_words.values(), reverse=True)

for n in sorted_val:
    for m in dictionary_words.keys():
        if dictionary_words[m] == n:
            sorted_dict_words[m] = dictionary_words[m]
            break

idx = 0
for key, var in sorted_dict_words.items():
    if idx < 9:
        print(f'{key} - {var}')
        idx += 1
    else:
        continue