# Jargons with Community-Agreed Fixed Meanings

## Background: What you may find disappointing and frustrating
AI is a far less established discipline than many assume—especially when compared with fields such as physics or chemistry. In biology, we often say the discipline is “messy” and that textbooks lag behind discovery; however, AI today is arguably even earlier in its scientific maturity. A historical analogy may help: during the first industrial revolution, steam engines were already transforming society long before the principles of thermodynamics were formally understood. Modern AI is in a similar state. Despite its enormous influence, the field lacks even a widely acknowledged textbook. Much of the excitement today traces back to breakthroughs after 2017, and theory continues to trail substantially behind empirical success. Fundamental questions—such as why the architectural components of AlphaFold work as well as they do, or what protein language models truly learn—remain active areas of research.

This immaturity, juxtaposed with the overwhelming public buzz surrounding AI, produces several practical challenges for newcomers, especially biologists:
- Terminology without formal definitions. Many core terms—AI, machine learning, deep learning, neural networks—are defined only through community convention rather than standardized meaning.
- Difficult entry by reading. Concepts like transformers vs. diffusion models or LLMs vs. other architectures cannot be understood reliably through passive reading alone, because the literature itself is evolving and inconsistent.
- No clear answers to seemingly basic questions. Examples include: Why use CNNs instead of LSTMs in certain domains? Are transformers always better? When does a simple model outperform a sophisticated one? In many cases, the field has no settled consensus.

To support biologists entering this rapidly shifting landscape, we compiled a collection of clear, practical explanations for the AI jargons and conceptual distinctions that most frequently cause confusion. This glossary is not meant to formalize the field, but to serve as a reliable, stable reference in an environment where the terminology itself is still evolving.

## AI, Machine Learning, Deep Learning, and Reinforcement Learning — What They Actually Mean

Because AI grew fast without standardized definitions, common terms can be confusing. Here are concise, practical explanations for biologists.

---

### **Artificial Intelligence (AI)**  
The broadest term.  
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

## Pretraining, Fine-Tuning, and Prompting — Short, Practical Explanations

These three terms describe how modern AI models are built and adapted. They are often used inconsistently, so here are concise definitions for biology researchers.

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

## Training Fundamentals — The Learning Process Explained

Understanding how models actually learn is crucial for evaluating AI work and managing projects.

---

### **Loss Function**  
The mathematical penalty signal that guides training—tells the model how wrong its predictions are.  
- Used during training to update model parameters  
- Different from performance metrics you care about  
Example: Mean squared error for regression, cross-entropy for classification.

---

### **Parameters (or Weights)**  
The learned values inside a neural network that get adjusted during training.  
- Millions to billions of numbers that encode learned patterns  
- Start random, become useful through training  
- The "knowledge" of the model is stored in these parameters.

---

### **Overfitting**  
When a model memorizes training examples instead of learning general patterns.  
- High accuracy on training data, poor on new data  
- Like memorizing exam questions instead of understanding concepts  
- Prevented by: more data, regularization, early stopping.

---

### **Underfitting**  
When a model hasn't learned enough—too simple to capture important patterns.  
- Poor performance on both training and test data  
- Like studying the wrong material for an exam  
- Fixed by: more complex model, longer training, better features.

---

### **Training Data vs. Testing Data**  
**Training data**: What the model learns from during training.  
**Testing data**: Held-out examples used to evaluate how well learning generalized.  
- Testing data must never be seen during training  
- The gap between training and testing performance reveals overfitting  
Critical in biology: Are test proteins from the same families as training? Same organisms?

---

### **Batch Size**  
How many training examples are processed together before updating model parameters.  
- Larger batches = faster training but more memory  
- Smaller batches = noisier but sometimes better generalization  
- Typical values: 32, 64, 128, 256.

---

### **Hyperparameters**  
Configuration choices you make before training (not learned from data).  
Examples: learning rate, number of layers, batch size, dropout rate.  
- Require experimentation to find good values  
- Different from parameters (weights), which are learned during training.

---

## Generalization — The Central Challenge

The ultimate goal: models that work on new, unseen data.

---

### **Generalization**  
How well a model performs on data it hasn't seen during training.  
- The core challenge in machine learning  
- Good generalization = learned real patterns, not memorized examples  
- Evaluated by testing on held-out data.

---

### **Out-of-Distribution (OOD) Generalization**  
Performance when test data is fundamentally different from training data.  
- Much harder than standard generalization  
- Critical in biology: different organisms, protocols, experimental conditions  
Example: Model trained on human proteins tested on bacterial proteins.  
**This is an active research area—most models struggle here.**

---

### **Transfer Learning**  
Using knowledge from one task to help with another.  
- Typically: pretrain on large general dataset, fine-tune on specific task  
- Reduces data requirements dramatically  
- Assumes source and target tasks share underlying patterns  
Example: Protein language model pretrained on all sequences, then fine-tuned for your stability prediction task.

