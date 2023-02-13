#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

user_profiles = [{
  'age': '53',
  'username': 'WDenaro',
  'weapons': '',
  'is_active': True,
  'clan': 'House Stark'
}]

#2 iterate and print all the keys in the above user.
print(user_profiles[0].keys())
print('\n')

#3 Add a new weapon to your user
user_profiles[0]['weapons'] = ['Trebuchet', 'Catapult', 'Scythe']

#4 Add a new key to include 'is_banned'. Set it to true
user_profiles[0]['is_banned'] = True

#5 Ban the user by setting the previous key to false
user_profiles[0]['is_banned'] = False

#6 create a new user2 by copying the previous user and update the age value and username value.
user_profiles.append(user_profiles[0].copy())

user_profiles[1]['username'] = 'Yoaster'
user_profiles[1]['age'] = '49'
user_profiles[1]['weapons'] = ['Valyrian Steel Sword']
user_profiles[1]['clan'] = 'House Mormont'

print(user_profiles)