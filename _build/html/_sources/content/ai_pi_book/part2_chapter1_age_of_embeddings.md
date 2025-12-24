# The Age of Embeddings: Representations Are the Real Output

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```

## The Fundamental Paradigm Shift

**The Old View:** A model's job is to produce a final prediction (classification label, regression value, etc.)

**The New Reality:** The intermediate representations (embeddings) are often more valuable than the final output.

Modern AI systems like language models, variational autoencoders (VAEs), and contrastive learning frameworks don't just predict—they learn rich internal representations of data. For biology:
- A protein language model's embedding captures evolutionary relationships, structural motifs, and functional properties
- These embeddings can be used for downstream tasks the model was never explicitly trained for
- Think of embeddings as a learned "language" for describing your data that captures patterns humans might never articulate

---

## What Are Embeddings?

```{figure} embedding_idea.png
---
name: embedding-concept
alt: Conceptual illustration of embeddings
align: center
---
The embedding concept: transforming discrete, high-dimensional, or complex data into continuous vector representations that capture semantic relationships.
```

At their core, **embeddings** are dense vector representations of data that encode meaningful relationships in a continuous space. Instead of representing data through sparse, hand-crafted features, embeddings allow models to learn compact representations where similar items are positioned close together.

```{figure} embedding_illustration_1.png
---
name: embedding-vectors
alt: Vector representation of words in embedding space
width: 70%
align: center
---
Words represented as dense vectors in continuous embedding space. Each word is mapped to a point where semantic relationships are preserved through geometric proximity.
```

### Key Properties of Good Embeddings

1. **Dimensionality Reduction**: Embeddings compress high-dimensional or complex data into lower-dimensional vectors (typically 128-1024 dimensions) while preserving the most important information.

2. **Semantic Similarity**: Items that are functionally or structurally similar have embeddings that are close in vector space. Distance in embedding space corresponds to meaningful relationships.

```{figure} embedding_illustration_3.png
---
name: embedding-analogies
alt: Semantic relationships in embedding space showing king-queen-man-woman analogy
width: 80%
align: center
---
Semantic relationships encoded as geometric relationships in embedding space. The famous word2vec analogy: "king" - "man" + "woman" ≈ "queen" demonstrates how embeddings capture meaningful semantic relationships through vector arithmetic.
```

3. **Continuous Representation**: Unlike discrete one-hot encodings, embeddings place data on a continuous manifold where interpolation is meaningful. Points between known examples represent plausible intermediate states.

4. **Task-Agnostic Features**: Well-trained embeddings capture general properties of the data that are useful across many different downstream tasks, not just the original training objective.

---

## From Hand-Crafted Features to Learned Representations

### The Traditional Approach

Historically, machine learning required domain experts to manually engineer features:
- For proteins: amino acid composition, charge, hydrophobicity scores, secondary structure propensity
- For images: edge detectors, color histograms, texture descriptors
- For text: word counts, TF-IDF scores, hand-crafted linguistic features

**Problems with this approach:**
- Labor-intensive and requires deep domain expertise
- Features may not capture the patterns that matter for your specific task
- Difficult to represent complex, hierarchical relationships
- Fixed features can't adapt as you get more data

### The Embedding Revolution

Modern deep learning automatically learns representations through training:

```python
# Traditional approach: manual feature engineering
protein_features = [
    calculate_hydrophobicity(sequence),
    count_charged_residues(sequence),
    get_secondary_structure_propensity(sequence),
    # ... hundreds of hand-crafted features
]

# Modern approach: learned embeddings
embedding = protein_model.encode(sequence)  # Returns 1024-dim vector
# The model learned what matters from millions of sequences
```

```{figure} Kernel-trick-By-transforming-the-original-space-left-into-a-space-of-increased.png
---
name: embedding-transformation
alt: Transformation from original space to higher-dimensional embedding space
width: 75%
align: center
---
The power of learned transformations: Data that is not linearly separable in the original space (left) can be transformed into a higher-dimensional embedding space (right) where patterns become clear and separable. Embeddings learn these transformations automatically from data rather than requiring hand-crafted feature engineering.
```

The model discovers features that humans might never think to look for, often outperforming decades of domain knowledge encoded in hand-crafted features.

---

## How Embeddings Are Learned

### Self-Supervised Learning

Many of the most powerful embedding models are trained through **self-supervised learning**—they learn from the data itself without requiring explicit labels:

**Protein Language Models (e.g., ESM, ProtBERT)**
- Training task: Predict masked amino acids in a sequence
- What's learned: Evolutionary constraints, structural compatibility, functional motifs
- Result: Embeddings that capture "protein-ness" in general

**Molecular Embeddings (e.g., MolCLR, GraphMVP)**
- Training task: Predict relationships between different views of molecules (2D graphs vs 3D conformations)
- What's learned: Chemical properties, reactivity patterns, binding characteristics
- Result: Embeddings useful for drug discovery, property prediction, synthesis planning

### Contrastive Learning

A particularly powerful approach for learning embeddings:

1. **Positive pairs**: Create pairs of related items (same protein, different mutations; same molecule, different conformations)
2. **Negative pairs**: Sample unrelated items
3. **Training objective**: Push positive pairs closer together in embedding space while pushing negative pairs apart

This creates embeddings where meaningful similarity corresponds to vector proximity.

---

## Why Embeddings Matter for Biology

### 1. Transfer Learning

Train once on massive datasets, use everywhere:

```python
# Use pre-trained protein embeddings
esm_model = load_pretrained("ESM-2")  # Trained on 250M sequences

