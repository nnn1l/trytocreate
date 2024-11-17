# Make a directory with 2 modules; make a function in one of them;
# then import this function in the other module and use that in your script of choice.

def module():
    quest = input('А и Б сидели на трубе. А упала, Б пропала, кто остался на трубе? : ')
    if quest.lower() == 'и':
        print('Молодец! Возьми с полки пирожок')
    else:
        print('Это была \'и\'')