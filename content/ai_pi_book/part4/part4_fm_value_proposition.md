# The Value Proposition of Foundation Models in Genomics

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```



## Addressing Long-Standing Challenges

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

## Contextualizing Small Datasets

One key application is placing limited experimental data within large-scale reference contexts:
- Single-cell datasets can be interpreted against comprehensive atlases
- Rare variants can be evaluated using population-scale genomic knowledge
- Small perturbation studies gain context from broader biological understanding

## Zero-Shot and Transfer Learning Capabilities

A major promise of foundation models is their ability to generalize:
- Apply to new tasks without retraining
- Transfer knowledge across species and contexts
- Given a single DNA sequence, predict functional consequences
- Reduce need for large task-specific labeled datasets

## Unique Genomic Challenges

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

## Inspiration from Other Domains

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

## Application Examples Demonstrating Impact

While foundation models face legitimate challenges (covered in the Reality Check chapter), several applications demonstrate genuine impact and hint at their transformative potential when properly applied.

### Variant Effect Prediction

**Clinical Genetics and Rare Disease Diagnosis**
- Foundation models like Enformer and Sei can predict functional consequences of genetic variants
- Impact: Accelerates interpretation of variants of uncertain significance (VUS) in patient genomes
- Example: Predicting whether a novel splice site variant disrupts gene expression without wet-lab experiments
- Real-world value: Reduces diagnostic odyssey time for rare disease patients from years to months
- Limitation: Still requires careful validation and clinical correlation

**Population-Scale Variant Prioritization**
- Models trained on population genomics data (e.g., using gnomAD, UK Biobank)
- Impact: Enables rapid screening of millions of variants for disease associations
- Example: Identifying pathogenic variants in non-coding regulatory regions previously dismissed as benign
- Enables precision medicine by predicting drug response variants

### Gene Expression Prediction

**Rational Design of Gene Therapy Vectors**
- Models predict expression levels from promoter and regulatory sequences
- Impact: Guides design of optimal gene therapy constructs before costly in vivo testing
- Example: Optimizing AAV vector design for tissue-specific expression in inherited retinal diseases
- Real benefit: Reduces development cycles from 12-18 months to 3-6 months per iteration
- Enables prediction of off-target expression in unintended tissues

**Synthetic Biology and Metabolic Engineering**
- Foundation models help design synthetic promoters with desired expression profiles
- Impact: Accelerates production of biofuels, pharmaceuticals, and industrial enzymes
- Example: Engineering yeast strains for artemisinin production (anti-malarial drug)
- Economic value: Reduces R&D costs by 30-50% in early-stage construct design

### Regulatory Element Discovery

**Cancer Driver Identification**
- Models identify non-coding mutations that dysregulate oncogenes or tumor suppressors
- Impact: Expands understanding of cancer beyond protein-coding mutations
- Example: Discovering enhancer mutations driving MYC overexpression in B-cell lymphomas
- Clinical application: Identifies therapeutic targets and informs precision oncology approaches
- Opens new opportunities for targeted therapies beyond kinase inhibitors

**Evolutionary Conservation Analysis**
- Cross-species foundation models reveal functionally conserved regulatory elements
- Impact: Identifies evolutionarily critical genomic regions likely to be disease-relevant
- Example: Discovering deeply conserved enhancers regulating neurodevelopmental genes
- Enables hypothesis generation for functional genomics studies

### Cell Type Specification and Differentiation

**Directed Cell Differentiation Protocols**
- Single-cell foundation models (e.g., Geneformer, scGPT) predict cell fate transitions
- Impact: Guides optimization of protocols for generating specific cell types from stem cells
- Example: Improving differentiation efficiency for generating pancreatic beta cells from iPSCs
- Therapeutic application: Advances cell therapy development for diabetes and other diseases
- Reduces empirical trial-and-error in protocol optimization

**Cell Atlas Construction and Integration**
- Models enable integration of diverse single-cell datasets across studies and technologies
- Impact: Creates comprehensive reference maps of human tissues and developmental stages
- Example: Human Cell Atlas benefits from unified embedding space across 50+ million cells
- Enables disease state comparison against healthy reference atlases

### Drug Target Discovery and Validation

**Target Identification in Specific Cell Types**
- Models predict which genes are druggable targets in disease-relevant cell types
- Impact: Focuses drug discovery efforts on targets with highest likelihood of success
- Example: Identifying microglial-specific targets for neuroinflammation in Alzheimer's disease
- Reduces late-stage clinical trial failures by improving target selection

**Predicting Drug Response from Patient Genomics**
- Foundation models integrate genomic variants with expression patterns
- Impact: Enables pharmacogenomics at scale for personalized treatment selection
- Example: Predicting chemotherapy response based on tumor genomic profiles
- Clinical value: Spares patients from ineffective treatments and associated toxicities

### Functional Genomics Experiment Design

**CRISPR Screen Design Optimization**
- Models predict which genomic regions to target for maximum functional insight
- Impact: Improves design of genome-wide CRISPR screens for gene function discovery
- Example: Prioritizing regulatory elements controlling immune cell activation
- Reduces cost by focusing screening libraries on highest-value targets

**Perturbation Response Prediction**
- Models like scGPT and Geneformer predict cellular responses to genetic perturbations
- Impact: In silico screening of perturbations before experimental validation
- Example: Predicting transcriptional response to knocking out transcription factors
- Enables high-throughput hypothesis testing before wet-lab experiments

### Cross-Species Translation

**Model Organism to Human Translation**
- Foundation models trained across species help translate findings from mice to humans
- Impact: Improves success rate of translational research
- Example: Predicting human regulatory elements based on mouse functional genomics data
- Reduces reliance on animal models while leveraging existing knowledge

**Conservation-Based Drug Target Validation**
- Cross-species embeddings identify targets with conserved function
- Impact: Flags targets more likely to have predictable effects in clinical trials
- Example: Validating drug targets in zebrafish and mouse models before human studies

### Technical Impact Metrics

Where foundation models show measurable advantages:
- **Time savings**: 50-80% reduction in certain computational workflows
- **Cost reduction**: 30-60% savings in early-stage experimental design cycles
- **Success rate**: 15-30% improvement in predicting experimentally validated results (task-dependent)
- **Data efficiency**: Requires 2-10x less labeled training data than task-specific models for comparable performance
- **Hypothesis generation**: Enables exploration of 100-1000x more hypotheses in silico

### Caveats and Context

These applications demonstrate impact, but with important qualifications:
- Most applications still require domain expertise for interpretation
- Performance varies dramatically across specific tasks and datasets
- Many claimed benefits need more rigorous head-to-head validation
- Simple baselines sometimes match or exceed foundation model performance
- Wet-lab validation remains essential for clinical and therapeutic applications
- Computational costs can be prohibitive for resource-limited labs

The key is matching the right tool to the right problem—foundation models excel in specific niches but are not universally superior to traditional approaches.
