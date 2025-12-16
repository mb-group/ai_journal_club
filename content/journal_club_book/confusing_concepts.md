# Frequently Confusing AI Concepts

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```



*Clarifying the most commonly misunderstood concepts in AI for biology*

## Overview

Through our journal club discussions, certain AI concepts consistently emerge as sources of confusion or misinterpretation. This section provides clear, accessible explanations of these concepts with specific examples from biological applications.

## Common Confusions

### Machine Learning vs. Deep Learning vs. AI

**The Confusion**: These terms are often used interchangeably, leading to misunderstanding about what different methods can actually do.

**The Clarity**: 
- **Artificial Intelligence (AI)**: The broad field of making machines perform tasks that typically require human intelligence
- **Machine Learning (ML)**: A subset of AI that learns patterns from data without being explicitly programmed
- **Deep Learning (DL)**: A subset of ML using neural networks with multiple layers

**Biology Example**: AlphaFold uses deep learning (neural networks), but not all protein prediction methods are deep learning - some use traditional ML or even rule-based approaches.

### Supervised vs. Unsupervised vs. Self-Supervised Learning

**The Confusion**: The distinction between these learning paradigms and when each is appropriate.

**The Clarity**:
- **Supervised**: Learning from labeled examples (input-output pairs)
- **Unsupervised**: Finding patterns in data without labels
- **Self-supervised**: Creating labels from the data itself

**Biology Example**: 
- Supervised: Predicting protein function from sequence with known functional annotations
- Unsupervised: Clustering cells by gene expression without knowing cell types
- Self-supervised: Predicting masked amino acids in protein sequences (like in ESM models)

### Transfer Learning vs. Foundation Models

**The Confusion**: When and how pre-trained models can be applied to new biological problems.

**The Clarity**:
- **Transfer Learning**: Adapting a model trained on one task to a related task
- **Foundation Models**: Large models trained on diverse data that can be adapted to many downstream tasks

**Biology Example**: ESM-2 is a foundation model for proteins that can be fine-tuned for various tasks like stability prediction, function annotation, or contact prediction.

### Attention Mechanisms and Transformers

**The Confusion**: What attention actually computes and why it's useful for biological sequences.

**The Clarity**: Attention allows models to focus on different parts of the input when making predictions, capturing long-range dependencies that are crucial in biology.

**Biology Example**: In protein sequences, attention can learn which amino acids interact despite being far apart in the sequence, mimicking the 3D structure relationships.

### Generative vs. Discriminative Models

**The Confusion**: The difference between models that generate new data vs. those that classify existing data.

**The Clarity**:
- **Generative**: Models that can create new examples (P(X,Y))
- **Discriminative**: Models that separate or classify examples (P(Y|X))

**Biology Example**: 
- Generative: ProtGPT generates new protein sequences
- Discriminative: A model that predicts whether a protein is an enzyme or not

### Overfitting vs. Underfitting

**The Confusion**: Recognizing and addressing poor model performance.

**The Clarity**:
- **Overfitting**: Model memorizes training data but fails on new data (high variance)
- **Underfitting**: Model is too simple to capture the underlying pattern (high bias)

**Biology Example**: An overfitted protein function predictor might memorize specific sequences but fail on homologs. An underfitted one might miss important sequence motifs entirely.

## Key Takeaways

1. **Context Matters**: The same AI technique can behave very differently depending on the biological context and data quality
2. **No Universal Solution**: Different biological problems require different AI approaches
3. **Interpretability Trade-offs**: More complex models often perform better but are harder to interpret
4. **Data Quality Over Quantity**: Clean, well-annotated biological data often trumps large, noisy datasets
5. **Validation is Critical**: Biological validation should complement computational metrics

## Discussion Points

- How do we choose the right AI approach for a given biological question?
- What are the most common pitfalls when applying AI to biological data?
- How can we better communicate AI capabilities and limitations to the broader biology community?

---

*This section will be continuously updated based on recurring themes in our journal club discussions.*