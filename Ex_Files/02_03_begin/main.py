'''
NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

JOHN_PAUL = NAMES[:2]
GEORGE_RINGO = NAMES[2:]
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
'''

FRUITS = ["Apple", "Orange", "Banana", "Cherry", "Kiwi"]
scores = [75, 92, 100, 65, 50]

print(FRUITS, scores)
firstThreeFruits = FRUITS[:3]
print(firstThreeFruits)
remainingFruits = FRUITS[3:]
print(remainingFruits)
reverseFruits = FRUITS[::-1]
print(reverseFruits)

print(sum(scores))
print(max(scores))
print(min(scores))