# Chapter 5: Conformational Properties of Polypeptide Chains

## Peptide

### Pepflow - Peptide conformation sampling from energy landscape

- **Input**: peptide sequence
- **Output**: all-atom sampling conformations
- **Training data**: peptide and protein fragments from PDB; md simulation of antimicrobial activity and structure peptide database
- **Technical highlight**: transferable, generative, diffusion, equivalent flow, hypernetwork-conditioned
- **GitHub**: Available
- **Paper**: Nature Machine Intelligence 2024
- **Name to choose on playground**: `pepflow_env`

### Target-specific peptide inhibitor

- **Inference stage**
  - Input: none
  - Output: peptide sequence in generative mode, than use classic methods to predict target specific binding affinity for screening purpose
- **Training stage**
  - Input: peptide sequence
  - Output: peptide sequence (just to recover the input but enable the possibility to generate peptide)
- **GitHub**: Available
- **Paper**: Nature Communication 2024
- **Name on playground**: `target_peptide`

### Antibiotic peptide discovery

- **Inference stage**
  - Input: peptide sequence
  - Output: probability to be antibiotic
- **Training stage**: same as inference stage on the difference on what data set to trained is with known annotation of whether antibiotic, while at inference stage on new data set
- **GitHub**: Available
- **Paper**: Nature Biomedical Engineering 2024
- **Name on playground**: `apex`

### Self-assembling peptide discovery

- **Inference stage**
  - Input: sliding over proteins to create in silico peptide
  - Output: aggregation score
- **Training stage**
  - Input: peptide
  - Output: aggregation score, and some other scores given knowledge of self-assembling
- **GitHub**: Available
- **Paper**: Nature Machine Intelligence 2024
- **Name on playground**: `ml_peptide_self_assembly`

## IDR (Intrinsically Disordered Regions)

### Feature Discovery

#### ReverseHomology - finds IDR feature

- **Paper**: PLOS Computational Biology 2022
- *(not replicable from original github repo)*

#### AIUPred - deep learning version of Balint's work

- **Paper**: NAR 2024
- **Name to choose on playground**: `fabric`

### Property Prediction

#### DisoFLAG - jointly predicts both IDR and its function

- **Inference**
  - Input: protein sequence
  - Output: IDR, 6 functions (protein-binding, DNA-binding, RNA-binding, ion-binding, lipid-binding, flexible linker)
- **Technical highlight**: assume the 6 functions has some correlation to be learned, using GNN
- **GitHub**: Available
- **Paper**: BMC Biology 2024
- **Name to choose on playground**: `disoflag`

### Conformation

#### ALBATROSS - predict sequence-dependent IDR ensemble properties

- **Training**: *[to be specified]*
- **Inference**
  - Input: protein sequence
  - Output: ensemble dimensions including radius of gyration, end-to-end distance, polymer-scaling exponent, ensemble asphericity
- **Technical highlights**: generated training data using classical methods; LSTM modeling
- **GitHub**: Available
- **Paper**: Nature Methods 2024
- *(its own github under maintenance, not replicable from original repo)*

#### idpSAM - generates IDR conformation, with promise on generalization

- **Technical highlights**: diffusion, transformer
- **GitHub**: Available
- **Paper**: PLOS Computational Biology 2024
- **Name to choose on playground**: `idpsam`