# DesignPilot Skills

A practical, open-source library of reusable design workflows for AI coding agents and creative assistants.

DesignPilot Skills turns experienced design practice into clear, repeatable instructions that an AI agent can follow when helping with brand systems, typography, color, social content, posters, design critique, and visual research.

> **Status:** Early-stage project. Skills are being developed and validated; review each output before using it in production.

## Why this exists

AI can generate visual assets quickly, but speed alone does not create good design. Strong work still depends on hierarchy, contrast, consistency, audience, accessibility, production constraints, and a clear brief.

This project provides focused skill files that help an AI assistant reason through those decisions instead of jumping straight to decoration.

## Skill library

| Skill | What it helps with | Status |
|---|---|---|
| [Brand identity](skills/brand-identity/SKILL.md) | Positioning, identity direction, logo-system planning, and brand consistency | Available |
| [Typography](skills/typography/SKILL.md) | Type pairing, hierarchy, readability, and responsive type systems | Available |
| [Color systems](skills/color-systems/SKILL.md) | Palette construction, contrast, semantic roles, and accessible color use | Available |
| [Social media design](skills/social-media-design/SKILL.md) | Platform-aware creative briefs, layouts, and export checks | Available |
| [Poster design](skills/poster-design/SKILL.md) | Message hierarchy, composition, and print-ready poster planning | Available |
| [Design critique](skills/design-critique/SKILL.md) | Structured, actionable visual review | Available |
| [Design research](skills/design-research/SKILL.md) | Reference gathering, source evaluation, and visual direction | Available |
| [Anti-generic design](skills/anti-generic-design/SKILL.md) | Avoiding repetitive, template-like AI design decisions | Available |

## AI agent compatibility

See the [AI agent compatibility guide](docs/agent-compatibility.md) for setup patterns for Claude Code, Cursor, and GitHub Copilot. These are documented integration patterns, not claims of automated end-to-end testing.

## Installation

Read the [installation and usage guide](docs/installation.md) to add DesignPilot Skills to your AI assistant's workflow. It covers project-level references, conversation-based use, and adapting skills to agent-specific formats.

## Quick start

1. Open the skill you need in the `skills/` directory.
2. Copy its contents into your AI coding agent's skill or instruction workflow.
3. Give the agent your brief, audience, format, constraints, and references.
4. Ask it to follow the skill and explain important design decisions.
5. Review the result for accuracy, accessibility, licensing, and production readiness.

These files are plain Markdown and can be adapted to different AI assistants and workflows. They are not tied to one vendor.

## Example prompt

```text
Use the DesignPilot social media design skill.

Create a square launch announcement for [brand/product].
Audience: [audience]
Primary message: [message]
Platform: Instagram
Brand colors and fonts: [details]
Required content: [details]
Avoid: generic stock-style layouts, unreadable text, unsupported claims.

First propose the visual hierarchy and layout direction. Then produce the creative specification and a final quality checklist.
```

## Case studies

Explore [illustrative before-and-after design case studies](docs/case-studies.md) showing how structured skills improve solar launch announcements and event poster briefs. These are teaching examples, not claimed client work.

## Practical examples

See [Practical examples](examples/README.md) for ready-to-adapt workflows covering a solar product launch, starter brand identity, event poster planning, and structured design critique.

## Principles

- **Brief before visuals:** clarify the audience, message, objective, and constraints.
- **Hierarchy over decoration:** make the most important information easiest to understand.
- **Distinctive, not random:** use references and brand context to create a coherent visual direction.
- **Accessible by default:** consider contrast, legibility, and inclusive communication.
- **Production-aware:** account for dimensions, bleed, safe areas, export formats, and platform constraints.
- **Honest AI assistance:** do not invent facts, credentials, testimonials, or brand claims.
- **Human review:** treat generated concepts as drafts that need professional judgment.

## Repository structure

```text
designpilot-skills/
├── skills/
│   ├── anti-generic-design/
│   ├── brand-identity/
│   ├── color-systems/
│   ├── design-critique/
│   ├── design-research/
│   ├── poster-design/
│   ├── social-media-design/
│   └── typography/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── SECURITY.md
└── README.md
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for the initial release notes and future project updates.

## Contributing

Contributions are welcome: new skills, clearer workflows, examples, accessibility improvements, and corrections.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request. Keep skills tool-agnostic, specific, practical, and easy to validate.

## License

MIT. See [LICENSE](LICENSE).

---

Created and maintained by [@akhilalladi-code](https://github.com/akhilalladi-code).