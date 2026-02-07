day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

belgi='a'
match belgi:
  case 'a':
    print('a')
  case 'b':
    print('b')
  case 'a':
    print('b')

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")


month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")


value = 2

match value:
    case 1:
        print("Бір")
    case 2:
        print("Екі")
    case 3:
        print("Үш")
    case _:
        print("Белгісіз мән")


person = ("John", 25)

match person:
    case (name, age) if age >= 18:
        print(f"{name} — ересек адам")
    case (name, age):
        print(f"{name} — кәмелетке толмаған адам")

coordinates = (10, 20)

match coordinates:
    case (x, y):
        print(f"X: {x}, Y: {y}")