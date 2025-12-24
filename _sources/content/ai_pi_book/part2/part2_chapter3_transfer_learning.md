# Transfer Learning: Standing on the Shoulders of Giants

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```

Perhaps the biggest paradigm shift: you rarely train models from scratch anymore.

**Pre-training + Fine-tuning** has become the dominant workflow:
1. Someone trains a massive model on general data (e.g., all known protein sequences)
2. You adapt (fine-tune) that model to your specific task with your data
3. The pre-trained model brings general "knowledge" that dramatically reduces your data requirements

This is why a model trained on human proteins might work surprisingly well on bacterial proteins—it learned general principles of protein biology during pre-training.
