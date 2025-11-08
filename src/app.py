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

@app.put("/tasks/<int:task_id>")
def update_task(task_id):
    data = request.get_json() or {}

    for task in tasks:
        if task["id"] == task_id:
            # Atualiza só o que foi enviado
            task["title"] = data.get("title", task["title"])
            task["description"] = data.get("description", task["description"])
            task["status"] = data.get("status", task["status"])
            return jsonify(task), 200

    return jsonify({"error": "not found"}), 404

@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    global tasks
    before = len(tasks)

    tasks = [t for t in tasks if t["id"] != task_id]

    if len(tasks) == before:
        return jsonify({"error": "not found"}), 404

    return "", 204
