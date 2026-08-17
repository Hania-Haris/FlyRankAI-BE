# Week 02 AI Fluency — Prompting Fundamentals on Real Tasks v2

**Assignment Code:** FL-02  
**Track:** General AI Fluency  
**Phase:** Foundations  
**Week:** 02  
**Estimated Workload:** 6 hours

---

## 1. Assignment Objective

The purpose of this exercise was to practice prompt engineering on a real task rather than a toy example.

**Real FL-01 task:** Turn my Week 02 FastAPI CRUD API project into a portfolio case study.

The exercise required six total prompt runs:

1. Naive baseline
2. Role assignment
3. Context and motivation
4. Few-shot examples
5. Output structure
6. Step decomposition

The final prompt was then run on both Claude and ChatGPT for an honest cross-model comparison.

---

## 2. Real Task and Project Context

The Week 02 backend engineering assignment was to build a basic Task CRUD API in Python using FastAPI.

The final API used Python, FastAPI, Pydantic, Uvicorn, and in-memory storage. It implemented:

- `GET /tasks`
- `GET /tasks/{task_id}`
- `POST /tasks`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

Each task contained an integer `id`, `title`, `description`, and `completed` boolean.

The API was tested locally with curl, including successful requests, missing-task cases, status codes, deletion behavior, and automatic ID generation.

An important project decision was rebuilding an earlier, more feature-rich version so that the final API matched the actual assignment scope rather than retaining unnecessary features.

---

# 3. Version 0 — Naive Baseline

## Technique
**None**

## Hypothesis

If I use the kind of vague one-line prompt I would have used before learning prompt engineering, the AI will have to make many assumptions and may produce something generic.

## Prompt

> Write a case study about my Week 02 CRUD API project.

## Output

Claude responded:

> Covers the objective, tech stack, and — the more interesting part — the scoping decision to rebuild from the general version down to exactly what the assignment asked for, plus the actual curl-based verification you ran against status codes and ID generation. That last section doubles as a good "how I work" note if you're using this for a portfolio or report.

It also offered to make a shorter LinkedIn/resume version.

## What changed and why

Nothing. This was deliberately the naive baseline.

## What improved in the output

Nothing yet; this was the reference point for later versions.

## What still failed

The response was too brief to be a usable case study. It mostly described what the case study would cover instead of actually presenting a developed narrative.

## What I would try next

Assign a relevant role so the AI approaches the task as a technical portfolio writer.

---

# 4. Version 1 — Role Assignment

## Technique
**Role assignment**

## Hypothesis

If I assign the AI the role of an experienced technical portfolio writer, it will frame the project more like a portfolio case study rather than simply summarizing it.

## Prompt

> You are an experienced technical portfolio writer who helps early-career software developers turn real projects into clear, honest case studies. Write a case study about my Week 02 CRUD API project.

## Output

Claude described the result as more like a portfolio entry:

> This one's written more like a portfolio entry — first-person, leading with the judgment call (rebuilding to match the exact spec instead of keeping the fancier version) rather than just listing features, since that's the part that actually differentiates the work.

It also retained the verification material:

> The verification table stays, since "I checked this, here's the proof" is a stronger claim than "this works."

## What changed and why

I added only the role assignment.

## What improved in the output

The output became more portfolio-oriented. It used first-person framing, emphasized the decision to rebuild to the exact specification, and treated testing evidence as proof rather than an unsupported claim.

## What still failed

The AI still had to infer important project context. The prompt did not yet explain the assignment requirements, purpose, scope boundaries, or why in-memory storage was used.

## What I would try next

Add context and motivation.

---

# 5. Version 2 — Context and Motivation

## Technique
**Context and motivation**

## Hypothesis

If I provide the actual project purpose, technology, scope, and learning goals, the AI will produce a more technically grounded case study and connect implementation decisions to the reason the project existed.

## Prompt

> You are an experienced technical portfolio writer who helps early-career software developers turn real projects into clear, honest case studies.
>
> Write a case study about my Week 02 CRUD API project.
>
> This was a backend engineering internship assignment where I was expected to build a basic Task CRUD API in Python using FastAPI. The goal was to demonstrate REST API fundamentals, request validation, HTTP status codes, endpoint testing, and a disciplined Git workflow. The assignment deliberately used in-memory storage rather than a database and required only the basic CRUD functionality.

## Output / observed result

Claude produced a more technically grounded case study and connected the project to REST fundamentals, validation, status codes, endpoint testing, Git workflow, and the intentionally narrow scope.

