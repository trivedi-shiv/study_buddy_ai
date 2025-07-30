# src/study_buddy_ai/crew.py

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from .agents import agents_config
from .tasks import tasks_config

load_dotenv()

PROVIDER = os.getenv("PROVIDER")
MODEL = os.getenv("MODEL")
API_KEY = os.getenv("GROQ_API_KEY")

class StudyBuddyCrew:
    def __init__(self, topic):
        self.topic = topic
        llm_model = f"{PROVIDER}/{MODEL}"

        self.research_agent = Agent(
            **agents_config['research_agent'],
            llm=llm_model,
            api_key=API_KEY
        )

        self.quiz_agent = Agent(
            **agents_config['quiz_agent'],
            llm=llm_model,
            api_key=API_KEY
        )

    def run(self):
        # SUMMARY
        summarize_task = Task(
            description=tasks_config['summarize_topic']['description'].format(topic=self.topic),
            expected_output=tasks_config['summarize_topic']['expected_output'],
            agent=self.research_agent
        )
        summary_result = Crew(
            agents=[self.research_agent],
            tasks=[summarize_task]
        ).kickoff()

        summary_text = str(summary_result).replace("Thought:", "").strip()

        print("\n===== SUMMARY =====")
        print(summary_text)

        # QUIZ
        quiz_description = tasks_config['generate_quiz']['description'].format(summary=summary_text)
        quiz_task = Task(
            description=quiz_description,
            expected_output=tasks_config['generate_quiz']['expected_output'],
            agent=self.quiz_agent
        )
        quiz_result = Crew(
            agents=[self.quiz_agent],
            tasks=[quiz_task]
        ).kickoff()

        quiz_text = str(quiz_result)
        #.replace("Thought:", "").strip()

        print("\n===== QUIZ =====")
        print(quiz_text)



if __name__ == "__main__":
    topic_input = input("Enter a topic for Study Buddy AI: ")
    crew = StudyBuddyCrew(topic_input)
    crew.run()
    
    