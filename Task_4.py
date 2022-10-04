# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# AAAAAAAABCCCC
# 8×A, B, 4×c

# Модуль сжатия
# def compression(x):
#     compression_result = {}
#     for c in x:
#        compression_result[c] = x.count(c)
#     return compression_result

# print(compression("AAAAAAAABCCCC"))




# Модуль восстановления
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

info = {'A': 8, 'B': 1, 'C': 4}
print(recovery(info))


