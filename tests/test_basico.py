import sys, os
sys.path.append(os.path.abspath("src"))

from app import app
import json

def test_criar_tarefa():
    client = app.test_client()

    resposta = client.post(
        "/tarefas",
        data=json.dumps({"titulo": "Estudar"}),
        content_type="application/json"
    )

    assert resposta.status_code == 201
    dados = resposta.get_json()
    assert dados["titulo"] == "Estudar"
    assert dados["status"] == "pendente"


def test_listar_tarefas():
    client = app.test_client()

    # cria uma tarefa
    client.post(
        "/tarefas",
        data=json.dumps({"titulo": "Tarefa X"}),
        content_type="application/json"
    )

    # agora lista
    resposta = client.get("/tarefas")
    assert resposta.status_code == 200

    dados = resposta.get_json()
    assert isinstance(dados, list)
    assert len(dados) >= 1
    assert "titulo" in dados[0]


def test_atualizar_tarefa():
    client = app.test_client()

    # cria uma tarefa
    resposta = client.post(
        "/tarefas",
        data=json.dumps({"titulo": "Antigo"}),
        content_type="application/json"
    )
    tarefa = resposta.get_json()
    id_tarefa = tarefa["id"]

    # atualiza a tarefa
    resposta2 = client.put(
        f"/tarefas/{id_tarefa}",
        data=json.dumps({"titulo": "Novo título"}),
        content_type="application/json"
    )

    assert resposta2.status_code == 200
    dados = resposta2.get_json()
    assert dados["titulo"] == "Novo título"


def test_apagar_tarefa():
    client = app.test_client()

    # cria uma tarefa
    resposta = client.post(
        "/tarefas",
        data=json.dumps({"titulo": "Apagar"}),
        content_type="application/json"
    )
    tarefa = resposta.get_json()
    id_tarefa = tarefa["id"]

    # apaga a tarefa
    resposta2 = client.delete(f"/tarefas

