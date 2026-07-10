# Bootstrapping Enterprise Semantics
How does an organisation obtain its initial semantic model?

## Purpose

This document explores how an AI-powered semantic platform can bootstrap an enterprise semantic model from an organisation's existing knowledge and data landscape.

Rather than requiring organisations to manually define thousands of business concepts before obtaining value, the platform should automatically discover candidate semantic objects, infer relationships, detect inconsistencies and progressively build an enterprise semantic model with human guidance.

This document captures the initial design ideas and open research questions around that process.

---

# Problem

One of the largest barriers to successful data governance and business glossary initiatives is the initial effort required to define and maintain enterprise semantics.

Traditional approaches often require business users to manually document concepts, agree definitions across departments and continuously maintain them as the organisation evolves.

This process is expensive, slow and frequently becomes the bottleneck of the entire governance initiative.

The objective of this project is to investigate whether AI agents can dramatically reduce that effort by automatically discovering business semantics from existing enterprise artefacts while keeping humans in control of governance decisions.

---

# Vision

Enterprise semantics should not start from a blank page.

Every organisation already contains a vast amount of business knowledge distributed across reports, documentation, applications, APIs, databases, source code and collaboration tools.

The platform should continuously learn from these artefacts, propose semantic objects together with supporting evidence and confidence scores, while humans focus on validation rather than manual creation.

Bootstrapping should therefore not be considered a one-off import activity but the beginning of a continuously evolving semantic understanding of the organisation.

---

# Design Principles

## AI starts from evidence

Candidate concepts should only be proposed when supported by evidence found within organisational artefacts.

The system should avoid inventing business concepts without traceable sources.

## Humans govern

AI discovers.

Humans approve.

The goal is to reduce manual work rather than eliminate governance.

## Confidence over certainty

Every discovery should include a confidence score rather than pretending certainty.

Confidence should increase as additional evidence is found across multiple sources.

## Continuous learning

Bootstrapping is not a one-time process.

The semantic model should continuously evolve as the organisation changes.

---

# Bootstrap Workflow

## Phase 1 — Understand the Organisation

The process begins with a human providing high-level organisational context.

Initial information may include:

- organisational structure
- departments
- business domains
- products or services
- organisational chart
- initial system landscape

The objective is not to fully document the organisation but to provide enough context for AI to reason more effectively during semantic discovery.

---

## Phase 2 — Connect Enterprise Knowledge Sources

The human connects the enterprise systems that should be scanned.

Initial sources could include:

### Business documentation

- Company website
- Office 365 documents
- Wikis
- Business documentation
- Process documentation

### Analytics

- Power BI
- Tableau
- Looker
- Existing dashboards
- KPI catalogues

### Technical systems

- APIs
- SQL
- dbt
- Source code
- Jira

The platform should allow organisations to decide which sources are considered authoritative for different business domains.

For example, HR documentation may be considered authoritative for employee terminology while Finance documentation may lead for financial concepts.

---

## Phase 3 — Semantic Discovery

The platform scans connected sources looking for recurring business concepts rather than individual words.

Potential signals include:

- repeated terminology
- recurring KPIs
- similar definitions
- calculation logic
- relationships between concepts
- data lineage
- ownership information

The objective is to infer business meaning from patterns observed across the enterprise rather than relying on any single source.

---

## Phase 4 — Candidate Semantic Object Creation

Discovered concepts are not automatically accepted into the semantic repository.

Instead they are created as Candidate Semantic Objects.

Each candidate should contain information such as:

- proposed concept
- suggested definition
- supporting evidence
- source systems
- confidence score
- suggested owner
- relationships to other concepts
- current review status

---

## Phase 5 — Human Review

Depending on governance policies, candidate objects may require:

- automatic approval
- AI agent validation
- human review
- domain expert approval

High-impact business concepts (for example Revenue, Customer or Churn) may always require human approval before becoming official enterprise semantics.

---

## Phase 6 — Continuous Learning

The platform continues monitoring connected systems after the initial bootstrap.

New reports, documentation, APIs or data models may introduce:

- new concepts
- changed definitions
- duplicate concepts
- conflicting calculations
- ownership changes

Rather than rebuilding the semantic model, the platform continuously proposes updates for review.

---

# Duplicate Detection

Duplicate detection is expected to combine multiple techniques.

Potential approaches include:

- similar names
- similar business definitions
- identical calculation logic
- similar data lineage
- graph relationship similarity
- semantic similarity using language models

Rather than relying on a single rule, the platform should combine multiple signals into an overall confidence score.

This remains an important research area.

---

# Ownership Discovery

Where possible, ownership should be inferred rather than manually assigned.

Possible signals include:

- document ownership
- department usage
- BI workspace ownership
- Git ownership
- Jira ownership
- approval history

Suggested ownership should always remain editable by humans.

---

# Confidence Scoring

Every AI-generated suggestion should include a confidence score.

Confidence may be influenced by:

- number of supporting sources
- consistency across systems
- semantic similarity
- frequency of usage
- agreement between independent AI agents

The confidence model is expected to evolve as the project matures.

---

# Automation vs Human Governance

The platform should automate as much of the discovery process as possible while allowing organisations to define their desired governance model.

Different organisations may require different approval workflows depending on business risk, regulatory requirements or data sensitivity.

The balance between automation and human review is expected to be configurable.

---

# Bootstrap Output

Following the initial scan, the platform could generate an Enterprise Semantic Discovery Report summarising:

- candidate concepts
- duplicate definitions
- conflicting terminology
- suggested owners
- confidence distribution
- terminology consistency across departments
- semantic coverage
- missing definitions
- orphan concepts
- concepts requiring review

This report provides immediate value even before the semantic catalogue has been fully approved.

---

# Open Research Questions

Some of the key research questions remain open.

Examples include:

- How should confidence scores be calculated?
- How should duplicate concepts be identified?
- How can AI distinguish synonyms from genuinely different business concepts?
- Which enterprise sources provide the highest semantic value?
- How should conflicting authoritative sources be resolved?
- How should multiple AI agents collaborate during semantic discovery?
- How can semantic drift be detected over time?

## Non-goals

The bootstrap process is not intended to:

- Automatically replace existing governance processes.
- Automatically overwrite approved definitions.
- Infer business semantics without supporting evidence.
- Produce a perfect semantic model on the first scan.
- Remove the need for human governance.

Its purpose is to accelerate semantic discovery and continuously assist human experts.
