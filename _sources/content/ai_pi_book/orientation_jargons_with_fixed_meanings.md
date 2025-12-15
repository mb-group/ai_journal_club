# Jargons with Community-Agreed Fixed Meanings

## Background: What you may find disappointing and frustrating
AI is a far less established discipline than many assume—especially when compared with fields such as physics or chemistry. In biology, we often say the discipline is “messy” and that textbooks lag behind discovery; however, AI today is arguably even earlier in its scientific maturity. A historical analogy may help: during the first industrial revolution, steam engines were already transforming society long before the principles of thermodynamics were formally understood. Modern AI is in a similar state. Despite its enormous influence, the field lacks even a widely acknowledged textbook. Much of the excitement today traces back to breakthroughs after 2017, and theory continues to trail substantially behind empirical success. Fundamental questions—such as why the architectural components of AlphaFold work as well as they do, or what protein language models truly learn—remain active areas of research.

This immaturity, juxtaposed with the overwhelming public buzz surrounding AI, produces several practical challenges for newcomers, especially biologists:
- Terminology without formal definitions. Many core terms—AI, machine learning, deep learning, neural networks—are defined only through community convention rather than standardized meaning.
- Difficult entry by reading. Concepts like transformers vs. diffusion models or LLMs vs. other architectures cannot be understood reliably through passive reading alone, because the literature itself is evolving and inconsistent.
- No clear answers to seemingly basic questions. Examples include: Why use CNNs instead of LSTMs in certain domains? Are transformers always better? When does a simple model outperform a sophisticated one? In many cases, the field has no settled consensus.

To support biologists entering this rapidly shifting landscape, we compiled a collection of clear, practical explanations for the AI jargons and conceptual distinctions that most frequently cause confusion. This glossary is not meant to formalize the field, but to serve as a reliable, stable reference in an environment where the terminology itself is still evolving.

## AI, Machine Learning, Deep Learning, and Reinforcement Learning — What They Actually Mean

Because AI developed rapidly and without a unifying textbook, many commonly used terms are community conventions rather than precise scientific definitions. Below is a practical, biology-friendly way to understand four of the most frequently confused concepts.

---

### **Artificial Intelligence (AI)**  
**The broadest umbrella.**  
“AI” refers to any computational system designed to perform tasks that appear to require reasoning, pattern recognition, or decision-making. It can include:

- Hand-coded rules  
- Classical statistical models  
- Machine learning  
- Modern deep neural networks  

**In practice:** AI ≈ anything that gives computers behaviors that *look* intelligent, regardless of how it is implemented.

---

### **Machine Learning (ML)**  
**A subset of AI.**  
Machine learning refers to methods in which computers *learn patterns from data* instead of relying on manually written rules.

ML systems:

- Take data  
- Learn patterns  
- Use those patterns to make predictions or decisions  

Examples: logistic regression, random forests, support vector machines, early neural networks.

**Key distinction:** ML requires learning from data; AI does not necessarily.

---

### **Deep Learning (DL)**  
**A subset of machine learning.**  
Deep learning uses multi-layer (“deep”) neural networks that automatically learn increasingly abstract representations from raw data.

DL powers nearly all major breakthroughs since 2017:

- Protein language models  
- AlphaFold components  
- Large language models (LLMs)  
- Diffusion models  

**Why it matters:** DL is not just “bigger ML.” It is more empirical, less theoretically understood, and central to modern AI’s rapid advances—and its instability.

---

### **Reinforcement Learning (RL)**  
**A different paradigm of learning.**  
Reinforcement learning does not rely on labeled datasets. Instead, an *agent* interacts with an *environment* and learns through trial and error to maximize cumulative reward.

Core components:

- **Agent**  
- **Environment**  
- **Actions**  
- **Rewards**  

RL powers systems like:

- AlphaGo  
- Robotics controllers  
- RLHF (reinforcement learning from human feedback) used in modern LLM alignment

**Distinction:**  
ML/DL learn from *datasets*.  
RL learns from *experience*.

---

### **One-sentence summary**

- **AI** = the whole space of making machines appear intelligent  
- **ML** = AI that learns from data  
- **DL** = ML using deep neural networks  
- **RL** = learning by interacting with an environment to maximize reward  

---



### Pretraining

Content coming soon...

### Fine-Tuning

Content coming soon...

### Prompting

Content coming soon...

### Embeddings

Content coming soon...
Model architecture: The structure of a neural network, including layers, types (e.g., CNN, Transformer), and how data flows through it. 

Training behavior/scheme: The process of feeding labeled data to an AI model so it can learn patterns and adjust its parameters. 

Evaluation behavior/scheme: The set of methods and metrics used to assess model performance, such as accuracy, AUROC, or precision-recall. 

Inference behavior/scheme: The process of using a trained model to make predictions on new, unseen data. 

State-of-the-art: The most advanced or highest-performing models or techniques available in the field. 

Embedding: A numerical vector representation of complex input (e.g., protein sequences), used as input to models. 
---
