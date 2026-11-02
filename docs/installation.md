# Installation and usage

DesignPilot Skills is a collection of plain Markdown instructions. You can use the files with an AI coding agent or creative assistant that can read project instructions or reference files.

There is no package manager or automatic installer yet. The reliable, tool-agnostic method is to copy the skill you need into your assistant's supported instruction location, or provide the file as context in a conversation.

## 1. Choose a skill

Browse the [skill library](../skills/) and select the workflow that matches your task.

| Goal | Skill |
|---|---|
| Create or refine a brand identity | [Brand identity](../skills/brand-identity/SKILL.md) |
| Build a type hierarchy | [Typography](../skills/typography/SKILL.md) |
| Develop a usable palette | [Color systems](../skills/color-systems/SKILL.md) |
| Plan social media creative | [Social media design](../skills/social-media-design/SKILL.md) |
| Plan a print or digital poster | [Poster design](../skills/poster-design/SKILL.md) |
| Review an existing design | [Design critique](../skills/design-critique/SKILL.md) |
| Research visual references | [Design research](../skills/design-research/SKILL.md) |
| Avoid generic AI design output | [Anti-generic design](../skills/anti-generic-design/SKILL.md) |

## 2. Add the skill to your workflow

Choose the method supported by your assistant:

### Method A — Reference the file in your project

1. Download or clone this repository.
2. Keep the `skills/` directory in your project.
3. In your assistant's project instructions, tell it which skill file to read before starting the relevant task.
4. Include the actual brief, audience, deliverables, dimensions, brand rules, and constraints.

Example project instruction:

```text
For graphic design tasks, consult the relevant DesignPilot Skills
Markdown file in ./designpilot-skills/skills/ before proposing a solution.

Choose the most relevant skill for the task. Follow its workflow,
quality checklist, output format, and guardrails. If information is
missing, ask rather than inventing facts or brand requirements.
```

### Method B — Paste a skill into the conversation

1. Open the required `SKILL.md` file on GitHub.
2. Copy its contents or attach the Markdown file to your assistant.
3. Ask the assistant to follow that skill for the task.
4. Provide your brief and reference assets.

This method works well when you cannot configure project-level instructions.

### Method C — Adapt it to an agent-specific skills format

Some agents support dedicated skills directories, project rules, or custom instruction files. If yours does, place the selected skill in the location and format documented by that agent.

Keep the original DesignPilot file as the source of truth. Do not assume that every assistant uses the same directory structure or automatically discovers Markdown files.

## 3. Example task prompt

```text
Read and follow the DesignPilot social media design skill.

Project: Product launch announcement
Audience: [describe the audience]
Platform and dimensions: [specify]
Main message: [provide approved copy]
Brand rules: [colors, fonts, logo and imagery]
Required information: [list]
Restrictions: [list]

First explain the audience, message hierarchy, and proposed layout.
Then provide the creative specification and quality checklist.

Do not invent product claims, statistics, testimonials, or brand rules.
Ask questions when essential information is missing.
```

## 4. Keep the library updated

When you want the latest workflows, pull the latest repository changes or download the current files from GitHub. Review changes before replacing any customized local copies.

## Important notes

- DesignPilot Skills provides instructions, not a design-rendering application.
- Outputs depend on the capabilities of the AI assistant and the quality of the brief.
- Always review generated work for accuracy, accessibility, licensing, brand consistency, and production readiness.
- Follow the documentation and security guidance of the AI tool you use.
