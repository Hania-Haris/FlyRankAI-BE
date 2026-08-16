# Week 02 AI Fluency --- The Prompt Ladder

## Assignment

**Track:** General AI Fluency\
**Week:** 02\
**Assignment:** The Prompt Ladder

### Why this matters

The gap between a weak prompt and an engineered prompt can be a cheap
but significant performance upgrade. The purpose of this exercise was
not simply to produce a better prompt, but to change one ingredient at a
time, compare the outputs, and identify which ingredients actually
earned their place.

This ladder uses a real piece of work from my Week 02 backend
engineering internship: a **FastAPI CRUD API for managing tasks**.

------------------------------------------------------------------------

# 1. Starting Point

## Real project used for the ladder

I had built a basic CRUD API in Python using FastAPI as part of my Week
02 backend engineering internship work.

The actual API supported:

-   `GET /tasks`
-   `GET /tasks/{task_id}`
-   `POST /tasks`
-   `PUT /tasks/{task_id}`
-   `DELETE /tasks/{task_id}`

The implementation used an in-memory list rather than a database. Tasks
had an integer ID, title, description, and completed status.

The purpose of the Prompt Ladder was to see how much better an AI
response became when I gave it progressively better instructions.

------------------------------------------------------------------------

# 2. Ladder Overview

  -----------------------------------------------------------------------
  Run               Version           Single layer      Main result
                                      added             
  ----------------- ----------------- ----------------- -----------------
  1                 Baseline          None              AI guessed the
                                                        technology,
                                                        resource, scope,
                                                        and even
                                                        unrelated context

  2                 Version 1         Clearer goal      AI understood
                                                        that the resource
                                                        was tasks, but
                                                        still guessed the
                                                        technology and
                                                        scope

  3                 Version 2         Real context      AI switched to
                                                        FastAPI and
                                                        in-memory
                                                        storage, but
                                                        still overbuilt
                                                        the API

  4                 Version 3         Specified output  Output became
                                      format            more usable, but
                                                        the scope problem
                                                        remained

  5                 Version 4         Constraints       Major reduction
                                                        in invented
                                                        features; output
                                                        closely matched
                                                        the actual
                                                        assignment

  6                 Version 5         Verification      AI explicitly
                                      requirements      checked the
                                                        required
                                                        behaviors and
                                                        reported the test
                                                        results
  -----------------------------------------------------------------------

A key lesson was that **not every layer helped equally**. Constraints
made the biggest practical difference, while output format improved
usability without fixing the underlying scope problem.

------------------------------------------------------------------------

# 3. Run 1 --- Weak Baseline

## Layer

**Baseline --- no added layer**

## Hypothesis

If I give AI the kind of vague prompt I might have written a month ago,
it will have to fill in many missing details itself. The baseline should
reveal what the model assumes when I do not provide enough information.

## Prompt

> Write backend code for a CRUD API.

## Output

Claude responded:

> Here's a Node.js + Express CRUD API with in-memory storage (easy to
> swap for a real DB later). I picked a generic "items" resource ---
> rename it to match whatever you're building.
>
> Full CRUD for an `items` resource --- create, list (with
> search/pagination), get one, full/partial update, delete, plus
> validation and error handling. `npm install && npm start` gets it
> running on port 3000.
>
> Since you've been doing Firebase-backed work (like the Pizza Bar admin
> dashboard), swapping the in-memory array for Firestore calls would be
> a quick follow-up if you want --- just say the word and I'll wire it
> in.

## What changed in the prompt

Nothing. This was deliberately the weak baseline.

## What improved in the output

Nothing yet. This was the reference point against which all later
versions were compared.

## What still failed

The response guessed almost everything:

-   It chose **Node.js + Express** even though my project used
    Python/FastAPI.
-   It chose a generic `items` resource instead of tasks.
-   It added search and pagination that I did not ask for.
-   It assumed Firebase/Firestore context that was not present in the
    prompt.
