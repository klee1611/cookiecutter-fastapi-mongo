#!/usr/bin/env bash

# Restore project metadata in pyproject.toml.
# The template uses valid placeholder values ("app", "0.1.0") so that
# Dependabot can parse the file. Cookiecutter renders its variables inside
# this hook before execution, so the replacements below produce real values.
python3 - <<'PYEOF'
with open("pyproject.toml", "r") as f:
    content = f.read()
content = content.replace('name = "app"', 'name = "{{cookiecutter.app_name}}"', 1)
content = content.replace('version = "0.1.0"', 'version = "{{cookiecutter.app_version}}"', 1)
with open("pyproject.toml", "w") as f:
    f.write(content)
PYEOF

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "⚠️  uv is not installed. Please install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo ""
    echo "After installing uv, run:"
    echo "   uv sync --all-extras"
else
    # Initialize uv project and install dependencies
    echo "Installing dependencies with uv..."
    uv sync --all-extras
fi

# Move environment sample
mv env.sample .env

echo ""
echo "✅ Project created successfully!"
echo ""
if ! command -v uv &> /dev/null; then
    echo "Next steps:"
    echo "1. Install uv: curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "2. Run: uv sync --all-extras"
    echo "3. Edit .env file"
    echo "4. Run: make test"
else
    echo "Next steps:"
    echo "1. Edit .env file"
    echo "2. Run: make test"
fi
