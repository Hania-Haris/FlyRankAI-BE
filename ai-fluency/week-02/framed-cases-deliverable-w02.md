# Framed Cases — Hania Haris

## Voice Card
Professional, capable, approachable, calm, friendly, grounded, clear

---

## Case 1: Task CRUD API (Backend AI Engineering Internship, Week 2)

**The Problem**
As part of the backend engineering track of my internship, I was assigned to build a small CRUD API using FastAPI — a Task API that could create, view, update, and delete tasks, test all endpoints properly, and follow a real Git branching workflow rather than committing straight to `main`.

**What I Did (and Decided)**
I built the API with FastAPI and Pydantic models for validation, using in-memory storage as scoped by the assignment (database integration was the following week's task, not this one). I worked on a separate branch, `backend/week-2-crud-api`, committing in stages as each part was completed rather than mixing changes together — a habit I adopted *after* hitting a Git conflict in `main.py` while restoring some staged work earlier in the project.

When I merged the branch into `main`, I hit a real conflict in `.gitignore` (both branches had added the file, with an overlapping `Thumbs.db` entry). I resolved it by keeping the combined, clean version, completed the merge, and verified the history and status afterward.

For testing, I didn't just click through each endpoint once. I used curl from PowerShell and tested both normal and edge cases — for example, GET, PUT, and DELETE against a nonexistent task ID (999) to confirm the API returned 404 instead of failing. For task creation, I verified the 201 response, correct ID generation, and that the new task could be retrieved afterward. Testing actually caught two real problems: curl couldn't initially find my test JSON file, and a PowerShell JSON-quoting issue caused a PUT request to fail with 422 — not a bug in the API itself, but in how I was sending the request. Switching to a JSON file for the PUT request fixed it.

**What Came Of It**
The Week 2 CRUD API is complete: tested, committed in stages, pushed, and merged cleanly into `main`. It's a learning project, not a production backend — it uses in-memory storage (data resets on restart), has no authentication or authorization, and isn't deployed. What it does demonstrate: working FastAPI CRUD design, deliberate Git branching and conflict resolution, and testing discipline that included edge cases, not just happy paths.

---

## Other Sitemap Pieces — Status

The sitemap calls for cases beyond this one. As of this submission, they have not yet been interviewed to the same depth and are **not included here** rather than filled in with invented details:

- **Chromia** (AI-powered skin tone color analysis / palette generator, university final project) — likely next case; not yet interviewed.
- Other coursework/project work — not yet reviewed for portfolio fit.

---

## Before / After: One Line, Edited

**Generic AI-generated version:**
"Leveraging cutting-edge FastAPI technology, I engineered a robust and scalable Task Management API that showcases my passion for building innovative backend solutions."

**Edited (my voice):**
"I built a Task API in FastAPI — create, read, update, delete — and tested every endpoint by hand, including the ones that should fail. It's not production-ready yet: no database, no auth, no deployment. That's next."

*Why the edit matters: the generic version claims things I can't back up yet — "robust," "scalable," "innovative" — none of which this project actually proves. The edited version says exactly what I built, what I tested, and what's missing, which is more credible to someone evaluating entry-level backend work than buzzwords would be.*
