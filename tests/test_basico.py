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
