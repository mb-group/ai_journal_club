# AI Fundamentals at Intuition Level

```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```



```{admonition} Overview
:class: info

Gain an intuitive understanding of AI core concepts without getting lost in mathematical details. This chapter focuses on building conceptual models that help you make informed decisions when designing AI models.
```

---

## Core Concepts Without the Math

### How a Model Learns from Data

Think of training an AI model like training a circus lion. The lion learns behaviors through a system of rewards and corrections—it tries different actions, receives feedback, and gradually learns which behaviors lead to desired outcomes.

This analogy reveals several key insights about AI training:

**Loss Functions vs. Performance Metrics**
- The **loss function** (or training objective) is the immediate "penalty" signal during training—like the trainer's corrections to the lion
- **Performance metrics** evaluate how well the model achieves your actual goals—like whether the lion can perform the full routine
- These are often different: you optimize one thing during training to achieve another goal in practice

**Population-Level vs. Individual Performance**
- AI models are evaluated on their **overall performance** across many examples (the entire data population)
- Just like a circus lion that performs well most nights but occasionally has an off performance, models are judged by their aggregate success rate

**Training Data vs. Testing Data**
- **Training data** is what the model learns from—the practice sessions
- **Testing data** reveals how well those lessons generalize to new situations—the actual performance
- The relationship between these two tells crucial stories: Does your model truly understand patterns, or has it just memorized the training examples?

---

### The AI Workflow: From Design to Deployment

Building an AI model follows a structured process:

**1. Design the Model Architecture**
   - Define how input data transforms into output predictions
   - Think of it as designing the "wiring" that connects inputs to outputs through mathematical transformations
   - This happens in linear algebra space, but conceptually you're deciding: what information flows where, and how is it processed?

**2. Design the Training Scheme**
   - Decide how training data is organized and fed to the model (batch size, order, etc.)
   - Choose the loss function that defines "good" vs. "bad" predictions
   - Set the learning strategy: how aggressively should the model update based on errors?

**3. Initialize and Train**
   - The model starts with random parameters (it knows nothing)
   - Through repeated exposure to training data and penalty signals, it gradually adjusts its parameters
   - Like the circus lion's gradual improvement, the model minimizes penalties through iterative updates

**4. Determine Stopping Criteria**
   - Set thresholds that terminate training (based on loss values, performance metrics, or time limits)
   - Too little training = underfitting (the model hasn't learned enough)
   - Too much training = overfitting (the model memorized training examples but can't generalize)

---

### Why AI Stands Out: Comparing to Traditional Data Analysis

Deep learning is fundamentally statistical learning, but with crucial advantages over older methodologies:

**Beyond Linear Relationships**
- Traditional statistical analysis typically assumes linear relationships between variables
- Deep learning can capture complex, non-linear patterns that better reflect biological reality

**From Analysis to Prediction and Generation**
- Classical biostatistics focuses on understanding relationships in existing data
- AI models can make predictions about unseen cases and even generate novel examples (like new protein sequences)

**Handling Complex Data Modalities**
- Traditional methods struggle with images, sequences, and graphs—they need features extracted and converted to numerical representations first
- Deep learning directly processes these complex modalities more efficiently, learning relevant patterns automatically

**Scaling with Data Volume**
- As data grows, traditional methods often hit computational or theoretical limits
- Deep learning models improve with more data, automatically discovering patterns that would be impossible to manually specify

This power comes at a cost: deep learning requires specialized infrastructure (GPUs), careful design choices, and larger datasets. But for many biological problems—especially those involving complex patterns, large-scale data, or predictive tasks—AI's advantages make it the right tool for the job.

---

## For Biology PIs: What to Focus On (and What to Delegate)

As a principal investigator evaluating AI work, you don't need to understand everything. Here's a practical guide to where you should invest your attention.

### You Can Safely Ignore

**Hardware and Infrastructure Details**
- Memory requirements, GPU specifications, distributed training architectures
- These are real constraints, but they're engineering problems, not scientific ones
- Your role: Ensure your team has access to adequate resources, but trust them on the specifics

**Implementation Details of Algorithms**
- The inner workings of transformers, BERT architectures, diffusion models
- How exactly the loss function is computed
- Specific training schemes and optimization techniques

**Why this is okay:** These are tools. Just as you don't need to understand mass spectrometry physics to interpret proteomics data, you don't need to understand backpropagation details to evaluate AI results. What matters is whether the tool is appropriate for the question.

### You Should Actively Question

**Input and Output Definitions**
- What exactly goes into the model? How is biological data represented?
- What comes out? Is it interpretable in biological terms?
- If there are intermediate outputs (embeddings, attention maps), what do they represent?

**Data Splits: Training vs. Testing**
- How were training and test sets created? Are they truly independent?
- Do test examples represent the same distribution as training examples, or something different?
- For biological data: Are you testing on the same protein families you trained on? Same organisms? Same experimental conditions?

**Performance Evaluation Metrics**
- What metrics are being used? Are they appropriate for your biological question?
- Does high accuracy on a test set actually mean the model will work for your application?
- Are there important failure modes being hidden by aggregate statistics?

**Generalization Capacity**
- **Generalization** means how well a model performs on data it hasn't seen, especially data that differs from its training set
- Critical questions:
  - Will this model work on my lab's data, which may differ from public datasets?
  - Can it handle rare variants, novel protein families, or unusual experimental conditions?
  - What are the boundaries of its applicability?

### How to Avoid Sounding Uninformed

**Don't Be Too Pessimistic**

Common mistake: "These models are just black boxes making predictions we can't interpret."

More informed view: Modern AI offers tools to understand what models learn. Embeddings, attention mechanisms, and interpretability methods reveal internal representations. The model isn't just predicting—it's learning a compressed understanding of your data that can be examined and leveraged.

Example: A protein language model's embeddings cluster proteins by function even when never explicitly trained on functional labels. This internal representation has scientific value beyond any specific prediction task.

**Don't Be Too Optimistic**

Common mistake: "The model achieved 95% accuracy, so it's solved the problem."

More informed view: High performance on test data doesn't guarantee real-world utility. Key concerns:
- **Generalization capacity:** Does the model work on substantially different data than it was trained on?
- **Dataset bias:** Is the model learning the actual biological signal or spurious correlations in training data?
- **Robustness:** How does performance degrade with noisy data, edge cases, or distribution shifts?
- **Model design assumptions:** Every model architecture carries implicit assumptions about the data and problem structure. Model designers don't necessarily know best how to align these assumptions with real biology problems. AI is not one thing—especially for biology, each problem deserves its own thoughtfully designed model.


Example: A model trained on proteins from model organisms might fail on proteins from extremophiles. A model trained on high-quality crystal structures might struggle with cryo-EM data.

**The Balanced Perspective**

AI models are powerful tools that can discover patterns humans miss, but they're not magic. They have well-defined capabilities and limitations. Your job as a PI is to ensure the AI approach matches the biological question, the validation is rigorous, and the claims are appropriately scoped.

---