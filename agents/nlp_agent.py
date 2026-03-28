def extract_decisions(transcript):
    lines = transcript.split(".")
    
    decisions = []
    actions = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Simple logic
        if "decided" in line or "will" in line:
            decisions.append(line)
        
        if "will" in line or "handle" in line:
            actions.append(line)

    result = "Decisions:\n"
    for d in decisions:
        result += f"- {d}\n"

    result += "\nAction Items:\n"
    for a in actions:
        result += f"- {a}\n"

    return result