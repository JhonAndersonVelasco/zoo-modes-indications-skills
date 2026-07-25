---
name: project-tracker
description: Manage project continuity, tracking state, handoffs, and session updates across model switches or developers using a .PROJECT_STATE.md file.
modeSlugs:
  - architect
  - code
  - ask
  - debug
  - orchestrator
  - tool-writer
  - skill-writer
  - documentation-writer
---

# Project Tracker

## Instructions

### When to use this skill
- When starting any interaction with the repository or switching AI models.
- Before finalizing a work session to document progress.
- When needing to transfer the exact project state to another session.

### When NOT to use this skill
- For simple theoretical queries or highly isolated tasks that do not affect the project's code base.

### Workflow

1. **Initial State Reading**: At the start of the task, immediately check if the `.PROJECT_STATE.md` file exists at the project's root.
   - If it exists: read it with `read_file` to understand the main goal, agreed architecture, progress, and active task.
   - If it does not exist: propose its creation to the user, guided by the standard template below.

2. **Progress Update**: Whenever a milestone or backlog subtask is completed, record the progress in the "Progress Status" section of `.PROJECT_STATE.md`.

3. **Closure and Handoff**: Before ending the session or if you recommend restarting the chat to free context, update the file with:
   - The exact current development state.
   - The immediate next step and the specific files involved.
   - Pending and already agreed design decisions.

### Template of `.PROJECT_STATE.md`
This file should be kept in the root of the workspace with the following simple structure in spanish language:

```
markdown
# Estado del Proyecto

## 1. Objetivo General
- [Meta macro del proyecto expresada de forma clara y directa]

## 2. Arquitectura y Tecnologías
- [Stack tecnológico básico]
- [Reglas de modularidad y estructura de carpetas]

## 3. Estado de Avance
- [ ] Tarea 1 (Pendiente/En progreso/Completado)
- [ ] Tarea 2

## 4. Foco Actual (Próximo Paso Inmediato)
- [Detalle de la tarea que se está ejecutando justo ahora y qué archivos se están editando]

## 5. Decisiones de Diseño Acordadas
- [Registro de decisiones técnicas validadas con el usuario]
```
