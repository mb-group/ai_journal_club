# Understanding "Models": From Biology to Deep Learning

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```



## Introduction

The word "model" means something quite different in biology versus deep learning, which creates confusion for biological researchers. This document provides a comprehensive comparison of different types of models to clarify these conceptual differences.

---


## The Spectrum of "Model"

```
More Interpretable ←———————————————————————————————————————→ Less Interpretable
More Mechanistic ←———————————————————————————————————————→ More Empirical

MD Simulation — Structure — PK — Biostatistics — Wet Lab — Deep Learning
(pure physics)                                                  (pure pattern)
```

**Where they sit on the spectrum:**
- **MD Simulation**: Pure physics-based, fully mechanistic
- **Structure**: Atomic-level reality, fully interpretable
- **PK Models**: Physiologically-grounded with interpretable parameters
- **Biostatistics**: Statistical associations with explicit effect sizes
- **Wet Lab Models**: Complex biology, partially understood
- **Deep Learning**: Pure pattern recognition, minimal interpretability

---

### Deep learning models as statistical association learners

A trained deep learning model is best understood as a **learned representation of statistical association patterns** between inputs and outputs.  
These associations are high-dimensional, implicit, and distributed across the model's parameters—not interpretable in the way traditional statistical models are.

### Comparison: Deep learning associations vs. biostatistical associations

Although both deep learning and classical biostatistics deal with "associations," the nature of these associations is fundamentally different.

#### **Biostatistical association**
- Explicit and interpretable  
- Parameters correspond to meaningful effect sizes (e.g., β coefficients, hazard ratios)  
- Built on predefined functional forms and assumptions (linearity, proportional hazards, independence)  
- Designed for explanation, inference, and hypothesis testing  
- Low- to moderate-dimensional structure  

#### **Deep learning association**
- Implicit and distributed across millions of parameters  
- No predefined functional form; the model discovers complex nonlinear relationships  
- Not directly interpretable; does not yield effect sizes or p-values  
- Designed for high-performance prediction rather than causal inference  
- Naturally suited for high-dimensional, unstructured data (images, sequences, text)

### Summary

- **Biostatistics** → interpretable, assumption-driven, low-dimensional associations  
- **Deep learning** → high-dimensional, assumption-light, representation-based associations  

Both operate on the idea of "association," but they do so in **fundamentally different ways and for different scientific purposes**.

---

## Key Contrasts

### What Each Model IS

| Model Type | What it Represents | What's Inside |
|------------|-------------------|---------------|
| **MD Simulation** | Molecular motion from physics | Force field equations |
| **Structure** | Atomic coordinates | Atoms and residues |
| **PK Model** | Drug movement through body | Compartments and rates |
| **Biostatistics** | Explicit associations between variables | Regression coefficients, effect sizes |
| **Wet Lab** | Living approximation | Actual biological system |
| **Deep Learning** | Implicit high-dimensional patterns | Millions of learned weights/parameters |

### How Each is Built

| Model Type | Built From | Can Explain Each Part? | Number of Parameters |
|------------|------------|------------------------|---------------------|
| **MD Simulation** | Physics equations | Yes - every force traceable | ~10-100 physics parameters |
| **Structure** | Experimental data or prediction | Yes - "this is leucine at position 47" | ~1000s of atoms |
| **PK Model** | Physiological principles | Yes - "this is liver clearance" | ~5-10 parameters |
| **Biostatistics** | Mathematical assumptions + data | Yes - "this is the effect of age" | ~5-50 coefficients |
| **Wet Lab** | Actual biology | Partly - but complex | Billions of molecules |
| **Deep Learning** | Patterns in data only | No - "this is neuron layer 47" | Millions to billions |

### Workflow Comparison

| Model Type | Design Phase | Learning/Fitting | Ready to Use |
|------------|-------------|------------------|--------------|
| **MD Simulation** | Set physics equations | None - physics is universal | Immediately |
| **Structure** | Set up experiment | Data collection | After solving |
| **PK Model** | Write equations | Fit ~5-10 parameters (quick) | After fitting |
| **Biostatistics** | Choose model form (linear, Cox, logistic) | Fit coefficients (moderate) | After fitting + validation |
| **Wet Lab** | Generate/establish | Growing/maintaining | After establishment |
| **Deep Learning** | Architecture only | **Train millions of parameters (expensive!)** | Only after extensive training |

---

## The Critical Difference: The Training Phase

### Traditional Models: Design Encodes Understanding

When you design traditional models, you're encoding your knowledge:
- **MD simulation**: "Atoms repel at short distances" → van der Waals equation
- **PK model**: "Drugs clear through the liver" → clearance parameter
- **Biostatistics**: "Age affects survival" → proportional hazards with age coefficient

**Design IS the model** - fitting is just calibrating predefined, interpretable parameters

### Deep Learning: Design ≠ Understanding

When you design a neural network architecture:
- "Stack 12 transformer layers with 16 attention heads"
- This is just scaffolding - an empty container with no biological knowledge

**The model doesn't exist until training!** The architecture is useless without the learned weights.

---

## Example: Predicting Protein Stability

### Mechanistic Approach (like PK model)
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

### With Mechanistic Models (MD, Structure, PK):
- "Why does this drug clear slowly?" → "Because the clearance parameter is 0.05 L/hr"
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

**The confusion is semantic:**
- Deep learning is a "model" in the **computer science/machine learning sense**: a parameterized function learned from data
- But it's NOT a "model" in the **traditional biological/statistical sense**: an interpretable simplification that explains mechanisms or provides explicit associations

This is why biostatisticians and biologists often feel uncomfortable with deep learning—it claims to "model" biology while abandoning the interpretability and explanatory power that traditionally define modeling in their fields.

---

## The Training Phase is Alien to Biology

In traditional biology, you don't usually:
- Build something that starts empty/useless
- Feed it massive data to "learn"
- End up with something useful but opaque

The closest biological analogies might be:
- **Directed evolution**: Start with random mutants → select for function → end with optimized protein (but you can sequence it and understand it)
- **Training a mouse**: Start with naive mouse → condition with rewards → get learned behavior (but the mouse is a black box)

But even these aren't quite right because:
- **Training is the expensive part** - for ESM-2 (protein language model), training cost ~$1M in compute
- **Design is relatively cheap** - architecture is reusable
- **The value is in the trained weights** - the parameters after training are what you actually use

---

## Practical Implications

### You can't just "update" a deep learning model like other models:
- **PK model**: Get new patient data → refit parameters (minutes)
- **Biostatistics**: Add new covariates → refit regression (minutes to hours)
- **Deep learning**: Get new data → might need to retrain entire model (days to weeks, $$$!)

### You can't easily inspect what was learned:
- **MD simulation**: "Why did it unfold?" → trace forces step by step
- **Biostatistics**: "What's the effect?" → β = 0.23, p < 0.001, here's the confidence interval
- **Deep learning**: "Why this prediction?" → ...look at billions of weights? Use attention visualization?

### Different outputs for different purposes:
- **Biostatistics**: Effect sizes, p-values, confidence intervals → inference and hypothesis testing
- **Deep learning**: Point predictions, maybe uncertainty estimates → high-performance prediction

### The model is a trained artifact:
- You can download "ESM-2-650M" - someone else did the expensive training
- You can't download "the physics" or "the regression" - you just implement them yourself
- This is more like downloading a trained dog vs. downloading the laws of genetics

---

## Summary: Model Development Lifecycle

```
Mechanistic Models (MD, PK):
Design (encode physics/biology) ——————————→ Use

