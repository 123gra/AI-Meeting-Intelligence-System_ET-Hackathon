from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

from agents.nlp_agent import extract_decisions
from agents.task_agent import create_tasks
from agents.assignment_agent import assign_tasks
from agents.tracking_agent import track_tasks
from agents.escalation_agent import check_escalations
from utils.logger import log_event

app = FastAPI()


class MeetingInput(BaseModel):
    transcript: str


@app.post("/process-meeting")
def process_meeting(data: MeetingInput):
    logs = []

    log_event("Meeting processing started")
    logs.append("NLP Agent → Extracting decisions")

    decisions = extract_decisions(data.transcript)

    logs.append("Task Agent → Creating tasks")
    tasks = create_tasks(decisions)

    logs.append("Assignment Agent → Assigning owners")
    tasks = assign_tasks(tasks)

    logs.append("Tracking Agent → Updating status")
    tasks = track_tasks(tasks)

    logs.append("Escalation Agent → Checking risks")
    escalations = check_escalations(tasks)

    logs.append("Process completed successfully")

    return {
        "decisions": decisions,
        "tasks": tasks,
        "escalations": escalations,
        "logs": logs
    }


@app.get("/")
def serve_ui():
    return FileResponse("index.html")