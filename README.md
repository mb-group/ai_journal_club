# AI Journal Club

Welcome to the AI Journal Club project! This is a Jupyter Book containing resources and discussions for our AI journal club.

## Setup

### Prerequisites
Make sure you have access to the conda module on the system:
```bash
module load conda3/202402
```

### Environment Setup
This project uses a conda environment with all necessary dependencies. To set up and activate the environment:

1. Create the conda environment (if not already created):
```bash
conda create -n ai_journal_club python=3.9 jupyter-book matplotlib numpy -y
```

2. Activate the environment:
```bash
conda activate ai_journal_club
```

### Building the Book
Once the environment is activated, you can build the Jupyter Book:
```bash
jupyter-book build .
```

### Deactivating the Environment
When you're done working, you can deactivate the environment:
```bash
conda deactivate
```

## Project Structure
- `_config.yml` - Configuration file for the Jupyter Book
- `_toc.yml` - Table of contents structure
- `requirements.txt` - Python package dependencies
- `intro.md` - Introduction page
- `protein_book.md` - Protein-related content
- `selection_criteria.md` - Selection criteria documentation
- Various other markdown files and notebooks

## Contributing
Please ensure you're working in the correct conda environment before making any changes or running the book build process.