import time
from playsound import playsound

print('Bem vindo ao nosso app de Pomodoro ')
while True:
    try:
        numero_de_repeticoes = int(input('Quantas vezes você quer realizar o pomodoro? '))
        tempo_de_trabalho = int(input('Por quantos minutos você quer trabalhar? '))
        tempo_de_descanso = int(input('Por quantos minutos voce quer descansar? '))
        print('Bom trabalho! ')
        while numero_de_repeticoes > 0:
            time.sleep(tempo_de_trabalho * 60)
            print('Hora de descansar! ')
            playsound('rick.mp3')
            time.sleep(tempo_de_descanso * 60)
            if numero_de_repeticoes > 1:
                print('Hora de trabalhar!')
            else:
                print('Muito bem! Bom descanso ^^ ')
            playsound('rick.mp3')
            numero_de_repeticoes -= 1
        break
    except ValueError:
        print('O valor deve ser em numeriais! ')
