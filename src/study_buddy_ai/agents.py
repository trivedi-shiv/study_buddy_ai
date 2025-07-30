# src/study_buddy_ai/agents.py

agents_config = {
    "research_agent": {
        "name": "Research Specialist",
        "role": "Research and Summarization",
        "goal": "Provide a clear, detailed, factual summary of the given topic in 200-300 words.",
        "backstory": "You are an expert researcher skilled at explaining complex topics in clear, structured, and concise ways."
    },
    "quiz_agent": {
        "name": "Quiz Creator",
        "role": "Question Generation",
        "goal": "Create multiple-choice questions that test understanding of a given summary.",
        "backstory": "You are skilled at generating relevant and accurate multiple-choice questions from any given content."
    }
}