Claude also flagged that it did not have enough reliable information to describe the actual Git history in detail, so it avoided inventing commit or branch details.

## What changed and why

I added the actual context and motivation for the project.

## What improved in the output

The case study became more specific to the real assignment rather than a generic CRUD project. Technical decisions were now connected to the assignment's goals.

## What still failed

The Git section remained generic because the prompt did not provide the actual Git history.

## What I would try next

Add few-shot examples showing the difference between generic portfolio writing and specific, evidence-based writing.

---

# 6. Version 3 — Few-Shot Examples

## Technique
**Few-shot examples**

## Hypothesis

If I provide examples showing the difference between generic and specific project writing, the AI will imitate the more grounded style and produce a more project-specific case study.

## Prompt addition

The Version 2 prompt was retained, with these examples added:

> **Example 1 — too generic:**
>
> "I built a FastAPI CRUD API that demonstrates my backend development skills."
>
> **Better:**
>
> "I built the API around the assignment's exact five endpoints, then tested both successful requests and missing-task cases to verify the required HTTP status codes."
>
> **Example 2 — too generic:**
>
> "I used Git to manage the project."
>
> **Better:**
>
> "I developed the API on a separate feature branch, committed the work in stages, and merged the completed branch into main, resolving a `.gitignore` conflict during the merge."
>
> Use the second style: specific, grounded in actual decisions and actions, without exaggerating the technical difficulty or inventing results.

## Output

Claude responded that this looked like the same request as the previous one and returned essentially the same case study again.

It continued to note that it did not have enough actual Git history to make that section specific.

## What changed and why

I added few-shot examples demonstrating generic versus specific, evidence-based writing.

## What improved in the output

**Little to nothing visibly changed.**

## What still failed

The examples did not produce a meaningful visible change in this run.

This became an important finding:

> **Adding examples did not automatically change the output when Claude already had a similar response in context.**

## What I would try next

Try output structure to control how the information is organized.

---

# 7. Version 4 — Output Structure

## Technique
**Output structure**

## Hypothesis

If I explicitly define the structure of the final case study, the AI will organize the available information more deliberately instead of repeating its previous format.

## Prompt addition

The Version 3 prompt was retained, with this instruction added:

> Structure the case study with exactly these sections:
>
> 1. Problem
> 2. What I Did
> 3. Key Decisions
> 4. Testing and Evidence
> 5. Outcome
> 6. What This Demonstrates
>
> Keep each section focused on specific things I actually did, and do not invent information that is not provided.

## Output

Claude generated essentially the same case-study file again.

The previous response was already organized in almost exactly the requested way.

## What changed and why

I added an explicit output structure.

## What improved in the output

**Nothing meaningful.**

## What still failed

This produced another honest finding:

> **Output structure did not meaningfully improve this particular task because the previous output was already structured in almost exactly the requested way.**

## What I would try next

Use step decomposition to change the process used to produce the answer rather than just its final organization.

---

# 8. Version 5 — Step Decomposition

## Technique
**Step decomposition**

## Hypothesis

If I explicitly break the task into smaller stages before drafting, the AI will first identify requirements, actions, decisions, evidence, and the differentiating story, then produce a more accurate and grounded case study.

## Complete V5 Prompt

```text
You are an experienced technical portfolio writer who helps early-career software developers turn real projects into clear, honest case studies.

Write a case study about my Week 02 CRUD API project.

This was a backend engineering internship assignment where I was expected to build a basic Task CRUD API in Python using FastAPI. The goal was to demonstrate REST API fundamentals, request validation, HTTP status codes, endpoint testing, and a disciplined Git workflow. The assignment deliberately used in-memory storage rather than a database and required only the basic CRUD functionality.

Use these examples as a guide for the level of specificity and tone I want:

Example 1 — too generic:
"I built a FastAPI CRUD API that demonstrates my backend development skills."

Better:
"I built the API around the assignment's exact five endpoints, then tested both successful requests and missing-task cases to verify the required HTTP status codes."

Example 2 — too generic:
"I used Git to manage the project."

Better:
"I developed the API on a separate feature branch, committed the work in stages, and merged the completed branch into main, resolving a .gitignore conflict during the merge."

Use the second style: specific, grounded in actual decisions and actions, without exaggerating the technical difficulty or inventing results.

Structure the case study with exactly these sections:

1. Problem
2. What I Did
3. Key Decisions
4. Testing and Evidence
5. Outcome
6. What This Demonstrates

Keep each section focused on specific things I actually did, and do not invent information that is not provided.

Work through the task in these stages before producing the final case study:

1. Identify the actual problem and assignment requirements from the information provided.
2. Extract only the technical actions and decisions I actually made.
3. Separate verified evidence from claims or assumptions.
4. Identify the most useful story or decision that differentiates this project from a generic CRUD API.
5. Draft the case study using the required six-section structure.
6. Review the draft for invented details, generic portfolio language, unnecessary technical claims, and unsupported results, then revise it before presenting the final version.

Do not show this internal process or reasoning. Present only the final case study.
```

