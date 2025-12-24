# Actual Performance of Foundation Models in Genomics

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

## The Value Proposition of Foundation Models

### Addressing Long-Standing Challenges

The genomics field has accumulated vast amounts of sequencing data, but lacked efficient methods to extract knowledge from this data at scale until foundation models emerged.

**Knowledge Emergence from Big Data**
- Central belief: patterns and insights emerge when data is large and diverse enough
- Foundation models provide a framework to systematically "digest" genomic big data
- Enable discovery of relationships not apparent from smaller datasets

**Capturing Long-Range Dependencies**
- Genomic regulation often involves interactions across long distances
- Traditional methods struggle with context windows beyond a few hundred base pairs
- Transformer architectures can theoretically capture dependencies across thousands of bases
- Critical for understanding regulatory elements, chromatin interactions, and gene networks

### Contextualizing Small Datasets

One key application is placing limited experimental data within large-scale reference contexts:
- Single-cell datasets can be interpreted against comprehensive atlases
- Rare variants can be evaluated using population-scale genomic knowledge
- Small perturbation studies gain context from broader biological understanding

### Zero-Shot and Transfer Learning Capabilities

A major promise of foundation models is their ability to generalize:
- Apply to new tasks without retraining
- Transfer knowledge across species and contexts
- Given a single DNA sequence, predict functional consequences
- Reduce need for large task-specific labeled datasets

### Unique Genomic Challenges

Foundation models aim to address challenges that traditional bioinformatics approaches struggle with:

**Sequence Length Complexity**
- Genomic sequences are much longer than protein sequences
- Genes can span hundreds of thousands of base pairs
- Regulatory elements may be distant from their target genes
- Current models still struggle with truly genome-scale contexts

**Sparse Signal Problem**
- Coding regions represent only ~2% of the human genome
- Functional elements are scattered and context-dependent
- Much of the genome's regulatory code remains poorly understood
- Models must learn meaningful patterns from predominantly non-coding sequence

**Data Heterogeneity and Noise**
- Sequencing technologies vary in quality and error profiles
- Cross-dataset comparisons are challenging
- Batch effects and technical artifacts are common
- Foundation models promise robustness through training on diverse data sources

**Unlabeled Data Abundance**
- Far more sequence data exists than functional annotations
- Self-supervised learning leverages this unlabeled data
- Enables learning beyond current biological knowledge
- May discover patterns not yet characterized experimentally

### Inspiration from Other Domains

The development of genomics foundation models was catalyzed by success in:

**Natural Language Processing**
- GPT, BERT, and other language models demonstrated power of self-supervised pre-training
- Transfer learning showed single models could excel at diverse tasks
- Attention mechanisms proved effective for capturing long-range dependencies

**Protein Language Models**
- ESM, ProtBERT, and others successfully learned protein structure and function
- Demonstrated that biological sequences contain learnable patterns
- Showed embeddings could capture evolutionary and functional relationships
- Provided direct blueprint for genomics applications

## Evaluation Methods for Foundation Models

Assessing foundation models is challenging due to their general-purpose nature and self-supervised training. Multiple evaluation strategies have emerged:

### Training-Based Evaluation

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

### Downstream Task Evaluation

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

### Common Benchmark Tasks

- **Variant effect prediction**: Does mutation increase or decrease function?
- **Regulatory element identification**: Promoters, enhancers, silencers
- **Splicing prediction**: Will a sequence variant affect RNA splicing?
- **Gene expression prediction**: Predict expression from sequence
- **Chromatin state prediction**: Predict accessibility, histone marks
- **Evolutionary conservation**: Identify constrained regions

## The Reality Check: Drama and Disappointment

### Proliferation Without Clear Differentiation

