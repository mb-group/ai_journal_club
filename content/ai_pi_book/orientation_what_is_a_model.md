# Understanding "Models": From Biology to Deep Learning

## Introduction

The word "model" means something quite different in biology versus deep learning, which creates confusion for biological researchers. This document provides a comprehensive comparison of different types of models to clarify these conceptual differences.

---


## The Spectrum of "Model"

```
More Interpretable ←——————————————————————→ Less Interpretable
More Mechanistic ←——————————————————————→ More Empirical

MD Simulation ——— Structure ——— PK ——— Wet Lab ——— Deep Learning
(pure physics)                                      (pure pattern)
```

---

## Key Contrasts

### What Each Model IS

| Model Type | What it Represents | What's Inside |
|------------|-------------------|---------------|
| **MD Simulation** | Molecular motion from physics | Force field equations |
| **Structure** | Atomic coordinates | Atoms and residues |
| **PK Model** | Drug movement through body | Compartments and rates |
| **Wet Lab** | Living approximation | Actual biological system |
| **Deep Learning** | Statistical patterns | Millions of weights/parameters |

### How Each is Built

| Model Type | Built From | Can Explain Each Part? | Number of Parameters |
|------------|------------|------------------------|---------------------|
| **MD Simulation** | Physics equations | Yes - every force traceable | ~10-100 physics parameters |
| **Structure** | Experimental data or prediction | Yes - "this is leucine at position 47" | ~1000s of atoms |
| **PK Model** | Physiological principles | Yes - "this is liver clearance" | ~5-10 parameters |
| **Wet Lab** | Actual biology | Partly - but complex | Billions of molecules |
| **Deep Learning** | Patterns in data | No - "this is neuron layer 47" | Millions to billions |

### Workflow Comparison

| Model Type | Design Phase | Learning/Fitting | Ready to Use |
|------------|-------------|------------------|--------------|
| **MD Simulation** | Set physics equations | None - physics is universal | Immediately |
| **Structure** | Set up experiment | Data collection | After solving |
| **PK Model** | Write equations | Fit ~5-10 parameters (quick) | After fitting |
| **Wet Lab** | Generate/establish | Growing/maintaining | After establishment |
| **Deep Learning** | Architecture only | **Train millions of parameters** | Only after training |

---

## The Critical Difference: The Training Phase

### Other Models: Design = Understanding

When you design an MD simulation or PK model, you're encoding your understanding:
- "Atoms repel at short distances" → van der Waals equation
- "Drugs clear through the liver" → clearance parameter

**Design IS the model** - there's no separate "learning" phase

### Deep Learning: Design ≠ Understanding

When you design a neural network architecture:
- "Stack 12 transformer layers with 16 attention heads"
- This is just scaffolding - an empty container

**The model doesn't exist until training!**

---

## Example: Predicting Protein Stability

### Traditional Approach (like PK model)
1. **Design**: "Stability = f(hydrophobic burial, H-bonds, electrostatics)" - you write the equation based on biophysics
2. **Fit**: Maybe calibrate a few coefficients from experimental data
3. **Use**: Plug in new protein → get prediction

*You designed the model based on understanding*

### Deep Learning Approach
1. **Design**: "12 attention layers, 512 dimensions" - no biology here yet!
2. **Train**: Show 100M protein sequences for 2 weeks on 256 GPUs
   - Model adjusts 380M parameters to learn patterns
   - **This is where the "understanding" emerges** (but in uninterpretable form)
3. **Use**: Plug in new protein → get prediction

*You designed the container; training filled it with learned patterns*

---

## Conversational Examples

### With Structure or PK Models:
- "Why does this drug clear slowly?" → "Because the clearance parameter is 0.05 L/hr"
- "Why does this protein fold?" → "Because these hydrophobic residues cluster away from water"
- "Why did the protein unfold in MD?" → "This salt bridge broke at 340K, reducing stability by 15 kcal/mol"

### With Deep Learning:
- "Why does this model think this protein binds DNA?" → "Because neuron activations in layer 23 are high, which correlates with DNA-binding in training data"

**It's more like asking**: "Why does your brain recognize your mother's face?" The pattern is *encoded* but not *explicit*.

---

## Why This Confuses Biologists

For biologists, "model" traditionally means:

1. **Something simpler than reality** (MD simplifies to force fields; mouse is simpler than human)
2. **Something you can reason through** (I can trace cause → effect)
3. **Something that explains** (tells you *why*, not just *what*)

Deep learning breaks all three:

1. **More complex** - billions of parameters vs. real biology
2. **Can't reason through** - no human can trace input → output
3. **Doesn't explain** - predicts without mechanistic insight

**It's a model in the statistical sense** (mathematical function fitted to data) but not in the biological sense (simplified representation of mechanism).

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
- **PK model**: Get new patient data → refit parameters (quick)
- **Deep learning**: Get new data → might need to retrain entire model (expensive!)

### You can't easily inspect what was learned:
- **MD simulation**: "Why did it unfold?" → trace forces step by step
- **Deep learning**: "Why this prediction?" → ...look at billions of weights?

### The model is a trained artifact:
- You can download "ESM-2-650M" - someone else did the expensive training
- You can't download "the physics" - you just implement it yourself
- This is more like downloading a trained dog vs. downloading the laws of genetics

---

## Summary: The Three-Phase Life

```
Traditional Biology Model:
Design (encode understanding) ——————————→ Use

Deep Learning Model:
Design (create container) → Train (learn patterns) → Use
                              ↑
                    This phase is unique and expensive
                    This is where patterns are learned
                    This is why it's a black box
```

---

## Key Takeaway

Deep learning models are more like **compressed recordings of patterns in data** rather than **explanations of how systems work**. 

They're incredibly useful for prediction but require additional work (like mechanistic interpretability) to extract biological understanding.

The critical insight: **The training phase is where the magic happens** - where billions of parameters adjust to capture patterns - but this phase doesn't exist in traditional biological models, and the result is opaque in a way that traditional models are not.