-   It suggested a much broader implementation than the simple Week 02
    CRUD API I actually needed.

## What I would try next

Make the goal clearer by specifying what the CRUD API is actually
supposed to manage.

------------------------------------------------------------------------
# 4. Run 2 --- Version 1

## Layer added

**Clearer goal**

## Hypothesis

If I only clarify what resource the API is supposed to manage, the model
should stop inventing a generic resource such as `items`. I am
deliberately not telling it the technology or implementation details
yet, so I can isolate the effect of this one change.

## Prompt

> Build a CRUD API for managing tasks.

## Output

Claude responded:

> Full CRUD for tasks --- title, description, status
> (`todo`/`in-progress`/`done`), priority, and due date. Endpoints
> support filtering by status/priority, search, sorting by due date, and
> pagination. `npm install && npm start` runs it on port 3000.

## What changed in the prompt

I changed the vague resource description from "a CRUD API" to a CRUD API
specifically for **managing tasks**.

## What improved in the output

The response correctly focused on a **task resource** instead of generic
`items`. The subject of the API was clearer.

## What still failed

The model still made major assumptions:

-   It chose Node.js/Express.
-   It invented `status`, `priority`, and `due date` fields.
-   It added filtering, search, sorting, and pagination.
-   It still assumed npm commands and a Node.js environment.

The clearer goal helped, but it was not enough to make the answer match
my actual project.

## What I would try next

Add **real context** about the project, including the technology I am
actually using and the fact that this is an internship project.

------------------------------------------------------------------------

# 5. Run 3 --- Version 2

## Layer added

**Real context**

## Hypothesis

If I provide the actual project context and technology, the model should
stop choosing the wrong stack and should understand that the API is a
small FastAPI internship project using in-memory storage.

## Prompt

> Build a CRUD API for managing tasks. This is a Week 02 backend
> engineering internship project, and I am building it in Python using
> FastAPI. The API uses an in-memory list for task storage.

## Output

Claude responded:

> Full CRUD in FastAPI with Pydantic models for validation
> (`TaskCreate`, `TaskUpdate`, `TaskPatch`, `Task`), enums for
> `status`/`priority`, and an in-memory list (`tasks_db`) as required. I
> tested it locally --- server boots, create/list endpoints both work
> correctly, and `/docs` gives you Swagger UI out of the box for demos.
>
> `uvicorn main:app --reload` runs it. Same feature set as before
> (filtering, search, sorting, pagination) but idiomatic FastAPI:
> type-hinted, auto-validated, auto-documented.

## What changed in the prompt

I added the real project context:

-   Week 02 backend engineering internship
-   Python
-   FastAPI
-   in-memory list storage

## What improved in the output

The model correctly switched from Node.js/Express to **FastAPI** and
understood the in-memory storage requirement. It also recognized
FastAPI-specific concepts such as Pydantic validation and Swagger
documentation.

## What still failed

The model continued inventing features and requirements:

-   filtering
-   search
-   sorting
-   pagination
-   PATCH
-   status and priority enums
-   multiple extra models

It also claimed that it had tested the API locally, even though I had
not asked it to run anything and the prompt did not establish that it
had access to my environment.

The real context fixed the technology mismatch, but it did not
sufficiently control the scope.

## What I would try next

Specify the **output format** so the answer is presented as a concrete
implementation rather than an expanding feature description.

------------------------------------------------------------------------

# 6. Run 4 --- Version 3

## Layer added

**Specified output format**

## Hypothesis

If I tell the model exactly how I want the answer presented, the
response should become easier to use and copy into the project. I am
testing presentation separately from scope.

## Prompt

> Build a CRUD API for managing tasks. This is a Week 02 backend
> engineering internship project, and I am building it in Python using
> FastAPI. The API uses an in-memory list for task storage. Return the
> solution as a single `main.py` file, followed by the commands needed
> to run and test it.

## Output

Claude produced a complete `main.py`, followed by setup, run, and curl
commands.

