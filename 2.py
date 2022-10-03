#Иван решил создать самый большой словарь в мире. 
# Для этого он придумал функцию biggest_dict(**kwargs), 
# которая принимает неограниченное количество параметров «ключ:значение» 
# и обновляет созданный им словарь my_dict, 
# состоящий всего из одного элемента «first_one» 
# со значением «we can do it». Воссоздайте эту функцию.
#key= input('введите ключ ')
#znachenie=input('введите значение ')
#def biggest_dict(**kwargs):
#key= input('введите ключ ')
#znachenie=input('введите значение ')
 #first_one=["we can do it"]
 #my_dict=dict.fromkeys(first_one, "от Ивана")
 #my_dict[key]=znachenie

#def to_dict(lst):

#print(biggest_dict(key,znachenie))

my_dict={"first_one":"we can do it"}
def biggest_dict(**kwargs):
    my_dict.update(kwargs)
    print( my_dict)

biggest_dict(banana=5, mango=7, apple=8)