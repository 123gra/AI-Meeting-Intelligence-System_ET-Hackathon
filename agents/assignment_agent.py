import random

def assign_tasks(tasks):
    owners = ["Alice", "Bob", "Charlie"]

    for task in tasks:
        task["owner"] = random.choice(owners)

    return tasks