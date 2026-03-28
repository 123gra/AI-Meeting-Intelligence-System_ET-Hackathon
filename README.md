# AI-Meeting-Intelligence-System_ET-Hackathon
#  AI Meeting Intelligence System

##  Overview

The **AI Meeting Intelligence System** is a multi-agent application that processes raw meeting transcripts and converts them into structured insights such as **decisions, tasks, and escalations**.

It simulates an AI-powered workflow using modular agents, making meetings more actionable and efficient.

---

##  Features

* Extracts key **decisions** from meeting transcripts
* Generates **actionable tasks**
*  Assigns tasks to owners
*  Tracks task progress
*  Identifies and flags **escalations**
* Displays **agent-level processing logs**
*  Interactive UI for real-time processing

---

##  System Architecture

The system follows a **multi-agent architecture**:

1. **NLP Agent**

   * Extracts decisions and action items from transcript

2. **Task Agent**

   * Converts extracted insights into structured tasks

3. **Assignment Agent**

   * Assigns owners to tasks

4. **Tracking Agent**

   * Updates task status

5. **Escalation Agent**

   * Flags critical or high-priority tasks

6. **Logger**

   * Tracks system workflow and events

---

##  Tech Stack

* **Backend:** FastAPI (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Architecture:** Multi-Agent System
* **Deployment:** GitHub Codespaces

---

##  Project Structure

```
AI-Meeting-Intelligence-System/
│
├── agents/
│   ├── nlp_agent.py
│   ├── task_agent.py
│   ├── assignment_agent.py
│   ├── tracking_agent.py
│   └── escalation_agent.py
│
├── utils/
│   └── logger.py
│
├── main.py
├── index.html
├── requirements.txt
└── README.md
```

---

## ▶ How to Run

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd AI-Meeting-Intelligence-System
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Open in browser

```
http://localhost:8000/
```

---

##  Sample Input

```
We decided to launch the product next month.
John will handle marketing.
Sarah will handle budget.
```

---

##  Sample Output

### Decisions

* Launch product next month

### Tasks

* John will handle marketing
* Sarah will handle budget

### Escalations

* Important tasks flagged for attention

---

##  Use Cases

* Corporate meeting automation
* Project management assistance
* Team productivity tools
* Decision tracking systems

---

##  Key Highlights

* Modular **agent-based design**
* Easy to extend with real AI models (OpenAI, Gemini)
* Clean UI for demonstration
* Scalable architecture for enterprise use

---

##  Future Enhancements

* Integration with real LLM APIs
* User authentication & dashboards
* Database integration for task persistence
* Email/Slack notifications for escalations

---

##  Hackathon Value

This project demonstrates:

* End-to-end system design
* Multi-agent workflow orchestration
* Practical AI use case implementation
* Clean UI + backend integration

---

##  Author

**Grace Magdalene**

---

##  Acknowledgements

Built as part of the **ET Gen AI Hackathon 2026**
