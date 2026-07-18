# Enron Sample Dataset

## Purpose

This dataset provides the first realistic business artefacts used to develop and evaluate the work of Semantic Lab Agents

Rather than relying on synthetic examples created specifically for the project, the goal is to work with publicly available organisational data that reflects the ambiguity, inconsistency and incompleteness typically found in real enterprises.

The Enron email corpus was selected as the initial dataset because it is one of the most widely used public datasets for research in information retrieval, natural language processing and organisational knowledge discovery.

---

## Why Enron?

One of the first questions when developing the Semantic Lab Bootstrap Agent was which data to use for experimentation.

The Bootstrap Agent aims to answer a fundamental research question:

> Can AI bootstrap an organisation's business semantics from existing organisational artefacts with minimal manual input?

To investigate this realistically, the project requires data that:

- originates from a real organisation;
- contains authentic business language;
- includes multiple business domains;
- reflects imperfect documentation rather than curated examples;
- is publicly available for reproducibility.

The Enron corpus satisfies these requirements and provides a common benchmark that other researchers can access.

---

## Dataset Scope

The complete Enron corpus contains hundreds of thousands of business emails exchanged within Enron Corporation before its collapse in 2001.

Semantic Lab intentionally uses only a very small curated subset during the early experiments.

The objective is **not** to analyse Enron itself, but to develop and validate the bootstrapping process on realistic business artefacts before expanding to larger and more diverse datasets.

---

## Intended Evolution

As the project evolves, additional datasets will be introduced, including examples containing:

- company websites
- organisational charts
- product documentation
- KPI definitions
- BI reports
- dashboards
- SQL models
- data catalogues
- knowledge bases
- APIs
- source code

The long-term objective is to investigate how different organisational artefacts contribute to building and maintaining enterprise semantics.

---

## Directory Structure

```
enron_sample/
│
├── README.md
└── emails/
```

Additional folders may be added in future experiments as new artefact types become available.

---

## Research Principles

This dataset is intentionally treated as **evidence**, not as ground truth.

The Bootstrap Agent should:

- discover information rather than assume it;
- attach evidence to every inference;
- express uncertainty where appropriate;
- avoid inventing missing information;
- propose candidate semantics for human review.

---

## Source and data handling

The sample is derived from the Enron Email Dataset published by Carnegie Mellon University.

https://www.cs.cmu.edu/~enron/


The corpus contains real organisational communications. Although it is publicly available and widely used in research, individual messages may contain personal, sensitive or irrelevant material.

Semantic Lab therefore uses only a very small curated subset while preserving the original artefacts as faithfully as possible.

The original documents are treated as immutable evidence. Any semantic interpretation, metadata enrichment, anonymisation or governance decisions are performed separately by the platform rather than by modifying the source artefacts themselves.

## Dataset Version

Semantic Lab references the **May 7, 2015** release of the original Carnegie Mellon University Enron Email Dataset 
https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz 

If a newer official version is published, the project will evaluate whether to migrate to it. Any such migration should be documented together with its impact on reproducibility of previous experiments.


