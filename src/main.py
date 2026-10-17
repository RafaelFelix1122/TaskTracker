from datetime import datetime

ordem_prioridade = {"alta": 1, "média": 2, "baixa": 3}

lista_tarefas = [
    {
        "responsavel": "Rafael",
        "titulo": "Estudar Python",
        "descricao": "Revisar listas, dicionários e repetições.",
        "prioridade": "média",
        "Status": "Pendente",
        "prazo": datetime(2026, 12, 20, 18, 30),
        "categoria": "Estudo",
        "data_criacao": datetime(2026, 10, 16, 0, 0),
    }
]

print("Bem-vindo ao TaskTracker!")

while True:
    print()
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Editar tarefa")
    print("4 - Excluir tarefa")
    print("5 - Listar status da tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        responsavel = input(
            "Responsável (Enter para deixar sem responsável): "
        ).strip()

        while True:
            titulo = input("Digite o título da tarefa: ").strip()

            if titulo:
                break

            print("Título da tarefa não pode ser vazio.")

        descricao = input("Digite a descrição da tarefa: ")

        while True:
            prioridade = input(
                "Digite a prioridade da tarefa (Alta, Média, Baixa): "
            ).strip().lower()

            if prioridade in ["alta", "média", "baixa"]:
                break

            print("Prioridade inválida. Escolha Alta, Média ou Baixa.")

        categoria = input(
            "Categoria (ex.: Trabalho, Estudo, Reunião; "
            "Enter para deixar sem categoria): "
        ).strip()

        while True:
            prazo_texto = input(
                "Digite o prazo da tarefa (DD/MM/AAAA HH:MM): "
            ).strip()

            try:
                prazo = datetime.strptime(
                    prazo_texto, "%d/%m/%Y %H:%M"
                )

                if prazo <= datetime.now():
                    print("O prazo deve ser uma data e horário futuros.")
                    continue

                break

            except ValueError:
                print("Data ou horário inválido. Use DD/MM/AAAA HH:MM.")

        tarefa = {
            "responsavel": responsavel,
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade,
            "categoria": categoria,
            "Status": "Pendente",
            "prazo": prazo,
            "data_criacao": datetime.now(),
        }

        lista_tarefas.append(tarefa)
        print(f"Tarefa '{titulo}' criada com sucesso!")

    elif opcao == "2":
        pendentes = 0
        em_andamento = 0
        concluidas = 0
        atrasadas = 0

        for tarefa in lista_tarefas:
            if tarefa["Status"] == "Pendente":
                pendentes += 1
            elif tarefa["Status"] == "Em andamento":
                em_andamento += 1
            elif tarefa["Status"] == "Concluída":
                concluidas += 1

        if not lista_tarefas:
            print("Nenhuma tarefa cadastrada.")

        else:
            while True:
                print("Como deseja ordenar as tarefas?")
                print("1 - Alta prioridade primeiro")
                print("2 - Baixa prioridade primeiro")

                escolha_ordem = input("Escolha uma opção: ").strip()

                if escolha_ordem in ["1", "2"]:
                    break

                print("Opção inválida. Escolha 1 ou 2.")

            lista_tarefas.sort(
                key=lambda tarefa: ordem_prioridade[tarefa["prioridade"]],
                reverse=(escolha_ordem == "2")
            )

            print("Lista de tarefas:")

            for i, tarefa in enumerate(lista_tarefas, start=1):
                if (
                    tarefa["prazo"] < datetime.now()
                    and tarefa["Status"] != "Concluída"
                ):
                    situacao_prazo = "Atrasada"
                    atrasadas += 1
                else:
                    situacao_prazo = "Sem atraso"

                print(
                    f"{i}. Responsável: "
                    f"{tarefa['responsavel'] or 'Não atribuído'} "
                    f"- Título: {tarefa['titulo']} "
                    f"- Descrição: {tarefa['descricao']} "
                    f"- Prioridade: {tarefa['prioridade'].capitalize()} "
                    f"- Categoria: {tarefa['categoria'] or 'Sem categoria'} "
                    f"- Prazo: "
                    f"{tarefa['prazo'].strftime('%d/%m/%Y %H:%M')} "
                    f"- Situação do prazo: {situacao_prazo} "
                    f"- Status: {tarefa['Status']} "
                    f"- Criada em: "
                    f"{tarefa['data_criacao'].strftime('%d/%m/%Y %H:%M')}"
                )

            print("Resumo:")
            print(f"  - Pendentes: {pendentes}")
            print(f"  - Em andamento: {em_andamento}")
            print(f"  - Concluídas: {concluidas}")
            print(f"  - Atrasadas: {atrasadas}")

            print(
                "Digite o número da tarefa para alterar o status "
                "ou 0 para voltar ao menu."
            )

            while True:
                escolha = input(
                    "Número da tarefa (0 para voltar): "
                ).strip()

                if escolha == "0":
                    break

                elif (
                    escolha.isdigit()
                    and 1 <= int(escolha) <= len(lista_tarefas)
                ):
                    index = int(escolha) - 1

                    while True:
                        print("1 - Pendente")
                        print("2 - Em andamento")
                        print("3 - Concluída")

                        novo_status = input(
                            "Escolha o novo status: "
                        ).strip()

                        if novo_status == "1":
                            lista_tarefas[index]["Status"] = "Pendente"

                        elif novo_status == "2":
                            lista_tarefas[index]["Status"] = "Em andamento"

                        elif novo_status == "3":
                            lista_tarefas[index]["Status"] = "Concluída"

                        else:
                            print("Status inválido. Escolha 1, 2 ou 3.")
                            continue

                        print("Status atualizado com sucesso.")
                        break

                    break

                else:
                    print(
                        "Escolha inválida. "
                        "Digite um número da lista ou 0."
                    )
        

    elif opcao == "3":
        if not lista_tarefas:
            print("Nenhuma tarefa cadastrada para editar.")

        else:
            while True:
                print("Diga qual tarefa deseja editar:")

                for i, tarefa in enumerate(lista_tarefas, start=1):
                    print(f"{i}. ({tarefa['titulo']})")

                escolha_tarefa = input(
                    "Número da tarefa (0 para voltar ao menu): "
                ).strip()

                if escolha_tarefa == "0":
                    break

                elif (
                    escolha_tarefa.isdigit()
                    and 1 <= int(escolha_tarefa) <= len(lista_tarefas)
                ):
                    index = int(escolha_tarefa) - 1

                    while True:
                        print(
                            f"\nEditando: {lista_tarefas[index]['titulo']}"
                        )
                        print("1 - Editar título")
                        print("2 - Editar descrição")
                        print("3 - Editar prioridade")
                        print("4 - Editar categoria")
                        print("5 - Editar prazo")
                        print("0 - Voltar à seleção de tarefas")

                        escolha_edicao = input(
                            "Escolha uma opção: "
                        ).strip()

                        if escolha_edicao == "0":
                            break

                        elif escolha_edicao == "1":
                            novo_titulo = input(
                                "Digite o novo título: "
                            ).strip()

                            if novo_titulo:
                                lista_tarefas[index]["titulo"] = novo_titulo
                                print("Título atualizado com sucesso.")
                            else:
                                print("Título não pode ser vazio.")

                        elif escolha_edicao == "2":
                            nova_descricao = input(
                                "Digite a nova descrição: "
                            ).strip()

                            lista_tarefas[index]["descricao"] = nova_descricao
                            print("Descrição atualizada com sucesso.")

                        elif escolha_edicao == "3":
                            while True:
                                nova_prioridade = input(
                                    "Digite a nova prioridade "
                                    "(Alta, Média, Baixa): "
                                ).strip().lower()

                                if nova_prioridade in [
                                    "alta", "média", "baixa"
                                ]:
                                    lista_tarefas[index]["prioridade"] = (
                                        nova_prioridade
                                    )
                                    print("Prioridade atualizada com sucesso.")
                                    break

                                else:
                                    print(
                                        "Prioridade inválida. "
                                        "Escolha Alta, Média ou Baixa."
                                    )

                        elif escolha_edicao == "4":
                            nova_categoria = input(
                                "Digite a nova categoria "
                                "(ou Enter para deixar sem categoria): "
                            ).strip()

                            lista_tarefas[index]["categoria"] = nova_categoria
                            print("Categoria atualizada com sucesso.")

                        elif escolha_edicao == "5":
                            while True:
                                novo_prazo_texto = input(
                                    "Digite o novo prazo "
                                    "(DD/MM/AAAA HH:MM): "
                                ).strip()

                                try:
                                    novo_prazo = datetime.strptime(
                                        novo_prazo_texto,
                                        "%d/%m/%Y %H:%M"
                                    )

                                    if novo_prazo <= datetime.now():
                                        print(
                                            "O prazo deve ser uma data "
                                            "e horário futuros."
                                        )
                                        continue

                                    lista_tarefas[index]["prazo"] = novo_prazo
                                    print("Prazo atualizado com sucesso.")
                                    break

                                except ValueError:
                                    print(
                                        "Data ou horário inválido. "
                                        "Use DD/MM/AAAA HH:MM."
                                    )

                        else:
                            print("Opção de edição inválida.")

                else:
                    print(
                        "Tarefa inválida. "
                        "Digite um número da lista ou 0."
                    )
                            
    elif opcao == "4":
        if not lista_tarefas:
            print("Nenhuma tarefa cadastrada para excluir.")

        else:
            while True:
                print("Diga qual tarefa deseja excluir (0 para voltar):")
                
                for i, tarefa in enumerate(lista_tarefas, start=1):
                    print(f"{i}. ({tarefa['titulo']})")
                escolha_exclusão = input("Digite o numero da tarefa que deseja excluir (0 para voltar): ").strip()

                if escolha_exclusão == "0":
                    break

                elif (
                    escolha_exclusão.isdigit()
                    and 1 <= int(escolha_exclusão) <= len(lista_tarefas)
                ):
                    index = int(escolha_exclusão) - 1
                    tarefa = lista_tarefas[index]
                    print(f"Tarefa a ser excluída: {tarefa['titulo']}")
                    confirmacao = input("Tem certeza? (s/n): ").strip().lower()
                    if confirmacao == "s":
                        del lista_tarefas[index]
                        print("Tarefa excluída com sucesso.")
                    else:
                        print("Exclusão cancelada.")
                
                else:
                    print("Número inválido. Escolha uma tarefa da lista.")


    elif opcao == "5":
        if not lista_tarefas:
            print("Nenhuma tarefa cadastrada.")

        else:
            while True:
                print("1 - Pendente")
                print("2 - Em andamento")
                print("3 - Concluída")
                print("0 - Voltar ao menu")

                escolha_status = input("Escolha o status: ").strip()

                if escolha_status == "0":
                    break

                elif escolha_status in ["1", "2", "3"]:
                    status_disponiveis = [
                        "Pendente",
                        "Em andamento",
                        "Concluída"
                    ]

                    status_filtro = status_disponiveis[
                        int(escolha_status) - 1
                    ]

                    quantidade = 0

                    for tarefa in lista_tarefas:
                        if tarefa["Status"] == status_filtro:
                            quantidade += 1

                            print(
                                f"- {tarefa['titulo']} "
                                f"| Prioridade: "
                                f"{tarefa['prioridade'].capitalize()} "
                                f"| Prazo: "
                                f"{tarefa['prazo'].strftime('%d/%m/%Y %H:%M')} "
                                f"| Responsável: "
                                f"{tarefa['responsavel'] or 'Não atribuído'} "
                                f"| Status: {tarefa['Status']}"
                            )

                    if quantidade == 0:
                        print("Nenhuma tarefa encontrada nesse status.")
                    else:
                        print(f"Total encontrado: {quantidade}")

                else:
                    print("Opção inválida. Escolha 1, 2, 3 ou 0.")

    elif opcao == "0":
        print("Encerrando o TaskTracker.")
        break

    else:
        print("Opção inválida. Tente novamente.")