## Claude V5 output — observed result

Claude produced a detailed six-section case study covering:

- the exact assignment scope;
- the single `main.py`;
- `TaskCreate` and `Task` models;
- in-memory storage;
- incrementing IDs;
- `find_task()`;
- the five endpoints;
- the decision to rebuild the over-scoped version;
- explicit status codes;
- curl testing and results;
- the final outcome;
- what the project demonstrates.

## What changed and why

I added step decomposition, requiring the model to identify requirements, actions, evidence, and the differentiating story before drafting and reviewing the final case study.

## What improved in the output

This produced the clearest improvement in the final stage.

The output became more deliberately evidence-focused and separated:

- problem;
- implementation;
- decisions;
- evidence;
- outcome;
- lessons.

The testing section was especially concrete, and the scoping decision remained the central differentiating story.

## What still failed

The case study was still somewhat long for a portfolio page, and some technical explanations could be tightened.

Step decomposition improved organization and evidence selection, but did not make the project itself more technically sophisticated.

---

# 9. Cross-Model Comparison

The same final V5 prompt was run on Claude and ChatGPT.

## Overall

Both models produced useful, specific case studies. Both identified the most interesting aspect of the project as the decision to reduce an earlier, over-scoped implementation to the exact assignment requirements.

The main difference was:

> **Claude was more conservative about unsupported information, while ChatGPT produced a slightly more polished and accessible portfolio narrative.**

## Accuracy

### Claude

Claude was particularly careful about unsupported Git information. It explicitly recognized that the Git example in the prompt was a style example rather than sufficient evidence of the actual project history.

**Strength:** strong resistance to inventing project facts.

### ChatGPT

ChatGPT also stayed close to the project, but it made broader statements about using Git and merging work based on information available in the broader conversation.

**Winner: Claude**

## Tone

### Claude

More technical and report-like.

### ChatGPT

Slightly more natural for a portfolio audience. Its closing takeaway turned the technical experience into a broader engineering lesson:

> "A more feature-rich implementation is not necessarily a better implementation."

**Winner: ChatGPT**

## Structure

Both followed:

1. Problem
2. What I Did
3. Key Decisions
4. Testing and Evidence
5. Outcome
6. What This Demonstrates

**Winner: Tie**

## Technical specificity

Claude gave more implementation-level detail, including `TaskCreate`, `Task`, `find_task()`, incrementing IDs, exact endpoint names, input/response model separation, and explicit `201`/`404` behavior.

**Winner: Claude**

## Testing evidence

Claude's test table mapped individual tests to their results particularly clearly.

**Winner: Claude**

## Cross-model summary

| Category | Claude | ChatGPT | Stronger |
|---|---|---|---|
| Accuracy | Very cautious | Mostly accurate | **Claude** |
| Tone | Technical/report-like | More portfolio-friendly | **ChatGPT** |
| Structure | Strong | Strong | **Tie** |
| Technical detail | More specific | Slightly broader | **Claude** |
| Testing evidence | Very concrete | Concrete | **Claude** |
| Hiring-manager readability | Strong | Slightly more polished | **ChatGPT** |
| Avoiding unsupported claims | Excellent | Good | **Claude** |

### Final cross-model conclusion

> Claude produced the more technically precise and conservative case study, while ChatGPT produced the slightly more polished and accessible portfolio narrative. Claude was better at avoiding unsupported claims, particularly around Git history, whereas ChatGPT did a better job of turning the technical experience into a broader engineering lesson.

---

# 10. Technique Findings

| Technique | Hypothesis | Observed result |
|---|---|---|
| Role assignment | A relevant role will improve portfolio framing | **Confirmed** |
| Context & motivation | Real project context will reduce generic assumptions | **Confirmed** |
| Few-shot examples | Examples will improve specificity | **Little/no visible effect** |
| Output structure | Explicit structure will improve organization | **Little/no visible effect** |
| Step decomposition | Breaking the task into stages will improve evidence selection and accuracy | **Confirmed** |

