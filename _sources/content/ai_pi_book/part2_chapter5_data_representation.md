# Data Representation: Tokenization Changes Everything

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```

How you represent input data fundamentally shapes what patterns models can learn.

**Tokenization** means breaking complex data into discrete units:
- Text: words or sub-word pieces
- Proteins: individual amino acids, or k-mers (overlapping subsequences)
- Genomic data: nucleotides, codons, or functional motifs

The choice of tokenization isn't just technical—it determines what patterns are "visible" to the model. A model that sees proteins as individual amino acids learns different patterns than one that sees them as structural domains.
