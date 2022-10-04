# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
import ast

# 8×A, B, 4×c

# Модуль сжатия

# def compression(x):
#     compression_result = {}
#     for c in x:
#        compression_result[c] = x.count(c)
#     return compression_result


# first_com = open('Task_4_start.txt', 'r')
# first_com_str = first_com.read()

# print(compression(first_com_str))
# first_com.close()



# # Модуль восстановления

def recovery(x):
    k = 0
    result = []
    list_num = []
    for i in x.values():
        list_num.append(i)
    i = 0
    for j in x.keys():
        while(k < list_num[i]):
            result.append(j)
            k+=1
        k = 0
        i+=1
    return result



def new_dict(second_com_str):
    result = ast.literal_eval(second_com_str)
    return result


second_com = open('Task_4_end.txt', 'r')
second_com_str = second_com.read()
dict = new_dict(second_com_str)

print(recovery(dict))


