---
title: Excluding Files with .readmeaiignore
description: Step-by-step guide to create custom ignore patterns for your project.
---

# Excluding Files with .readmeaiignore

This guide shows you how to exclude specific files and directories from ReadmeAI analysis using a `.readmeaiignore` file.

## Quick Start

1. **Create the ignore file** in your repository root:
   ```bash
   touch .readmeaiignore
   ```

2. **Add patterns** for files to exclude:
   ```text
   # Exclude all log files
   *.log

   # Exclude secrets directory
   secrets/

   # Exclude specific file
   config/database.yaml
   ```

3. **Run ReadmeAI** as normal - it will automatically detect and use your ignore file.

## Common Use Cases

### Exclude Sensitive Files

```text
# Environment files
.env
.env.local
.env.production

# Configuration with secrets
config/secrets.yaml
private/

# Database files
*.db
*.sqlite
```

### Exclude Development Files

```text
# IDE settings
.vscode/settings.json
.idea/workspace.xml

# OS files
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.cache
temp/
```

### Exclude Large Data Files

```text
# Data directories
data/
datasets/
models/

# Media files
*.mp4
*.avi
images/raw/

# Archive files
*.zip
*.tar.gz
```

### Include Important Files

Use `!` to include files that would otherwise be excluded:

```text
# Exclude all logs
*.log

# But include the important one
!important.log

# Exclude entire directory
docs/generated/

# But include examples
!docs/generated/examples/
```

## Testing Your Patterns

To verify your ignore patterns work correctly:

1. **Run ReadmeAI** on your repository
2. **Check the generated README** for unwanted file references
3. **Adjust patterns** as needed

The system will log when it finds your `.readmeaiignore` file:

```text
INFO     Found .readmeaiignore file: /path/to/repo/.readmeaiignore
```

## Pattern Examples by Language

### Python Projects

```text
# Virtual environments
venv/
env/
.venv/

# Jupyter checkpoints
.ipynb_checkpoints/

# Coverage reports
htmlcov/
.coverage

# Distribution
dist/
build/
*.egg-info/
```

### JavaScript/Node.js

```text
# Dependencies
node_modules/

# Build outputs
dist/
build/

# Environment files
.env.local
.env.production

# Cache directories
.cache/
.parcel-cache/
```

### Documentation Projects

```text
# Generated docs
_site/
site/
_build/

# Temporary files
*.swp
*.swo

# OS files
.DS_Store
```

## Advanced Patterns

### Recursive Exclusion

```text
# Exclude all node_modules anywhere
**/node_modules/

# Exclude all .cache directories
**/.cache/

# Exclude all test files
**/test_*.py
```

### Conditional Inclusion

```text
# Exclude all config files
config/*

# But include the template
!config/template.yaml

# And include the public configs
!config/public/
```

## Troubleshooting

**Problem**: Files still being analyzed despite ignore patterns

**Solutions**:
- Check file path case sensitivity
- Verify pattern syntax (use forward slashes)
- Test with simpler patterns first
- Check the ignore file is in repository root

**Problem**: Important files being excluded

**Solutions**:
- Add negation patterns with `!`
- Review default exclusions in [ignore patterns concepts](../../concepts/advanced/ignore-patterns.md)
- Be more specific with your exclusion patterns
