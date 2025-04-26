# Live Coding HR Server

Lightweight FastAPI server to serve a coding model for hint generation and dynamic follow-up questions during live coding rounds.

## Features
- /hint/ endpoint: Generate a hint based on user's partial code and task description.
- /followup/ endpoint: Generate a follow-up question if the user finishes early.
- Multi-user concurrent handling.

## Setup

```bash
# Clone the repository
git clone <repo-url>
cd live-coding-hr-server

# Build Docker image
docker build -t live-coding-server .

# Run Docker container
docker run -p 8000:8000 live-coding-server
```

## API Endpoints

### POST /hint/
Input:
```json
{
    "code": "partial code",
    "task_description": "task",
    "is_completed": false
}
```
Output:
```json
{
    "hint": "short helpful hint"
}
```

### POST /followup/
Input:
```json
{
    "code": "complete code",
    "task_description": "task",
    "is_completed": true
}
```
Output:
```json
{
    "follow_up_question": "a harder question"
}
```

## Deployment Option
- Deploy easily to RunPod, Modal, or any cloud that supports Docker.

---

# (Done!)