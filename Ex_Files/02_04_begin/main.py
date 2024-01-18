'''
NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)
'''
# enumerate
Names = ["Quana", "Mason", "Erric", "Tori", "Bria"]
Titles = ["EC", "EC","Tech", "Eng", "Tech"]
Levels = [1, 1, 3, 5, 3]

i = 0
while i < len(Names):
    staff = f"{Names[i]} {Titles[i]} , {Levels[i]}"
    print(staff)
    i += 1

for name in Names:
    print(name)

for name, level in zip(Names, Levels):
    print(f"name: {name} \n level: {level}")

for i in range(10):
    i+=1
    print(i)

for i, name in enumerate(Names):
    print(f"{i} {name}")