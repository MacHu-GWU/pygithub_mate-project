Project Specific Guide:

See @README.rst for project overview

Code Structure

- Source Code: pygithub_mate/**/*.py
- Unit test: tests/**/*.py
- Documentation: docs/source/**/*.index

Additional Python Best Practices Used in this Project:

- Virtual Environment Setup: @~/.claude/claude-markdown/pywf-open-source-Python-virtual-environment-setup-instruction-CLAUDE.md
- Test Strategy: @~/.claude/claude-markdown/pywf-open-source-Python-test-strategy-instruction-CLAUDE.md
- Python docstring Guide: @~/.claude/claude-markdown/pywf-open-source-Python-docstring-guide-CLAUDE.md
- Cross Reference API Doc Guide: @~/.claude/claude-markdown/pywf-open-source-Python-cross-reference-api-doc-guide-CLAUDE.md
- Document Structure Guide: @~/.claude/claude-markdown/pywf-open-source-Python-documentation-structure-guide-CLAUDE.md

Design Patterns:

- Pythonic API Wrapper: @.claude/Pythonic-API-developer-instruction-CLAUDE.md

Logging Guidelines:

**When to Add Logging:**

- Do NOT add logging to methods that are simple API call wrappers
- DO add logging to methods that involve multi-step decision-making workflows based on conditions
- For complex workflow methods, the first log message should typically follow the pattern: "--- ${description of what this function does}"

**Examples:**
- Simple API wrapper (no logging): `get_git_tag_and_ref()`, `delete_tag()`, `create_tag_on_commit()`
- Complex workflow (with logging): `put_tag_on_commit()`, `put_release()` - these involve checking conditions, making decisions, and performing different actions based on the results

This approach keeps logs focused on meaningful workflow steps while avoiding noise from simple operations.

**Documentation Generation:**

Use `/update-public-apis` slash command to regenerate the Public APIs documentation at docs/source/01-Public-APIs/index.rst
