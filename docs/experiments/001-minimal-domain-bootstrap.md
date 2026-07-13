# Experiment 001 — Minimal Domain Bootstrap

## Purpose

The purpose of this experiment is to determine whether an AI-driven semantic system can construct an initial understanding of an organisation from a small amount of human guidance and a limited set of enterprise artefacts.

Rather than requiring a complete business glossary or manually curated ontology, the system should progressively infer business context, identify candidate concepts and highlight uncertainties requiring human validation.

This experiment forms the foundation for all subsequent semantic reasoning.

---

# Motivation

Traditional data governance initiatives often fail because they require organisations to manually define hundreds or thousands of business terms before any value is delivered.

This experiment explores an alternative approach:

> Can AI bootstrap an enterprise semantic model by combining human guidance with evidence extracted from existing organisational artefacts?

Instead of asking people to build the semantic layer first, the semantic layer should emerge progressively from the organisation itself.

---

# Research Question

Given:

- minimal human orientation
- a small collection of enterprise artefacts

can the system construct a useful initial semantic context that allows future reasoning and governance?

---

# Objectives

The system should be able to:

- identify the business domain being analysed
- discover relevant enterprise artefacts
- extract candidate business concepts
- identify candidate relationships
- recognise possible synonyms
- preserve evidence supporting every inference
- identify uncertainty rather than invent certainty
- produce an initial semantic context for later experiments

The objective is **not** to produce a complete enterprise ontology.

---

# Inputs

The experiment begins with two sources of information.

## 1. Human orientation

The human provides only enough information to orient the system.

Example:

- organisation name
- business domain
- systems to inspect
- available document repositories
- known stakeholders
- objective of the bootstrap

Example:

```yaml
organisation:
  name: Example Company

domain:
  Customer Support Analytics

systems:
  - Power BI
  - SQL Repository
  - SharePoint

objective:
  Discover business concepts used in operational reporting.
```

---

## 2. Enterprise artefacts

The system scans a small collection of representative artefacts.

Examples include:

- dashboard descriptions
- SQL queries
- dbt models
- Power BI semantic models
- documentation
- wiki pages
- KPI glossaries
- organisation charts

The experiment intentionally uses only a handful of documents.

---

# Expected Process

The bootstrap process follows six stages.

## Stage 1 — Source Inventory

Identify available artefacts and classify them.

Output:

- source catalogue
- source type
- owner
- timestamp
- system

---

## Stage 2 — Information Extraction

Extract structured information from each artefact.

Examples:

- business terms
- entities
- metrics
- KPIs
- tables
- columns
- descriptions
- ownership
- relationships

---

## Stage 3 — Candidate Concept Discovery

Cluster similar terms into candidate concepts.

Example:

```
Ticket
Case
Support Case
Interaction
```

may become

```
Candidate Concept:
Customer Support Interaction
```

Confidence should be recorded.

---

## Stage 4 — Candidate Relationship Discovery

Infer relationships between concepts.

Examples:

- measures
- belongs to
- owned by
- calculated from
- synonym of
- parent of

These relationships are hypotheses, not facts.

---

## Stage 5 — Evidence Graph

Every proposed concept must preserve evidence.

For every statement the system should be able to answer:

> Why do you believe this?

Example:

```
Resolved Interaction

Evidence

✓ Finance KPI document
✓ SQL query
✓ Power BI measure
```

Evidence is never discarded.

---

## Stage 6 — Human Questions

The bootstrap should identify uncertainty.

Example:

Questions:

- Are Ticket and Case equivalent?
- Is Finance or Customer Success the authoritative owner?
- Is "Resolved" identical to "Closed"?

Rather than guessing, the system should ask.

---

# Outputs

The experiment should produce a Bootstrap Context.

The Bootstrap Context is **not** the enterprise semantic model.

It is the system's current understanding of the organisation.

It should contain:

- discovered concepts
- discovered relationships
- source inventory
- evidence
- confidence
- unresolved questions
- recommended next actions

This becomes the input for future experiments.

---

# Success Criteria

The experiment is considered successful if:

- concepts can be discovered from heterogeneous artefacts
- evidence is preserved
- uncertainty is explicitly represented
- the resulting context is sufficient for subsequent semantic reasoning
- no unsupported assumptions are presented as facts

---

# Out of Scope

This experiment does not attempt to:

- resolve conflicting KPI definitions
- create a complete ontology
- automate governance decisions
- publish semantic models
- continuously monitor organisational change

These capabilities are addressed by later experiments.

---

# Relationship to Future Experiments

This experiment provides the initial semantic context.

Subsequent experiments consume that context.

```
Experiment 001
Minimal Domain Bootstrap
        │
        ▼
Experiment 002
KPI Definition Reconciliation
        │
        ▼
Experiment 003
Semantic Governance
        │
        ▼
Experiment 004
Continuous Semantic Monitoring
        │
        ▼
Enterprise Semantic Operating System
```

---

# Key Design Principles

## AI proposes

The system should infer, not assume.

---

## Evidence first

Every semantic assertion must be traceable to one or more enterprise artefacts.

---

## Humans govern

Humans approve, reject or refine semantic proposals.

---

## Context evolves

The bootstrap context is never considered complete.

It continuously evolves as new artefacts, systems and organisational knowledge become available.

---

# Open Questions

This experiment intentionally leaves several research questions open.

Examples include:

- Which artefacts should be scanned first?
- Which sources are most trustworthy?
- How should confidence be calculated?
- When should AI ask a human?
- How much automation is acceptable?
- Can previous governance decisions improve future bootstrap quality?
