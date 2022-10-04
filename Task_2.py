import random


def how_many_take(candies):
    move = 28
    result = 0
    list_num = []
    i = 1
    while(result < candies):
        result = i * (move + 1)
        list_num.append(result)
        i+=1
    return list_num


def behavior_of_computer(j, list_of_numbers, player_number):
    if(list_of_numbers[j] == list_of_numbers[0]):
        return player_number
    subtraction = list_of_numbers[j] - player_number
    result = subtraction - list_of_numbers[j-1]
    return result

def wrong_count(move):
    if(move > 29 or move < 0):
        print('Ты ввел не то количество. Попробуй еще раз')
        return False
    else: return True

def who_first():
    result = random.randint(1,2)
    if(result == 1):
        print('Первым ходит компьютер')
        return 1
    else: 
        print('Первым ходит человек')

        count_player_number = int(input(f'Человек ты ходишь\nСколько ты берешь конфет из оставшихся: {candies}? '))
        return count_player_number

    
def the_game(candies):
    j = -1
    count_player_number = who_first()

    while (candies >= 1):

        if(candies <= 28):
            return print('Победил компьютер!')

        print(f'Компьютер ты ходишь\nСколько ты берешь конфет из оставшихся: {candies}?')
        result = behavior_of_computer(j, list_of_numbers, count_player_number)
        candies -=result
        j-=1
        print(f'Компьютер взял {result} конфет \n')
        print(f'Осталось {candies}')


        count_player_number = int(input(f'Человек ты ходишь\nСколько ты берешь конфет из оставшихся: {candies}? '))
        correct_count = wrong_count(count_player_number)

        while(correct_count == False):
            count_player_number = int(input(f'Сколько ты берешь конфет из оставшихся: {candies}? '))
            correct_count = wrong_count(count_player_number)

        candies -=count_player_number
        print(f'Осталось {candies}')



 

candies = 2021
list_of_numbers = how_many_take(candies)
the_game(candies)