Biostatistical Models:
Design (choose functional form) → Fit (estimate coefficients) → Use
                                   ↑ quick, interpretable

Deep Learning Models:
Design (create architecture) → Train (learn patterns) → Use
                                ↑
                    This phase is unique and expensive
                    This is where patterns are learned
                    This is why it's a black box
                    Millions of parameters adjusted
```

---

## Key Takeaway

Deep learning models are fundamentally different from both mechanistic models and biostatistical models:

| Aspect | Mechanistic (MD, PK) | Biostatistical | Deep Learning |
|--------|---------------------|----------------|---------------|
| **What it captures** | Physical/biological mechanisms | Explicit statistical associations | Implicit high-dimensional patterns |
| **Parameters** | Few, interpretable | Few to moderate, interpretable (β, HR, OR) | Millions, uninterpretable |
| **Output** | Mechanistic predictions | Effect sizes + p-values + CI | Point predictions |
| **Purpose** | Understanding mechanisms | Inference & hypothesis testing | High-performance prediction |
| **When training matters** | No training (physics is universal) | Quick fitting (interpretable) | Expensive training (black box) |

**Bottom line:**
- **Mechanistic models** → explain *how* systems work via physics/biology
- **Biostatistical models** → quantify *associations* with explicit effect sizes and statistical inference
- **Deep learning models** → learn *patterns* for prediction without explicit associations or mechanisms

Deep learning models are more like **compressed recordings of patterns in data** rather than **explanations of how systems work** or **explicit quantifications of associations**. 

They're incredibly useful for prediction but require additional work (like mechanistic interpretability or post-hoc statistical analysis) to extract biological understanding or perform statistical inference.

**The critical insight:** The training phase is where billions of parameters adjust to capture patterns—but this phase either doesn't exist (mechanistic models) or is quick and interpretable (biostatistics) in traditional approaches. Deep learning's expensive, opaque training process fundamentally changes what a "model" means.