# What Protein Language Models Actually Learn

## Introduction

Protein language models (PLMs) have emerged as transformative tools in computational biology, fundamentally changing how we approach protein engineering, functional prediction, and evolutionary analysis. These models, trained on vast databases of protein sequences, learn to represent proteins in ways that capture functional and structural properties—often without explicit supervision on these properties. But what exactly do these models learn? And why do they work so well?

This chapter explores the journey from the inception of protein language models to our current understanding of their internal representations, drawing on recent breakthrough studies that have begun to decode what these "black box" models actually capture about protein biology.

### The Paradigm Shift: From Sequential to Direct Prediction

Traditionally, understanding protein function required following a sequential path: sequence → structure → function. PLMs have enabled a revolutionary shortcut:

```{mermaid}
flowchart TB
    subgraph Traditional["Traditional Paradigm"]
        S1[Protein Sequence] --> ST[Structure Determination<br/>X-ray, Cryo-EM, NMR] --> F1[Function Prediction<br/>Experimental assays]
    end
    
    subgraph PLM["PLM-Enabled Paradigm"]
        S2[Protein Sequence] --> PLM_Model[Protein Language Model<br/>Embeddings]
        PLM_Model --> F2[Direct Function Prediction]
        PLM_Model -.->|implicit representation| ST2[Structure Prediction<br/>ESMFold, AlphaFold]
        ST2 -.->|optional refinement| F2
    end
    
    style PLM_Model fill:#4CAF50,stroke:#2E7D32,stroke-width:3px,color:#fff
    style S2 fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#fff
    style F2 fill:#FF9800,stroke:#E65100,stroke-width:2px,color:#fff
    style Traditional fill:#f5f5f5,stroke:#999,stroke-width:2px
    style PLM fill:#e8f5e9,stroke:#4CAF50,stroke-width:2px
```

**Key insight**: PLMs learn evolutionary patterns that implicitly encode both structural and functional information. This allows them to predict function directly from sequence, or generate structure predictions as an intermediate step when needed. The solid arrows show the primary workflow, while dashed arrows indicate optional or implicit pathways.

## A Brief History: The Birth of Protein Language Models

### The 2020 Watershed Moment

