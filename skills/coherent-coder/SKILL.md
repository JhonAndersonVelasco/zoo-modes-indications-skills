---
name: coherent-coder
description: Write clean, modular, and cohesive code following KISS, verifying external signatures with precise tool calls and running build/test validations.
modeSlugs:
  - architect
  - code
  - debug
  - tool-writer
  - skill-writer
---

# Coherent Coder

## Files
- `scripts/verify_symbol.py`: deterministic checker for third-party library symbols. It lives inside THIS skill's own folder, wherever that was loaded from (global `~/.roo/skills/coherent-coder/` or project `<workspace>/.roo/skills/coherent-coder/`). Before executing it: resolve this skill folder's absolute path (you already know it — it's the directory containing this SKILL.md) and run `python <that_absolute_path>/scripts/verify_symbol.py <dotted.path>` via `execute_command`. Do NOT assume the shell's current working directory is this skill's folder — `execute_command` normally runs from the project root, not from here.

## Instructions

### When to use this skill
- During active implementation of any code snippet, refactoring, or bug fixing.

### When NOT to use this skill
- During pure theoretical planning phases, diagramming, or requirement gathering.

### Workflow

1. **Signature Inspection (project code)**: Before importing or interacting with existing project modules, functions, or classes, obligatorily use the `read_file` tool to inspect their exact definitions. Do not assume data types or function signatures from memory.
2. **Signature Verification (third-party libraries)**: You do not have perfect recall of every library's real API, and library APIs change between versions (e.g. `numpy.trapz` was removed and renamed to `numpy.trapezoid` in NumPy 2.0). Never write a call to a third-party symbol that "sounds right" without checking it first:
   - Trivial, unambiguous stdlib calls (`os.path.join`, `json.loads`) can proceed without a check.
   - For everything else — and ALWAYS for less common submodules/functions — run `verify_symbol.py` (see "Files" above for how to build its absolute path) via `execute_command` and confirm it prints `OK` before using that symbol in code.
   - If it prints `NOT_FOUND`, do NOT guess a second name from memory either. Inspect the real package (`python -c "import <lib>; print(dir(<lib>))"`, `pip show <lib>`, or its installed source) until you find the actual symbol, then re-verify it.
3. **KISS Philosophy (Keep It Simple, Stupid)**:
- Write direct, readable, and modular code, minimizing unnecessary abstractions or strong coupling.
- Each function or component should handle a single responsibility.
- Prioritize native language solutions before proposing additional packages.
4. **Precise Editing**: Use focused editing tools (like `apply_diff` or `edit_file` depending on your tooling) to modify only the necessary lines, avoiding accidental overwriting of surrounding code.
5. **Validation and Command Execution (CRITICAL RULE)**:
- Immediately after applying changes, run compilation commands, linters, or local tests using execute_command.
- ANTI-LOOP RULE: execute_command is a BLOCKING action. Once you send a command, you MUST wait for its output.
- If a command takes longer than expected (e.g., npm install, running heavy tests, docker builds), DO NOT open a new terminal, DO NOT re-run the command, and DO NOT panic.
- If you receive a timeout error or no output after a while, simply inform the user: "El comando está tardando más de lo habitual. ¿Deseas que espere, lo ejecutamos en segundo plano o lo cancelamos?".
- NEVER execute the exact same execute_command twice in a row without an explicit instruction from the user. Duplicate executions are strictly forbidden.
- A validation run that raises ImportError or AttributeError on a third-party symbol is NOT "done" — it means step 2 was skipped. Go back to step 2 instead of patching it with a second guess.
