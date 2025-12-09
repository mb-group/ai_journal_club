# Understanding "Models": From Biology to Deep Learning

## Introduction

The word "model" means something quite different in biology versus deep learning, which creates confusion for biological researchers. This document provides a comprehensive comparison of different types of models to clarify these conceptual differences.

---

## Five Types of "Models" in Biology

### 1. Molecular Dynamics (MD) Simulation

**What it represents**: How molecules move over time based on physics

**Workflow**: Design → Use → Use → Use...

**How it's made**: 
- Start with structure model
- Apply force fields (equations from physics: bonds, angles, electrostatics, van der Waals)
- Simulate: calculate forces → move atoms → repeat millions of times (nanoseconds to microseconds)

**What you get**: Movie of molecular motion - how protein breathes, how drug binds, why mutations destabilize

**Interpretability**: VERY HIGH - every force is from known physics; you can pause and ask "why did that atom move?" → "because of this electrostatic repulsion"

**Timeline**: 
- Design (days) → Use immediately and forever
- Simulating 1 microsecond might take days/weeks of computing

**Key characteristic**: Same physics every time - design once, use repeatedly

---

### 2. Protein Structure Model

**What it represents**: Physical coordinates - where each atom sits in 3D space

**Workflow**: Collect data → Build/Solve → Use

**How it's made**: 
- *Experimental*: Crystallize → X-rays → electron density → fit atoms
- *Computational (traditional)*: Find similar proteins → align sequences → model by homology
- *Deep learning*: AlphaFold learns from sequences → predicts coordinates

**What you get**: Spatial arrangement you can visualize and measure - actual structural coordinates

**Interpretability**: HIGH - every atom has meaning; you can rotate it, zoom in, measure angles, design mutations

**Timeline**: Build (weeks-months) → Use immediately

**Key characteristic**: One structure per protein

---

### 3. Pharmacokinetic (PK) Model

**What it represents**: How drug moves through body compartments

**Workflow**: Design → Fit → Use → Update

**How it's made**: 
- **Design**: Write differential equations based on physiology
- **Fit**: Collect patient data → estimate parameters (clearance, volume)
- **Use**: Predict drug levels
- May refine parameters with more data

**What you get**: Parameters with clear biological meaning (clearance rate, volume of distribution, half-life)

**Interpretability**: HIGH - each equation term and parameter maps to a real physiological process

**Timeline**: Design (days) → Fit (hours-days) → Use

**Key characteristic**: Mechanistic equations with biologically interpretable parameters

---

### 4. Wet Lab Model

**What it represents**: A *living physical system* that approximates another system you can't easily study

**Workflow**: Establish → Maintain → Use → Use → Use...

**Examples**:
- Mouse model of Alzheimer's → represents human disease
- Cancer cell line → represents patient tumor
- Liver organoid → represents liver tissue

**How it's made**: 
- **Establish**: Generate mouse line, establish cell culture, grow organoid
- **Maintain**: Keep alive (feed mice, passage cells)
- **Use**: Run experiments repeatedly

**What you get**: Actual living biology you can perturb and measure

**Interpretability**: MEDIUM-HIGH - it's real biology, but doesn't perfectly match what it represents (mouse ≠ human, cell line ≠ tumor in body)

**Timeline**: Establish (months-years) → Maintain + Use (ongoing)

**Key characteristic**: Living system requires constant maintenance; the "model" is itself a complex system

---

### 5. Deep Learning Model

**What it represents**: Statistical patterns learned from data

**Workflow**: Design → Train → Use → Use → Use...

#### Phase 1: DESIGN (architecture engineering)
- Choose architecture (transformer, CNN, RNN)
- Decide: how many layers? what connections?
- Set hyperparameters (learning rate, etc.)
- *Model knows NOTHING yet - just empty structure*
- **Timeline**: Days to weeks

#### Phase 2: TRAIN (learning from data)
- Feed millions of examples
- Optimization algorithm adjusts billions of parameters
- Compute intensive: thousands of GPU-hours
- *Model learns patterns - becomes "useful"*
- **This is the expensive, critical step that doesn't exist for other models**
- **Timeline**: Hours to weeks (or months for largest models)

#### Phase 3: USE (inference/prediction)
- Frozen parameters - no more learning
- Input new data → get predictions
- Relatively cheap and fast
- *Like using any other model now*
- **Timeline**: Milliseconds per prediction, use indefinitely

**What you get**: Function that makes predictions but doesn't show its work - numbers that somehow encode patterns, useful for prediction but not directly interpretable

**Interpretability**: LOW - parameters don't map to biological concepts; you can't point to parameter #47,382,991 and say "this represents hydrophobicity"

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