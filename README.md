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

## Mudança de escopo (feature adicional)
Originalmente o sistema teria apenas título, descrição e status.
Para atender a uma necessidade da startup, foi incluída uma nova
funcionalidade: **campo de prioridade** da tarefa (low, medium ou high).

### Justificativa
Isso permite que as tarefas mais urgentes sejam identificadas rapidamente,
melhorando o fluxo de trabalho no ambiente ágil.

## Links úteis
- Kanban: GitHub → Projects do repositório
- Ações: GitHub → Actions (CI executa testes a cada push)
