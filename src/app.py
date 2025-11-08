from flask import Flask

app = Flask(__name__)

# Lista onde vamos guardar as tarefas
tasks = []
next_id = 1

@app.get("/")
def home():
    return "Olá! O sistema está funcionando!"

if __name__ == "__main__":
    app.run(debug=True)

from flask import request, jsonify

@app.post("/tasks")
def create_task():
    global next_id
    data = request.get_json() or {}

    # Pega o título enviado
    title = data.get("title", "").strip()

    # Se não tiver título, erro
    if not title:
        return jsonify({"error": "title is required"}), 400

    # Cria a tarefa
    task = {
        "id": next_id,
        "title": title,
        "description": data.get("description", ""),
        "status": "todo"  # sempre começa como "a fazer"
    }

    tasks.append(task)
    next_id += 1

    return jsonify(task), 201

@app.get("/tasks")
def list_tasks():
    return jsonify(tasks), 200