---

# 11. Main Lessons

The exercise showed that prompt engineering is not simply about making prompts longer.

- **Role assignment** changed the perspective.
- **Context and motivation** changed the model's understanding of the project.
- **Few-shot examples** did not visibly improve this particular task.
- **Output structure** was largely redundant because the existing output was already similarly structured.
- **Step decomposition** produced the clearest final improvement by making the model separate requirements, evidence, decisions, and the differentiating story before drafting.

The important lesson was:

> **Prompting should be empirical. Change one ingredient, compare the output, and keep the ingredient only if it actually improves the result.**

---

# 12. Final Reusable Prompt Template

The following template is reusable by someone with a completely different project.

```text
You are an experienced technical portfolio writer who helps early-career software developers turn real projects into clear, honest case studies.

Write a portfolio case study about the following project:

PROJECT:
[Project name]

MY ROLE:
[Your role]

TECH STACK:
[Languages, frameworks, libraries, tools]

CONTEXT:
[What the project was for: internship, course, personal project, client project, etc.]

PROBLEM / REQUIREMENT:
[What you were asked to build or what problem you were trying to solve]

WHAT I ACTUALLY DID:
[List the implementation work, actions, and decisions you personally made]

KEY DECISIONS:
[List important technical or scope decisions and why you made them]

TESTING / EVIDENCE:
[List tests, measurements, observations, user feedback, deployment results, or other evidence that can actually be supported]

OUTCOME:
[What was completed, what worked, and what changed as a result]

LIMITATIONS:
[What the project does not do or what remains unfinished]

Use a specific, grounded writing style.

Avoid generic claims such as:
"I demonstrated my technical skills."

Prefer evidence-based statements such as:
"I tested both successful requests and failure cases and verified the expected status codes."

Do not exaggerate the project's technical difficulty or invent results, technologies, decisions, metrics, or responsibilities.

Structure the case study with these sections:

1. Problem
2. What I Did
3. Key Decisions
4. Testing and Evidence
5. Outcome
6. What This Demonstrates

Work through the task in these stages before producing the final case study:

1. Identify the actual problem and requirements.
2. Extract only the actions and decisions I actually made.
3. Separate verified evidence from assumptions.
4. Identify the most useful story or decision that differentiates this project from a generic project of the same type.
5. Draft the case study using the required structure.
6. Review the draft for invented details, generic portfolio language, unnecessary technical claims, and unsupported results.
7. Revise before presenting the final version.

Do not show the internal reasoning or intermediate analysis. Present only the final case study.
```

---

# 13. Why the Final Template Is Reusable

The template does not depend on my CRUD API.

It uses placeholders for:

- project name;
- role;
- technology;
- context;
- problem;
- actions;
- decisions;
- evidence;
- outcome;
- limitations.

It also preserves the useful lessons from the experiment:

- **Role** establishes perspective.
- **Context** explains why the work exists.
- **Examples** demonstrate the difference between generic and evidence-based language.
- **Output structure** defines the final organization.
- **Step decomposition** encourages evidence-first drafting.
- **Anti-invention constraints** reduce unsupported claims.

---

# 14. Final Reflection

Before this exercise, a prompt such as:

> "Write a case study about my Week 02 CRUD API project."

would have been enough to start, but it left too much for the AI to infer.

The iterations showed that improving a prompt is not simply about making it longer.

The final useful progression was:

> **Role → Context → Examples → Structure → Decomposition**

with an important qualification: examples and structure did not materially improve this particular task, while role, context, and step decomposition did.

The most important lesson is that prompt engineering should be treated as an experiment. Instead of assuming that every technique works, I can change one ingredient, compare the output, and decide whether that ingredient actually earned its place.

The final reusable template combines the techniques that proved useful with explicit safeguards against unsupported claims and generic portfolio language.

---

# 15. Submission Checklist

- [x] Real FL-01 task selected
- [x] Naive baseline included
- [x] Five additional versions completed
- [x] Role assignment tested
- [x] Context and motivation tested
- [x] Few-shot examples tested
- [x] Output structure tested
- [x] Step decomposition tested
- [x] Each version has a hypothesis
- [x] Each version explains what changed
- [x] Each version evaluates the observed output
- [x] Honest "little/no improvement" findings included
- [x] Final prompt run on Claude
- [x] Final prompt run on ChatGPT
- [x] Specific cross-model comparison included
- [x] Reusable prompt template included
- [x] Template does not depend on the personal CRUD API context
