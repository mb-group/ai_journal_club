# The Age of Embeddings: Representations Are the Real Output

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```

**The Old View:** A model's job is to produce a final prediction (classification label, regression value, etc.)

**The New Reality:** The intermediate representations (embeddings) are often more valuable than the final output.

Modern AI systems like language models, variational autoencoders (VAEs), and contrastive learning frameworks don't just predict—they learn rich internal representations of data. For biology:
- A protein language model's embedding captures evolutionary relationships, structural motifs, and functional properties
- These embeddings can be used for downstream tasks the model was never explicitly trained for
- Think of embeddings as a learned "language" for describing your data that captures patterns humans might never articulate
