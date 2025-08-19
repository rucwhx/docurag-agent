# DocuRAG Agent

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A modern, production-ready document-based RAG (Retrieval-Augmented Generation) system for intelligent question answering. Built with Python 3.9+ and modern tooling.

## ✨ Features

- 🔍 **Advanced Retrieval**: Multiple retrieval strategies including dense, sparse, and hybrid search
- 🧠 **Intelligent Reranking**: Cross-encoder models for improved relevance
- 🔄 **Query Rewriting**: HyDE (Hypothetical Document Embeddings) for better retrieval
- 📊 **Comprehensive Evaluation**: Built-in metrics for retrieval and QA performance
- 🚀 **Production Ready**: FastAPI backend with Gradio UI
- 🛠️ **Modern Tooling**: Uses `uv`, `ruff`, `black`, and `mypy` for development

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

#### Using uv (recommended)

```bash
# Clone the repository
git clone https://github.com/rucwhx/docurag-agent.git
cd docurag-agent

# Install with uv
uv pip install -e .

# For development
uv pip install -e ".[dev]"

# For GPU support
uv pip install -e ".[gpu]"
```

#### Using pip

```bash
git clone https://github.com/rucwhx/docurag-agent.git
cd docurag-agent

pip install -e .

# For development
pip install -e ".[dev]"
```

### Running the Application

#### Web UI (Gradio)
```bash
# Using the installed script
docurag-ui

# Or directly
python -m docurag.app.ui
```

#### API Server (FastAPI)
```bash
# Using the installed script
docurag-serve

# Or directly
python -m docurag.app.api
```

#### Basic Usage Example

```python
from docurag import make_chunks, build_index, retriever, generator

# Process documents
chunks = make_chunks("path/to/documents.csv")

# Build search index
index = build_index(chunks)

# Retrieve relevant documents
results = retriever.search("What is machine learning?", index)

# Generate answer
answer = generator.generate(query="What is machine learning?", context=results)
```

## 📁 Project Structure

```
docurag-agent/
├── src/                    # Source code
│   ├── chunk/             # Document chunking
│   ├── embed/             # Embedding & indexing
│   ├── retrieve/          # Document retrieval
│   ├── rerank/            # Result reranking
│   ├── generate/          # Answer generation
│   ├── query_rewrite/     # Query enhancement
│   └── eval/              # Evaluation metrics
├── app/                   # Web applications
│   ├── api.py            # FastAPI backend
│   └── ui.py             # Gradio frontend
├── data/                  # Sample data
├── scripts/               # Utility scripts
├── tests/                 # Test suite
├── pyproject.toml         # Project configuration
└── README.md             # This file
```

## 🛠️ Development

### Setup Development Environment

```bash
# Clone and install for development
git clone https://github.com/rucwhx/docurag-agent.git
cd docurag-agent
uv pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Code Quality Tools

We use modern Python tooling for code quality:

```bash
# Format code
black src/ app/ tests/
ruff format src/ app/ tests/

# Lint code
ruff check src/ app/ tests/

# Type checking
mypy src/ app/

# Run tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=html
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_retrieval.py

# Run with verbose output
pytest -v
```

## 📊 Evaluation

The system includes comprehensive evaluation metrics:

```bash
# Run retrieval evaluation
python -m docurag.eval.retrieval_eval

# Run QA evaluation
python -m docurag.eval.qa_eval
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Sentence Transformers](https://www.sbert.net/)
- Uses [FAISS](https://faiss.ai/) for efficient similarity search
- Powered by [Transformers](https://huggingface.co/transformers/)
- UI built with [Gradio](https://gradio.app/)
- API built with [FastAPI](https://fastapi.tiangolo.com/)

## 📈 Roadmap

- [ ] Support for more document formats (PDF, DOCX, etc.)
- [ ] Advanced query expansion techniques
- [ ] Multi-language support
- [ ] Vector database integrations (Pinecone, Weaviate, etc.)
- [ ] Cloud deployment guides
- [ ] Performance optimizations