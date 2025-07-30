# src/study_buddy_ai/tasks.py

tasks_config = {
    "summarize_topic": {
        "description": (
            "You are a research assistant. Research the topic \"{topic}\" in detail and provide a clear, factual, "
            "and concise summary of around 200-300 words suitable for college students. "
            "Do not include phrases like 'Thought:' or any reasoning steps. "
            "Only output the final summary."
        ),
        "expected_output": "A 200-300 word factual summary of the topic."
    },
    "generate_quiz": {
        "description": (
            "You are a quiz creator. Based on the provided summary, create exactly 5 multiple-choice questions. "
            "Each question must have exactly 4 options labeled A), B), C), and D). "
            "After each question, clearly state the correct answer in the format: Correct Answer: X). "
            "Do not add explanations, thoughts, or any extra commentary — only output the questions, options, and correct answers.\n\n"
            "Summary:\n{summary}"
        ),
        "expected_output": (
            "5 multiple-choice questions with 4 labeled options each (A-D) "
            "and a clearly indicated correct answer."
        )
    }
}