Beginning in 2021, the field experienced a flood of similar foundation model papers ([Dalla-Torre et al., 2024, Nature Methods](https://www.nature.com/articles/s41592-024-02201-0), [Zhou et al., 2024, Nature Methods](https://www.nature.com/articles/s41592-024-02191-z)):
- Dozens of models with nearly identical architectures
- Often trained on overlapping or similar datasets
- Marginal improvements claimed over previous models
- Limited head-to-head comparisons
- Difficult for practitioners to choose appropriate models

Examples include models like Nucleotide Transformer, DNABERT-2, HyenaDNA, Evo, and many others.

### The Benchmarking Problem

Until 2024, there was no standardized benchmark for fair comparison ([Zrimec et al., 2024, arXiv](https://arxiv.org/abs/2410.13956)):
- Each paper used different evaluation datasets
- Tasks and metrics varied across studies
- Cherry-picking of favorable results was common
- Reproducibility challenges were widespread

The development of comprehensive benchmarks like GenomicBenchmarks finally enabled systematic evaluation, but revealed sobering results.

### Limited Performance Gains

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

### Over-Promising Nomenclature

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

### The Marketing Problem

There's a disconnect between marketing and scientific reality:
- Provocative claims in abstracts not supported by thorough evaluation
- "Revolutionary" language in press releases and grant applications
- Limited acknowledgment of failures and limitations
- Incentive structures favor novelty over rigorous validation
- Preprints may overstate performance before peer review 

## Current Trends and Future Directions

### Multi-Omics Foundation Models

An emerging trend is integrating multiple data modalities ([Wu et al., 2024, arXiv](https://arxiv.org/pdf/2512.14019)):

**Beyond Sequence Alone**
- Combining DNA sequence with epigenetic marks
- Integrating gene expression, protein abundance, metabolomics
- Incorporating chromatin accessibility and 3D structure
- Linking sequence to cellular phenotypes

**Potential Advantages**
- Richer representations of biological state
- Better prediction of complex phenotypes
- More comprehensive understanding of regulation
- Alignment with systems biology perspective

**Technical Challenges**
- Different modalities have different scales and distributions
- Missing data is common across modalities
- Computational requirements multiply
- Interpretation becomes more complex

**Examples**
- Models combining scRNA-seq with scATAC-seq
- Integration of sequence with chromatin conformation data
- Multi-modal cell state representations

### Cell-State Foundation Models

Rather than pure sequence models, focus on cellular representation:
- scRNA-seq based models (scGPT, Geneformer, scBERT)
- Learning from perturbation data (e.g., Perturb-seq)
- Predicting cellular responses to genetic/chemical perturbations
- Drug discovery and cell engineering applications

### More Realistic Evaluation

The field is moving toward:
- Standardized benchmarks with diverse tasks
- Rigorous comparison with simple baselines
- Transparent reporting of limitations
- Focus on practical utility over novelty
- Better understanding of when foundation models actually help
- Cost-benefit analysis including computational requirements

### Architectural Innovations

Beyond standard transformers:
- State space models (e.g., Mamba, Hyena) for longer contexts
- Sparse attention mechanisms
- Hierarchical architectures for multi-scale genomics
- Graph neural networks for 3D genome structure
- Hybrid models combining multiple approaches

### Open Questions

**Scientific Questions**
- What genomic patterns do these models actually learn?
- Are emergent properties real or measurement artifacts?
- How can we make models more interpretable?
- What's the minimal data needed for useful foundation models?
- Do models capture causal relationships or just correlations?

**Practical Questions**
- When should practitioners use foundation models vs. traditional methods?
- How to make these models accessible beyond large research groups?
- What compute requirements are justified by performance gains?
- How to ensure reproducibility and reliability?
- How to handle model versioning and updates?

**Ethical and Policy Questions**
- How to ensure equitable access to powerful genomic AI tools?
- Privacy concerns with genomic data in foundation models
- Potential misuse in synthetic biology applications
- Intellectual property and commercialization issues

## Key Takeaways

1. **Foundation models in genomics are promising but overhyped**: The theoretical potential is real, but current implementations often underdeliver relative to claims.

2. **Simple baselines are surprisingly strong**: Before deploying complex foundation models, validate that they outperform straightforward alternatives like linear models with k-mer features.

3. **Evaluation matters critically**: Claims should be backed by rigorous, standardized evaluation against appropriate baselines. Be skeptical of papers lacking comprehensive benchmarking or comparing only to weak baselines.

4. **Context is crucial**: "Genomics foundation model" can mean very different things. Understand the training data, architecture, intended use cases, and actual performance before adoption.

5. **The field is maturing**: Moving from hype to rigorous science, with better benchmarks and more honest assessment of limitations. Recent publications show increased methodological rigor.

6. **Look beyond sequence**: Multi-omics and cell-state models may ultimately prove more valuable than pure sequence models for many biological applications.

7. **Traditional bioinformatics still valuable**: Foundation models are tools to complement, not replace, existing methods. Domain knowledge and mechanistic understanding remain essential.

8. **Computational costs matter**: The environmental and financial costs of training and deploying foundation models must be justified by tangible performance gains.

9. **Interpretability is often lacking**: Understanding *why* a model makes predictions remains challenging, limiting scientific insight and trust.

10. **Success depends on the task**: Foundation models may excel for some applications while offering no advantage for others. Task-specific evaluation is essential.

## Recommendations for Practitioners

### When to Consider Foundation Models

- You have limited labeled data but access to relevant unlabeled sequence data
- Transfer learning from other species/contexts could be valuable
- Task requires capturing long-range dependencies (>1kb)
- You need embeddings for multiple downstream tasks
- Computational resources are available

### When to Use Simpler Approaches

- Strong baseline methods exist for your task
- Interpretability is critical
- Computational resources are limited
- Training data is abundant for your specific task
- Real-time predictions are needed

### Best Practices

1. **Start with baselines**: Establish performance of simple methods first
2. **Use existing benchmarks**: Compare against standardized tasks
3. **Report honestly**: Include negative results and limitations
4. **Consider costs**: Factor in computational requirements
5. **Validate thoroughly**: Test on held-out data from different sources
6. **Seek interpretability**: Use attention analysis, ablations, probes
7. **Be specific**: Clearly define model capabilities and limitations
8. **Share resources**: Make models and code openly available
9. **Update regularly**: Re-evaluate as new benchmarks emerge
10. **Combine approaches**: Consider ensemble methods with traditional tools

## Conclusion

Foundation models represent an important development in genomics, bringing powerful machine learning approaches to bear on fundamental biological questions. However, the field must move beyond hype to rigorous evaluation and honest assessment of capabilities.

The coming years will likely see continued progress in architecture design, multi-omics integration, and task-specific optimization. Success will require collaboration between machine learning researchers, experimental biologists, and clinicians to ensure models address real biological needs rather than just technical benchmarks.

Most importantly, foundation models should be viewed as one tool among many in the genomics toolkit—powerful when applied appropriately, but not a universal solution. The goal is not to build the biggest model or claim the most revolutionary advance, but to develop practical tools that genuinely advance our understanding of genome biology and improve human health.
