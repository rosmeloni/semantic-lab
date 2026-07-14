# ADR 001: Introduce a provider-independent LLM interface

- **Status:** Accepted
- **Date:** 2026-07-14
- **Decision owners:** Semantic Lab
- **Related experiment:** `experiments/001-bootstrap-agent`

## Context

The Bootstrap Agent will use a large language model to analyse business artefacts and propose candidate enterprise semantics.

Several model providers could support this work, including OpenAI, Anthropic and Google. Their APIs, model capabilities, structured-output mechanisms, pricing and operational characteristics differ and will continue to evolve.

Connecting the Bootstrap Agent directly to one provider would couple the agent workflow to that provider's SDK and request format. This would make it harder to:

- compare models experimentally;
- change providers;
- benchmark output quality, latency and cost;
- test the agent independently of an external API;
- preserve the agent workflow as model capabilities evolve.

Semantic Lab is also intended to investigate semantic reasoning rather than demonstrate the use of one particular model provider.

## Decision

The Bootstrap Agent will interact with language models through a small provider-independent interface.

The agent workflow will depend on an internal contract rather than directly on a provider SDK.

Conceptually:

```text
Bootstrap Agent
       |
       v
LLM Interface
       |
       +-- OpenAI adapter
       +-- Anthropic adapter
       +-- Gemini adapter