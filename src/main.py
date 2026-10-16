from datetime import datetime

lista_tarefas = [
    {
        "responsavel": "Rafael",
        "titulo": "Estudar Python",
        "descricao": "Revisar listas, dicionários e repetições.",
        "prioridade": "média",
        "Status": "Pendente",
        "prazo": datetime(2026, 12, 20, 18, 30),
        "categoria": "Estudo"
    }
]

print("Bem-vindo ao TaskTracker!")

while True:
    print()
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

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
            "Categoria (ex.: Trabalho, Estudo, Reunião; Enter para deixar sem categoria): "
        ).strip()

        while True:
            prazo_texto = input(
                "Digite o prazo da tarefa (formato DD/MM/AAAA): ").strip()
            
            try: 
                prazo = datetime.strptime(prazo_texto, "%d/%m/%Y %H:%M")
                if prazo <= datetime.now():
                    print("O prazo deve ser uma data futura. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Formato de data inválido. Use DD/MM/AAAA HH:MM.")

        tarefa = {
            "responsavel": responsavel,
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade,
            "categoria": categoria,
            "Status": "Pendente",
            "prazo": prazo
        }
        lista_tarefas.append(tarefa)
        print(f"Tarefa '{titulo}' criada com sucesso!")

    elif opcao == "2":
        if not lista_tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("Lista de tarefas:")

            for i, tarefa in enumerate(lista_tarefas, start=1):
                if tarefa["prazo"] < datetime.now() and tarefa["Status"] != "Concluída":
                    situacao_prazo = "Atrasada"
                else:
                    situacao_prazo = "Sem atraso"

                print(
                    f"{i}. Responsável: {tarefa['responsavel'] or 'Não atribuído'}"
                    f" Título: {tarefa['titulo']} "
                    f"- Descrição: {tarefa['descricao']} "
                    f"- Prioridade: {tarefa['prioridade'].capitalize()} "
                    f"- Categoria: {tarefa['categoria'] or 'Sem categoria'}"
                    f"- Prazo: {tarefa['prazo'].strftime('%d/%m/%Y %H:%M')} "
                    f"- Situação do prazo: {situacao_prazo} "
                    f"- Status: {tarefa['Status']} "
                )
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