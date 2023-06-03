first_name = 'Francisco'
def print_name(name):
    print(name)
print_name(first_name)




def sum(nota_1, nota_2):
    media = (nota_1 + nota_2)/2
    if media >= 14: return print('Dispensou com a media: ', media)
    elif(media < 10): return print('excluido com a media: ', media)
    elif(media > 10 or media < 13): return print('Admitido para os exames com a media: ', media)
    else: return print('sem nota')
    
sum(20, 20) 



# def sum(nota_1, nota_2):
#     media = (nota_1 + nota_2)/2
#     if media >= 14: return f'Dispensou com a media: {media}'
#     elif(media < 10): return f'excluido com a media: {media}'
#     elif(media > 10 or media < 13): return f'Admitido para os exames com a media: {media}'
#     else: return 'sem nota'
    
# call_sum = sum(20, 20) 
# print(call_sum)
