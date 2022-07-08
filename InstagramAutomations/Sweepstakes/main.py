import datetime

from Data.users import *
from Functions import *

# Coordenadas do sorteio
coordenadas = [line.strip('\n').split() for line in open('Data/coordenadas', 'r').read().splitlines()]
navegador = coordenadas[0]
post = coordenadas[1]
copia_inicial = coordenadas[2]
copia_final = coordenadas[3]
campo_input = coordenadas[4]
button = coordenadas[5]
bloqueio = coordenadas[6]
sair_post = coordenadas[7]
refresh = coordenadas[8]

# Dicionário de parâmetros
p_sorteio = {
    'Quantidade de participantes': 2,
    'Contador': pegar_contagem('Data/contagem'),
    'Contagem final': 200,
}

# Clica no navegador
vai_e_clica(randomiza(int(navegador[0]), int(navegador[1])))

while p_sorteio['Contador'] <= p_sorteio['Contagem final']:
    # CLica na publicação
    vai_e_clica(randomiza(int(post[0]), int(post[1])))

    sleep(1)

    # Copia algo aleatório
    pg.moveTo(
        int(copia_inicial[0]) + (randint(-100, 100) / 1000),
        int(copia_inicial[1]) + (randint(-100, 100) / 1000),
        randint(50, 100) / 100
    )
    pg.mouseDown(button='left')
    pg.moveTo(
        int(campo_input[0]) + (randint(-100, 100) / 1000),
        int(copia_final[1]) + (randint(-100, 100) / 1000),
        randint(50, 100) / 100
    )
    pg.mouseUp(button='left')
    pg.hotkey('ctrl', 'c')

    # Clica no campo de escrita
    vai_e_clica(randomiza(int(campo_input[0]), int(campo_input[1])))

    # Faz os comentários
    for i in range(
            p_sorteio['Contador'],
            p_sorteio['Contador'] + p_sorteio['Quantidade de participantes']
    ):
        pg.write(f'@{lista_users[i]} ', interval=randint(10, 25) / 100)
        print(f'{lista_users[i]} || {i}')

    # Comenta
    vai_e_clica(randomiza(int(button[0]), int(button[1])))

    # Atualiza os arquivos de texto e parâmetros da função
    atualizar_contagem(
        'Data/contagem',
        pegar_contagem('Data/contagem'),
        p_sorteio['Quantidade de participantes']
    )
    p_sorteio['Contador'] = pegar_contagem('Data/contagem')

    print('')
    sleep(2.5)

    # Checa bloqueio
    valor_copiado = verifica_bloqueio(randomiza(int(bloqueio[0]), int(bloqueio[1])))
    print(f'Valor copiado: {valor_copiado}\n')
    if 'comentário.' in valor_copiado:
        vai_e_clica(randomiza(int(sair_post[0]), int(sair_post[1])))

        sleep_time = randint(500, 1000)

        hora_atual = datetime.datetime.now()
        hora_final = hora_atual + datetime.timedelta(minutes=sleep_time / 60)

        hora_atual = hora_atual.strftime("%H:%M")
        hora_final = hora_final.strftime("%H:%M")

        print(f'Nanarei {sleep_time}s. Logo, acordarei {hora_final}.')
        sleep(sleep_time)

        vai_e_clica(randomiza(int(refresh[0]), int(refresh[1])))
        sleep(randint(5, 10))