---

### **Zero-Shot Learning**  
Model performing a task it was never explicitly trained to do.  
- Relies entirely on knowledge from pretraining  
- No task-specific training examples  
Example: Asking a language model to write code when only trained on text, or using protein embeddings for function prediction without function labels during training.

---

## Model Architectures — The Building Blocks

Different neural network designs for different types of data.

---

### **Neural Network**  
A computational model inspired by biological neurons—layers of interconnected processing units.  
- Each connection has a weight (parameter) that's learned during training  
- Data flows through layers, transforming input to output  
- The foundation of deep learning.

---

### **Transformer**  
A neural network architecture using self-attention mechanisms.  
- Processes sequences without inherent order bias (unlike RNNs)  
- Can attend to any part of the input simultaneously  
- Powers: GPT, BERT, AlphaFold components, protein language models  
Advantage: Captures long-range dependencies efficiently.

---

### **CNN (Convolutional Neural Network)**  
Architecture designed for spatial data (images, structures).  
- Uses sliding "filters" to detect local patterns  
- Assumes nearby positions are related  
- Excellent for: microscopy images, protein structure analysis  
Assumption: Spatial proximity matters.

---

### **RNN (Recurrent Neural Network)**  
Architecture for sequential data with temporal dependencies.  
- Processes sequences one step at a time, maintaining "memory"  
- Older approach, largely replaced by transformers  
- Can struggle with long sequences  
Used in: early protein/DNA sequence analysis, time-series data.

---

### **GNN (Graph Neural Network)**  
Architecture for relational data (networks, molecular graphs).  
- Nodes exchange information with neighbors iteratively  
- Natural for: protein interaction networks, molecular structures, pathway analysis  
Assumption: Relationships between entities matter.

---

### **Attention Mechanism**  
A component that lets models focus on relevant parts of input.  
- Learns which parts of the input are important for each prediction  
- Can be visualized to understand model decisions  
- Core component of transformers  
Example: In protein sequences, attention might focus on active site residues.

---

### **Self-Attention**  
A specific type of attention where elements in a sequence attend to each other.  
- Each amino acid "looks at" all other amino acids  
- Captures relationships and dependencies within the sequence  
- Foundation of transformer architectures.

---

## Embeddings and Representations — The Hidden Value

Modern AI's most powerful outputs are often not the final predictions.

---

### **Embeddings**  
Dense numerical representations learned by models that capture patterns.  
- Transform discrete items (words, amino acids, proteins) into continuous vectors  
- Similar items have similar embeddings  
- Can be used for tasks the model wasn't explicitly trained for  
Example: Protein embeddings cluster by function even without function labels during training.  
**Key insight: Embeddings are often more valuable than final predictions.**

---

### **Feature Engineering**  
Manually designing input representations based on domain knowledge.  
- Traditional ML approach: extract biophysical features, motifs, statistical properties  
- Deep learning often learns features automatically  
- Still useful when data is limited or domain knowledge is strong  
Example: Calculating hydrophobicity, charge, secondary structure propensity as inputs.

---

## Advanced Training Paradigms

Beyond simple supervised learning.

---

### **Multi-Task Learning**  
Training one model to solve multiple related tasks simultaneously.  
- Shares knowledge across tasks  
- Can improve performance on all tasks  
- Requires careful balancing of task objectives  
Example: Predicting protein structure AND function AND stability in one model.

---

### **Self-Supervised Learning**  
Learning from unlabeled data by predicting parts of the data from other parts.  
- No human annotations needed  
- Creates its own training signal  
- Foundation of modern language models  
Example: Predicting masked amino acids in protein sequences (how ESM models are trained).

---

### **Meta-Learning (Learning to Learn)**  
Training models to quickly adapt to new tasks with minimal data.  
- Learns general learning strategies rather than specific tasks  
- Useful when you have many small datasets  
- Active research area, not yet mainstream in biology.

---

## Model Types by Function

What different models are designed to do.

---

### **Foundation Models**  
Large-scale, general-purpose models trained on massive diverse datasets.  
- Intended to serve as base for many downstream tasks  
- Expensive to train, but widely reusable  
- Examples: GPT, BERT, ESM (protein language models)  
**In biology: Performance varies—excellent on benchmarks, inconsistent on novel problems.**

---

### **Protein Language Models (pLMs)**  
Models that treat protein sequences like language.  
- Learn evolutionary patterns, structure hints, functional motifs from sequences alone  
- Can generate embeddings or predict masked positions  
- Examples: ESM-2, ProtBERT, ProtTrans  
**What they actually learn: Broad patterns, evolutionary constraints—but not fine-grained biology or dynamics.**

---

### **Generative Models**  
Models that create new examples (sequences, molecules, images).  
- Learn the distribution of training data  
- Can sample novel examples similar to training data  
- Types: GANs, VAEs, diffusion models  
Example: Generating new protein sequences with desired properties.

