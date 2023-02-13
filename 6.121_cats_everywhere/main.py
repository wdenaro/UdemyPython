# Given the below class:
class Cat:
  species = 'mammal'

  def __init__(self, name, gender, age):
    self.name = name
    self.gender = gender
    self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Nala', 'female', 13)
cat2 = Cat('Garfield', 'male', 43)
cat3 = Cat('Puss', 'male', 9)


# 2 Create a function that finds the oldest cat
def find_oldest(cats):
  oldest = {'name': '', 'gender': '', 'age': 0}

  for cat in cats:
    if cat.age > oldest['age']:
      oldest['name'] = cat.name
      oldest['gender'] = cat.gender
      oldest['age'] = cat.age
      oldest['pronoun'] = 'he' if oldest['gender'] == 'male' else 'she'

  return oldest


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest_cat = find_oldest([cat1, cat2, cat3])

print(
  f"The oldest cat is {oldest_cat['name']}, {oldest_cat['pronoun']} is {oldest_cat['age']} years old."
)



# # Instructor's Solution
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # Instantiate the Cat object with 3 cats
# peanut = Cat("Peanut", 3)
# garfield = Cat("Garfield", 5)
# snickers = Cat("Snickers", 1)


# # Find the oldest cat
# def get_oldest_cat(*args):
#     return max(args)


# # Output
# print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")