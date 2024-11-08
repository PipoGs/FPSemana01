
character_number1 = str(input("What is the first Character name? "))
health_number1=int(input("Choose the Health points: "))
level_number1=int(input("Choose Character level: "))

character_number2 = str(input("What is the second Character name? "))
health_number2=int(input("Choose the Health points: "))
level_number2=int(input("Choose Character level: "))

character_number3 = str(input("What is the third Character name? "))
health_number3=int(input("Choose the Health points: "))
level_number3=int(input("Choose Character level: "))

chr_data=[
    [character_number1,(health_number1,level_number1)],
    [character_number2,(health_number2,level_number2)],
    [character_number3,(health_number3,level_number3)]
]

print(chr_data)

if level_number1 > level_number2 and level_number1 > level_number3:
    print(character_number1)
    if level_number2 > level_number3:
        print(character_number2)
        print(character_number3)
    else:
        print(character_number3)
        print(character_number2)

if level_number2 > level_number1 and level_number2 > level_number3:
    print(character_number2)
    if level_number1 > level_number3:
        print(character_number1)
        print(character_number3)
    else:
        print(character_number3)
        print(character_number1)

if level_number3 > level_number1 and level_number3 > level_number2:
    print(character_number1)
    if level_number2 > level_number3:
        print(character_number2)
        print(character_number3)
    else:
        print(character_number3)
        print(character_number2) 
