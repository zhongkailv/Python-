
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

my_records = [{'favorite_book' :'Grapes 0f Wrath',
               'favorite_movie':'Free Willie',
               'favorite_show' :'Two Broke Girls',
               'favorite_game' :'魔兽争霸',
               },
               {'favorite_book' :'The Grapes 0f Wrath',
                'favorite_movie':'Free Willy',
                'favorite_show' :'2 Broke Girls',
                'favorite_game' :'魔兽争霸3',
               }]

##########################ratio函数##########################
print(fuzz.ratio(my_records[0].get('favorite_book'),
                 my_records[1].get('favorite_book')))
#返回88

print(fuzz.ratio(my_records[0].get('favorite_movie'),
                 my_records[1].get('favorite_movie')))
#返回86

print(fuzz.ratio(my_records[0].get('favorite_show'),
                 my_records[1].get('favorite_show')))
#返回86

print(fuzz.ratio(my_records[0].get('favorite_game'),
                 my_records[1].get('favorite_game')))
#返回0，汉语需要另外处理

##########################partial_ratio函数##########################
print(fuzz.partial_ratio(my_records[0].get('favorite_book'),
                         my_records[1].get('favorite_book')))
#返回100

print(fuzz.partial_ratio(my_records[0].get('favorite_movie'),
                         my_records[1].get('favorite_movie')))
#返回90

print(fuzz.partial_ratio(my_records[0].get('favorite_show'),
                         my_records[1].get('favorite_show')))
#返回92

print(fuzz.partial_ratio(my_records[0].get('favorite_game'),
                         my_records[1].get('favorite_game')))
#返回0，处理汉语需要在字符前加u,即把'favorite_game' :'魔兽争霸3',
#改为'favorite_game' :u'魔兽争霸3',即可



##########################token_sort_ratio函数##########################
my_records2 = [{'favorite_food'   :'cheeseburgers with bacon',
               'favorite_drink'   :'wine,beer,and tequila',
               'favorite_dessert' :'cheese or cake',
               'favorite_game'    :'魔兽争霸',
               },
               {'favorite_food'   :'burgers with cheese and bacon',
               'favorite_drink'   :'beer,wine,and tequila',
               'favorite_dessert' :'cheese cake',
               'favorite_game'    :'魔兽争霸3',
               }]

print(fuzz.token_sort_ratio(my_records2[0].get('favorite_food'),
                            my_records2[1].get('favorite_food')))
#返回68

print(fuzz.token_sort_ratio(my_records2[0].get('favorite_drink'),
                            my_records2[1].get('favorite_drink')))
#返回100

print(fuzz.token_sort_ratio(my_records2[0].get('favorite_dessert'),
                            my_records2[1].get('favorite_dessert')))
#返回88

print(fuzz.token_sort_ratio(my_records2[0].get('favorite_game'),
                            my_records2[1].get('favorite_game')))
#返回89，汉语也可以处理






