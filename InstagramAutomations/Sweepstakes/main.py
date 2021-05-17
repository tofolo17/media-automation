import datetime

import pandas as pd

from Functions import *

# Coordenadas do sorteio
coordenadas = [line.strip('\n').split() for line in open('text/coordenadas', 'r').read().splitlines()]
navegador = coordenadas[0]
post = coordenadas[1]
copia_inicial = coordenadas[2]
copia_final = coordenadas[3]
campo_input = coordenadas[4]
botao = coordenadas[5]
bloqueio = coordenadas[6]
sair_post = coordenadas[7]
refresh = coordenadas[8]

# Lista de usuários para comentários
lista_de_usuarios = pd.read_csv('text/usuarios.csv')['username'].to_list()

# Dicionário  de parâmetros
parametros_sorteio = {
    'Quantidade de participantes': 3,
    'Contador': pegar_contagem('text/contagem'),
    'Contagem final': 150,
}

# Clica no navegador
vai_e_clica(int(navegador[0]), int(navegador[1]))

while parametros_sorteio['Contador'] <= parametros_sorteio['Contagem final']:
    # CLica na publicação
    vai_e_clica(int(post[0]), int(post[1]))

    sleep(1)

    # Copia algo aleatório
    pg.moveTo(int(copia_inicial[0]), int(copia_inicial[1]), randint(50, 100) / 100)
    pg.mouseDown(button='left')
    pg.moveTo(int(copia_final[0]), int(copia_final[1]), randint(50, 100) / 100)
    pg.mouseUp(button='left')
    pg.hotkey('ctrl', 'c')

    # Clica no campo de escrita
    vai_e_clica(int(campo_input[0]), int(campo_input[1]))

    # Faz os comentários
    for i in range(
            parametros_sorteio['Contador'],
            parametros_sorteio['Contador'] + parametros_sorteio['Quantidade de participantes']
    ):
        pg.write(f'@{lista_de_usuarios[i]} ', interval=randint(10, 25) / 100)
        print(f'{lista_de_usuarios[i]} || {i}')

    # Comenta
    vai_e_clica(int(botao[0]), int(botao[1]))

    # Atualiza os arquivos de texto e parâmetros da função
    atualizar_contagem(
        'text/contagem',
        pegar_contagem('text/contagem'),
        parametros_sorteio['Quantidade de participantes']
    )
    parametros_sorteio['Contador'] = pegar_contagem('text/contagem')

    print('')
    sleep(2.5)

    # Checa bloqueio
    valor_copiado = verifica_bloqueio(int(bloqueio[0]), int(bloqueio[1]))
    print(f'Valor copiado: {valor_copiado}\n')
    if 'comentário.' in valor_copiado:
        vai_e_clica(int(sair_post[0]), int(sair_post[1]))

        sleep_time = randint(500, 1000)

        hora_atual = datetime.datetime.now()
        hora_final = hora_atual + datetime.timedelta(minutes=sleep_time / 60)

        hora_atual = hora_atual.strftime("%H:%M")
        hora_final = hora_final.strftime("%H:%M")

        print(f'Nanarei {sleep_time}s. Logo, acordarei {hora_final}.')
        sleep(sleep_time)

        vai_e_clica(int(refresh[0]), int(refresh[1]))
        sleep(randint(5, 10))
