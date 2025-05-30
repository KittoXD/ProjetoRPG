import random
from collections import deque

classes_e_poderes = {
    "Guerreiro": ["Spartan Rage", "Gorgon Gaze", "Oath of Olympus"],
    "Feiticeiro": ["Darkflare", "Icebreaker", "Abyssal Chains"],
    "Arqueiro": ["Blightpiercer", "Skybreaker", "Eagle’s Mark"],
    "Espadachim": ["Tsukikage no Ken", "Oni no Tsuki", "Mangetsu Hōkai"],
    "Necromante": ["Arise", "Soul Reaver", "Spiritual Collapse"],
    "Assassino": ["Eviscerar", "A Noite Cai", "Julgamento de um Corte"],
    "Lutador": ["Raging Uppercut", "Counter Strike", "Send The Jab"]
}

ultimates = {
    "Guerreiro": "This is Sparta",
    "Feiticeiro": "Arcane Cataclysm",
    "Arqueiro": "Eclipse Shot",
    "Espadachim": "Tsuki no Kokyū: Yoi no Miya",
    "Necromante": "Eternal Requiem",
    "Assassino": "Funeral em Quatro Partes",
    "Lutador": "One Punch"
}   

campeoes_lendarios = {}
proximo_codigo_campeao = 1

arena_de_batalhas = deque()

legiões = {}
proximo_codigo_legiao = 1

