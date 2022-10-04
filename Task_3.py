
import random

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def choose_symbol():
   result = random.randint(1, 2)
   if(result == 1):
      return 'X'
   else: return'O'
   

def who_first():
    result = random.randint(1,2)
    if(result == 1):
        print('Первым ходит компьютер. Выбери О или Х')
        computer_symbol = choose_symbol()
        print(f'Компьютер выбрал {computer_symbol}')
        if(computer_symbol == 'X'): human_symbol = 'O'
        else: human_symbol = 'X'
        return human_symbol, computer_symbol
    else: 
        print('Первым ходит человек')
        human_symbol = input('Выбери символ: X или O? ')
        if(human_symbol == 'X'): computer_symbol = 'O'
        else: computer_symbol = 'X'
        return human_symbol, computer_symbol



def the_game(human_symbol, computer_symbol, board):
   steps = 0
   while(steps != 9):

         print("Человек ты ходишь")
         i = int(input("Выбери цифру, куда поставишь: "))
         board[i - 1] = human_symbol
         draw_board(board)
         if (check_win(board, winner = 'человек') == True):
            break
         steps +=1

         print("Компьютер ты ходишь. Выбери цифру, куда поставишь: ")
         result = random.randint(0,8)
         while(board[result-1] == 'X' or board[result-1] == 'O'):
            result = random.randint(0,8)
         board[result - 1] = computer_symbol
         print(f'Компьютер поставил в позицию {result}')

         if (check_win(board, winner = 'компьютер') == True):
            break
         steps +=1

         draw_board(board)
      
   if steps == 9:
      print("Ничья!")

      


def check_win(board, winner):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for i in win_coord:
       if board[i[0]] == board[i[1]] == board[i[2]]:
            print(f'Победитель - {winner}! Ура!')
            return True
   return False



human_symbol, computer_symbol = who_first()

board = list(range(1,10))

draw_board(board)
the_game(human_symbol, computer_symbol, board)