"""DocuRAG Agent - A document-based RAG system for intelligent question answering."""

__version__ = "0.1.0"
__author__ = "rucwhx"
__email__ = "your-email@example.com"

from .chunk import make_chunks
from .embed import build_index
from .retrieve import retriever
from .rerank import reranker
from .generate import generator
from .query_rewrite import hyde

__all__ = [
    "make_chunks",
    "build_index", 
    "retriever",
    "reranker",
    "generator",
    "hyde",
]
