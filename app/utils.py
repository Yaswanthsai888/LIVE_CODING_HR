def format_prompt_for_hint(task_description: str, code_snippet: str) -> str:
    return f"Task: {task_description}\nUser's Code:\n{code_snippet}\nGive a short hint to improve:"

def format_prompt_for_followup(task_description: str) -> str:
    return f"Given this completed coding task: {task_description}\nCreate a follow-up harder question:"
