def create_tasks(decisions_text):
    tasks = []
    seen = set()

    for line in decisions_text.split("\n"):
        line = line.strip()

       
        if not line or "Decisions" in line or "Action Items" in line:
            continue

       
        if line.startswith("-"):
            line = line[1:].strip()

       
        if line in seen:
            continue

        seen.add(line)

        tasks.append({
            "task": line,
            "status": "in-progress"
        })

    return tasks