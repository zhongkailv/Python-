
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


##########################token_set_ratio函数##########################
print(fuzz.token_set_ratio(my_records2[0].get('favorite_food'),
                           my_records2[1].get('favorite_food')))
#返回68

print(fuzz.token_set_ratio(my_records2[0].get('favorite_drink'),
                           my_records2[1].get('favorite_drink')))
#返回100

print(fuzz.token_set_ratio(my_records2[0].get('favorite_dessert'),
                           my_records2[1].get('favorite_dessert')))
#返回100

print(fuzz.token_set_ratio(my_records2[0].get('favorite_game'),
                           my_records2[1].get('favorite_game')))
#返回89，汉语也可以处理

##########################process.extract函数##########################
choices = ['Yes','No','Maybe','N/A']

process.extract('ya',choices,limit = 2)
#返回[('Yes', 45), ('Maybe', 45)]

process.extractOne('ya',choices)
#返回('Yes', 45)

process.extract('nope',choices,limit = 2)
#返回[('No', 90), ('Yes', 29)]

process.extractOne('nope',choices)
#返回('No', 90)


##########################process.extract函数测试##########################
choices2 = ['魔兽世界','No','Maybe','N/A','魔兽争霸3']

process.extract('魔兽争霸',choices2,limit = 2)
#返回[('魔兽争霸3', 89), ('魔兽世界', 50)]

process.extractOne('魔兽争霸',choices2)
#返回('魔兽争霸3', 89)

process.extract('魔兽',choices2,limit = 2)
#返回[('魔兽世界', 90), ('魔兽争霸3', 90)]

process.extractOne('魔兽',choices2)
#返回('魔兽世界', 90)

process.extract('魔兽争霸4',choices2,limit = 2)
#返回[('魔兽争霸3', 80), ('魔兽世界', 44)]

process.extractOne('魔兽争霸4',choices2)
#返回('魔兽争霸3', 80)

process.extract('魔兽争霸3',choices2,limit = 2)
#返回[('魔兽争霸3', 100), ('魔兽世界', 44)]

process.extractOne('魔兽争霸3',choices2)
#返回('魔兽争霸3', 100)

###以下也是测试代码
choices3 = ['四川省成都市高新区天府软件园B6-3',
            '四川省成都市天府软件园B6-3',
            '四川省成都市高新区天华一路天府软件园B6-3',
            '四川省成都市高新区天府软件园A1',
            '四川省成都市天府软件园A1',
            '四川省成都市高新区天华一路天府软件园A1',
            ]

process.extract('四川省成都市天府软件园B6',choices3,limit = 2)
#返回[('四川省成都市天府软件园B6-3', 95), ('四川省成都市天府软件园A1', 85)]

process.extract('四川省成都市天府软件园B6',choices3)
#返回[('四川省成都市天府软件园B6-3', 95),
# ('四川省成都市天府软件园A1', 85),
# ('四川省成都市高新区天府软件园B6-3', 84),
# ('四川省成都市高新区天府软件园A1', 76),
# ('四川省成都市高新区天华一路天府软件园B6-3', 74)]


fuzz.ratio('colour','color')  #91
fuzz.ratio('colour','coloue')  #83
fuzz.ratio('colour','col')  #67
fuzz.ratio('mysterious','MYSTERIOUS'.lower())  #100
fuzz.ratio('mysterious','mystery')  #71

fuzz.ratio('中国','中华人民共和国')  #44
fuzz.ratio('四川省成都市高新区天府软件园B6-3','四川省成都市天府软件园B6-3') #91
fuzz.ratio('四川省成都市高新区天府软件园B6-3','四川省成都市高新区天府软件园B6-4')#94
fuzz.ratio('四川省成都市高新区天府软件园B6-3','四川省成都市天府软件园A1') #71
fuzz.ratio('四川省成都市高新区天府软件园B6-3','成都市天府软件园A1') #57
fuzz.ratio('四川省成都市高新区天府软件园B6-3','成都市天府软件园B6-3') #80

fuzz.ratio('四川省成都市高新区天府软件园B6-3','重庆市天府软件园A1') #43
fuzz.ratio('上海市天府软件园A1','重庆市天府软件园A1') #80
fuzz.ratio('北京市天府软件园A1','重庆市天府软件园A1') #80
fuzz.ratio('北京市天府软件园A1','天津市天府软件园A1') #80
fuzz.ratio('北京市天府软件园A1','成都市天府软件园A1') #80
fuzz.ratio('asdjhasjdhasdasdasfdsdkfhsdvndsfv',
           'asdjhasjdhasdasdasfdsdkfhsdvndsf') #98
fuzz.ratio('asdjhasjdhasdasdasfdsdkfhsdvndsfv',
           'asdjhasjdhasdasdasfdsdkfhsdvndsvf') #97
fuzz.ratio('jhasjdhasdasdasfdsdkfhsdvndsfv',
           'jhasjdhasdasdasfdsdkfhsdvndsf') #98
fuzz.ratio('jhasjdhasdasdasfdsdkfhsdvndsfv',
           'jhasjdhasdasdasfdsdkfhsdvndsvf') #97
           
fuzz.partial_ratio('四川省成都市高新区天府软件园B6-3','成都市天府软件园B6-3') #75        
fuzz.partial_ratio('中国','中华人民共和国')#50
fuzz.partial_ratio('中华人民','中华人民共和国')#100

from xpinyin import Pinyin
p = Pinyin()
p.get_pinyin(u"上海市徐汇区")
p.get_pinyin(u"吕忠楷")
p.get_pinyin(u"长辈")
p.get_pinyin(u"阿胶")
p.get_pinyin(u"阿胶",show_tone_marks=True)
p.get_pinyin(u"吕忠楷",show_tone_marks=True)
p.get_pinyin(u"四川省成都市高新区天府软件园",'',show_tone_marks=True)




