---
description: Update the Public APIs documentation at docs/source/01-Public-APIs/index.rst
argument-hint: ""
allowed-tools: ["Read", "Edit", "Grep", "Glob"]
---

Update the Public APIs documentation at docs/source/01-Public-APIs/index.rst

Follow these instructions:

1. Read docs/source/01-Public-APIs/index.rst to learn the format and structure examples
2. Examine tests/test_api.py to identify all public APIs (those referenced with `_ = api.ClassName` or `_ = api.ClassName.method_name`)
3. Review source code implementation files to understand what each API does
4. Organize APIs into logical categories (Core Classes, Data Containers, Repository Information, Commit Operations, Tag Operations, Release Operations, Utilities)
5. Write one-line descriptions for each API focusing on what it does, not how it works
6. Use proper Sphinx cross-reference syntax (:class:, :meth:, :attr:) with full module paths
7. Maintain the categorized structure for better readability