The modern era of protein language models began in earnest in 2020 with the publication of [ESM (Evolutionary Scale Modeling)](https://www.pnas.org/doi/full/10.1073/pnas.2016239118) by Rives et al. The fact that this groundbreaking work was published in *PNAS* rather than a "higher-tier" journal reflects the initial skepticism the field faced. At the time, the idea of treating proteins as a language—with amino acids as vocabulary and sequences as sentences—was met with considerable resistance from parts of the structural biology community.

ESM's key insight was deceptively simple: apply transformer-based language models directly to protein sequences, treating amino acids as tokens. The model was trained using masked language modeling—randomly masking amino acids and training the model to predict them from context—on millions of protein sequences from UniRef. No structural information, no functional annotations—just sequences and the evolutionary patterns they contained.

### Parallel Innovations and Convergent Evolution

Almost simultaneously, independent research groups arrived at remarkably similar solutions. [ProtTrans](https://ieeexplore.ieee.org/document/9477085), developed by Elnaggar et al., took an almost identical approach, with differences that were largely negligible from a conceptual standpoint. ProtTrans later made all its embeddings publicly available through UniProt, significantly accelerating adoption across the field.

This convergence was no accident. Protein sequence modeling has historically borrowed heavily from natural language processing—even in the pre-deep learning era of statistical models like profile HMMs. When GPT and BERT demonstrated the power of transformer architectures for language, it was only natural that the protein modeling community would follow suit. The question was not *if* but *when* transformers would revolutionize protein sequence analysis.

## The Expanding Impact of PLMs

Since their introduction, protein language models have demonstrated remarkable utility across diverse applications:

### Protein Engineering and Design
- **Variant effect prediction**: PLMs can predict the functional impact of mutations with accuracy rivaling or exceeding experimental deep mutational scanning
- **Zero-shot fitness prediction**: Models like ESM-1v predict protein fitness without task-specific training
- **Directed evolution**: PLMs guide library design by identifying promising sequence regions

### Structure Prediction
- **Contact and distance prediction**: PLM embeddings serve as powerful inputs for structure prediction pipelines
- **AlphaFold integration**: Modern structure prediction methods leverage PLM representations
- **Fold recognition**: PLMs can identify remote homologs and novel folds

### Functional Annotation
- **GO term prediction**: Transfer learning from PLMs enables accurate functional annotation
- **Subcellular localization**: Embeddings capture cellular targeting signals
- **Protein-protein interactions**: Representations encode interaction propensities

### Drug Discovery and Therapeutics
- **Antibody design**: PLMs optimize antibody sequences for improved binding and developability
- **Enzyme engineering**: Models guide the design of enzymes with altered substrate specificity
- **Stability prediction**: PLMs predict thermodynamic stability changes

## The Central Question: What Do PLMs Actually Learn?

Despite their empirical success, protein language models have largely remained black boxes. Their internal representations—the high-dimensional vectors that encode protein sequences—clearly capture biologically meaningful information, but *what* exactly do they capture, and *how*?

Recent work in 2024-2025 has begun to provide concrete answers, revealing that PLMs learn far more structured biological knowledge than previously appreciated.

### Decoding the Latent Space

Several landmark studies have systematically probed PLM representations:

#### 1. **Structural Information Emerges Without Supervision** {cite}`Heinzinger2025`

[Heinzinger et al. (2025)](https://www.nature.com/articles/s41592-025-02836-7) demonstrated that PLMs trained solely on sequences nonetheless learn to represent 3D structural features. Through careful analysis of ESM-2 embeddings, they found that:

- **Secondary structure** is explicitly encoded in middle layers
- **Tertiary contacts** emerge in deeper layers, even without structure-based training
- **Residue burial and solvent accessibility** are predictable from embeddings with high accuracy

This suggests that evolutionary patterns in sequences carry sufficient information about structure for models to implicitly learn structural constraints.

#### 2. **PLMs Learn Evolutionary Statistics, Not Physics** {cite}`Zhang2024`

[Zhang et al. (2024)](https://www.pnas.org/doi/10.1073/pnas.2406285121) provided crucial evidence that PLMs **do not learn the physics of protein folding**. Instead, they store and leverage evolutionary statistics:

- **Coevolutionary patterns**: PLMs learn which amino acid pairs tend to co-occur across evolution
- **Motif interactions**: Models store statistics of interacting sequence fragments, not physical forces
- **Context dependence**: Contact prediction requires local sequence context, suggesting lookup of evolutionary patterns rather than physics-based computation

This work definitively counters the hypothesis that PLMs understand biophysical principles. The models work because evolutionary selection has imprinted physical constraints into sequence patterns—not because the models learned physics themselves.

#### 3. **Evolutionary and Functional Constraints Are Disentangled** {cite}`Notin2024`

[Notin et al. (2024)](https://www.pnas.org/doi/10.1073/pnas.2406285121) revealed that PLMs learn to separate different types of biological constraints:

- **Evolutionary constraint**: Conservation patterns across homologs
- **Functional constraint**: Requirements for specific biological activities
- **Structural constraint**: Physical requirements for proper folding

Importantly, these constraints are represented in partially orthogonal subspaces of the embedding space, allowing models to distinguish between conserved-but-flexible sites and invariant functional residues.

#### 4. **Sparse Features Reveal Biological Organization** {cite}`Hsu2024`

[Hsu et al. (2024)](https://www.pnas.org/doi/10.1073/pnas.2506316122) used sparse autoencoders to decode PLM representations:

- **Gene ontology associations**: Sparse features map cleanly to specific GO terms and protein families
- **Functional monosemanticity**: Individual features correspond to specific biological processes
- **Hierarchical organization**: Features capture biology at multiple levels of abstraction

Importantly, this interpretability work shows PLMs organize biological knowledge systematically, even though they don't understand underlying physics.

```{note}
**The Physics vs. Evolution Distinction**: A critical insight from recent research is that PLMs do **not** learn the physics of protein folding. Instead, they memorize evolutionary patterns that reflect physical constraints. This is a subtle but crucial distinction—the models work because evolution has already solved the physics problem, and PLMs learn to recognize those solutions.
```

## Rising Trends: Augmenting PLMs with Explicit Knowledge

### Structure-Aware Models

[ProstT5](https://academic.oup.com/nargab/article/6/4/lqae150/7901286) extends the ProtT5 architecture by treating 3D structure tokens as additional vocabulary. By training on sequence-structure pairs, the model learns joint representations that:

- Improve structure prediction quality
- Enable structure-conditioned sequence design
- Better capture conformational flexibility

This approach bridges the gap between sequence and structure modeling, creating models that understand their relationship bidirectionally.

### Biophysics-Informed Models

[Recent work in *Nature Methods*](https://www.nature.com/articles/s41592-025-02776-2) demonstrates the value of incorporating biophysical principles:

- **Energy-based terms**: Augmenting loss functions with physics-based constraints
- **Mechanistic inductive biases**: Building in known biochemical rules
- **Multi-scale representations**: Explicitly modeling interactions at different scales

These hybrid approaches combine the flexibility of data-driven learning with the interpretability and reliability of physics-based modeling.

## What This Means for Protein Scientists

The emerging understanding of what PLMs learn has practical implications:

### For Experimentalists
- **Trust but verify**: PLM predictions are powerful but not infallible—use them to guide, not replace, experiments
- **Exploit embeddings**: Use PLM representations for clustering, visualization, and hypothesis generation
- **Understand limitations**: PLMs struggle with truly novel folds and functions absent from training data

### For Computational Biologists
- **Choose models wisely**: Different PLMs capture different aspects of biology—match the model to your task
- **Fine-tuning matters**: Task-specific adaptation can dramatically improve performance
- **Interpret with care**: High-dimensional embeddings resist simple interpretation—use probing methods rigorously

### For AI Researchers
- **Biology as a testbed**: Proteins offer a rich domain for studying representation learning with ground truth
- **Evolution ≠ Physics**: PLMs demonstrate that memorizing evolutionary patterns can substitute for understanding physics
- **Hybrid approaches**: Combining learned and explicit knowledge remains an important frontier

## Conclusion: From Black Boxes to Mechanistic Understanding

Protein language models have evolved from mysterious black boxes to increasingly interpretable systems. We now understand that these models:

- **Learn evolutionary statistics, not physics**: PLMs memorize coevolutionary patterns rather than understanding biophysical principles
- **Store motif-level interactions**: Models lookup statistics of interacting sequence fragments conditioned on local context
- **Represent biological information hierarchically**: From GO terms to protein families, information is organized systematically
- **Benefit from explicit structure and physics when available**: Hybrid approaches show promise for improving reliability

The key takeaway: **PLMs are powerful because evolution has already solved the physics problem**. These models learn to recognize evolutionary solutions without understanding the underlying forces that shaped them. This insight is crucial for understanding both their capabilities and limitations.

## Further Reading

- Original ESM paper: [Rives et al., 2021, PNAS](https://www.pnas.org/doi/full/10.1073/pnas.2016239118)
- ProtTrans: [Elnaggar et al., 2021, IEEE TPAMI](https://ieeexplore.ieee.org/document/9477085)
- **PLMs learn evolution, not physics**: [Zhang et al., 2024, PNAS](https://www.pnas.org/doi/10.1073/pnas.2406285121) - Key paper showing PLMs memorize evolutionary statistics
- Structure emerges from evolution: [Heinzinger et al., 2025, Nature Methods](https://www.nature.com/articles/s41592-025-02836-7)
- Interpretable sparse features: [Hsu et al., 2024, PNAS](https://www.pnas.org/doi/10.1073/pnas.2506316122)
- Structure-augmented models: [ProstT5, NAR Genomics and Bioinformatics](https://academic.oup.com/nargab/article/6/4/lqae150/7901286)
- Biophysics-informed models: [Nature Methods, 2025](https://www.nature.com/articles/s41592-025-02776-2)
