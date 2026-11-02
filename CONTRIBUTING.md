# Contributing to DesignPilot Skills

Thank you for helping make practical design knowledge easier to use with AI tools.

## What makes a good contribution?

A useful skill is:
- Focused on one clear design task.
- Written as actionable instructions, not a generic essay.
- Tool-agnostic unless a tool-specific skill is clearly labelled.
- Grounded in a real brief, audience, and production context.
- Honest about assumptions, uncertainty, and verification needs.
- Respectful of accessibility, copyright, trademarks, and cultural context.

## Before opening a pull request

1. Search existing skills to avoid duplication.
2. Open an issue for substantial new directions or structural changes.
3. Use the existing skill structure: YAML frontmatter, objective, inputs, workflow, quality checklist, output format, and guardrails.
4. Keep examples fictional or clearly marked as illustrative.
5. Do not include confidential client material, personal data, unlicensed assets, or generated claims presented as facts.
6. Run the validator: `python scripts/validate_skills.py`.

## Skill frontmatter

Every skill must begin with:

```yaml
---
name: short-kebab-case-name
description: A concise description of when the skill should be used.
---
```

The `name` must match its containing directory.

## Pull request checklist

- [ ] The change solves a clear user problem.
- [ ] The skill has specific, ordered steps.
- [ ] Assumptions and required inputs are clear.
- [ ] Quality checks are actionable.
- [ ] Safety, accessibility, and rights considerations are included where relevant.
- [ ] Links and examples are valid.
- [ ] The validator passes.

By contributing, you agree that your contribution is provided under the repository's MIT license.