---

### **Discriminative Models**  
Models that classify or predict labels for given inputs.  
- Most common type in traditional ML  
- Learn boundaries between categories  
- Examples: classifiers, regression models  
Example: Predicting whether a protein binds DNA.

---

### **Variational Autoencoder (VAE)**  
A generative model that learns compressed representations.  
- Encodes data into low-dimensional space (embeddings)  
- Can decode to reconstruct or generate new examples  
- Used for: exploring chemical space, learning protein representations.

---

### **Diffusion Models**  
Generative models that learn to reverse a noise-adding process.  
- Start with noise, gradually denoise to create data  
- State-of-the-art for image generation  
- Emerging in biology: protein structure generation, molecular design.

---

## Practical Deployment Terms

Making models accessible and usable.

---

### **API (Application Programming Interface)**  
A way to access a model's functionality programmatically.  
- Send data to a server, get predictions back  
- No need to install or run the model yourself  
- Examples: AlphaFold Server, OpenAI API  
Trade-off: Convenient but data leaves your control.

---

### **GPU (Graphics Processing Unit)**  
Specialized hardware that accelerates neural network training and inference.  
- Essential for deep learning at scale  
- Training large models requires multiple GPUs  
- Inference can often run on CPUs (slower) or single GPU  
**For PIs: Major cost consideration—cloud GPUs vs. local cluster.**

---

### **Inference**  
Using a trained model to make predictions on new data.  
- The "using" phase (vs. training phase)  
- Much cheaper and faster than training  
- What most biology labs do with models like AlphaFold  
Example: Running AlphaFold on your protein sequence.

---

## Interpretability — Understanding What Models Learn

Critical for scientific trust and insight.

---

### **Saliency Map**  
Visualization showing which input features most influenced a prediction.  
- Highlights important regions in images or sequences  
- Computed using gradients  
Example: Which amino acids were most important for a binding prediction?

---

### **SHAP (SHapley Additive exPlanations)**  
Method to quantify each feature's contribution to predictions.  
- Based on game theory  
- Provides consistent, interpretable importance scores  
- More rigorous than simple feature importance  
Example: Ranking which experimental measurements matter most for your prediction.

---

### **Mechanistic Interpretability**  
Understanding the internal computations and circuits within neural networks.  
- Goes beyond "what features matter" to "how does the model process information"  
- Identifies specific neurons or layers responsible for particular behaviors  
- Active research area, especially for understanding what models truly learn.

---

## Performance Evaluation

How to assess model quality.

---

### **Performance Metrics**  
Measures of how well a model achieves your goals.  
- Different from loss functions (what's optimized during training)  
- Choose metrics that match your biological question  
Examples: Accuracy, precision, recall, AUC, correlation (for regression).  
**Critical: High accuracy on benchmarks ≠ useful for your problem.**

---

### **Domain Invariant Representations**  
Features that remain stable across different experimental conditions or contexts.  
- Goal: Learn patterns that generalize across domains  
- Helps with distribution shifts  
Example: Cell state features that work across different imaging platforms or protocols.

---

## Biology-Specific AI Terms

Models and concepts specific to biological applications.

---

### **AlphaFold**  
AI system that predicts 3D protein structure from amino acid sequence.  
- Revolutionary impact on structural biology  
- **Critical caveat**: Predicts *a* structure, not *the* structure  
- Proteins are dynamic; AlphaFold shows one state  
- Doesn't specify biological conditions, alternative conformations, or dynamics.

---

### **Virtual Cell Models**  
Computational models simulating cellular processes and responses.  
- Dream: In silico substitute for wet-lab experiments  
- Reality: Currently limited to transcriptomic responses to perturbations  
- Don't model proteomics, dynamics, or mechanistic depth yet  
- Assumptions: Transcriptomics = cell state (it's not).

---

### **Tokenization**  
Breaking complex data into discrete units the model can process.  
- **Proteins**: Individual amino acids, k-mers, or structural domains  
- **DNA**: Nucleotides, codons, or functional motifs  
- **Text**: Words or sub-word pieces  
**Choice matters**: Defines what patterns the model can see.

---

## One-Line Memory Aids for Key Distinctions

**Loss function** = penalty during training | **Performance metric** = what you actually care about  
**Overfitting** = memorized examples | **Underfitting** = didn't learn enough  
**Training data** = what model learns from | **Testing data** = evaluates generalization  
**Generalization** = works on similar new data | **OOD generalization** = works on different distributions  
**Embeddings** = learned representations | **Final predictions** = task-specific outputs  
**CNN** = spatial patterns | **RNN** = sequential | **Transformer** = attention-based | **GNN** = relational  
**Foundation model** = big general-purpose base | **Fine-tuned model** = adapted to your task  
**Generative** = creates new examples | **Discriminative** = classifies given examples





