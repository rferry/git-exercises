import json

# Open file
with open("data.json", "r") as f:
    # Load json
    data = json.load(f)
    answer = data["answer"]
    # Print answer
    print(answer)
