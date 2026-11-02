# JSBSim Learn to Fly

A course for a Python-proficient aviation beginner, from flight vocabulary
through a Mini Plank simulation with JSBSim and Godot visualization.

## Use

1. Install Python 3.11+ and uv.
2. Create the course environment (skip creation if it already exists):

   ```bash
   uv venv .venv
   uv pip install --python .venv/bin/python -r requirements-course.txt
   ```
3. Run the site:

   ```bash
   uv run mkdocs serve
   ```

4. Validate before publishing:

   ```bash
   uv run mkdocs build --strict
   ```

## Layout

- `docs/` — MkDocs pages
- `docs/modules/` — lessons grouped by module
- `examples/` — runnable examples matching modules
- `design/` — decisions and plans that need to outlive implementation
- `.vscode/tasks.json` — build and preview tasks
- `AGENTS.md` and `CONTEXT.md` — Codex project guidance
