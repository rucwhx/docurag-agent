#!/usr/bin/env bash
set -e


python -m src.chunk.make_chunks --input data/docs.csv --output data/chunks.parquet \
--chunk_size 800 --chunk_overlap 200


python -m src.embed.build_index --chunks data/chunks.parquet --faiss index/faiss.index \
--meta index/meta.parquet --model BAAI/bge-small-zh-v1.5


python -m app.ui --config config.yaml