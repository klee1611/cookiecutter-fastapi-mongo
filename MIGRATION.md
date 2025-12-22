# Migration Guide: Poetry to uv

This project has been migrated from Poetry to uv for faster and more modern Python package management.

## What Changed

### For New Projects
- **Poetry** → **uv**: All dependency management now uses uv
- `poetry install` → `uv sync`
- `poetry run` → `uv run`
- `poetry.lock` → `uv.lock`
- `pyproject.toml` updated to use standard PEP 621 format

### Key Benefits of uv
- ⚡ **10-100x faster** than Poetry
- 🐍 **Python version management** built-in
- 📦 **Modern** - follows latest Python packaging standards (PEP 621)
- 🔒 **Compatible** - works with standard `pyproject.toml`

## For New Users

### Prerequisites
Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Creating a New Project
```bash
cookiecutter gh:klee1611/cookiecutter-fastapi-mongo
```

The post-generation hook will automatically run `uv sync` to install dependencies.

### Common Commands
```bash
# Install dependencies
uv sync

# Install with dev dependencies
uv sync --all-extras

# Run tests
make test
# or
uv run pytest -s -vv

# Run development server
make dev
# or
uv run gunicorn -k uvicorn.workers.UvicornWorker --reload --bind 0.0.0.0:8888 -w 1 app.server:app

# Add a new dependency
uv add fastapi

# Add a dev dependency
uv add --dev pytest

# Update dependencies
uv lock --upgrade
```

## For Existing Projects

If you have an existing project created with the old Poetry template:

### Option 1: Start Fresh (Recommended)
1. Create a new project with the updated template
2. Copy your custom code (`app/` directory content)
3. Copy your `.env` configuration

### Option 2: Manual Migration
1. Install uv:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Update `pyproject.toml` to PEP 621 format (see template for reference)

3. Create `.python-version` file:
   ```bash
   echo "3.10" > .python-version
   ```

4. Remove Poetry files:
   ```bash
   rm poetry.lock
   ```

5. Initialize uv:
   ```bash
   uv sync --all-extras
   ```

6. Update Makefile commands:
   - Replace `poetry run` with `uv run`

7. Update Dockerfile:
   - Replace Poetry installation with uv
   - Replace `poetry export` with `uv export`

8. Test everything:
   ```bash
   make test
   make dev
   ```

## Troubleshooting

### "uv: command not found"
Install uv using the installation script:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Then restart your shell or source the configuration file.

### Dependencies not installing
Make sure you're in the project directory with `pyproject.toml` and run:
```bash
uv sync --all-extras
```

### Python version issues
uv will automatically manage Python versions. The `.python-version` file specifies Python 3.10.
If you need a different version:
```bash
echo "3.11" > .python-version
uv sync
```

## Resources

- [uv Documentation](https://docs.astral.sh/uv/)
- [uv GitHub Repository](https://github.com/astral-sh/uv)
- [PEP 621 - Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/)
