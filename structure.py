import os
from pathlib import Path

list_of_files = [
    "src/__init__.py",
    "src/data_scraper/__init__.py",
    "src/data_scraper/google_reviews.py",
    "src/data_scraper/tripadvisor_reviews.py",
    "src/image_processor/__init__.py",
    "src/image_processor/menu_ocr.py",
    "src/rag_pipeline/__init__.py",
    "src/rag_pipeline/retriever.py",
    "src/rag_pipeline/vector_store.py",
    "src/llm/__init__.py",
    "src/llm/simple_llm.py",
    "src/api/__init__.py",
    "src/api/fastapi_app.py",
    "src/api/endpoints.py",
    "src/utils/__init__.py",
    "src/utils/config.py",
    "src/utils/logging.py",
    "src/utils/exceptions.py",
    "src/utils.py",
    "tests/__init__.py",
    "tests/test_data_scraper.py",
    "tests/test_image_processor.py",
    "tests/test_rag_pipeline.py",
    "tests/test_llm.py",
    "configs/config.yaml",
    "configs/secrets.yaml",
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/vector_store/.gitkeep",
    "scripts/run_scraper.py",
    "scripts/process_images.py",
    "scripts/train_rag.py",
    "requirements.txt",
    "README.md",
    ".gitignore",
    "main.py",
    "Dockerfile",
    ".dockerignore",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")