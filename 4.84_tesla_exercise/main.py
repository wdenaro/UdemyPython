def checkDriverAge(age):

  try:
    if int(age) < 18:
      print('Sorry, you are too young to drive this car. Powering off')

    elif int(age) == 69:
      print(
        'You are either an experienced driver or have that special sense of humor that I, as an automible of the 2020s enjoy. Have a great ride!'
      )

    elif int(age) > 75:
      print(
        'Powering On... but reluctantly. Please be careful... Do you have your spectacles?'
      )

    elif int(age) > 18:
      print('Powering On. Enjoy the ride!')

    else:
      print('Congratulations on your first year of driving. Enjoy the ride!')

  except ValueError:
    try:
      val = float(age)
      print('Please enter a whole number. Powering off. Try again.')

    except ValueError:
      print(
        'I\'m sorry, You didn\'t enter a number. No Ride for you, dumbass.')

  return None


your_age = input('What is your age?: ')

checkDriverAge(your_age)

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.