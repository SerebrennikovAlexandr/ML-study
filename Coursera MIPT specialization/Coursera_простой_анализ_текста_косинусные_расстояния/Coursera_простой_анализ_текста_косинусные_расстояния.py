'''

ТЕМА ДАННОЙ ПРОГРАММЫ:
Знакомство с методами подсчета косинусного расстояния и решения систем линейных уравнений.
На решении систем линейных уравнений основана настройка линейных моделей —
очень большого и важного класса алгоритмов машинного обучения.
Косинусное расстояние же часто используется в анализе текстов для измерения сходства между ними.

ОПИСАНИЕ ЗАДАЧИ:
Дан набор предложений, скопированных с Википедии.
Каждое из них имеет "кошачью тему" в одном из трех смыслов:
 - кошки (животные)
 - UNIX-утилита cat для вывода содержимого файлов
 - версии операционной системы OS X, названные в честь семейства кошачьих

Задача — найти два предложения, которые ближе всего по смыслу
к расположенному в самой первой строке.
В качестве меры близости по смыслу мы будем использовать косинусное расстояние.

'''
import scipy.spatial as ss
import numpy as np
import re


sentences = open("Wiki_cat_sentences.txt", 'r').readlines()
sentences = list(map(lambda x: x.lower(), sentences))
sentences = list(map(lambda x: x.strip(), sentences))
sentences_by_words = list(map(lambda x: re.split('[^a-z]', x), sentences))
words = []

for i in range(len(sentences_by_words)):
    while '' in sentences_by_words[i]:
        sentences_by_words[i].remove('')
    words += sentences_by_words[i]

all_words = list(set(words))
all_words.sort()
matrix = np.zeros((len(sentences), len(all_words)))
for i in range(len(sentences_by_words)):
    for j in range(len(sentences_by_words[i])):
        k = all_words.index(sentences_by_words[i][j])
        matrix[i][k] += 1
cos_reslts = []
for i in range(1, len(sentences)):
    cos_new = ss.distance.cosine(matrix[0], matrix[i])
    cos_reslts.append(1-cos_new)
with open("Wiki_cat_results.txt", "w") as f:
    if len(sentences) == 1:
        print("No sentences to analyze", file=f, end="")
    elif len(sentences) < 4:
        print(cos_reslts.index(max(cos_reslts))+1, file=f, end="")
    else:
        mx = max(cos_reslts)
        print(cos_reslts.index(mx) + 1, file=f, end=" ")
        cos_reslts.remove(mx)
        print(cos_reslts.index(max(cos_reslts)) + 1, file=f, end="")








