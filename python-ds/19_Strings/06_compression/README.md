##Задача 6. Сжатие
С увеличением объема данных возникла потребность в сжатии этих данных, при этом не потеряв важную информацию. Для этого было придумано кодирование, которое осуществляется следующим образом:

s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на экран. Кодирование должно учитывать регистр символов.

####Пример:
```
Введите строку: aaAAbbсaaaA

Закодированная строка: a2A2b2c1a3A1
```