def calcular_vida_inicial(nivel):
    nivel = min(nivel, 100)
    bonus_vida = (nivel // 10) * 50
    return 100 + bonus_vida

def mostrar_classes_disponiveis():
    print("Classes disponíveis:")
    for classe_nome, poderes in classes_e_poderes.items():
        print(f"- {classe_nome}: poderes -> {poderes[0]}, {poderes[1]}")

def registrar_campeao():
    global proximo_codigo_campeao
    nome_heroi = input("Digite o nome do Campeão: ").strip()

    mostrar_classes_disponiveis()
    while True:
        classe_heroi = input("Escolha a classe do Campeão: ").strip()
        if classe_heroi in classes_e_poderes:
            break
        else:
            print("Classe inválida, tente novamente.")

    while True:
        try:
            nivel_heroi = int(input("Informe o nível do Campeão (1 a 100): "))
            if 1 <= nivel_heroi <= 100:
                break
            else:
                print("O nível deve estar entre 1 e 100.")
        except ValueError:
            print("Digite um número válido para o nível.")

    poderes_heroi = classes_e_poderes[classe_heroi]
    ult = ultimates.get(classe_heroi, "Poder Supremo")
    vida_inicial = calcular_vida_inicial(nivel_heroi)

    campeao = {
        "nome": nome_heroi,
        "classe": classe_heroi,
        "nivel": nivel_heroi,
        "poderes": poderes_heroi,
        "vida": vida_inicial,
        "barra_ult": 0,
        "ult": ult
    }

    campeoes_lendarios[proximo_codigo_campeao] = campeao
    print(f"\nCampeão '{nome_heroi}' da classe {classe_heroi} registrado com código {proximo_codigo_campeao}.")
    print(f"Poderes concedidos: {poderes_heroi[0]} e {poderes_heroi[1]}")
    print(f"Ultimate especial: {ult}")
    print(f"Vida inicial baseada no nível: {vida_inicial}\n")

    proximo_codigo_campeao += 1

def usar_ult(heroi):
    if heroi['barra_ult'] >= 100:
        print(f"{heroi['nome']} está tentando usar a Ultimate: {heroi['ult']}!")
        if random.random() <= 0.65:
            dano = heroi['nivel'] + 10 + random.randint(10, 20)
            print(f"Ultimate {heroi['ult']} acertou e causou {dano} de dano!")
        else:
            dano = 0
            print(f"{heroi['nome']} falhou ao tentar usar a Ultimate!")
        heroi['barra_ult'] = 0
        return dano
    else:
        print(f"Ultimate de {heroi['nome']} ainda não está carregada. ({heroi['barra_ult']}%)")
        return 0

def listar_campeoes():
    if not campeoes_lendarios:
        print("Nenhum Campeão registrado até agora.")
        return
    print("\nLista de Campeões Registrados:")
    for codigo, dados in campeoes_lendarios.items():
        poderes_str = ", ".join(dados["poderes"])
        print(f"Código: {codigo} | Nome: {dados['nome']} | Classe: {dados['classe']} | "
              f"Nível: {dados['nivel']} | Vida: {dados['vida']} | Poderes: {poderes_str}")

def escolher_poder(heroi):
    poderes = heroi['poderes']
    print(f"\nPoderes de {heroi['nome']} ({heroi['classe']}):")
    for i, poder in enumerate(poderes, 1):
        print(f"{i}. {poder}")
    while True:
        escolha = input("Escolha o poder para usar (1 ou 2): ").strip()
        if escolha in ['1', '2']:
            return poderes[int(escolha) - 1]
        else:
            print("Escolha inválida. Tente novamente.")

def calcular_forca_ataque(nivel, poder):
    bonus_por_poder = {
        "Spartan Rage": 10,
        "Gorgon Gaze": 10,
        "Oath of Olympus": 10,
        "Darkflare": 10,
        "Icebreaker": 10,
        "Abyssal Chains": 10,
        "Blightpiercer": 10,
        "Skybreaker": 10,
        "Eagle’s Mark": 10,
        "Tsukikage no Ken": 10,
        "Oni no Tsuki": 10,
        "Mangetsu Hōkai": 10,
        "Arise": 10,
        "Soul Reaver": 10,
        "Spiritual Collapse": 10,
        "Eviscerar": 10,
        "A Noite Cai": 10,
        "Julgamento de um corte": 10,
        "Raging Uppercut": 10,
        "Counter Strike": 10,
        "Send The Jab": 10
    }
    bonus = bonus_por_poder.get(poder, 4)
    dano = nivel + bonus + random.randint(1, 6)
    return dano

def batalha(heroi1, heroi2):
    print(f"\nBatalha: {heroi1['nome']} (Nível {heroi1['nivel']}) vs {heroi2['nome']} (Nível {heroi2['nivel']})")
    vida1 = heroi1['vida']
    vida2 = heroi2['vida']

    heroi1['barra_ult'] = 0
    heroi2['barra_ult'] = 0

    turno = 1
    while vida1 > 0 and vida2 > 0:
        print(f"\nTurno {turno}:")

        heroi1['barra_ult'] = min(100, heroi1['barra_ult'] + 10)
        heroi2['barra_ult'] = min(100, heroi2['barra_ult'] + 10)

        print(f"Ultimate [{heroi1['barra_ult']}%] {heroi1['nome']}")
        print(f"Ultimate [{heroi2['barra_ult']}%] {heroi2['nome']}")

        while True:
            acao_heroi1 = input(f"{heroi1['nome']}, escolha sua ação (atacar / defender): ").strip().lower()
            if acao_heroi1 in ['atacar', 'defender']:
                break
            else:
                print("Ação inválida. Digite 'atacar' ou 'defender'.")

        poder_heroi1 = None
        if acao_heroi1 == 'atacar':
            poder_heroi1 = escolher_poder(heroi1)

        while True:
            acao_heroi2 = input(f"{heroi2['nome']}, escolha sua ação (atacar / defender): ").strip().lower()
            if acao_heroi2 in ['atacar', 'defender']:
                break
            else:
                print("Ação inválida. Digite 'atacar' ou 'defender'.")

        poder_heroi2 = None
        if acao_heroi2 == 'atacar':
            poder_heroi2 = escolher_poder(heroi2)

        dano_heroi1 = 0
        dano_heroi2 = 0

        if acao_heroi1 == 'atacar':
            dano_heroi1 = calcular_forca_ataque(heroi1['nivel'], poder_heroi1)
        if acao_heroi2 == 'atacar':
            dano_heroi2 = calcular_forca_ataque(heroi2['nivel'], poder_heroi2)

        def calcular_dano_final(dano_base, defesa_oponente, defendendo):
            if defendendo:
                defesa_oponente += 3  # bônus de defesa ao defender
            dano_final = dano_base - defesa_oponente
            return max(dano_final, 0)

        # Para simplicidade, consideramos a defesa igual ao nível dividido por 2, ajustável
        defesa_heroi1 = heroi1['nivel'] // 2
        defesa_heroi2 = heroi2['nivel'] // 2

        if acao_heroi2 == 'defender':
            dano_heroi1 = calcular_dano_final(dano_heroi1, defesa_heroi2, True)
        if acao_heroi1 == 'defender':
            dano_heroi2 = calcular_dano_final(dano_heroi2, defesa_heroi1, True)

        # Ajuste de vida
        vida2 -= dano_heroi1
        vida1 -= dano_heroi2

        print(f"{heroi1['nome']} causou {dano_heroi1} de dano em {heroi2['nome']}. Vida de {heroi2['nome']}: {max(vida2, 0)}")
        print(f"{heroi2['nome']} causou {dano_heroi2} de dano em {heroi1['nome']}. Vida de {heroi1['nome']}: {max(vida1, 0)}")

        # Verificar se algum herói pode usar ultimate (barra cheia)
        if heroi1['barra_ult'] >= 100:
            dano_ult_1 = usar_ult(heroi1)
            vida2 -= dano_ult_1
            if dano_ult_1 > 0:
                print(f"{heroi2['nome']} recebeu {dano_ult_1} de dano da ultimate de {heroi1['nome']}. Vida restante: {max(vida2, 0)}")

        if heroi2['barra_ult'] >= 100:
            dano_ult_2 = usar_ult(heroi2)
            vida1 -= dano_ult_2
            if dano_ult_2 > 0:
                print(f"{heroi1['nome']} recebeu {dano_ult_2} de dano da ultimate de {heroi2['nome']}. Vida restante: {max(vida1, 0)}")

        turno += 1

    if vida1 <= 0 and vida2 <= 0:
        print("Empate!")
        return None
    elif vida1 > 0:
        print(f"\n{heroi1['nome']} venceu a batalha!")
        return heroi1
    else:
        print(f"\n{heroi2['nome']} venceu a batalha!")
        return heroi2

def criar_legiao():
    global proximo_codigo_legiao
    nome_legiao = input("Digite o nome da Legião: ").strip()
    legiao = {
        "nome": nome_legiao,
        "campeoes": []
    }
    legiões[proximo_codigo_legiao] = legiao
    print(f"Legião '{nome_legiao}' criada com código {proximo_codigo_legiao}.")
    proximo_codigo_legiao += 1

def adicionar_campeao_a_legiao():
    if not campeoes_lendarios:
        print("Nenhum Campeão disponível para adicionar.")
        return
    if not legiões:
        print("Nenhuma Legião criada ainda.")
        return

    listar_campeoes()
    while True:
        try:
            codigo_campeao = int(input("Digite o código do Campeão para adicionar à Legião: "))
            if codigo_campeao in campeoes_lendarios:
                break
            else:
                print("Código inválido.")
        except ValueError:
            print("Digite um número válido.")

    print("\nLegiões disponíveis:")
    for codigo, legiao in legiões.items():
        print(f"Código: {codigo} | Nome: {legiao['nome']} | Número de campeões: {len(legiao['campeoes'])}")

    while True:
        try:
            codigo_legiao = int(input("Digite o código da Legião para adicionar o Campeão: "))
            if codigo_legiao in legiões:
                break
            else:
                print("Código inválido.")
        except ValueError:
            print("Digite um número válido.")

    legiões[codigo_legiao]['campeoes'].append(campeoes_lendarios[codigo_campeao])
    print(f"Campeão '{campeoes_lendarios[codigo_campeao]['nome']}' adicionado à Legião '{legiões[codigo_legiao]['nome']}'.")

def listar_legioes():
    if not legiões:
        print("Nenhuma Legião criada.")
        return
    print("\nLegiões criadas:")
    for codigo, legiao in legiões.items():
        print(f"Código: {codigo} | Nome: {legiao['nome']} | Campeões: {len(legiao['campeoes'])}")
        for c in legiao['campeoes']:
            print(f"  - {c['nome']} ({c['classe']}, Nível {c['nivel']})")

def batalha_de_legioes():
    if len(legiões) < 2:
        print("Precisamos de pelo menos duas Legiões para batalhar.")
        return

    listar_legioes()

    while True:
        try:
            codigo_legiao1 = int(input("Escolha o código da primeira Legião: "))
            if codigo_legiao1 in legiões and legiões[codigo_legiao1]['campeoes']:
                break
            else:
                print("Legião inválida ou sem campeões.")
        except ValueError:
            print("Digite um número válido.")

    while True:
        try:
            codigo_legiao2 = int(input("Escolha o código da segunda Legião: "))
            if codigo_legiao2 in legiões and legiões[codigo_legiao2]['campeoes'] and codigo_legiao2 != codigo_legiao1:
                break
            else:
                print("Legião inválida, sem campeões ou igual à primeira.")
        except ValueError:
            print("Digite um número válido.")

    legiao1 = legiões[codigo_legiao1]
    legiao2 = legiões[codigo_legiao2]

    print(f"\nBatalha entre Legiões: {legiao1['nome']} vs {legiao2['nome']}")
    pontuacao_legiao1 = 0
    pontuacao_legiao2 = 0

    # Para simplificar, vamos batalhar todos os campeões na ordem
    for c1, c2 in zip(legiao1['campeoes'], legiao2['campeoes']):
        vencedor = batalha(c1.copy(), c2.copy())  # copia para não alterar os originais
        if vencedor is None:
            print("Empate nessa batalha.")
        elif vencedor['nome'] == c1['nome']:
            pontuacao_legiao1 += 1
        else:
            pontuacao_legiao2 += 1

    print(f"\nResultado da batalha das Legiões:")
    print(f"{legiao1['nome']} venceu {pontuacao_legiao1} batalhas.")
    print(f"{legiao2['nome']} venceu {pontuacao_legiao2} batalhas.")

    if pontuacao_legiao1 > pontuacao_legiao2:
        print(f"Legião vencedora: {legiao1['nome']}!")
    elif pontuacao_legiao2 > pontuacao_legiao1:
        print(f"Legião vencedora: {legiao2['nome']}!")
    else:
        print("A batalha das Legiões terminou empatada!")

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Registrar Campeão")
        print("2. Listar Campeões")
        print("3. Criar Legião")
        print("4. Adicionar Campeão a Legião")
        print("5. Listar Legiões")
        print("6. Batalha entre Campeões")
        print("7. Batalha entre Legiões")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            registrar_campeao()
        elif opcao == '2':
            listar_campeoes()
        elif opcao == '3':
            criar_legiao()
        elif opcao == '4':
            adicionar_campeao_a_legiao()
        elif opcao == '5':
            listar_legioes()
        elif opcao == '6':
            if len(campeoes_lendarios) < 2:
                print("É necessário ter pelo menos 2 Campeões registrados para batalhar.")
                continue
            listar_campeoes()
            try:
                c1 = int(input("Escolha o código do primeiro Campeão: "))
                c2 = int(input("Escolha o código do segundo Campeão: "))
                if c1 in campeoes_lendarios and c2 in campeoes_lendarios and c1 != c2:
                    batalha(campeoes_lendarios[c1].copy(), campeoes_lendarios[c2].copy())
                else:
                    print("Códigos inválidos ou iguais.")
            except ValueError:
                print("Digite números válidos.")
        elif opcao == '7':
            batalha_de_legioes()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()