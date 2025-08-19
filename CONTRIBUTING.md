# Contributing to DocuRAG Agent

Thank you for your interest in contributing to DocuRAG Agent! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- [uv](https://docs.astral.sh/uv/) (recommended package manager)
- Git

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/docurag-agent.git
   cd docurag-agent
   ```

2. **Install uv (if not already installed)**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install dependencies**
   ```bash
   uv sync --all-extras --dev
   ```

4. **Install pre-commit hooks**
   ```bash
   uv run pre-commit install
   ```

## 🛠️ Development Workflow

### Code Quality

We use modern Python tooling to maintain code quality:

- **Ruff**: For linting and formatting
- **Black**: Code formatting (via ruff)
- **MyPy**: Type checking
- **Pre-commit**: Automated checks

### Running Quality Checks

```bash
# Lint and format
uv run ruff check .
uv run ruff format .

# Type checking
uv run mypy src/ app/

# Run all pre-commit hooks
uv run pre-commit run --all-files
```

### Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=html

# Run specific test
uv run pytest tests/test_specific.py
```

## 📝 Coding Standards

### Python Code Style

- Follow PEP 8 (enforced by ruff)
- Use type hints for all function signatures
- Write descriptive docstrings for public functions and classes
- Maximum line length: 88 characters

### Example Function

```python
def process_documents(
    documents: List[str], 
    chunk_size: int = 512
) -> List[DocumentChunk]:
    """Process documents into chunks.
    
    Args:
        documents: List of document texts
        chunk_size: Maximum size of each chunk
        
    Returns:
        List of processed document chunks
        
    Raises:
        ValueError: If chunk_size is invalid
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    
    # Implementation here
    return chunks
```

### Commit Messages

Use conventional commits format:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Maintenance tasks

Examples:
```
feat(retrieval): add hybrid search capability
fix(api): handle empty query responses
docs(readme): update installation instructions
```

## 🧪 Testing Guidelines

### Test Structure

- Place tests in the `tests/` directory
- Mirror the `src/` structure in `tests/`
- Use descriptive test names
- Include unit, integration, and end-to-end tests

### Test Example

```python
import pytest
from docurag.retrieve import Retriever

class TestRetriever:
    @pytest.fixture
    def sample_documents(self):
        return ["Document 1 content", "Document 2 content"]
    
    def test_retriever_initialization(self):
        """Test that retriever initializes correctly."""
        retriever = Retriever()
        assert retriever is not None
    
    def test_search_returns_results(self, sample_documents):
        """Test that search returns relevant results."""
        retriever = Retriever()
        retriever.index_documents(sample_documents)
        
        results = retriever.search("content")
        assert len(results) > 0
        assert all(isinstance(r, dict) for r in results)
```

## 📋 Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code following our standards
   - Add tests for new functionality
   - Update documentation if needed

3. **Run quality checks**
   ```bash
   uv run pre-commit run --all-files
   uv run pytest
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat(scope): add your feature"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Fill out PR template**
   - Describe your changes
   - Link related issues
   - Confirm all checks pass

## 🐛 Bug Reports

When reporting bugs, please include:

- **Environment**: Python version, OS, package versions
- **Steps to reproduce**: Minimal code example
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Error messages**: Full traceback if applicable

## 💡 Feature Requests

For feature requests:

- Check existing issues first
- Describe the use case clearly
- Explain why it would be valuable
- Consider implementation approaches

## 📚 Documentation

- Update docstrings for new/changed functions
- Add examples for new features
- Update README if needed
- Consider adding tutorials for complex features

## 🔧 Architecture Guidelines

### Module Organization

- Keep modules focused and cohesive
- Use clear, descriptive names
- Minimize dependencies between modules
- Follow the existing structure

### Performance Considerations

- Profile code for performance bottlenecks
- Use appropriate data structures
- Consider memory usage for large datasets
- Add performance tests for critical paths

## 🤝 Community

- Be respectful and inclusive
- Help others in discussions
- Share knowledge and best practices
- Follow our code of conduct

## 📞 Getting Help

- Open an issue for bugs or questions
- Start a discussion for design questions
- Check existing documentation first
- Be patient and descriptive in your requests

Thank you for contributing to DocuRAG Agent! 🎉
