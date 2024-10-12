#Створити лист із днями тижня.
#В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
#Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dict1 = dict([(number_day + 1, day) for number_day, day in enumerate(week_days)])
dict_reversed = dict([(day, number_day + 1) for number_day, day in enumerate(week_days)])
print(dict1, '\n', dict_reversed)