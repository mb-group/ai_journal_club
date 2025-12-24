# Biology Needs ASI—Artificial Specific Intelligence, not AGI

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```

The popular narrative around artificial intelligence today revolves around **AGI**—Artificial General Intelligence—systems that can perform many diverse tasks across domains. ChatGPT, Claude, and Gemini are often framed this way.

But biological research does not need AGI. **Biology needs ASI—Artificial Specific Intelligence.**

---

## What Does This Mean?

Biological research demands **custom, context-specific AI models** that do not yet exist. These models must:

- Be tailored to **novel, non-shareable datasets** unique to each biological question
- Incorporate **deep domain understanding** of biological principles
- Adapt to specialized data types—single-cell RNA-seq, proteomics, spatial transcriptomics, imaging, clinical phenotypes
- Work with **limited labeled data** and domain-specific constraints
- Be **interpretable** and mechanistically transparent

These are not generic capabilities. They require specialized architectures, training strategies, and validation methods rooted in the specifics of biology.

---

## The Scale of the Problem: Severe Shortages

Biology is not facing one bottleneck—it is facing three distinct crises, each of which compounds the others.

### 1. Shortage in Scale
**Too few AI experts to meet thousands of biological questions.**

- Biology generates an enormous diversity of research questions, each requiring tailored AI approaches
- The number of trained AI researchers with biological expertise is vanishingly small
- Even large institutions often have only one or two people capable of bridging AI and biology meaningfully
- The ratio of biological questions to expert AI-biology practitioners is growing, not shrinking

This is not a temporary hiring problem. It is a structural mismatch in training pipelines and career paths.

### 2. Shortage in Quality
**Lack of integration between biological insight and AI modeling.**

Many collaborations between biologists and AI researchers fail not because of lack of effort, but because:

- AI researchers do not understand biological context, causality, or constraints
- Biologists do not understand what questions are tractable for AI or how to structure data
- Both groups use different standards for validation, rigor, and interpretability
- "Black box" models that predict accurately but explain nothing are scientifically insufficient

Bridging this gap requires individuals with **dual fluency**—people who can think both biologically and computationally. Such individuals are rare, and training programs to create them barely exist.

### 3. Shortage in Transparency
**Existing models are often opaque and not adaptable.**

- Many state-of-the-art AI models (including foundation models) are proprietary and closed
- Even open models are often incompletely documented
- Pretrained models are rarely reusable across biological contexts without significant retraining
- Biological datasets used in model training are often not shared due to patient privacy, proprietary concerns, or competitive pressures

This creates a paradox: AI models appear ubiquitous, yet biologists cannot **adapt, interrogate, or repurpose** them for their specific scientific questions.

---

## Why General-Purpose AI Is Not Enough

Foundation models like GPT-4 or general-purpose vision models are impressive, but they do not solve biological AI challenges:

- **Language models know text, not biology.** ChatGPT can summarize literature but cannot reason about protein folding constraints or gene regulatory logic.
- **Vision models trained on ImageNet cannot interpret microscopy.** Biological images (fluorescence, electron microscopy, histology) require domain-specific pretraining.
- **Multi-modal models lack biological grounding.** Integrating genomics, proteomics, and imaging requires more than concatenating embeddings.

Biological AI must be **specific by design**.

---

## What Biology Actually Needs

To address these shortages, the field requires:

1. **Custom, interpretable AI architectures** designed for biological reasoning
2. **Training programs that integrate biology and AI** from the start, not as separate fields connected by collaboration
3. **Open, adaptable models** that researchers can interrogate, modify, and repurpose
4. **Data-sharing frameworks** that respect privacy but enable model development
5. **Validation standards** that prioritize biological interpretability, not just predictive accuracy

---

> ## Core Takeaways
> **• Biology needs Artificial Specific Intelligence, not AGI.**  
> Biological research demands specialized, context-aware models.
>
> **• Severe shortage in scale.**  
> Too few AI experts exist to address thousands of biological questions.
>
> **• Shortage in quality.**  
> Lack of deep integration between biological insight and AI expertise.
>
> **• Shortage in transparency.**  
> Existing models are often opaque, proprietary, and not adaptable.
>
> **• General-purpose AI is not enough.**  
> Foundation models lack the biological grounding and specificity required.
>
> **• What we need: custom, interpretable, open AI systems.**  
> The path forward requires new training paradigms, architectures, and collaboration models.

