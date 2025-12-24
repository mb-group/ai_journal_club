# The Reality Check: Drama and Disappointment

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```



## Proliferation Without Clear Differentiation

Beginning in 2021, the field experienced a flood of similar foundation model papers ([Dalla-Torre et al., 2024, Nature Methods](https://www.nature.com/articles/s41592-024-02201-0), [Zhou et al., 2024, Nature Methods](https://www.nature.com/articles/s41592-024-02191-z)):
- Dozens of models with nearly identical architectures
- Often trained on overlapping or similar datasets
- Marginal improvements claimed over previous models
- Limited head-to-head comparisons
- Difficult for practitioners to choose appropriate models

Examples include models like Nucleotide Transformer, DNABERT-2, HyenaDNA, Evo, and many others.

## The Benchmarking Problem

Until 2024, there was no standardized benchmark for fair comparison ([Zrimec et al., 2024, arXiv](https://arxiv.org/abs/2410.13956)):
- Each paper used different evaluation datasets
- Tasks and metrics varied across studies
- Cherry-picking of favorable results was common
- Reproducibility challenges were widespread

The development of comprehensive benchmarks like GenomicBenchmarks finally enabled systematic evaluation, but revealed sobering results.

## Limited Performance Gains

Recent rigorous evaluations have revealed disappointing performance ([Sasse et al., 2024, Nature Machine Intelligence](https://www.nature.com/articles/s42256-024-00949-w), [Chu et al., 2025, Nature Methods](https://www.nature.com/articles/s41592-025-02772-6)):

**Not Better Than Simple Linear Models**
- On many tasks, foundation models perform comparably to simple baselines
- Linear models trained on k-mer features often match or exceed foundation model performance
- Traditional bioinformatics tools remain competitive
- Massive computational cost of foundation models often not justified

**Where Are the Gains?**
- Some improvement on truly novel sequences
- Benefits for transfer learning across species (sometimes)
- Potential value in zero-shot scenarios
- Best performance often requires substantial fine-tuning anyway

**Specific Findings**
- Enhancer prediction: k-mer models competitive with foundation models
- Variant effect prediction: marginal improvements, high computational cost
- Gene expression: traditional features + simple models often sufficient
- Cross-species transfer: mixed results, often species-specific retraining needed

## Over-Promising Nomenclature

The term "foundation model" and claims of generality often don't match reality:

**Narrow Scope**
- Many "genomics foundation models" are actually transcriptomics-only
- Often limited to specific cell lines or tissue types
- Small molecule perturbation studies don't necessarily generalize
- Species-specific models may not transfer well

**Context Limitations**
- Despite long-range claims, effective context windows remain limited
- Most models max out at 10-100kb, tiny compared to genome scale
- Gene-gene interactions and chromosome topology still poorly captured
- 3D genome organization not effectively modeled

**Task Specificity**
- Models often excel only at tasks similar to training objective
- Claimed "general purpose" abilities don't materialize
- Fine-tuning often required, undermining zero-shot premise
- Transfer across biological domains remains challenging

## The Marketing Problem

There's a disconnect between marketing and scientific reality:
- Provocative claims in abstracts not supported by thorough evaluation
- "Revolutionary" language in press releases and grant applications
- Limited acknowledgment of failures and limitations
- Incentive structures favor novelty over rigorous validation
- Preprints may overstate performance before peer review
