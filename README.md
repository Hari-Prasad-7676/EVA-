# EVA-
An emotionally Viable assistant 

# AI Flask App with Ollama

This is a Flask-based web application integrated with Ollama for running local AI models.

The project provides a simple web interface where users can send prompts and receive AI-generated responses.

---

## Tech Stack

- Python
- Flask
- Ollama (Local LLM runtime)
- HTML (Jinja Templates)
- Gunicorn (Production server)

---

## Project Structure

```
app.py
main.py
gui.py
requirements.txt
templates/
memory.json
```

---

## Local Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create virtual environment

Mac/Linux:
```
python -m venv venv
source venv/bin/activate
```

Windows:
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com/download

After installation, pull a model:

```
ollama pull llama3
```

### 5. Run the app locally

```
python app.py
```

The app runs at:

```
http://127.0.0.1:5000
```

---

## Deployment (Render / Cloud)

Important: Ollama runs locally and cannot run on most free cloud platforms like Render.

If deploying to Render:

Build Command:
```
pip install -r requirements.txt
```

Start Command:
```
gunicorn app:app
```

---

## Important Note About Ollama

Ollama requires:
- Local machine access
- System-level installation
- Model files stored locally

Free cloud platforms do not support running Ollama directly.

If you want cloud AI:
- Use OpenAI API
- Or host Ollama on a VPS (AWS / DigitalOcean)

---

## Production Configuration

Ensure app.py includes:

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
```

---

## Features

- Flask-based web interface
- Memory storage using JSON
- AI prompt-response system
- Modular structure

---

## License

This project is for educational and development purposes.
