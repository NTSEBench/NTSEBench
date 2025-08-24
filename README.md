# NTSEBench

**NTSEBench** (_Cognitive Reasoning Benchmark for Vision Language Models_) is a comprehensive dataset and benchmarking framework designed to evaluate the cognitive, multimodal reasoning capabilities of large language models (LLMs) and vision-language models (VLMs) on complex reasoning tasks.

This project accompanies our paper titled _“NTSEBENCH: Cognitive Reasoning Benchmark for Vision Language Models”_ (Findings of NAACL 2025) :contentReference[oaicite:0]{index=0}.

---

##  Overview

Real-world reasoning often demands much more than surface-level pattern matching—it requires deep cognitive understanding and the ability to integrate textual and visual information. NTSEBench addresses this by providing:

- A collection of **2,728 multiple-choice questions** sourced from India’s **National Talent Search Examination (NTSE)**.
- A total of **4,642 images**, covering a wide spectrum of cognitive challenges across **26 distinct problem categories** :contentReference[oaicite:1]{index=1}.
- A balanced mix of **text-only**, **image-only**, and **multi-modal** questions (text + images), reflecting the Mental Ability Test (MAT) format from NTSE :contentReference[oaicite:2]{index=2}.

### Problem Categories Include:

| Category Type          | Examples                                  |
|------------------------|--------------------------------------------|
| Pattern Recognition    | Series (numeric, alphabetic), Missing Character, Non-verbal Series, Dot Problem |
| Logical Deduction      | Blood Relation, Syllogisms, Statement & Conclusions, Data Sufficiency |
| Spatial Reasoning      | Direction Sense, Cube & Dice, Paper Folding & Cutting, Embedded Figures |
| Classification & Categorization | Odd One Out (Verbal & Non-verbal) |
| Verbal Reasoning       | Analogies, Mathematical Operations, etc. |

(See the NTSEBench website for the full breakdown of all 26 categories.) :contentReference[oaicite:3]{index=3}

---

##  Modeling Strategies & Baselines

To fairly and effectively evaluate different models, this benchmark implements **four modeling strategies**:

1. **Standard QA** – For text-only questions using models like GPT-3.5 or LLaMA3.
2. **Image-Only** – Presents images containing all question elements, leveraging models’ OCR capabilities.
3. **Interleaved Model** – Integrates text and related images in sequence to enhance contextual reasoning.
4. **Standard VQA (Vision QA)** – Uses composite imagery plus structured text prompting for multi-modal reasoning :contentReference[oaicite:4]{index=4}.

We establish benchmarks with both open-source and proprietary LLMs/VLMs, analyzing their strengths and limitations across text-only vs. multi-modal inputs :contentReference[oaicite:5]{index=5}.

---

##  Repository Contents

- `data/` – The full NTSEBench dataset, including question metadata, images, and solution annotations.
- `scripts/` – Utilities for loading, processing, and evaluating the benchmark.
- `models/` – Baseline implementation of modeling strategies and evaluation pipelines.
- `README.md` – Getting started guide, overview, and citation details (this file).
- Additional folders as required by development and contribution workflows.

---

##  Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/NTSEBench/NTSEBench.git
   cd NTSEBench
````

2. **Install dependencies**

   * Python ≥3.x
   * Standard ML and image-processing libraries (e.g., PyTorch/TensorFlow, PIL, OCR tools)

---

## Citation

If you use NTSEBench in your research, please cite:

> Pranshu Pandya, Vatsal Gupta, Agney S Talwarr, Tushar Kataria, Dan Roth, and Vivek Gupta.
> **NTSEBENCH: Cognitive Reasoning Benchmark for Vision Language Models.**
> *Findings of the Association for Computational Linguistics: NAACL 2025*, pages 3680–3708 ([ACL Anthology][1]).

---

## Acknowledgements

NTSEBench was developed by researchers at:

* Indian Institute of Technology Guwahati
* University of Utah
* University of Pennsylvania
* Arizona State University

Our work builds on a rich foundation of cognitive reasoning evaluation and multimodal learning research, and we hope this benchmark helps further that journey ([ntsebench.github.io][2], [cogcomp.seas.upenn.edu][3], [ACL Anthology][1]).

---

We’re excited to see how the community leverages and extends NTSEBench—feel free to open issues, contribute, or reach out with ideas!

```

