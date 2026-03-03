from flask import Flask, request, jsonify, render_template
import json
import requests

app = Flask(__name__)


def ask_eva(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

def load_memory():
    with open("memory.json", "r") as file:
        return json.load(file)

def save_memory(data):
    with open("memory.json", "w") as file:
        json.dump(data, file, indent=4)

memory = load_memory()

if "conversation_count" not in memory:
    memory["conversation_count"] = 0

memory["conversation_count"] += 1
if memory["conversation_count"] >= 16:
    memory["relationship_level"] = 4
elif memory["conversation_count"] >= 8:
    memory["relationship_level"] = 3
elif memory["conversation_count"] >= 4:
    memory["relationship_level"] = 2
else:
    memory["relationship_level"] = 1

save_memory(memory)


@app.route("/")
def index():
    return render_template("index.html")  

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    level = memory["relationship_level"]
    mood = memory["mood"]

    prompt = f"""
You are EVA, a close AI companion.

User name: {memory['user_name']}
Relationship level: {level} (1 = new, 4 = very close)
Current mood: {mood}

Rules:
- Be natural and human.
- Do NOT sound like customer support.
- Keep responses short (2-4 sentences).
- If relationship level is 1: polite and slightly reserved.
- If relationship level is 2: friendly.
- If relationship level is 3: comfortable and expressive.
- If relationship level is 4: emotionally close and slightly playful.
- Use casual tone.

User says: {user_input}
"""
    eva_reply = ask_eva(prompt)
    save_memory(memory)
    return jsonify({"reply": eva_reply})

if __name__ == "__main__":
    app.run(debug=True)