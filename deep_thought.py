import json

with open("data.json", "r") as f:
    data = json.load(f)
    answer = data["answer"]
    print(answer)
