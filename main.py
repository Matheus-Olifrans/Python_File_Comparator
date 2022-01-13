def separate(the_people):
    person = []
    index = 0
    for letter in the_people:
        if letter != '\n':
            try:
                person[index] = person[index] + letter
            except IndexError:
                [person.append('') for _ in range(index - len(person))]
                person.append(letter)
            except TypeError:
                [person.append('') for _ in range(index - len(person))]
                person.append(letter)
        else:
            index = index + 1
    return person


def compare(people, nearby):
    people_set = set(people)
    nearby_set = set(nearby)
    try:
        people_set.remove('')
    except KeyError:
        pass
    try:
        nearby_set.remove('')
    except KeyError:
        pass
    return nearby_set.intersection(people_set)


r = None
while 1 != 2:
    r = input('digite quem para adicionar amingos ou "done" para terminar: ')
    if r == 'done':
        break
    else:
        with open('people', 'a') as f:
            f.write(r + '\n')
with open('people', 'r') as f:
    just_people = f.read()
with open('nearby_people', 'r') as f:
    near_people = f.read()
# print(just_people)
# print(near_people)
print('\n\nAmigos próximos são: ')
near_friends = compare(separate(near_people), separate(just_people))
print(', '.join(near_friends))
