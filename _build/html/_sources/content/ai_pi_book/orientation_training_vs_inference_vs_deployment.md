# Training vs. Inference vs. Deployment

```{admonition} Chapter Overview
:class: info

Understanding the lifecycle stages of AI models is crucial for resource planning, team building, and project management. This chapter clarifies three fundamental phases in the AI workflow.
```

## The Three Phases of AI Model Usage

### 1. Training

**What it is**: The process of teaching a model to recognize patterns by showing it examples and adjusting its parameters to minimize errors.

#### Key Characteristics

- **Resource Intensive**: Requires powerful GPUs, large datasets, and significant time
- **One-Time (or Periodic)**: Done once initially, then updated occasionally
- **Expensive**: Can cost thousands to millions of dollars for large models
- **Requires Expertise**: Needs specialized knowledge in model architecture, optimization

```{admonition} Training in Practice
:class: note

For most biology labs, you'll rarely train large models from scratch. Instead, you'll:
- Use pre-trained models (transfer learning)
- Fine-tune existing models on your specific data
- Work with computational partners who handle training
```

### 2. Inference

**What it is**: Using a trained model to make predictions on new data. This is the "using" phase.

#### Key Characteristics

- **Lightweight**: Much less resource-intensive than training
- **Fast**: Often processes data in seconds to minutes
- **Repeated**: Done many times for different samples/inputs
- **User-Friendly**: Can often be done with simple tools or web interfaces

```{admonition} Inference Examples
:class: tip

- Running AlphaFold to predict a protein structure
- Using a genomics model to score variants
- Applying a trained classifier to new microscopy images
- Querying a protein language model for embeddings
```

### 3. Deployment

**What it is**: Making a trained model accessible for regular use by others (researchers, clinicians, or systems).

#### Key Characteristics

- **Infrastructure**: Requires servers, APIs, or software packaging
- **Maintenance**: Needs monitoring, updates, and bug fixes
- **Accessibility**: Determines how easily others can use your model
- **Security**: Involves data privacy and access control considerations

#### Deployment Options

```{dropdown} Web Service/API
:color: primary
:icon: cloud

Host the model on a server; users access via web interface or API calls.
- **Pros**: Easy for users, centralized updates
- **Cons**: Requires server maintenance, data must leave user's system
```

```{dropdown} Standalone Software
:color: primary
:icon: package

Package model with software that users install locally.
- **Pros**: Data stays local, no server needed
- **Cons**: Users must install and manage software
```

```{dropdown} Cloud Platform
:color: primary
:icon: cloud-upload

Deploy on platforms like AWS, Google Cloud, Azure.
- **Pros**: Scalable, managed infrastructure
- **Cons**: Ongoing costs, vendor lock-in
```

## As a PI: What You Need to Know

### Budget Planning

| Phase | Cost Considerations |
|-------|-------------------|
| **Training** | High upfront costs (GPUs, cloud compute, personnel) |
| **Inference** | Lower recurring costs (depends on usage volume) |
| **Deployment** | Ongoing costs (hosting, maintenance, support) |

### Team Composition

Different phases require different expertise:

- **Training**: ML engineers, computational biologists with deep learning experience
- **Inference**: Can be done by lab members with basic computational skills
- **Deployment**: Software engineers, DevOps specialists (if scaling)

### Common Scenarios for Biology Labs

```{admonition} Scenario 1: Using Existing Tools
:class: seealso

You only do **inference** using publicly available models (e.g., AlphaFold, ESM).
- **Your needs**: Computational resources for inference, training for lab members
- **No need for**: Training infrastructure, deployment systems
```

```{admonition} Scenario 2: Developing Lab-Specific Models
:class: seealso

You need to **train** models on your proprietary data and use them internally.
- **Your needs**: Training resources (GPU cluster or cloud), ML expertise, inference capability
- **Consider**: Collaborating with computational groups for training phase
```

```{admonition} Scenario 3: Creating Community Tools
:class: seealso

You develop models and want to **deploy** them for the community.
- **Your needs**: Full pipeline (training, inference, deployment)
- **Consider**: Grant funding for long-term maintenance, partnerships for hosting
```

## Key Distinctions Summary

| Aspect | Training | Inference | Deployment |
|--------|----------|-----------|------------|
| **Frequency** | Once or periodic | Many times | Continuous |
| **Resources** | Very high | Moderate to low | Moderate |
| **Speed** | Hours to weeks | Seconds to minutes | N/A (availability) |
| **Expertise** | High | Low to moderate | Moderate to high |
| **Cost** | High upfront | Low per use | Ongoing |

## Decision Framework

```{mermaid}
graph TD
    A[Do you have a biological question?] --> B{Does a model exist?}
    B -->|Yes| C[Inference only]
    B -->|No| D{Do you have data?}
    D -->|Yes| E[Need Training]
    D -->|No| F[Collect data first]
    E --> G{Share with community?}
    G -->|Yes| H[Need Deployment]
    G -->|No| I[Local inference]
```

## Further Reading

```{seealso}
- Previous: [What's a Model?](orientation_what_is_a_model.md)
- Next: [AI in Biology vs. ChatGPT vs. AlphaFold](orientation_ai_in_biology_vs_chatgpt_vs_alphafold.md)
- Related: [Browse Tools Catalog](browse_tools_catalog.md)
```

---

*Understanding these three phases helps PIs make informed decisions about resources, collaborations, and project planning.*