The implementation included:

-   FastAPI
-   Pydantic models
-   in-memory storage
-   task creation
-   listing
-   getting one task
-   PUT
-   PATCH
-   DELETE
-   filtering
-   search
-   sorting
-   pagination
-   UUIDs
-   timestamps
-   Swagger documentation
-   setup and curl examples

Representative excerpt:

``` python
class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in-progress"
    done = "done"


class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
```

It also included commands such as:

``` bash
uvicorn main:app --reload
```

and example curl requests.

## What changed in the prompt

I added only an **output-format requirement**: provide one complete
`main.py` file followed by run/test commands.

## What improved in the output

The response became substantially more usable as a deliverable.

Instead of only describing an API, it gave:

-   one complete file
-   setup instructions
-   run instructions
-   test commands

The structure was much easier to follow and copy.

## What still failed

The scope problem remained almost completely unchanged.

The model still added:

-   PATCH
-   filtering
-   search
-   pagination
-   sorting
-   UUIDs
-   timestamps
-   status/priority enums
-   additional models

This is the important **honest "this didn't help" moment** in the
ladder:

> **Adding the output format made the response easier to use, but it did
> not solve the scope problem.**

This showed that a better format is not the same thing as better task
control.

## What I would try next

Add explicit **constraints** that define the actual scope of the API and
prohibit features that are outside the assignment.

------------------------------------------------------------------------

# 7. Run 5 --- Version 4

## Layer added

**Constraints**

## Hypothesis

If I explicitly define the required endpoints and fields and prohibit
unnecessary features, the model should stop overbuilding the API and
produce something much closer to my actual Week 02 assignment.

## Prompt

> Build a CRUD API for managing tasks. This is a Week 02 backend
> engineering internship project, and I am building it in Python using
> FastAPI. The API uses an in-memory list for task storage. Return the
> solution as a single `main.py` file, followed by the commands needed
> to run and test it. Keep the API limited to the basic CRUD operations
> for tasks: GET all tasks, GET one task by integer ID, POST a task, PUT
> a task, and DELETE a task. Each task should only have an integer `id`,
> `title`, `description`, and `completed` boolean. Do not add PATCH,
> filtering, search, pagination, authentication, a database, UUIDs, or
> extra features.

## Output

Claude produced a much smaller FastAPI implementation with:

-   an in-memory list
-   integer IDs
-   `title`
-   `description`
-   `completed`
-   GET all
-   GET one
-   POST
-   PUT
-   DELETE
-   404 handling

Representative structure:

``` python
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False


class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool = False
```

The response also provided setup and curl commands for the five
operations.

## What changed in the prompt

I added only **constraints**:

-   exact CRUD operations
-   exact task fields
-   integer IDs
-   in-memory storage
-   explicit prohibition of extra features

## What improved in the output

This was the biggest improvement in the ladder.

The model stopped overbuilding the project and produced an API much
closer to the actual Week 02 assignment.

Instead of a large feature-heavy API, it focused on the basic five
operations:

-   GET all
-   GET one
-   POST
-   PUT
-   DELETE

It also stopped adding databases, UUIDs, PATCH, filtering, search, and
pagination.

## What still failed

The response still did not exactly reproduce my own implementation.

For example:

-   it used a Pydantic `Task` response model rather than my plain task
    dictionaries;
-   it used a separate `TaskCreate` model;
-   the structure differed from my implementation.

However, these were now implementation differences rather than major
scope failures.

The response also provided commands and instructions, but at this stage
it had not yet been given explicit verification requirements.

## What I would try next

Add **verification requirements** so the model checks the important
behaviors and does not casually claim that code has been tested when it
has not.

------------------------------------------------------------------------

# 8. Run 6 --- Version 5

## Layer added

**Verification requirements**

## Hypothesis

If I require explicit verification of the important behaviors, the model
should produce a more trustworthy answer and distinguish between code it
proposes and code it has actually tested.

