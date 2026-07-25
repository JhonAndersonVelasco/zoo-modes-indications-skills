---
name: context-optimizer
description: Manage local context limits, prevent token bloat, filter paths with .rooignore, and perform targeted file reads to preserve model attention.
---

# When to use this skill
- In medium to large projects where code exploration could unnecessarily saturate the context.
- When performing searches or reads throughout the repository.

# When NOT to use this skill
- In small repositories (fewer than 15 files) where all code comfortably fits in context without affecting the AI's reasoning.

# Workflow

1. **Focused Reading**:
- Avoid reading entire files if you only need a specific class or function. Use searches or range‑line reads whenever possible.
- Do not list deep directories recursively. Use semantic or pattern‑based searches (`search_files`) to locate specific files.
2. **Maintain .rooignore**:
- Ensure the `.rooignore` file at the project root is configured to ignore dependency folders (`node_modules`), compiled outputs (`dist`, `build`, `out`), version control (`.git`), or heavy test databases. This prevents model searches from being flooded with irrelevant results.
3. **Context Cleanup Cycle**:
- If you notice the conversation becoming very long, redundant, or containing massive console logs, update `.PROJECT_STATE.md` to consolidate the current state.
- Suggest the user start a fresh clean chat thread and load only `.PROJECT_STATE.md` to free the local model's context window without losing project progress.