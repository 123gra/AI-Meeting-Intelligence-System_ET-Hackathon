def check_escalations(tasks):
    escalations = []

    for task in tasks:
        task_text = task["task"]

        # Only escalate important/long tasks
        if len(task_text) > 40:
            escalations.append(f" '{task_text}' may need attention")

    return escalations