## Final ladder prompt used for Version 5

> Build a CRUD API for managing tasks. This is a Week 02 backend
> engineering internship project, and I am building it in Python using
> FastAPI. The API uses an in-memory list for task storage. Return the
> solution as a single `main.py` file, followed by the commands needed
> to run and test it. Keep the API limited to the basic CRUD operations
> for tasks: GET all tasks, GET one task by integer ID, POST a task, PUT
> a task, and DELETE a task. Each task should only have an integer `id`,
> `title`, `description`, and `completed` boolean. Do not add PATCH,
> filtering, search, pagination, authentication, a database, UUIDs, or
> extra features. Before considering the solution complete, verify that
> it includes all five CRUD endpoints, returns 201 for a successful
> POST, returns 404 for a nonexistent task on GET, PUT, and DELETE, and
> generates a new unique integer ID when creating a task. Do not claim
> that you ran or verified the code unless you actually did.

## Output

Claude returned the implementation and explicitly reported that it had
verified the required behaviors.

It reported:

-   `POST /tasks` → **201**, first task ID = 1
-   second `POST /tasks` → **201**, second task ID = 2
-   `GET /tasks` → **200**
-   `GET /tasks/1` → **200**
-   `GET /tasks/999` → **404**
-   `PUT /tasks/1` → **200**
-   `PUT /tasks/999` → **404**
-   `DELETE /tasks/1` → **200**
-   deleting task 1 again → **404**
-   GET after deletion confirmed the deleted task was gone

Representative verification excerpt:

> All five endpoints, all four required behaviors (201 on create, 404 on
> missing task for GET/PUT/DELETE, unique incrementing IDs) verified
> against the actual running server.

## What changed in the prompt

I added only **verification requirements**:

-   all five endpoints must exist
-   POST must return 201
-   missing GET/PUT/DELETE must return 404
-   new tasks must receive unique incrementing IDs
-   the model must not claim testing unless it actually verified it

## What improved in the output

The response became much easier to trust and evaluate.

Instead of only providing implementation and generic commands, it
explicitly described the expected checks and their results. The
verification focused directly on the requirements that mattered for the
project.

This made it easier to distinguish between:

-   code that merely looks correct
-   code that has actually been checked against the required behaviors

## What still failed

The code presentation was not perfect. Parts of the Python output were
compressed or poorly formatted, making it harder to read or copy
directly.

The verification requirement improved reliability, but it did not
automatically improve code presentation.

## What I would try next

For a reusable final prompt, keep the verification requirement but
explicitly require clean, readable, properly formatted Python code and
require the model to clearly distinguish between actual execution and
suggested tests.

------------------------------------------------------------------------

# 9. What the Ladder Taught Me

The main lesson was not simply that "more detailed prompts are better."

Different layers solved different problems.

### 1. Clearer goal

**Solved:** ambiguity about the resource.

The model stopped talking about generic `items` and understood that the
API was for tasks.

**Did not solve:** technology, scope, or invented requirements.

------------------------------------------------------------------------

### 2. Real context

**Solved:** technology and project context.

The model switched from Node.js/Express to Python/FastAPI and understood
the in-memory storage context.

**Did not solve:** overbuilding.

------------------------------------------------------------------------

### 3. Output format

**Solved:** usability and presentation.

The response became a concrete `main.py` plus commands rather than a
vague description.

**Did not solve:** scope.

This was the most important "this didn't help enough" finding.

------------------------------------------------------------------------

### 4. Constraints

**Solved:** scope creep.

This made the largest practical difference.

The model stopped adding:

-   PATCH
-   filtering
-   search
-   pagination
-   databases
-   UUIDs
-   unrelated task fields

The output became much closer to the actual project.

------------------------------------------------------------------------

### 5. Verification requirements

**Solved:** confidence and testability.

The model was pushed to check the actual required behaviors instead of
just presenting code that looked plausible.

------------------------------------------------------------------------

