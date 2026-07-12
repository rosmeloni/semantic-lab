# Experiment 001: KPI Definition Reconciliation

## Purpose

Test whether an AI-assisted process can identify, compare and reconcile
different definitions of the same business concept while preserving
evidence, uncertainty and unresolved disagreement.

## Research hypothesis

Given a small set of heterogeneous enterprise artefacts describing the
same business metric, the system can:

1. identify candidate definitions;
2. determine that they refer to the same or related concept;
3. expose meaningful semantic differences;
4. propose a canonical definition;
5. provide sufficient evidence for a human reviewer to make a decision.

## Scope

The experiment focuses on one metric and four synthetic source artefacts:

- a dashboard description;
- a glossary entry;
- a finance document;
- a SQL query.

The experiment does not include:

- live system connectors;
- automatic publication;
- enterprise authentication;
- a production knowledge graph;
- autonomous governance decisions.

## Inputs

List the source artefacts and describe the intentional differences between them.

## Expected output

A structured candidate concept containing:

- preferred name;
- proposed definition;
- source evidence;
- detected conflicts;
- confidence assessments;
- recommended governance action.

## Success criteria

The experiment is successful if:

- all materially relevant definitions are extracted;
- the records are recognised as referring to the same concept;
- the intentionally introduced conflicts are detected;
- every assertion can be traced back to source evidence;
- the output distinguishes facts, interpretations and recommendations;
- the system does not declare a definition authoritative without approval.

## Evaluation

Results will initially be evaluated manually against an expected findings file.

Future versions may use:

- precision and recall for conflict detection;
- reviewer agreement;
- time required for human resolution;
- false-positive semantic matches;
- confidence calibration.

## Findings

To be completed after implementation.

## Follow-up questions

- How should semantic similarity be measured?
- Which conflicts require human review?
- Can low-risk differences be resolved automatically?
- How should source authority influence recommendations?
- How should accepted decisions affect future inference?
