---
name: design-alignment
description: Consult and align design decisions, architecture proposals, library additions, and database schemas with the user through structured proposals and iterative feedback loops.
modeSlugs:
  - architect
  - code
  - debug
  - orchestrator
---

# Design Alignment

## Instructions

### When to use this skill
- Before creating new files, folders, or structural modules.
- When suggesting or incorporating libraries or external dependencies into the project.
- When modifying public API interfaces, global types, or critical application flows.

### When NOT to use this skill
- When fixing minor cosmetic UI issues, local styles, or internal function logic that has already been agreed upon.

### Workflow

1. **Design Decision Detection**: Identify when a task requires taking a structural or integration decision.
2. **KISS Proposal Creation**: Design a minimalistic and direct proposal. It should include:
- **Proposed Solution**: What changes will be made, which files will be created/modified, and how they interact.
- **Technical Argumentation**: Why this is the simplest, cleanest, and most maintainable option for the current system.
- **Evaluated Alternative**: What other option was considered and the precise reason for its rejection.
3. **User Consultation**: Present the detailed proposal using the `ask_followup_question` tool. Stop any code editing until explicit approval is received.
4. **Counterargument Analysis**:
- If the user rejects the proposal or adds observations, analyze them objectively considering the project's technical context.
- Modify the proposal incorporating their comments, explain the new balance of pros or cons, and re‑consult until consensus is reached.
5. **Decision Record**: Once the proposal is approved, document the decision in the "Design Decisions Agreed" section of `.PROJECT_STATE.md` before writing code.
