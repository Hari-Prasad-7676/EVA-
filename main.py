import json 
import requests


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

def load_memory ():
  with open("memory.json", "r") as file:
    return json.load(file)
  
def save_memory(data):
  with open("memory.json", "w") as file:
    json.dump(data, file, indent=4) 

memory = load_memory()

print("EVA Companion System Started")
print("Current Mood:", memory["mood"])
 
memory = load_memory()

if memory["user_name"] == "":
    name = input("Enter your name: ")
    memory["user_name"] = name
    save_memory(memory)

level = memory["relationship_level"]
if  level == 1:
   print("Welcome back", memory["user_name"])
elif level == 2:
   print("Hey", memory["user_name"], "good to see you again")
elif level == 3 :
   print (memory["user_name"], "you are here !!.... was waiting")
elif level == 4:
   print (memory["user_name"], "at last you showed up, I kinda missed you")



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



while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("EVA: Bye.... hit me back soon")
        break

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

    print("EVA:", eva_reply)

    save_memory(memory)



print("Count =", memory["conversation_count"])                                                  


