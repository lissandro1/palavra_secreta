import os

title = ' DESCUBRA A PALAVRA SECRETA '
print(f'{title:*^40}')
print()
password = 'juliana'
letters_correct = ''
cont = 0

while True:
    letter = input('Digite uma letra: ').lower()

    if len(letter) > 1:
        print('Digite apenas uma letra.')
        continue
   
    if letter.isalpha() == True:
        next
    else:
        print('Por favor, são aceitáveis apenas letras.')
    
    cont += 1
    if letter in password:
        letters_correct += letter
    
    word_correct = ''
    for letter_secret in password:
        if letter_secret in letters_correct:
            word_correct += letter_secret
        else:
            word_correct += '*'
    
    print(f'A palavra secreta: {word_correct}')
    
    if word_correct == password:
        os.system('cls')
        print(f'Parabéns! Você acertou a palavra secreta: "{word_correct}"')
        print(f'O número de tentativas foi: {cont}')
        letters_correct = ''
        cont = 0
        break
    
 


    
    
    
    
   
    

    







