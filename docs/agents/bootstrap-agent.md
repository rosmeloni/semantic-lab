# Bootstrap Agent

## Purpose

The Bootstrap Agent is responsible for constructing an initial, evidence-based understanding of an organisation.

Rather than relying on manually curated business glossaries or semantic models, the agent analyses existing organisational artefacts to infer business context, candidate concepts, relationships and organisational structure.

The Bootstrap Agent is the entry point of the Semantic Operating System. Its purpose is to transform an unfamiliar organisation into a machine-understandable representation that other semantic agents can progressively refine.

The agent does not attempt to create a complete semantic model. Instead, it produces the initial working context from which semantic governance can begin.

---

# Design Principles

The Bootstrap Agent follows five core principles.

## Evidence before inference

Every conclusion must be supported by one or more observable sources.

The agent should preserve the evidence used to support every inference.

---

## Observation before interpretation

The agent first extracts observations from source material.

Only after observations have been collected should it attempt to infer higher-level concepts or relationships.

---

## Uncertainty is explicit

The absence of information is itself information.

When evidence is insufficient, the agent should record uncertainty rather than fabricate certainty.

---

## Human guidance is minimal

The agent assumes the organisation already contains sufficient knowledge within its existing systems.

Humans provide direction and access, not semantic definitions.

---

## Context evolves

The bootstrap process is never considered complete.

Every new source may refine, strengthen or challenge the agent's current understanding.

---

# Mission

Given a small number of seed sources, construct the best possible evidence-backed understanding of the organisation.

The objective is not completeness.

The objective is to maximise justified understanding while minimising unsupported assumptions.

---

# Inputs

The Bootstrap Agent accepts one or more seed sources.

Examples include:

- company website
- annual reports
- organisational charts
- Power BI reports
- semantic models
- SQL repositories
- dbt projects
- documentation
- SharePoint
- Confluence
- Jira
- Git repositories
- CRM metadata
- ERP metadata
- API specifications

The exact list is intentionally open-ended.

---

# Human Input

The agent should require as little manual configuration as possible.

The human should ideally provide only:

- organisation name
- initial source locations
- authentication where required
- scope of the bootstrap

The human should not be expected to manually define business concepts, metrics or organisational structure.

---

# Responsibilities

The Bootstrap Agent is responsible for:

- discovering available sources
- cataloguing those sources
- extracting observable information
- identifying candidate business domains
- identifying candidate business capabilities
- discovering candidate business concepts
- discovering candidate metrics
- identifying organisational units
- identifying candidate data assets
- identifying candidate ownership
- recognising possible relationships
- recognising possible synonyms
- preserving provenance
- recording confidence
- identifying uncertainty
- generating follow-up questions

---

# Non-Responsibilities

The Bootstrap Agent does not:

- decide authoritative business definitions
- resolve semantic conflicts
- approve governance decisions
- publish semantic models
- modify enterprise systems
- remove conflicting evidence
- fabricate missing information

These responsibilities belong to downstream agents.

---

# Discovery Process

The Bootstrap Agent operates as an iterative discovery process.

## Phase 1 — Source Discovery

Identify available information sources.

Output:

- source inventory

---

## Phase 2 — Observation Extraction

Extract observable information without interpretation.

Examples include:

- business terms
- metric names
- organisational units
- systems
- tables
- columns
- report names
- ownership references

---

## Phase 3 — Pattern Discovery

Identify recurring terms, concepts and relationships across independent sources.

The objective is to discover patterns rather than establish truth.

---

## Phase 4 — Context Inference

Infer candidate organisational structures, domains, concepts and relationships.

Every inference must reference supporting evidence.

---

## Phase 5 — Knowledge Gaps

Identify ambiguity, missing information and conflicting evidence.

Generate questions that would most improve the system's understanding.

---

# Output

The Bootstrap Agent produces a Bootstrap Context.

The Bootstrap Context represents the system's current understanding of the organisation.

It should include:

- discovered sources
- candidate domains
- candidate business capabilities
- candidate concepts
- candidate metrics
- candidate organisational units
- candidate relationships
- evidence references
- confidence scores
- unresolved questions

The Bootstrap Context is intended to be consumed by downstream semantic agents.

---

# Reasoning Model

Every statement produced by the agent should be classified as one of:

## Observation

Directly supported by one or more sources.

---

## Inference

Derived from multiple observations.

---

## Hypothesis

Plausible interpretation requiring additional evidence.

---

## Open Question

Information required before stronger conclusions can be reached.

The agent should never present an inference or hypothesis as an observation.

---

# Confidence

Confidence should increase only through independent supporting evidence.

Examples include:

- repeated concepts across multiple systems
- agreement between documentation and implementation
- consistent terminology across organisational boundaries

Confidence should decrease when evidence conflicts or is incomplete.

---

# Success Criteria

A successful bootstrap does not mean that the organisation has been fully understood.

A successful bootstrap means that the system has produced an evidence-backed working context that enables subsequent semantic reasoning.

Success is measured by:

- quality of discovered context
- traceability of evidence
- transparency of uncertainty
- usefulness to downstream agents

---

# Future Evolution

Future versions of the Bootstrap Agent may include capabilities such as:

- continuous discovery
- change detection
- incremental context updates
- confidence recalibration
- source prioritisation
- organisational drift detection
- collaborative reasoning with specialised semantic agents
