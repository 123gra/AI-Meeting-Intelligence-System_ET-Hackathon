def track_tasks(tasks):
    for task in tasks:
        if task["status"] == "pending":
            task["status"] = "in-progress"
    return tasks