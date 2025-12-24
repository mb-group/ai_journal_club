# What Protein Language Models Actually Learn

## Introduction

To understand protein language models, we must first understand what a language model actually is. In its dry technical definition, a language model is one that can predict the next word given previous words. The profound implication: if a model can perform this task well, it has effectively learned the rules of grammar—the statistical patterns that govern how words combine to form meaningful sentences.

Now add "Protein" to this framework. A protein language model applies the exact same modeling methods, simply replacing human sentences with protein sequences and defining amino acids as the vocabulary. If these models learn the "grammar" of proteins, the natural question becomes: what exactly is this grammar?

We can examine this grammar by extracting and analyzing the models' embeddings—the high-dimensional representations they create for each protein sequence. However, a crucial caveat: in this research field, no clear-cut grammatical rules have been discovered. The language analogy is precisely that—an analogy, a useful metaphorical framework rather than a literal description. What the models learn turns out to be more nuanced than simple rules, as we'll explore throughout this chapter.

Protein language models (PLMs) have emerged as transformative tools in computational biology, fundamentally changing how we approach protein engineering, functional prediction, and evolutionary analysis. These models, trained on vast databases of protein sequences, learn to represent proteins in ways that capture functional and structural properties—often without explicit supervision on these properties. But what exactly do these models learn? And why do they work so well?

This chapter explores the journey from the inception of protein language models to our current understanding of their internal representations, drawing on recent breakthrough studies that have begun to decode what these "black box" models actually capture about protein biology.

### A Critical Distinction: Sequence-Based vs. Text-Based Language Models

Before diving deeper, we must clarify a crucial distinction that often causes confusion: **protein language models are fundamentally different from biomedical language models**, even though both are called "language models."

**Protein Language Models (Sequence-Based)**
- **Input**: Raw protein sequences (e.g., `MKLLVTSLVG...`)
- **Vocabulary**: 20 standard amino acids plus special tokens
- **Training data**: Millions of protein sequences from databases like UniRef, UniProt
- **What they learn**: Evolutionary patterns, coevolutionary constraints, sequence-function relationships
- **Examples**: ESM, ProtTrans, ProtBERT, ESM-2, ProGen
- **Applications**: Structure prediction, variant effect prediction, protein design, functional annotation

**Biomedical Language Models (Text-Based)**
- **Input**: Natural language text (e.g., "The protein kinase phosphorylates...")
- **Vocabulary**: Tens of thousands of words/subword tokens
- **Training data**: Scientific literature, PubMed abstracts, clinical notes, biomedical corpora
- **What they learn**: Scientific concepts, relationships between entities, domain terminology
- **Examples**: PubMedBERT, BioBERT, SciBERT, BioGPT, Med-PaLM
- **Applications**: Literature mining, entity recognition, relation extraction, question answering, clinical NLP

**Why This Matters**

These two classes of models serve complementary roles:

1. **Different biological scales**: Text-based models understand conceptual relationships described in papers; sequence-based models understand molecular patterns in proteins themselves.

2. **Different knowledge sources**: Biomedical LMs capture human-interpreted knowledge from literature; protein LMs capture evolution's "knowledge" encoded directly in sequences.

3. **Not interchangeable**: You cannot use PubMedBERT to predict protein structure from sequence, nor can you use ESM to extract protein-protein interactions from a research paper.

4. **Potential synergy**: Some recent work explores combining both—using text-based models to extract functional annotations from literature and sequence-based models to validate or predict these functions from sequence alone.

```{note}
**When people say "protein language model"**, they typically mean sequence-based models (ESM, ProtTrans). However, some hybrid approaches are emerging that integrate both sequence and text information, such as models that jointly learn from protein sequences and their associated textual descriptions in databases.
```

### The Paradigm Shift: From Sequential to Direct Prediction

Traditionally, understanding protein function required following a sequential path: sequence → structure → function. PLMs have enabled a revolutionary shortcut:

```{mermaid}
graph LR
    A[Sequence] --> B[Structure] --> C[Function]
    A -.PLM.-> C
    
    style A fill:#e3f2fd
    style B fill:#fff3e0
    style C fill:#e8f5e9
```

**Traditional path**: Sequence → Structure → Function (solid arrows)  
**PLM-enabled**: Sequence → Function (dashed arrow) - direct prediction by learning evolutionary patterns

**Key insight**: PLMs are not designed to replace structural biology, but rather to better leverage the rich existing knowledge of proteins toward function understanding—without being limited by the lack of structure knowledge. They complement structural approaches by unlocking functional insights even when structures are unavailable or difficult to obtain.

## A Brief History: The Birth of Protein Language Models

The modern era began in 2020 with [ESM (Evolutionary Scale Modeling)](https://www.pnas.org/doi/full/10.1073/pnas.2016239118) by Rives et al. The fact that this work appeared in *PNAS* rather than a "higher-tier" journal hints at the initial skepticism—treating proteins as a language met considerable resistance. ESM's insight was deceptively simple: apply transformers directly to protein sequences, treating amino acids as tokens. Train on millions of UniRef sequences using masked language modeling. No structural information, no functional annotations—just sequences and their evolutionary patterns.

Almost simultaneously, [ProtTrans](https://ieeexplore.ieee.org/document/9477085) (Elnaggar et al.) arrived at a nearly identical solution. This convergence was no accident. Protein modeling had always borrowed from NLP—even profile HMMs are statistical language models. When BERT and GPT revolutionized language, it was only a matter of time before transformers transformed protein analysis.

Not everyone followed the naive single-amino-acid approach. [DISAE](https://pubs.acs.org/doi/full/10.1021/acs.jcim.0c01285) (Cai et al., 2021) innovated at the vocabulary level: using amino acid **triplets** as tokens (capturing local structural motifs) and selecting only the ~210 most conserved MSA positions (focusing on functionally critical residues). While more domain-specific, DISAE achieved superior performance for chemical-protein interactions, especially for remote homologs.

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
- **Small molecule drug discovery**: PLMs enable genome-wide prediction of chemical-protein interactions for "dark" proteins (unknown ligands), as demonstrated by [PortalCG](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010851), identifying targets for currently undruggable proteins
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

