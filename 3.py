#Дана строка в виде случайной последовательности чисел от 0 до 9. 
# Требуется создать словарь, который в качестве ключей будет принимать данные числа 
# (т. е. ключи будут типом int), 
# а в качестве значений – количество этих чисел в имеющейся последовательности.
#  Для построения словаря создайте функцию 
# count_it(sequence) принимающую строку из цифр. 
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
import random
length= int(input ('сколько элементов в строке? '))
rand_num = [random.randint(0,9) for i in range(length)]

def count_it(sequence):
  d = {}
  for i in range(9):
    num_of_i = 0
    for e in sequence:
      if i == e:
        num_of_i = num_of_i + 1
    d[i] = num_of_i
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
  print(d)
  d_1 = {}
  for i, (k, v) in enumerate(d.items()):
   if i == 3: break
   d_1[k] = v
  return d_1


print(rand_num)
print (count_it(rand_num))



