# demo.py — Specifier Skill Demo

from logic import run
sample_input = {
    "claim": "Asian Americans have faced a lot of challenges in America.",
    "context": (
        """
        Reflective Assignment 1:
        One important aspect of this course is reflection. In order to reflect, we will set goals for ourselves and our learning.
        Write a letter to 'future you' 9 weeks from now. This letter can take the form of a video, an audio note to yourself, or you can write a traditional letter. You should address some of the questions below. The questions in bold are required. 
        Prior to this class, what was your conception of 'Asian American communities?'
        How would you define the term 'Asian American?'
        What are some issues that you think are salient to Asian American communities?
        Why does this course interest you? What made you want to learn more about contemporary issues in Asian American communities?
        Thinking about your own personal history, how does it relate to our course?
        Are there specific topics or issues that interest you? If so, tell us why.
        Reflect on the first day of class.
        What do you think this class will be about?
        How do you see yourself contributing to our learning community?
        Using the course learning goals, set two personalized goals for yourself. What do you hope to have learned and accomplished by the end of the quarter?
        Steps:
        Based on the prompt above, speak to your future self about this course, your learning (goals), and your contribution to your learning community.
        Engage with some of the questions listed above. You do not have to address all of the questions, but try to go in-depth with a few.
        Try to organize your thoughts so they don't jump from one topic to another. Give these questions some deep thought and write about it.
        You must answer the bolded questions.
        TIP: If you choose the video or audio format, write out a script.
        Submit Reflective Assessment 1 on Canvas.
        Format:
        Written: min. word count: 500; max. word count: 750
        Video/audio: min. 3 minutes; max. 5 minutes
        Informal/conversational tone
        Deadline: Fri, April 10, 2026 by 11:59 p.m. Central
        Assignment type: Reflective
        Grading criteria:
        Shows serious, thoughtful self-reflection
        Adheres to the word/time limit
        Clearly written or spoken
        Minimal errors
        
        
        Learning Outcomes:
        Recognize and articulate reciprocal relationships between societal forces (e.g., norms, laws, organizational structures), psychological forces (e.g., traits, motives, attitudes), and the behaviors of individuals and groups
        Demonstrate knowledge and understanding of social science theories related to the influence of culture and power on the behavior of individuals, interpersonal relationships, and/or group dynamics
        Reflect upon the way in which theories and research from the social and behavioral sciences help elucidate the factors underlying contemporary social issues, social problems, and/or ethical dilemmas in the U.S. and/or abroad, as well as inform potential solutions to societal problems
        """
    ),
}

if __name__ == "__main__":
    print("=" * 60)
    print("Specifier Skill — Demo Run")
    print("=" * 60)

    print("\n[INPUT]")
    print(f"  Claim   : {sample_input['claim']}")
    print(f"  Context : {sample_input['context']}")

    print("\n[RUNNING SKILL...]\n")
    result = run(sample_input)

    print("[TUTOR RESPONSE]")
    print("-" * 60)
    print(result)
    print("-" * 60)