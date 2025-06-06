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

while True:
    print("\n=== Sistema de Campeões Lendários ===")
    print("1. Registrar novo Campeão")
    print("2. Listar Campeões")
    print("3. Adicionar Campeão à arena de batalhas")
    print("4. Iniciar batalha na arena")
    print("5. Sair")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome_heroi = input("Digite o nome do Campeão: ").strip()

        print("Classes disponíveis:")
        for classe_nome, poderes in classes_e_poderes.items():
            print(f"- {classe_nome}: poderes -> {poderes[0]}, {poderes[1]}, {poderes[2]}")

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

        nivel = min(nivel_heroi, 100)
        bonus_vida = (nivel // 10) * 50
        vida_inicial = 100 + bonus_vida

        poderes_heroi = classes_e_poderes[classe_heroi]
        ult = ultimates.get(classe_heroi, "Poder Supremo")

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
        print(f"Poderes concedidos: {poderes_heroi[0]}, {poderes_heroi[1]} e {poderes_heroi[2]}")
        print(f"Ultimate especial: {ult}")
        print(f"Vida inicial baseada no nível: {vida_inicial}\n")

        proximo_codigo_campeao += 1

    elif opcao == "2":
        if not campeoes_lendarios:
            print("Nenhum Campeão registrado até agora.")
        else:
            print("\nLista de Campeões Registrados:")
            for codigo, dados in campeoes_lendarios.items():
                poderes_str = ", ".join(dados["poderes"])
                print(f"Código: {codigo} | Nome: {dados['nome']} | Classe: {dados['classe']} | "
                      f"Nível: {dados['nivel']} | Vida: {dados['vida']} | Poderes: {poderes_str}")

    elif opcao == "3":
        if not campeoes_lendarios:
            print("Nenhum Campeão cadastrado para adicionar.")
        else:
            print("\nCampeões disponíveis:")
            for codigo, dados in campeoes_lendarios.items():
                print(f"Código {codigo}: {dados['nome']} ({dados['classe']})")
            try:
                codigo = int(input("Digite o código do Campeão para adicionar à arena: "))
                if codigo in campeoes_lendarios:
                    arena_de_batalhas.append(campeoes_lendarios[codigo])
                    print(f"{campeoes_lendarios[codigo]['nome']} foi adicionado à arena!")
                else:
                    print("Código de Campeão inválido.")
            except ValueError:
                print("Digite um número válido.")

    elif opcao == "4":
        if len(arena_de_batalhas) < 2:
            print("É necessário pelo menos 2 campeões na arena para iniciar a batalha.")
        else:
            heroi1 = arena_de_batalhas.popleft()
            heroi2 = arena_de_batalhas.popleft()

            vida1 = heroi1['vida']
            vida2 = heroi2['vida']
            heroi1['barra_ult'] = 0
            heroi2['barra_ult'] = 0

            turno = 1
            while vida1 >= 0 and vida2 >= 0:
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
                    print(f"\nPoderes de {heroi1['nome']} ({heroi1['classe']}):")
                    for i, poder in enumerate(heroi1['poderes'], 1):
                        print(f"{i}. {poder}")
                    while True:
                        escolha = input("Escolha o poder para usar (1, 2 ou 3): ").strip()
                        if escolha in ['1', '2', '3']:
                            poder_heroi1 = heroi1['poderes'][int(escolha) - 1]
                            break
                        else:
                            print("Escolha inválida. Tente 1, 2 ou 3.")

                while True:
                    acao_heroi2 = input(f"{heroi2['nome']}, escolha sua ação (atacar / defender): ").strip().lower()
                    if acao_heroi2 in ['atacar', 'defender']:
                        break
                    else:
                        print("Ação inválida. Digite 'atacar' ou 'defender'.")

                poder_heroi2 = None
                if acao_heroi2 == 'atacar':
                    print(f"\nPoderes de {heroi2['nome']} ({heroi2['classe']}):")
                    for i, poder in enumerate(heroi2['poderes'], 1):
                        print(f"{i}. {poder}")
                    while True:
                        escolha = input("Escolha o poder para usar (1, 2 ou 3): ").strip()
                        if escolha in ['1', '2', '3']:
                            poder_heroi2 = heroi2['poderes'][int(escolha) - 1]
                            break
                        else:
                            print("Escolha inválida. Tente 1, 2 ou 3.")

                bonus_por_poder = {
                    "Spartan Rage": 10, "Gorgon Gaze": 10, "Oath of Olympus": 10,
                    "Darkflare": 10, "Icebreaker": 10, "Abyssal Chains": 10,
                    "Blightpiercer": 10, "Skybreaker": 10, "Eagle’s Mark": 10,
                    "Tsukikage no Ken": 10, "Oni no Tsuki": 10, "Mangetsu Hōkai": 10,
                    "Arise": 10, "Soul Reaver": 10, "Spiritual Collapse": 10,
                    "Eviscerar": 10, "A Noite Cai": 10, "Julgamento de um Corte": 10,
                    "Raging Uppercut": 10, "Counter Strike": 10, "Send The Jab": 10
                }

                def calcular_forca_ataque(nivel, poder):
                    base = nivel * 5
                    bonus = bonus_por_poder.get(poder, 0)
                    return base + bonus

                if acao_heroi1 == 'atacar':
                    dano_heroi1 = calcular_forca_ataque(heroi1['nivel'], poder_heroi1)
                else:
                    dano_heroi1 = 0

                if acao_heroi2 == 'atacar':
                    dano_heroi2 = calcular_forca_ataque(heroi2['nivel'], poder_heroi2)
                else:
                    dano_heroi2 = 0

                if acao_heroi1 == 'defender':
                    dano_heroi2 = dano_heroi2 // 2
                if acao_heroi2 == 'defender':
                    dano_heroi1 = dano_heroi1 // 2

                vida1 -= dano_heroi2
                vida2 -= dano_heroi1

                print(f"\n{heroi1['nome']} causou {dano_heroi1} de dano em {heroi2['nome']}.")
                print(f"\n{heroi2['nome']} causou {dano_heroi2} de dano em {heroi1['nome']}.")

                print(f"Vida restante - {heroi1['nome']}: {max(vida1, 0)} | {heroi2['nome']}: {max(vida2, 0)}")

                turno += 1

            if vida1 <= 0 and vida2 <= 0:
                print("\nEmpate! Ambos os campeões caíram na arena.")
            elif vida1 <= 0:
                print(f"\n{heroi2['nome']} venceu a batalha!")
            else:
                print(f"\n{heroi1['nome']} venceu a batalha!")

    elif opcao == "5":
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Opção inválida, tente novamente.")
