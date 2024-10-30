my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict ['Egor'])
print(my_dict.get ('Aleks'))
my_dict ['Kirill'] = 1980
my_dict ['Anton'] = 1991
del my_dict ['Masha']
print(my_dict)

my_set = {1, 2, 'Trak', 3.14}
print( my_set)
my_set.update({'Sasha',5})
print( my_set)
print( my_set.discard(3.14))
print( my_set)