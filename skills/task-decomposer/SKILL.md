---
name: task-decomposer
description: Break down complex goals, project plans, or refactoring tasks into a backlog of simple atomic subtasks to prevent local model disorientation
modeSlugs:
  - code
  - architect
  - orchestrator
  - debug
  - tool-writer
  - skill-writer
  - ask
---

# Task Decomposer

## Instructions

### When to use this skill
- When the user requests implementing a complex feature, a large refactor, or a brand‑new project.
- When the current task direction becomes ambiguous or spans too many files at once.

### When NOT to use this skill
- For single‑line tasks, typo fixes, or minor direct configuration changes.

### Workflow

1. **Task Breakdown**: Before modifying or creating files, split the overall goal into a list of strictly sequential and atomic tasks in a temporary file (e.g., `.roo/todo.md` or in the "Progress Status" section of `.PROJECT_STATE.md`).
2. **Atomicity Criteria**: Each individual task must satisfy:
- Focus on a single file, module, or function at a time.
- Have a clear, verifiable acceptance criterion (e.g., "Function X exported and tested").
- Be small enough for the local model to maintain focus without diluting its attention.
3. **Single‑Task Execution**:
- Resolve **ONLY** the first active task in the list.
- Implementing code for later steps in advance is prohibited.
4. **Verification and Progress**: Run tests, compilation, or linters to verify the current step's functionality before marking it as completed in the backlog and moving to the next step.
