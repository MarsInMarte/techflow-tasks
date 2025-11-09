from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de tarefas
tarefas = []
proximo_id = 1

@app.get("/")
def home():
    return "API de Tarefas funcionando!"

@app.post("/tarefas")
def criar_tarefa():
    global proximo_id
    dados = request.get_json() or {}

    titulo = dados.get("titulo", "").strip()

    if not titulo:
        return jsonify({"erro": "O campo 'titulo' é obrigatório."}), 400

    tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": dados.get("descricao", ""),
        "status": "pendente",  # em vez de "todo"
        "prioridade": dados.get("prioridade", "media")  # baixa / media / alta
    }

    tarefas.append(tarefa)
    proximo_id += 1
    return jsonify(tarefa), 201

@app.get("/tarefas")
def listar_tarefas():
    return jsonify(tarefas), 200

@app.put("/tarefas/<int:tarefa_id>")
def atualizar_tarefa(tarefa_id):
    dados = request.get_json() or {}

    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["titulo"] = dados.get("titulo", tarefa["titulo"])
            tarefa["descricao"] = dados.get("descricao", tarefa["descricao"])
            tarefa["status"] = dados.get("status", tarefa["status"])
            tarefa["prioridade"] = dados.get("prioridade", tarefa["prioridade"])
            return jsonify(tarefa), 200

    return jsonify({"erro": "Tarefa não encontrada."}), 404

@app.delete("/tarefas/<int:tarefa_id>")
def deletar_tarefa(tarefa_id):
    global tarefas
    antes = len(tarefas)

    tarefas = [t for t in tarefas if t["id"] != tarefa_id]

    if len(tarefas) == antes:
        return jsonify({"erro": "Tarefa não encontrada."}), 404

    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
