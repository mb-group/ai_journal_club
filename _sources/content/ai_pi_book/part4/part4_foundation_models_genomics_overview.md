# Foundation Models in Genomics: Overview

## Introduction

Following the success of protein language models, the genomics field has adopted similar approaches to build "genomics foundation models." Since nucleotide sequences—both DNA and RNA—share the sequential nature of proteins, the same transformer-based architectures can be readily adapted. This has led to the emergence of specialized DNA language models and RNA language models, collectively known as genomics foundation models.

The promise is compelling: models that can learn fundamental patterns from massive genomic datasets and then apply this knowledge to diverse downstream tasks without additional training. However, as we'll explore, the reality of these models' performance has proven more nuanced than initial excitement suggested.

## Characteristics of Foundation Models in Genomics

Foundation models in genomics share several defining characteristics, though not all are strictly necessary ([Nguyen et al., 2025, Nature Machine Intelligence](https://www.nature.com/articles/s42256-025-01007-9)).

### Core Architecture Components

**Tokenization Strategy**
- Defines the "vocabulary" for genomic sequences
- Common approaches include k-mer based tokenization (3-mers, 6-mers, etc.)
- Some models use byte-pair encoding (BPE) adapted from NLP
- Choice impacts model's ability to capture different scales of genomic features

**Self-Supervised Training**
- Typically uses masked language modeling (predicting masked tokens)
- No labeled data required during pre-training
- Models learn from sequence patterns themselves
- Analogous to BERT's approach in natural language processing

**Large-Scale, Diverse Training Data**
- Usually genome-level data from one or multiple species
- Includes both coding and non-coding regions
- May incorporate evolutionary information across species
- Training datasets often span millions to billions of base pairs

### What Makes Them "Foundation" Models

While most genomics foundation models are indeed language models, the key distinguishing features are:

1. **Scale**: Trained on comprehensive genomic datasets
2. **Generality**: Designed to be applicable across multiple downstream tasks
3. **Transfer learning**: Can be fine-tuned or used zero-shot for specific applications
4. **Learned representations**: Generate biologically meaningful embeddings
