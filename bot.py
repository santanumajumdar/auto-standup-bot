import openai

def summarize_standups(updates):
    prompt = "Summarize the following team standups and highlight blockers:\n" + "\n".join(updates)
    res = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    print(res.choices[0].message.content)

if __name__ == "__main__":
    updates = ["Alice: Did auth, blocked on DB.", "Bob: Fixed CSS."]
    summarize_standups(updates)
