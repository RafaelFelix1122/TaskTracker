lista_tarefas = []

print("Bem-vindo ao TaskTracker!")

while True:
    print()
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
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
        tarefa = {
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade,
            "Status": "Pendente"
        }
        lista_tarefas.append(tarefa)
        print(f"Tarefa '{titulo}' criada com sucesso!")

    elif opcao == "2":
        if not lista_tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("Lista de tarefas:")
            for i, tarefa in enumerate(lista_tarefas, start=1):
                print(f"{i}. Título: {tarefa['titulo']} - Descrição: {tarefa['descricao']} - Prioridade: {tarefa['prioridade'].capitalize()} - Status: {tarefa['Status']}")
            print("Digite o número da tarefa para marcar como concluída ou '0' para voltar ao menu.")
            while True:
                escolha = input("Número da tarefa para concluir (0 para voltar): ").strip()

                if escolha == "0":
                    break

                elif escolha.isdigit() and 1 <= int(escolha) <= len(lista_tarefas):
                    index = int(escolha) - 1
                    lista_tarefas[index]["Status"] = "Concluída"
                    print(
                        f"Tarefa '{lista_tarefas[index]['titulo']}' "
                        "marcada como concluída."
                    )
                    break

                else:
                    print("Escolha inválida. Digite um número da lista ou 0.")

    elif opcao == "0":
        print("Encerrando o TaskTracker.")
        break

    else:
        print("Opção inválida. Tente novamente.")