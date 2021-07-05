
# 딕셔너리
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

lux['health']  # 키가 중복되면 가장 뒤에 있는 값만 사용함

x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}

x = {}
y = dict()

lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux2 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})

lux1['health']

# 딕셔너리에 키를 지정하지 않으면 해당 딕셔너리 전체를 의미

'health' in lux  # 키 확인

len(lux2)
