# Chapter 11: Regulatory Circuits

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```



## Gene Regulatory Network Prediction

### Foundation Models

#### GeneCompass: Cross-Species Gene Regulatory Mechanisms
- **Description**: Knowledge-informed cross-species foundation model for gene regulation
- **Input**: Single-cell transcriptional profile, species information
- **Output**: Universal embedding vector for gene regulatory mechanisms
- **Publication**: Cell Research 2024
- **DOI**: https://doi.org/10.1038/s41422-024-01034-y
- **Technical Highlights**: 
  - Universal embeddings applicable to downstream tasks
  - Integrates GRN context, species information, cell types, promoter sequences, co-expression
- **Application Notes**: 
  - Generalization to bulk-seq is a concern
  - Downstream task performance not fully evaluated in paper

### GRN-Guided Simulation

#### GRouNdGAN: GRN-Guided Single Cell RNA-seq Simulation
- **Description**: GRN-guided simulation for in silico perturbation experiments
- **Input**: Gene regulatory network structure, baseline expression
- **Output**: Simulated single-cell expression under perturbations
- **GitHub**: Available
- **Paper**: Nature Communication 2024
- **Core Technology**: Generative Adversarial Networks (GANs)
- **Model Usage**: Synthesize cells under new conditions for in silico TF knockout experiments

#### LINGER: Gene Regulatory Network Inference from Single-Cell Multiome
- **Description**: Infer gene regulatory networks from single-cell multi-omics data
- **Input**: Single-cell RNA-seq and ATAC-seq data
- **Output**: Gene regulatory network predictions
- **GitHub**: Available
- **Paper**: Nature Biotechnology 2024
- **Application**: Multi-omics GRN reconstruction

### Dynamic and Developmental GRNs

#### Dictys: Dynamic Gene Regulatory Networks
- **Description**: Dynamic GRN inference across developmental continuum
- **Input**: Time-course single-cell data
- **Output**: Dynamic gene regulatory networks
- **Paper**: Nature Methods 2023
- **Application**: Developmental biology, cell differentiation

#### SCENIC+: Enhanced Single-Cell Regulatory Network Analysis
- **Description**: Enhanced version of SCENIC for regulatory network inference
- **Input**: Single-cell RNA-seq data
- **Output**: Cell-type-specific regulatory networks
- **Paper**: Nature Methods 2023
- **Application**: Cell-type-specific regulation analysis

#### Additional GRN Methods
- **Description**: Comprehensive review of GRN inference methods
- **Paper**: Briefings in Bioinformatics 2025
- **URL**: https://academic.oup.com/bib/article/26/2/bbaf089/8068119
- **Application**: Method comparison and selection

### Specialized GRN Applications

#### Discogen: Discriminative Gene Network Analysis
- **Description**: Discriminative approach to gene network inference
- **Paper**: Available
- **Application**: Disease-specific network analysis

## Perturbation Prediction

### Transcriptional Response Prediction

#### Prediction of Perturbed Transcriptional Response
- **Description**: Predicting transcriptional changes from perturbations
- **Input**: Baseline expression, perturbation information
- **Output**: Predicted transcriptional response
- **Paper**: Available
- **Note**: Some studies suggest it's not significantly better than linear models
- **Application**: Drug discovery, systems biology

#### Alternative Perturbation Methods
- **Description**: Alternative approaches to perturbation prediction
- **Papers**: Multiple available
- **Application**: Comparative analysis of perturbation methods

### Benchmark Platforms

#### PertEval-scFM: Perturbation Evaluation for Single-Cell Foundation Models
- **Description**: Benchmark platform for evaluating perturbation prediction models
- **Paper**: NIPS 2024
- **Application**: Model evaluation and comparison

#### PerturbBench: Perturbation Benchmarking Platform
- **Description**: Comprehensive benchmark for perturbation prediction methods
- **GitHub**: Available
- **Application**: Standardized evaluation of perturbation models

### Advanced Perturbation Models

#### PRnet: Perturbation Response Network
- **Description**: Network-based perturbation response prediction
- **Publication**: Predicting transcriptional responses to novel chemical perturbations using deep generative model for drug discovery
- **Journal**: Nature Communications 15, 9256 (2024)
- **DOI**: https://doi.org/10.1038/s41467-024-53457-1
- **Input**: SMILES strings, unperturbed transcriptional profile (single cell or bulk)
- **Output**: Perturbed transcriptional profile, up/down-regulated gene sets, drug ranking
- **Technical Highlights**: 
  - Handles both single-cell and bulk data
  - Considers drug dosage effects
- **Application Notes**: Generalization across cell types is a concern

#### PDGrapher: Combinatorial Perturbation Prediction
- **Description**: Causally-inspired neural networks for therapeutic perturbation prediction
- **GitHub**: Available
- **Application**: Combinatorial drug prediction

#### SAMS-VAE: Structured Perturbation Model
- **Description**: Structured approach to perturbation modeling using VAE
- **Paper**: NIPS 2023
- **Application**: Structured perturbation analysis

### Cellular Response Models

#### Cellular Response Modeling
- **Description**: Models for predicting cellular responses to perturbations
- **Paper**: ICLR 2023
- **Application**: Cell biology, drug screening

#### CPA: Compositional Perturbation Autoencoder
- **Description**: Autoencoder for compositional perturbation analysis
- **Paper**: Molecular Systems Biology 2023
- **Application**: Multi-factor perturbation analysis

#### RECOVER: Drug Combination Prediction
- **Description**: Model for predicting drug combination effects
- **Paper**: Cell Reports 2023
- **Application**: Combination therapy design

### Advanced Modeling Approaches

#### Optimal Transport Methods
- **Description**: Optimal transport for perturbation analysis
- **Paper**: Nature Methods 2023
- **Application**: Single-cell perturbation analysis

#### GEARs: Gene Expression Analysis of Response
- **Description**: Analysis of gene expression responses to perturbations
- **Paper**: Nature Biotechnology 2023
- **Application**: Response mechanism analysis

### Lineage and Developmental Responses

#### PORCELAIN: Lineage-Related Gene Expression Analysis
- **Description**: Analysis of lineage-related gene expression changes
- **Paper**: Nature Communication 2025
- **Application**: Developmental biology, cell fate analysis

#### Salt&Paper: Causal Simulation Framework
- **Description**: Framework for causal simulation in biology
- **Paper**: Available
- **Application**: Causal inference in biological systems

### Advanced Causal Models

#### Causal Simulation Models
- **Description**: Advanced causal simulation approaches
- **Papers**: Multiple available including Nature MI 2023
- **Application**: Mechanistic understanding of biological processes

#### Generative Intervention Model for Causal Perturbation
- **Description**: Generative approach to causal perturbation modeling
- **Paper**: Available
- **Application**: Causal intervention analysis

#### scCausalVI: Single-Cell Causal Variational Inference
- **Description**: Causal variational inference for single-cell data
- **Paper**: Available
- **Application**: Causal analysis in single-cell studies

#### GPO-VAE: Gene Perturbation Outcome VAE
- **Description**: VAE for predicting gene perturbation outcomes
- **Paper**: Available
- **Application**: Perturbation outcome prediction

### Data Resources and Benchmarks

#### scPerturb: Single-Cell Perturbation Database
- **Description**: Comprehensive database of single-cell perturbation studies
- **URL**: https://www.nature.com/articles/s41592-023-02144-y
- **Application**: Data resource for perturbation studies

#### Interpretable Perturbation Analysis
- **Description**: Methods for interpretable analysis of perturbation effects
- **URL**: https://www.cell.com/cell-systems/abstract/S2405-4712(25)00078-X
- **Application**: Mechanistic interpretation of perturbation effects