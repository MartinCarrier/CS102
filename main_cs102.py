from data import lego, lego_data

greetings = '''
 ******************************************************************************
 _                  
| |                 
| | ___  __ _  ___  
| |/ _ \/ _` |/ _ \ 
| |  __/ (_| | (_) |
|_|\___|\__, |\___/ 
         __/ |      
        |___/    
        
CS102 project by Martin Carrier, P.Eng.
******************************************************************************
        '''

def first_question():  # ask user if he/she wants to build some legos
    answer = input("Hey, you want to build some Lego's? (Y/N)")
    if answer in ['Y','y']:
        print("All right!!")
    elif answer in ['N','n']:
        print("OK...")
    else:
        print("Wrong input...")
        answer = first_question()  # recursive call
    return answer

def second_question():  # what is the desired level of difficulty?
    difficulty_level = input('\nWhat is the desired level of difficulty? Use this format: x+, per example: "10+" for 10 years old and over')
    if difficulty_level[-1] == '+':
        age = difficulty_level.strip('+')  # remove '+' sign
        if age.isnumeric():
            return int(age)
        else:
            print('Wrong format...')
            difficulty_level = second_question()  # recursive call
    else:
        print('Wrong format...')
        difficulty_level = second_question()  # recursive call
    return difficulty_level

def thematic():  # this function will return a list of different thematics within lego_data
    thematic_list = []
    for item in lego_data:
        if thematic_list != []:
            already_in = False
            for theme in thematic_list:
                if theme == item[2]:
                    already_in = True
                    break
            if already_in is False:
                thematic_list.append(item[2])
        else:
            thematic_list.append(item[2])
    return thematic_list

def third_question():  # what is the desired thematics
    thematic_list = thematic()
    print('\nPlease choose one of the available thematics: (just type number)...')
    for i in range(len(thematic_list)):
        print("{0}. {1}".format(i + 1, thematic_list[i]))
    theme = input('Your choice: ')
    if theme.isnumeric():
        if int(theme) <= len(thematic_list):
            return thematic_list[int(theme)-1]
        else:
            print('Choice out of range... Try again')
            theme = third_question()  # recursive call
    else:
        print('Wrong input...')
        theme = third_question()  # recursive call
    return theme

def search(diff, theme):
    # then filter thematics
    theme_match = search_list(lego_data, 2, theme)  # get a dictionary of thematics that matches

    # we have to find all legos that have same difficulty level or higher.
    key_to_remove = []
    for key, value in theme_match.items():
        if int(value[0].strip('+')) < diff:
            key_to_remove.append(key)

    if len(key_to_remove) > 0:
        for item in key_to_remove:
            theme_match.pop(item)

    #for key, value in theme_match.items():
    #    print(key, ' : ', value)

    if len(theme_match) == 0:
        #print('no match')
        return 'No match'
    else:
        return theme_match

def search_list(list, idx, target):  # return a dictionary of matches
    results = {}
    index = 0
    for item in list:
        if item[idx] == target:
            results[lego[index]] = item
        index += 1
    return results

def print_recommandation(matches):
    if matches == 'No match':
        print('\nThere is no match with your inputs...')
    else:
        for key, value in matches.items():
            print('\n')
            print('-----------------------------------------------------------------------')
            print("Lego name:",key, "- ID:", value[1])
            print('Difficulty level:', value[0])
            print('Number of pieces:', value[3])
            print('Price: ', value[4], '$')
            store_string = ''
            for i in range(len(value[5])):
                if i == len(value[5])-1:
                    store_string += value[5][i]
                elif i == len(value[5])-2:
                    store_string += value[5][i] + ' & '
                else:
                    store_string += value[5][i] + ', '
            print('Can be found at:',store_string)
            print('-----------------------------------------------------------------------')

def one_sequence():
    # Section to ask 2nd question: What is the desired level of difficulty?
    difficulty = second_question()
    # Section to ask 3rd question: What is the desired thematic?
    chosen_theme = third_question()
    # print('test')
    matches = search(difficulty, chosen_theme)
    print_recommandation(matches)


print(greetings)
first_question_answer = first_question()

if first_question_answer == 'N' or first_question_answer == 'n':
    print("Fair enough! Have a nice day")
    exit()  # terminate program here

loop_var = True
while loop_var:
    one_sequence()
    ask = input('\n\nWould you like to do another search? (Y/N)')
    if ask in ['Y','y']:
        loop_var = True
    else:
        loop_var = False
        print('Thank you and have fun!')
