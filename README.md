# TechFlow Tasks — Gerenciador Ágil de Tarefas

**Objetivo:** criar um sistema simples de tarefas para uma startup de logística, com fluxo de trabalho visível em tempo real e priorização.  
**Metodologia:** Kanban simples no GitHub Projects (A Fazer, Em Progresso, Concluído).  
**Escopo inicial:** CRUD de tarefas (título, descrição, status).

## Como rodar localmente
1. Instale Python 3.11+
2. `pip install -r requirements.txt`
3. `python src/app.py`
4. Acesse http://127.0.0.1:5000

## Testes
- Rodar: `pytest`

## Mudança de escopo (simulação)
Adicionamos **prioridade da tarefa (baixa/média/alta)**. Ajustamos o Kanban e registramos commits explicando a mudança.

## Links úteis
- Kanban: GitHub → Projects do repositório
- Ações: GitHub → Actions (CI executa testes a cada push)
