# TaskTracker

Projeto acadêmico desenvolvido para a Fase 2 do Bootcamp II,
do curso de Análise e Desenvolvimento de Sistemas.

## Objetivo

Organizar tarefas por meio de uma aplicação de terminal em Python,
permitindo acompanhar prioridades, responsáveis, prazos e status.

## Funcionalidades implementadas

- Cadastro de tarefas com título, descrição, prioridade, categoria,
  responsável e prazo.
- Registro automático da data de criação.
- Status inicial definido como Pendente.
- Validação de título obrigatório e prioridade.
- Validação de data e horário, aceitando somente prazos futuros
  no cadastro e na alteração do prazo.
- Listagem de tarefas e identificação de tarefas atrasadas.
- Contagem de tarefas pendentes, em andamento, concluídas e atrasadas.
- Alteração de status entre Pendente, Em andamento e Concluída.
- Edição de título, descrição, prioridade, categoria e prazo.
- Exclusão de tarefas com confirmação.
- Ordenação por prioridade, com Alta ou Baixa primeiro.
- Consulta de tarefas por status.
- Consulta de todas as tarefas em ordem de prazo.

## Tecnologias utilizadas

- Python 3 e biblioteca padrão `datetime`.
- Git para controle de versões.
- GitHub para hospedagem do repositório.
- Visual Studio Code como editor de código.

## Estrutura do projeto

- `src/main.py`: código principal da aplicação.
- `docs/planejamento_logico.pdf`: planejamento da Fase 1.
- `.gitignore`: regras para ignorar arquivos temporários.
- `README.md`: apresentação e instruções do projeto.

## Pré-requisitos

- Python 3 instalado.
- Terminal para executar os comandos.

Não é necessário instalar bibliotecas externas.

O projeto foi desenvolvido no Windows com Python 3.15.0.

## Como executar

1. Baixe ou clone este repositório.
2. Abra o terminal na pasta principal `TaskTracker`.
3. Execute:

```powershell
py src/main.py
```

Em ambientes que utilizam o comando `python3`, execute:

```bash
python3 src/main.py
```

## Como utilizar

Ao iniciar, o programa apresenta um menu. Digite o número da
opção desejada e siga as instruções exibidas no terminal.

Para informar um prazo, utilize o formato:

```text
DD/MM/AAAA HH:MM
```

Exemplo de preenchimento:

```text
20/12/2026 18:30
```

O prazo informado deve estar no futuro em relação ao relógio
do computador.

## Regras de funcionamento

- O título não pode estar vazio nem conter somente espaços.
- A prioridade deve ser Alta, Média ou Baixa.
- Toda tarefa cadastrada começa com status Pendente.
- Os status permitidos são Pendente, Em andamento e Concluída.
- Uma tarefa não concluída é identificada como atrasada quando
  ultrapassa o prazo.
- A exclusão depende de confirmação do usuário.
- Tarefas atrasadas também pertencem a um dos status.
  Portanto, sua quantidade não deve ser somada aos status
  para calcular o total de tarefas.

## Limitações e diferenças em relação ao planejamento

- Os dados ficam somente na memória e são perdidos ao encerrar
  o programa.
- Uma tarefa de exemplo é carregada a cada execução.
- Não há cadastro de usuários ou integrantes de equipe.
  O responsável é informado como texto.
- Não foram implementados filtros por responsável e prioridade.
  A ordenação por prioridade está disponível.
- A consulta exclusiva de tarefas do dia foi substituída pela
  consulta de todas as tarefas em ordem de prazo.
- Não há aviso específico de tarefas próximas do prazo.
- Não há uma opção exclusiva de consulta de detalhes individuais.
- A edição do responsável não está incluída nesta versão.

## Controle de versões

O desenvolvimento foi registrado com commits durante a
implementação das funcionalidades.

Para consultar o histórico local:

```bash
git log --oneline
```

## Autor

Rafael Thiago Felix dos Santos  
Curso: Análise e Desenvolvimento de Sistemas
