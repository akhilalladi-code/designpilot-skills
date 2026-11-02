# AI agent compatibility

DesignPilot Skills is written in plain Markdown so its workflows can be adapted to different AI coding assistants. This guide explains practical ways to reference the skills without claiming that every agent automatically discovers or executes them.

> **Compatibility note:** These are integration patterns based on each tool's documented instruction mechanisms. The DesignPilot repository does not currently include automated end-to-end tests against these assistants. Check the latest official documentation for supported file locations and behavior.

## Shared setup

1. Clone or download this repository.
2. Keep the `skills/` directory in your project, or copy only the skill files you need.
3. Add a short instruction telling the assistant when and how to consult the selected skill.
4. Give it a real brief, approved assets, dimensions, and constraints.
5. Review the output against the skill's quality checklist.

A useful shared instruction is:

```text
For design-related tasks, first identify the most relevant DesignPilot
skill in ./designpilot-skills/skills/.

Read that SKILL.md file and follow its workflow, quality checklist,
output format, and guardrails. If more than one skill is relevant,
combine them without duplicating steps.

Ask for essential missing information. Never invent brand rules,
product claims, credentials, testimonials, or factual specifications.
Explain important design decisions and identify what needs human review.
```

Adjust the relative path if you store the repository elsewhere.

## Claude Code

Claude Code supports project-level instructions through a `CLAUDE.md` file.

1. Place this repository inside your project, for example at `./designpilot-skills/`.
2. Add the shared setup instruction above to your project's `CLAUDE.md`.
3. In a task prompt, name the skill you want Claude to read.

Example:

```text
Read ./designpilot-skills/skills/brand-identity/SKILL.md and
./designpilot-skills/skills/color-systems/SKILL.md.

Use those workflows to propose a brand direction for the project.
Start with the brief and rationale before suggesting visual execution.
```

Official documentation: [Claude Code memory and project instructions](https://docs.anthropic.com/en/docs/claude-code/memory).

## Cursor

Cursor supports project rules in its rules system. A project-level rule can tell Cursor where the DesignPilot files are and when to consult them.

1. Keep the repository in your project workspace.
2. Create or update a project rule using the current Cursor-supported rules interface.
3. Add the shared setup instruction above.
4. Explicitly reference the relevant skill in the task prompt when precision matters.

Example task:

```text
Before working on this social campaign, read
./designpilot-skills/skills/social-media-design/SKILL.md
and ./designpilot-skills/skills/typography/SKILL.md.

Return a creative specification and checklist before implementation.
```

Official documentation: [Cursor Rules](https://docs.cursor.com/context/rules).

## GitHub Copilot

GitHub Copilot supports repository custom instructions and, in supported environments, path-specific instructions.

1. Keep the DesignPilot repository available in the workspace.
2. Add the shared setup instruction to the Copilot instructions file supported by your environment.
3. In Copilot Chat, specify the skill path for the task.
4. Confirm that the assistant has access to the repository files in the current environment.

Example task:

```text
Use ./designpilot-skills/skills/poster-design/SKILL.md to plan this poster.
Follow the skill's workflow and output format. Do not invent missing
event information. Provide print checks and flag details that need confirmation.
```

Official documentation: [GitHub Copilot repository custom instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions).

## Troubleshooting

| Problem | What to check |
|---|---|
| Assistant ignores a skill | Reference the exact `SKILL.md` path in the task prompt |
| Assistant cannot find the file | Confirm the repository is in the active workspace and the relative path is correct |
| Instructions are too broad | Select one primary skill and only add secondary skills when needed |
| Output is generic | Supply audience, objective, approved references, copy, dimensions, and constraints |
| Output invents facts | Require placeholders for missing facts and verify all claims before publishing |

## Compatibility contributions

If you verify a workflow with a specific assistant version, please contribute:

- Assistant and version tested
- Operating environment and project setup
- Exact instruction file and location used
- A minimal reproducible prompt
- What worked, what failed, and any limitations

Do not describe an integration as tested unless you have actually tested it.