# 10. Layer-by-Layer Hypotheses

  -----------------------------------------------------------------------
  Layer                   Hypothesis              Result
  ----------------------- ----------------------- -----------------------
  Clearer goal            Naming the resource     **Partially confirmed**
                          will stop generic       
                          assumptions             

  Real context            Giving the actual stack **Confirmed**
                          will stop technology    
                          guessing                

  Output format           Specifying the format   **Confirmed**
                          will make the answer    
                          more usable             

  Constraints             Explicit scope will     **Strongly confirmed**
                          stop unnecessary        
                          feature expansion       

  Verification            Explicit checks will    **Confirmed**
                          make the result more    
                          trustworthy             
  -----------------------------------------------------------------------

------------------------------------------------------------------------
# 11. The Biggest Finding

The biggest improvement did not come from simply making the prompt
longer.

It came from **telling the model what not to do**.

The transition from Version 3 to Version 4 was especially useful:

### Before constraints

The model produced:

-   PATCH
-   filtering
-   search
-   sorting
-   pagination
-   UUIDs
-   timestamps
-   status/priority enums
-   extra models

### After constraints

The model produced:

-   GET all
-   GET one
-   POST
-   PUT
-   DELETE
-   integer IDs
-   title
-   description
-   completed
-   in-memory storage

The lesson I would take from this is:

> **When AI is over-solving a problem, adding more context is not always
> enough. Explicit constraints can be much more effective because they
> define the boundaries of the solution.**

------------------------------------------------------------------------

# 12. Final Reusable Prompt

The final prompt should be clean enough that another person on my track
could use it without knowing the background conversation.

> Build a basic CRUD API for managing tasks.
>
> **Context:** This is a Week 02 backend engineering internship project.
> I am using Python and FastAPI, with an in-memory list for storage.
>
> **Scope:** Implement only these five operations:
>
> -   `GET /tasks` --- get all tasks
> -   `GET /tasks/{task_id}` --- get one task by integer ID
> -   `POST /tasks` --- create a task
> -   `PUT /tasks/{task_id}` --- update a task
> -   `DELETE /tasks/{task_id}` --- delete a task
>
> Each task should contain only:
>
> -   `id` --- integer
> -   `title` --- string
> -   `description` --- string
> -   `completed` --- boolean
>
> Generate unique incrementing integer IDs for new tasks.
>
> Do not add PATCH, filtering, search, pagination, authentication, a
> database, UUIDs, or other features outside this scope.
>
> **Output:** Return a complete, readable `main.py` file first, followed
> by the commands needed to install, run, and test it.
>
> **Verification:** Before considering the solution complete, check
> that:
>
> -   all five endpoints are implemented;
> -   POST returns `201 Created`;
> -   GET, PUT, and DELETE return `404 Not Found` for a nonexistent
>     task;
> -   new tasks receive unique incrementing IDs.
>
> Do not claim that you ran or verified the code unless you actually
> did. If you cannot run the code, clearly say that and provide the
> tests someone should run instead.

------------------------------------------------------------------------

# 13. Final Reflection

This exercise changed how I think about prompting.

My initial prompt was only:

> "Write backend code for a CRUD API."

That left almost everything open, so the model filled the gaps with its
own assumptions.

By changing one ingredient at a time, I could see what each layer
actually contributed.

The most useful progression was:

**Goal → Context → Format → Constraints → Verification**

The most important discovery was that **constraints had a larger effect
on the actual usefulness of the code than simply asking for a better
format**. The output-format layer made the answer easier to consume, but
the constraints were what finally stopped the model from building
features I did not need.

The verification layer then made the final result more trustworthy by
focusing attention on the behaviors that actually mattered.

The final prompt is therefore not just "more detailed." Each part has a
specific job:

-   **Goal** says what I am building.
-   **Context** says where it fits.
-   **Format** says how I want the answer delivered.
-   **Constraints** define the boundaries.
-   **Verification** defines what must be true before the answer is
    considered complete.

