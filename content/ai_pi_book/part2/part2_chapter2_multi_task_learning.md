# Multi-Task Learning: One Model, Many Outputs

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```

Classical ML typically means one model, one task. Modern AI routinely trains single models with multiple objectives simultaneously:
- Predict protein structure AND function AND stability
- Learn from labeled AND unlabeled data in the same training run
- Optimize for multiple performance criteria that may even conflict

This changes how you evaluate models—there's no longer a single "accuracy" number, but rather a profile of performance across tasks.
