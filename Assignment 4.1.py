def conversion():
  intro()

  try:
    
    miles_needed = int(input("Enter the number of miles driven: "))

    miles_kilometers(miles_needed)

  except:
    print("An exception occurred, try again by entering only a         number.")
    print()
  conversion()

def intro():
  print("This program converts measurements from miles to kilometers")
  print("For your reference the conversion is: ")
  print("1 mile = 1.609344 kilometers")
  print("1.609344 kilometers = 1 mile")
  print()

def miles_kilometers(kilometers):
  miles = kilometers * 1.609344
  kilometers = miles * 1
  print("That converts to", miles, "kilometers.")
  print("\n")

conversion()