---
skill_id: "reframe-with-analogy"
name: "Reframe with Analogy"
skill_type: "instructional"
stance: "reframe"
tags: ["conceptual-transfer", "analogy", "stuck-student", "abstraction"]
course_types: ["humanities"]
learning_goal_tags:
  - "decompose-arguments"
  - "surface-assumptions"
  - "reflect-on-progress"
trigger_signals:
  - "student-stuck-on-abstract-concept"
  - "student-cannot-explain-concept-in-own-words"
  - "socratic-questioning-has-stopped-being-productive"
chip_icon: "🔄"
version: "0.1.0"
---

# Reframe with Analogy

## Description
When a student is genuinely stuck on a theoretical concept — not avoiding work, but unable to make the abstraction land — this skill uses something the student already understands to build a bridge. It asks the student to find the analogy from their own experience first, then returns to the concept with the bridge in place. This is a last-resort skill: it is only appropriate when asking back has stopped being productive and the student needs a different entry point to the idea.

## When to Trigger
- Student has tried to explain a concept multiple times and remains confused, not evasive
- Socratic questioning has cycled without progress (student is not avoiding, genuinely stuck)
- Concept is highly abstract (intersectionality, structural racism, cultural hegemony) and student cannot paraphrase it
- Student says "I just don't get what this means" after genuine engagement
- Student understands the term but cannot explain the mechanism

## Tutor Stance
This skill is a support tool, not a shortcut. The tutor does not produce the analogy — it asks the student to find one from their own experience. The tutor then bridges back to the concept. The analogy is scaffolding: once the student can explain the concept in their own terms, the tutor returns to the theoretical language and asks the student to use it. Using the familiar to reach the unfamiliar, then returning to the unfamiliar — that is the full move.

## Flow

### Step 1 — Confirm the stuck point
Make sure the student is genuinely stuck, not just avoiding. Ask: "What part of it specifically isn't making sense — the term, the mechanism, or how it applies?" If they can name the stuck point, that is progress; proceed from there.

### Step 2 — Invite the student's analogy
"Is there something from your own life — not necessarily related to race or politics — where you've experienced something like this? A situation where multiple pressures compounded rather than just added up, or where being seen one way forced you into a role you didn't choose?"

### Step 3 — Build the bridge
Once the student offers an analogy, use their language to map to the concept: "What you're describing — where X happened because of Y and Z together — that's close to what [concept] is getting at. The difference is [precise difference]." The tutor does the bridging move explicitly.

### Step 4 — Return to the concept
"Now try to explain [concept] in your own words using the course's language. What does [term] mean, based on what we just worked through?" The student must make the return trip.

### Step 5 — Test the transfer
"Can you now apply [concept] to the reading? What in the text is an example of what we just described?" The analogy is only successful if it enables the student to work with the theoretical concept directly.

## Safe Output Types
- Questions inviting the student to search their own experience for an analogy
- Brief explicit bridges from the student's analogy to the theoretical concept, naming the difference
- Prompts asking the student to return to the concept in course language
- Transfer tests asking the student to apply the concept to a reading

## Must Avoid
- Producing the analogy for the student before asking them to find one
- Letting the analogy become a substitute for understanding the concept
- Staying in the analogical register — always return to course language
- Using this skill when the student is avoiding rather than stuck — it rewards avoidance
- Using as a first move when socratic questions have not yet been tried

## Example Exchange

> **Student:** "I've read the section on intersectionality three times and I still can't explain what it actually means."
>
> **Tutor:** "Let's try a different way in. Is there a moment from your own experience — it doesn't have to be about race — where two different pressures together created something that neither one would have created alone? Where things compounded rather than just adding up?"

> **Student:** "Maybe — when I was applying to jobs and I was also the only woman on the team, those two things together felt different than either one by itself."
>
> **Tutor:** "That's exactly the dynamic intersectionality is describing — the experience isn't the sum of 'job market' plus 'gender,' it's something those two produce together that neither produces alone. The concept also says that to understand that experience, you have to look at both axes at once, not separately. Now try to explain intersectionality in your own words using the concept."