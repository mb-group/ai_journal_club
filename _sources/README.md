# AI Journal Club

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```



Welcome to the AI Journal Club project! This is a Jupyter Book containing resources and discussions for our AI journal club. An interactive playground and zoo of AI models for exploring artificial intelligence's impact on scientific research.

## Environment Setup

### Prerequisites
Make sure you have access to the conda module on the system:
```bash
module load conda3/202402
```

### Conda Environment Setup
This project uses a conda environment with all necessary dependencies. To set up and activate the environment:

1. Create the conda environment (if not already created):
```bash
conda create -n ai_journal_club python=3.9 jupyter-book matplotlib numpy -y
```

2. Activate the environment:
```bash
conda activate ai_journal_club
```

### Alternative: pip installation
If you prefer using pip:
```bash
pip install jupyter-book matplotlib numpy
```

### Building the Book
Once the environment is activated, you can build the Jupyter Book:
```bash
jupyter-book build .
```

### Deactivating the Environment
When you're done working, you can deactivate the conda environment:
```bash
conda deactivate
```

## Publishing to GitHub Pages via gh-pages Branch

To publish this Jupyter Book to GitHub Pages using the `gh-pages` branch, follow these steps:

### Option 1: Using ghp-import (Recommended)

1. **Install ghp-import**:
   ```bash
   pip install ghp-import
   ```

2. **Build the book**:
   ```bash
   jupyter-book build .
   ```

3. **Push to gh-pages branch**:
   ```bash
   ghp-import -n -p -f _build/html
   ```
   - `-n`: adds a `.nojekyll` file
   - `-p`: pushes to the remote repository
   - `-f`: force push (overwrites existing gh-pages branch)

### Option 2: Manual Method

1. **Build the book**:
   ```bash
   jupyter-book build .
   ```

2. **Create and switch to gh-pages branch**:
   ```bash
   git checkout --orphan gh-pages
   git rm -rf .
   ```

3. **Copy built files**:
   ```bash
   cp -r _build/html/* .
   echo "" > .nojekyll
   ```

4. **Commit and push**:
   ```bash
   git add .
   git commit -m "Deploy Jupyter Book"
   git push origin gh-pages
   ```

5. **Switch back to main branch**:
   ```bash
   git checkout main
   ```

### Configure GitHub Pages Settings

1. Go to your repository on GitHub: `https://github.com/mb-group/ai_journal_club`
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select **"Deploy from a branch"**
4. Choose **"gh-pages"** branch and **"/ (root)"** folder
5. Click **Save**

Your site will be available at: `https://mb-group.github.io/ai_journal_club/`

### Automated Deployment (Alternative)

If you prefer automated deployment, you can use GitHub Actions instead. See the `.github/workflows/deploy.yml` file for the workflow configuration.

## Development

To work on this book locally:

1. Make sure you're in the correct conda environment: `conda activate ai_journal_club`
2. Make changes to the markdown files
3. Build and preview: `jupyter-book build .`
4. Open `_build/html/index.html` in your browser to preview
5. When ready to publish, follow the publishing steps above

## Project Structure

- `intro.md` - Introduction and executive summary
- `selection_criteria.md` - Criteria for selecting papers and models
- `protein_book.md` - Protein-related content
- `_toc.yml` - Table of contents configuration
- `_config.yml` - Book configuration
- `requirements.txt` - Python package dependencies
- Various other markdown files and notebooks

## Contributing

Please ensure you're working in the correct conda environment (`conda activate ai_journal_club`) before making any changes or running the book build process.
