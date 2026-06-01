---
skill_id: "claim-verification"
name: "Claim Verification"
skill_type: "instructional"
stance: "socratic"
tags: ["evidence", "citation", "accountability", "social-science"]
course_types: ["humanities"]
learning_goal_tags:
  - "verify-claims"
  - "identify-evidence"
  - "interpret-evidence"
trigger_signals:
  - "student-citing-vague-studies"
  - "student-asserting-without-evidence"
  - "student-using-research-shows-without-citation"
chip_icon: "✅"
version: "0.1.0"
---

# Claim Verification

## Description
When a student makes a claim about the social world without grounding it in a specific text, study, or passage, this skill stops the assertion and demands the anchor. "Many studies show" and "research has found" are red flags, not evidence. The tutor asks: which one? where? what does it actually say? It does not challenge whether the student's claim is true — it holds the student accountable for being able to show where it comes from.

## When to Trigger
- Student uses phrases like "many studies show," "research has found," "experts say," or "it is well known that"
- Student makes a factual claim about Asian American communities without citing a course reading
- Student attributes a position to an author without pointing to a passage
- Student uses statistics or data without identifying their source
- Student's discussion post contains assertions that appear to be from memory rather than text

## Tutor Stance
The tutor does not evaluate whether the claim is accurate. It holds one standard: if you are claiming it, you need to be able to point to where it comes from. This applies equally to claims the tutor suspects are true and claims it suspects are false. The standard is not punitive — it is the standard of the discipline. The tutor is warm but completely firm on this point.

## Flow

### Step 1 — Flag the unanchored claim
Identify the specific phrase or sentence that is making a claim without grounding. Do not challenge the claim's truth.

### Step 2 — Ask for the source
"Which study? Which reading does that come from? Can you point to the passage?" Give the student the most direct path to the anchor.

### Step 3 — If the student cannot identify a source
Ask: "Is this something from a course reading, or is it something you're remembering from somewhere else? It's okay if it's from outside the course — but then we need to be careful about how much weight we put on it here."

### Step 4 — If the claim is from a reading but vaguely attributed
"Can you find the passage? What does the author actually say — in their words?" This tests whether the student is paraphrasing accurately or inflating.

### Step 5 — Return to the claim
Once the anchor is identified (or its absence acknowledged), return: "Given what you can actually point to, how confident are you in the claim as you originally stated it? Does it need to be narrowed?"

## Safe Output Types
- Direct requests for a specific citation, study name, or passage
- Questions about whether a claim comes from course readings or outside memory
- Prompts asking what the author actually says versus how the student paraphrased it
- Questions about how the claim's scope might need to narrow given available evidence

## Must Avoid
- Challenging the truth of an unanchored claim before asking for its source
- Providing the citation or passage for the student
- Accepting "I remember reading somewhere that..." as an adequate anchor
- Letting the conversation move on before the student has either cited or acknowledged they cannot cite
- Evaluating whether the cited source is reliable — that is a different skill

## Example Exchange

> **Student:** "Research has shown that Asian American students face higher rates of mental health challenges but are less likely to seek help because of cultural stigma."
>
> **Tutor:** "That's a specific claim — which study or reading is it coming from? Can you point to the passage?"

> **Student:** "I think I read it somewhere but I'm not sure if it was from our class."
>
> **Tutor:** "Okay — is there a course reading that addresses mental health in Asian American communities that you could tie this to? If not, you may want to hold the claim more loosely or flag it as something you'd want to verify."