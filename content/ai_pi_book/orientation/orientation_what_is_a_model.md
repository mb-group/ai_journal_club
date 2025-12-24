# Understanding "Models": From Biology to Deep Learning

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```



## Introduction

The word "model" means different things in biology versus deep learning. Biologists use wet lab models (cell lines, animal models), PKPD models (drug kinetics), mechanistic simulations (MD, structures), statistical models (regression), and deep learning models (pattern learners).

**This document compares MD, Structure, Biostatistics, and Deep Learning** because they represent the clearest contrast points along a computational spectrum—from pure mechanistic (physics-based) to pure empirical (pattern-based). We exclude wet lab models (actual biological systems, not computational representations) and PKPD models (hybrid mechanistic-statistical approaches) to focus on the extremes that clarify why deep learning feels alien to traditional computational biology.

---


## The Spectrum of "Model"

```
More Interpretable ←———————————————————————————————————————→ Less Interpretable
More Mechanistic ←———————————————————————————————————————→ More Empirical
Lower Complexity ←———————————————————————————————————————→ Higher Complexity

MD Simulation — Structure — Biostatistics — Deep Learning
(pure physics)                                  (pure pattern)
```

**Where they sit on the spectrum:**
- **MD Simulation**: Pure physics-based, fully mechanistic, limited scope (single molecule/system)
- **Structure**: Atomic-level reality, fully interpretable, limited scope (one protein)
- **Biostatistics**: Statistical associations with explicit effect sizes, moderate complexity (multiple variables)
- **Deep Learning**: Pure pattern recognition, minimal interpretability, handles high complexity (millions of features/examples)

---

## Key Contrasts

### What Each Model IS

| Model Type | What it Represents | What's Inside |
|------------|-------------------|---------------|
| **MD Simulation** | Molecular motion from physics | Force field equations |
| **Structure** | Atomic coordinates | Atoms and residues |
| **Biostatistics** | Explicit associations between variables | Regression coefficients, effect sizes |
| **Deep Learning** | Implicit high-dimensional patterns | Millions of learned weights/parameters |

### How Each is Built

| Model Type | Built From | Can Explain Each Part? | Number of Parameters |
|------------|------------|------------------------|---------------------|
| **MD Simulation** | Physics equations | Yes - every force traceable | ~10-100 physics parameters |
| **Structure** | Experimental data (X-ray, cryo-EM) or physics-based prediction (Rosetta uses energy functions) | Yes - "this is leucine at position 47" | ~1000s of atoms |
| **Biostatistics** | Mathematical assumptions + data | Yes - "this is the effect of age" | ~5-50 coefficients |
| **Deep Learning** | Patterns in data only | No - "this is neuron layer 47" | Millions to billions |

### Workflow Comparison

| Model Type | Design Phase | Learning/Fitting | Ready to Use |
|------------|-------------|------------------|--------------|
| **MD Simulation** | Set physics equations | None - physics is universal | Immediately |
| **Structure** | Set up experiment | Data collection | After solving |
| **Biostatistics** | Choose model form (linear, Cox, logistic) | Fit coefficients (moderate) | After fitting + validation |
| **Deep Learning** | Architecture only | **Train millions of parameters (expensive!)** | Only after extensive training |

---

## The Critical Difference: The Training Phase

### Traditional Models: Design Encodes Understanding

When you design traditional models, you're encoding your knowledge:
- **MD simulation**: "Atoms repel at short distances" → van der Waals equation
- **Biostatistics**: "Age affects survival" → proportional hazards with age coefficient

**Design IS the model** - fitting is just calibrating predefined, interpretable parameters

### Deep Learning: Design ≠ Understanding

When you design a neural network architecture:
- "Stack 12 transformer layers with 16 attention heads"
- This is just scaffolding - an empty container with no biological knowledge

**The model doesn't exist until training!** The architecture is useless without the learned weights.

---

## Example: Predicting Protein Stability

### Mechanistic Approach
1. **Design**: "Stability = f(hydrophobic burial, H-bonds, electrostatics)" - you write the equation based on biophysics
2. **Fit**: Maybe calibrate a few coefficients from experimental data
3. **Use**: Plug in new protein → get prediction

*You designed the model based on mechanistic understanding*

### Biostatistical Approach
1. **Design**: "log(Stability) = β₀ + β₁(hydrophobic%) + β₂(charge) + β₃(size)" - you choose functional form and features
2. **Fit**: Estimate coefficients using regression on experimental data (e.g., β₁ = 0.23, p < 0.001)
3. **Use**: Plug in new protein → get prediction + confidence interval + p-values

*You designed the functional form; fitting gives interpretable effect sizes*

### Deep Learning Approach
1. **Design**: "12 attention layers, 512 dimensions" - no biology or statistics here yet!
2. **Train**: Show 100M protein sequences for 2 weeks on 256 GPUs
   - Model adjusts 380M parameters to learn patterns
   - **This is where the "understanding" emerges** (but in uninterpretable form)
3. **Use**: Plug in new protein → get prediction (no effect sizes, no p-values)

*You designed the container; training filled it with learned patterns*

---

## Conversational Examples

### With Mechanistic Models (MD, Structure):
- "Why does this protein fold?" → "Because these hydrophobic residues cluster away from water"
- "Why did the protein unfold in MD?" → "This salt bridge broke at 340K, reducing stability by 15 kcal/mol"

### With Biostatistical Models:
- "Does smoking increase cancer risk?" → "Yes, HR = 2.3 (95% CI: 1.8-2.9), p < 0.001"
- "Is age associated with disease progression?" → "Each year increases odds by β = 0.12 (SE = 0.03)"
- "What predicts survival?" → "Stage IV reduces median survival by 18 months (p < 0.0001)"

### With Deep Learning:
- "Why does this model think this protein binds DNA?" → "Because neuron activations in layer 23 are high, which correlates with DNA-binding in training data"
- "What features matter most?" → "...attention weights suggest sequence position 45-78 matters, but we can't say why"

**The difference:** 
- **Biostatistics** gives you explicit, testable associations with uncertainty quantification
- **Deep learning** gives you predictions without explicit associations or statistical inference

---

## Why This Confuses Biologists

For biologists and biostatisticians, "model" traditionally means:

1. **Something simpler than reality** (MD simplifies to force fields; Cox regression simplifies survival to a few covariates)
2. **Something you can reason through** (I can trace cause → effect, or interpret β coefficients)
3. **Something that explains** (tells you *why*, not just *what*)

Deep learning violates all three expectations:

1. **More complex** - billions of parameters vs. a handful of interpretable coefficients
2. **Can't reason through** - no human can trace input → output through millions of weights
3. **Doesn't explain** - predicts without mechanistic insight or interpretable effect sizes

**The confusion is semantic:** Deep learning is a "model" in the **computer science sense** (a parameterized function learned from data), but NOT in the **traditional biological/statistical sense** (an interpretable simplification that explains mechanisms).

### The Training Phase is Alien to Biology

In traditional biology, you don't usually build something that starts empty, feed it massive data to "learn," and end with something useful but opaque. Even directed evolution or mouse training don't match this pattern—because:
- **Training is the expensive part** - ESM-2 training cost ~$1M in compute
- **Design is relatively cheap** - architecture is reusable
- **The value is in the trained weights** - you download "ESM-2-650M" (someone else did the training), but you can't download "the physics" or "the regression"

---

## Practical Implications

**Updating models:**
- **Biostatistics**: Add new covariates → refit regression (minutes to hours)
- **Deep learning**: Get new data → might need to retrain entire model (days to weeks, $$$!)

**Interpreting results:**
- **Mechanistic/Biostatistics**: Trace mechanisms or get explicit effect sizes (β = 0.23, p < 0.001)
- **Deep learning**: Black box predictions—you can visualize attention weights but can't explain mechanisms

**Models as artifacts:**
- You download "ESM-2-650M" (pre-trained weights) but implement physics/regression yourself
- This is like downloading a trained dog vs. downloading the laws of genetics

---



## Key Takeaway

Deep learning models are fundamentally different from both mechanistic models and biostatistical models:

| Aspect | Mechanistic (MD) | Biostatistical | Deep Learning |
|--------|-----------------|----------------|---------------|
| **What it captures** | Physical/biological mechanisms | Explicit statistical associations | Implicit high-dimensional patterns |
| **Parameters** | Few, interpretable | Few to moderate, interpretable (β, HR, OR) | Millions, uninterpretable |
| **Output** | Mechanistic predictions | Effect sizes + p-values + CI | Point predictions |
| **Purpose** | Understanding mechanisms | Inference & hypothesis testing | High-performance prediction |
| **When training matters** | No training (physics is universal) | Quick fitting (interpretable) | Expensive training (black box) |

**Bottom line:** Deep learning models are **compressed recordings of patterns in data** rather than **explanations of mechanisms** or **explicit quantifications of associations**. They're incredibly useful for prediction but require additional work to extract biological understanding or perform statistical inference.

**The critical insight:** The expensive training phase—where billions of parameters adjust to capture patterns—fundamentally changes what a "model" means compared to traditional approaches.