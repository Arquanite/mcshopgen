#!/bin/python3

import yaml

config = ''

with open("shop.yml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        

for shop in config['shop']:
    with open(shop['name'] + config['buy-postfix'] + '.xd', "w") as text_file:
        text_file.write('/summon Villager ~ ~1 ~ {')
        text_file.write('Profession:0,')
        text_file.write('CustomName:"{0}",'.format(shop['name'] + config['buy-postfix']))
        text_file.write('CustomNameVisible:1,Career:1,CareerLevel:42,PersistenceRequired:1,NoAI:1,Silent:1,Invulnerable:1,')
        text_file.write('Attributes:[{Name:"generic.knockbackResistance",Base:"1f"},{Name:"generic.movementSpeed",Base:"0f"},{Name:"generic.maxHealth",Base: 99999}],')
        text_file.write('Offers:{Recipes:[')
        for offer in shop['offer']:
            text_file.write('{{buy:{{id:"{0}",Count:{1}'.format(offer['item'], offer['amount']))
            if 'type' in offer:
                text_file.write(',Damage:{0}'.format(offer['type']))
            text_file.write('}},maxUses:9999999,sell:{{id:"{0}",Count:{1}}},rewardExp:false}}'.format(shop['currency'],offer['price']))
            if not offer == shop['offer'][-1]:
                text_file.write(',')
        text_file.write(']},Rotation:[90f,0f]}')
        
    with open(shop['name'] + config['sell-postfix'] + '.xd', "w") as text_file:
        text_file.write('/summon Villager ~ ~1 ~ {')
        text_file.write('Profession:0,')
        text_file.write('CustomName:"{0}",'.format(shop['name'] + config['sell-postfix']))
        text_file.write('CustomNameVisible:1,Career:1,CareerLevel:42,PersistenceRequired:1,NoAI:1,Silent:1,Invulnerable:1,')
        text_file.write('Attributes:[{Name:"generic.knockbackResistance",Base:"1f"},{Name:"generic.movementSpeed",Base:"0f"},{Name:"generic.maxHealth",Base: 99999}],')
        text_file.write('Offers:{Recipes:[')
        for offer in shop['offer']:
            text_file.write('{{buy:{{id:"{0}",Count:{1}'.format(shop['currency'], offer['price']))
            text_file.write('}},maxUses:9999999,sell:{{id:"{0}",Count:{1}'.format(offer['item'],offer['amount']))
            if 'type' in offer:
                text_file.write(',Damage:{0}'.format(offer['type']))
            text_file.write('},rewardExp:false}')
            if not offer == shop['offer'][-1]:
                text_file.write(',')
        text_file.write(']},Rotation:[90f,0f]}')