# Your task: predict enzyme activity with only 500 labeled examples
embeddings = esm_model.encode(your_sequences)
activity_predictor.train(embeddings, your_labels)
# Often outperforms models trained from scratch on millions of examples
```

The embeddings capture fundamental biology learned from vast sequence databases. You leverage this knowledge even with small datasets.

### 2. Multi-Task Learning

One embedding, many predictions:

```python
embedding = protein_model.encode(sequence)

# Use the same embedding for different tasks
stability = stability_predictor(embedding)
localization = localization_predictor(embedding)
interaction_partners = interaction_predictor(embedding)
```

The embedding serves as a universal representation that supports diverse biological questions.

### 3. Similarity Search and Clustering

Find related proteins by embedding similarity:

```python
# Embed your query protein
query_embedding = model.encode(query_sequence)

# Search millions of proteins efficiently
similar_proteins = embedding_database.nearest_neighbors(
    query_embedding, 
    k=100
)
# Returns functionally related proteins, even with low sequence identity
```

This enables:
- Finding homologs that sequence alignment misses
- Discovering proteins with similar functions but different evolutionary origins
- Organizing the protein universe into functional families

### 4. Interpretable Latent Spaces

Well-trained embeddings often have interpretable structure:

```python
# Explore what the model learned
pca = PCA(n_components=2)
embedding_2d = pca.fit_transform(embeddings)

# Visualize: proteins often cluster by:
# - Structural fold families
# - Functional categories  
# - Evolutionary relationships
# Even though the model was never told about these categories!
```

```{figure} embedding_illustration_2.jpg
---
name: embedding-space-viz
alt: Visualization of embedding space showing clusters and relationships
width: 85%
align: center
---
Visualization of high-dimensional embeddings projected into 2D space. Similar items cluster together, revealing the learned structure and relationships. These patterns emerge naturally from training, without explicit supervision about categories or relationships.
```

The learned representations often rediscover biological organization principles.

---

## Practical Considerations

### Embedding Quality Depends on Training Data

- **Domain specificity**: Protein embeddings from models trained on all proteins may not be optimal for your specific protein family
- **Data scale**: More training data generally produces better embeddings
- **Task alignment**: Embeddings from models trained on related tasks transfer better

### Not All Layers Are Equal

Deep models create embeddings at multiple layers:
- **Early layers**: Capture low-level features (local sequence patterns)
- **Middle layers**: Often contain the most generalizable representations
- **Late layers**: More specialized for the original training task

```python
# Many models let you choose which layer's embeddings to use
embeddings_layer_6 = model.encode(sequence, layer=6)   # More general
embeddings_layer_33 = model.encode(sequence, layer=33)  # More specialized
```

### Dimensionality Matters

- **Higher dimensions**: Can capture more nuanced information but require more data and computation
- **Lower dimensions**: More efficient, less prone to overfitting, but may lose important details
- **Typical ranges**: 
  - Small molecules: 128-512 dimensions
  - Proteins: 512-1280 dimensions  
  - Large biomolecular complexes: 1024-2048 dimensions

---

## Common Pitfalls

1. **Assuming embeddings are magic**: They're only as good as their training. Embeddings from models trained on unrelated data may not help.

2. **Ignoring embedding space geometry**: Different models use different distance metrics and normalization schemes. Always check the documentation.

3. **Freezing when you should fine-tune**: Pre-trained embeddings are a starting point. For specialized tasks, fine-tuning the embedding model on your data often helps.

4. **Over-interpreting individual dimensions**: While embeddings capture meaningful patterns, individual dimensions rarely correspond to interpretable features. The information is distributed across the entire vector.

---

## Key Takeaways

```{admonition} Remember
:class: tip

1. **Embeddings are the product**: Modern AI's real value often lies in its learned representations, not just its predictions

2. **Transfer learning at scale**: Pre-trained embeddings let you leverage knowledge from massive datasets even when you have limited labeled data

3. **Similarity in embedding space is meaningful**: Close vectors represent related biological entities—a powerful property for search, clustering, and analysis

4. **One representation, many uses**: Good embeddings support diverse downstream tasks without modification

5. **Learn from the data**: Embeddings often capture patterns and relationships that human experts never explicitly encoded
```

---

## Further Reading

- {cite}`rives2021biological` - ESM protein language models
- {cite}`jumper2021highly` - AlphaFold structure prediction using embeddings
- {cite}`stärk2022equibind` - Molecular embeddings for drug design
- {cite}`su2023saprot` - Structure-aware protein embeddings
