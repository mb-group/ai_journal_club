# Evaluation Methods for Foundation Models in Genomics

## The Challenge of Assessment

Assessing foundation models is challenging due to their general-purpose nature and self-supervised training. Multiple evaluation strategies have emerged:

## Training-Based Evaluation

**Masked Token Recovery**
- Primary metric during training: how well does the model predict masked nucleotides?
- Perplexity scores indicate how "surprised" the model is by held-out sequences
- **Limitation**: Good perplexity doesn't guarantee biological utility
- Similar to evaluating language models by autocomplete accuracy

**Embedding Quality Assessment**
- Qualitative examination of learned representations
- Do related sequences cluster together in embedding space?
- Can visualizations (t-SNE, UMAP) show biological organization?
- **Weakness**: Only function-related control at training stage; subjective interpretation

## Downstream Task Evaluation

Since foundation models promise biologically meaningful representations, evaluation on specific tasks is crucial:

**Direct Embedding Usage**
- Use frozen model embeddings as features for prediction tasks
- Tests whether pre-trained representations capture relevant information
- Common for variant effect prediction, enhancer identification, etc.
- Zero-shot or few-shot performance indicates generalization

**Fine-Tuning Approaches**
- Add task-specific layers and train on labeled data
- May fine-tune the entire foundation model or keep it frozen
- Tests adaptability to specific applications
- More computationally expensive but often higher performance

**Separate Model Training**
- Extract embeddings and train independent classifier
- More common approach in practice
- Allows comparison with traditional feature engineering
- Can use simpler models (linear, random forest) for interpretability

## Common Benchmark Tasks

- **Variant effect prediction**: Does mutation increase or decrease function?
- **Regulatory element identification**: Promoters, enhancers, silencers
- **Splicing prediction**: Will a sequence variant affect RNA splicing?
- **Gene expression prediction**: Predict expression from sequence
- **Chromatin state prediction**: Predict accessibility, histone marks
- **Evolutionary conservation**: Identify constrained regions
