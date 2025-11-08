import sys, os
sys.path.append(os.path.abspath("src"))

from app import app
import json

def test_criar_tarefa():
    client = app.test_client()

    resposta = client.post(
        "/tasks",
        data=json.dumps({"title": "Estudar"}),
        content_type="application/json"
    )

    assert resposta.status_code == 201
    dados = resposta.get_json()
    assert dados["title"] == "Estudar"

def test_listar_tarefas():
    client = app.test_client()

    # cria uma tarefa
    client.post(
        "/tasks",
        data=json.dumps({"title": "Tarefa X"}),
        content_type="application/json"
    )

    # agora lista
    resposta = client.get("/tasks")
    assert resposta.status_code == 200

    dados = resposta.get_json()
    assert isinstance(dados, list)
    assert len(dados) >= 1
