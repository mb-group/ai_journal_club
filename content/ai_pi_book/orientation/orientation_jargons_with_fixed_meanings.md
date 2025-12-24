# Jargons with Community-Agreed Fixed Meanings

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```

```{admonition} Purpose of This Glossary
:class: tip

To support biologists entering this rapidly shifting landscape, we compiled a collection of clear, practical explanations for the AI jargons and conceptual distinctions that most frequently cause confusion. This glossary is not meant to formalize the field, but to serve as a reliable, stable reference in an environment where the terminology itself is still evolving.
```

---

## 🎯 Core Concepts: AI, Machine Learning, Deep Learning, and Reinforcement Learning

```{admonition} What They Actually Mean
:class: info

Because AI grew fast without standardized definitions, common terms can be confusing. Here are concise, practical explanations for biologists.
Because AI grew fast without standardized definitions, common terms can be confusing. Here are concise, practical explanations for biologists.

---

### **Artificial Intelligence (AI)**  
Any method—rules, statistics, or learning systems—that makes a machine behave in a way that appears intelligent.

---

### **Machine Learning (ML)**  
A subset of AI.  
Models that *learn patterns from data* instead of following hand-written rules.  
Examples: logistic regression, random forests, SVMs, simple neural nets.

---

### **Deep Learning (DL)**  
A subset of ML.  
Uses multi-layer neural networks to learn complex representations directly from raw data.  
Powers modern breakthroughs such as protein language models, AlphaFold components, LLMs, and diffusion models.

---

### **Reinforcement Learning (RL)**  
A distinct learning paradigm.  
An agent learns by *interacting with an environment* and improving behavior based on rewards—not by using labeled datasets.  
Used in AlphaGo, robotics, and RLHF for modern LLMs.

---

### **One-line memory aid**  
**AI** (broad idea) → **ML** (learns from data) → **DL** (ML with deep neural nets)  
**RL** = learns by trial-and-error interaction with rewards.

---

## 🔄 Model Adaptation: Pretraining, Fine-Tuning, and Prompting

```{admonition} Short, Practical Explanations
:class: info

These three terms describe how modern AI models are built and adapted. They are often used inconsistently, so here are concise definitions for biology researchers.
```

---

### **Pretraining**  
Training a model on a *very large, general-purpose dataset* so it learns broad patterns (e.g., protein grammar, language structure, image features).  
- Expensive and time-consuming  
- Produces a versatile “base model”  
Example: Protein language models trained on millions of sequences.

---

### **Fine-Tuning**  
Taking a pretrained model and training it *further on a smaller, task-specific dataset* so it adapts to your problem.  
- Much cheaper than pretraining  
- Injects domain knowledge  
Example: Fine-tuning a protein language model for thermostability prediction on your own experimental data.

---

### **Prompting**  
Using a pretrained model *as-is* by giving it carefully designed text or tokens that steer its output—no additional training required.  
- Fastest and easiest way to use a model  
- Depends on the model’s existing knowledge  
Example: Asking an LLM “Explain attention in simple terms,” or prompting a protein model with a sequence and a question.

---

### **One-line memory aid**  
**Pretraining** = teach the model the world.  
**Fine-tuning** = teach it your task.  
**Prompting** = ask it for what you need without retraining.

---
