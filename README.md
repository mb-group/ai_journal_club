# AI Journal Club

An interactive playground and zoo of AI models for exploring artificial intelligence's impact on scientific research.

## Publishing to GitHub Pages via gh-pages Branch

To publish this Jupyter Book to GitHub Pages using the `gh-pages` branch, follow these steps:

### Prerequisites

1. Install required packages:
   ```bash
   pip install jupyter-book matplotlib numpy
   ```

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

1. Make changes to the markdown files
2. Build and preview: `jupyter-book build .`
3. Open `_build/html/index.html` in your browser to preview
4. When ready to publish, follow the publishing steps above

## Book Structure

- `intro.md` - Introduction and executive summary
- `selection_criteria.md` - Criteria for selecting papers and models
- `_toc.yml` - Table of contents configuration
- `_config.yml` - Book configuration