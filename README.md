![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
# Blank-Portfolio

A modular and extensible Python package for managing personal portfolio data, with a clean CLI interface, service layers, and utilities. Supports Python 3.6+.

---

## Features

- Data models for portfolio components: skills, experiences, projects, education, certifications
- CLI for viewing and filtering portfolio data with presentable terminal output
- Layered architecture separating CLI presentation, service logic, and data provisioning
- Utilities for formatting with Rich for colored, tabular output
- Packaging and deployment automation with `uv` and GitHub Actions
- Compatible with Python 3.6 and above

---

## Installation

Install from PyPI:

```
pip install blank-portfolio
```

---

## Usage

### CLI Interface

Run the CLI tool:

```
blank-portfolio --help
```

Example: list skills filtered by type and level

```
blank-portfolio list-skills --type TOOL --level EXPERT
```

### Python API

Import and use programmatically:

```
from blank_portfolio.provider.cli import cli

# Access portfolio data via service layer
```

---

## Development

### Prerequisites

- Python 3.6+
- [uv](https://uv.io/) package manager

### Setup

Clone the repo, then:

```
uv sync
```

### Running Tests

```
uv run pytest
```

### Versioning and Publishing

Versioning is automated via [bump2version](https://github.com/c4urself/bump2version) integrated with GitHub Actions.  
Build and upload your package with:

```
uv run python -m build
uv run twine upload dist/*
```

---

## Contributing

Contributions are welcome via pull requests or issues.

---

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

## Contact

Project maintained by Shantanu Bindhani.

LinkedIn: https://linkedin.com/in/shantanubindhani  
GitHub: https://github.com/shantanubindhani