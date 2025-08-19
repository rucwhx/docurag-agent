"""Test configuration and fixtures."""

import pytest
import tempfile
import os
from pathlib import Path


@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_documents():
    """Sample documents for testing."""
    return [
        "Machine learning is a subset of artificial intelligence.",
        "Deep learning uses neural networks with multiple layers.",
        "Natural language processing deals with text and speech.",
        "Computer vision focuses on image and video analysis.",
    ]


@pytest.fixture
def sample_queries():
    """Sample queries for testing."""
    return [
        "What is machine learning?",
        "How do neural networks work?",
        "What is NLP?",
    ]
