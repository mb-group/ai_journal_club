# Chapter 3: Evolutionary and Genetic Origins of Protein Sequences

## Protein Language Models Capturing Evolution Info

### ESM and Its Many Variants

#### Original ESM

- **Model codename in playground**: `esm`
- **Vocabulary**: amino acids
- **Model usage**
  - Input: protein amino acid sequence
  - Output: an embedding
- **Training**
  - Input: protein amino acid sequence, with parts masked
  - Output: prediction of what's the masked amino acids
- **GitHub**: Available
- **Paper**: Available
- **Core-tech**: language model, masked training, transformer
- **Rationale**: if a model is able to predict masked "words", it knows the "grammar"
- **Biology interpretation**: given that the model is trained on all known protein sequence, the learned "grammar" is the learned law of evolution

#### ESM-AA - At both atom-scale and residue-scale

- **Model codename in playground**: `esm-aa`
- **Vocabulary**
  - Amino acids
  - Atoms: a spatial distance matrix that directly encodes 3D position of atoms of each residue
- **Model usage & training**: basically the same as original ESM
- **GitHub**: Available
- **Paper**: ICML 2024
- **Core tech**: multi-scale code-switch

#### CNN PLM

- **Model codename in playground**: `cnn_plm`
- **Model usage & training**: basically the same as original ESM
- **GitHub**: Available
- **Paper**: Cell Systems 2024
- **Core tech**: CNN
- **Core argument**: Transformer as the architecture is not the key to a powerful protein language model; CNN is good too as replacement; the key is masked training scheme to learn grammar to evolution

#### LASE - Learned Ancestral Sequence Embedding

- **Model codename in playground**: `lase`
- **Model usage**
  - Input: protein sequence
  - Output: protein embedding, which supposed to have better predictive power downstream because of ancestral info carried
- **Training**
  - Input: sequence generated using multiplexed ancestral sequence reconstruction
  - Output: *[to be specified]*
- **GitHub**: Available
- **Paper**: Nature Machine Intelligence 2024
- **Core tech**: multiplexed ancestral sequence reconstruction; protein LM