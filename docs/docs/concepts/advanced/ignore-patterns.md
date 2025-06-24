---
title: Ignore Patterns
description: Understanding how ReadmeAI filters files and how to customize file exclusion patterns.
---

# Ignore Patterns

ReadmeAI automatically excludes certain files and directories from analysis to focus on relevant code and documentation. This system works on two levels: built-in defaults and user-customizable patterns.

## How File Filtering Works

ReadmeAI uses a two-tier filtering system:

1. **Default Filters**: Built-in patterns that exclude common non-essential files
2. **Custom Patterns**: User-defined patterns in `.readmeaiignore` files

### Default Exclusions

ReadmeAI automatically ignores:

- **Development artifacts**: `__pycache__/`, `.pytest_cache/`, `node_modules/`
- **Build outputs**: `dist/`, `build/`, `.tox/`
- **Version control**: `.git/`, `.svn/`, `.hg/`
- **IDE files**: `.vscode/`, `.idea/`
- **Binary files**: `*.exe`, `*.dll`, `*.so`, `*.dylib`
- **Media files**: `*.jpg`, `*.png`, `*.mp4`, `*.gif`
- **Archive files**: `*.zip`, `*.tar`, `*.gz`

### Custom Ignore Patterns

You can override or extend the default behavior by creating a `.readmeaiignore` file in your repository root. This file follows gitignore-style syntax:

```text
# Comments start with #
# Ignore specific files
config/secrets.yaml
.env.local

# Ignore by extension
*.cache
*.tmp

# Ignore directories (trailing slash)
logs/
temp/

# Global patterns (recursive)
**/node_modules/
**/*.log

# Negation patterns (include despite other rules)
!important.log
!docs/examples/
```

## Pattern Syntax

ReadmeAI supports gitignore-style patterns:

| Pattern | Description | Example |
|---------|-------------|---------|
| `filename.ext` | Exact filename match | `config.yaml` |
| `*.ext` | All files with extension | `*.log` |
| `directory/` | Directory and contents | `temp/` |
| `**/pattern` | Recursive match | `**/cache/` |
| `pattern/**` | All files under directory | `logs/**` |
| `!pattern` | Negation (include) | `!important.log` |
| `/pattern` | Root-level only | `/config.yaml` |

## Precedence Rules

When multiple patterns could apply to a file:

1. **Custom patterns** take precedence over default patterns
2. **Negation patterns** (`!pattern`) override exclusion patterns
3. **More specific patterns** override general patterns
4. **Later patterns** in the file override earlier ones

## Why This Approach?

This filtering system serves several purposes:

- **Performance**: Analyzing fewer files means faster README generation
- **Relevance**: Focus on source code and documentation, not artifacts
- **Security**: Avoid accidentally including sensitive files in analysis
- **Customization**: Project-specific needs through `.readmeaiignore`

---
