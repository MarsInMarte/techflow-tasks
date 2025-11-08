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
