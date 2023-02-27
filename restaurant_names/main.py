# As an exercise to create a plausible Asian restaurant name by random selection.

import random

list1 = ['Madame Wu\'s', 'Silver', 'Red', 'Golden', 'Magic', 'Laughing Buddha', 'Bamboo', 'Jade',
         'Little', 'Green', 'China', 'Wuhan', 'Hong Kong', 'Yangtze River', 'Szechuan', 'Shanghai']

list2 = ['Hidden Tiger', 'Mandarin', 'Lotus', 'Dumpling', 'Dancing Panther', 'Noodle', 'Beijing', 'Dragon Egg',
         'Plum', 'Good Fortune', 'Star', 'Wonton', 'Happy Panda', 'Cuisine', 'Wall']

list3 = ['Palace', 'Lounge', 'House', 'Garden', 'Express', 'Dynasty', 'Buffet', 'Empire', 'Wok', 'Bowl']

colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']


def grab_from_list(li, pop=False):

    i = random.randint(0, (len(li) - 1))

    if pop:
        item = li.pop(i)
        return item
    else:
        return li[i]


restaurant_name = grab_from_list(colors)
restaurant_name += grab_from_list(list1) + ' '
restaurant_name += grab_from_list(list2) + ' '
restaurant_name += grab_from_list(list3, True) + ' '
restaurant_name += grab_from_list(list3) + ' '


print('\n' + restaurant_name + '\033[0m')
