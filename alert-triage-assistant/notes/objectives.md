# CCDV-F objectives tracker

Source: [Claude Certified Developer – Foundations Exam Guide (PDF)](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf) · exam target **2026-10-26** · started 2026-10-02

**Status key:** 🔴 `red` = can't explain it yet · 🟠 `amber` = can explain, haven't built or tested it · 🟢 `green` = built it *and* can answer exam-style questions cold

## Scoreboard

| Status | Count |
|---|---|
| 🔴 red | 25 |
| 🟠 amber | 0 |
| 🟢 green | 0 |

## Domain weights

| Domain | Weight | Note |
|---|---|---|
| 1. Agents and Workflows | 14.7% | ⭐ #3 by weight |
| 2. Applications and Integration | 33.1% | ⭐ one-third of the exam |
| 3. Claude Code | 3.1% |  |
| 4. Eval, Testing, and Debugging | 2.6% |  |
| 5. Model Selection and Optimization | 16.8% | ⭐ #2 by weight |
| 6. Prompt and Context Engineering | 11.0% |  |
| 7. Security and Safety | 8.1% |  |
| 8. Tools and MCPs | 10.6% |  |

> 🎯 **Top 5 task statements by weight:** 2.5 (8.6%) · 2.4 (7.4%) · 2.3 (6.8%) · 5.2 (6.1%) · 1.2 (5.3%). Together they are about a third of the exam.

## Domain 1: Agents and Workflows (14.7%)

| # | Task statement | Weight | Status | Evidence / day covered |
|---|---|---|---|---|
| **1.1** | **Agent Architecture**: Principles, patterns, and tradeoffs of agent and workflow architecture, including the decision criteria for using a workflow versus an agent, the structure of manager/supervisor hierarchies, and the role of subagents in improving task execution. | 4.5% | `red` | |
| **1.2** | **Agent Construction with Claude**: Methods, tools, and platforms for constructing Claude agents, including the Claude Agent SDK, custom agent loops and harnesses, managed agent deployment models (self-hosted vs. Anthropic-hosted), and hooks for deterministic actions. | 5.3% | `red` | |
| **1.3** | **Agent Patterns and Frameworks**: Common agent design patterns (tool-use loops, sub-agents, memory, context-window management) and agentic abstraction frameworks (e.g., Strands, LangGraph, PydanticAI) for building agents and workflows for multi-step tasks. | 4.9% | `red` | |

## Domain 2: Applications and Integration (33.1%)

| # | Task statement | Weight | Status | Evidence / day covered |
|---|---|---|---|---|
| **2.1** | **Understanding Requirements**: Functional and infrastructure requirements based on business requirements and solution architecture. | 3.4% | `red` | |
| **2.2** | **Systems Life Cycle**: Systems life cycle management concepts and frameworks used to develop, implement, operate, and maintain IT systems. | 2.8% | `red` | |
| **2.3** | **Claude API Mechanics**: Claude API behavior and mechanics, including messages, tools, streaming, vision, thinking, caching, invoking Claude through third-party vendors, Messages API data access patterns, batch API use, and tradeoffs between realtime and batch API selection. | 6.8% | `red` | |
| **2.4** | **Software Engineering Foundations**: Core software engineering principles and practices, including REST APIs, JSON, asynchronous programming, version control, SDLC integration, code review, and small- and large-scale refactoring. | 7.4% | `red` | |
| **2.5** | **Claude Application Design**: Design considerations for building Claude applications, including how Claude interprets instructions across interfaces (Claude Code, Desktop, claude.ai, API, SDKs), content boundaries, schema design, session hygiene, and plugin management. | 8.6% | `red` | |
| **2.6** | **Configuration Management**: Configuration management for Claude system components, including CLAUDE.md files, settings.json, model version pinning, prompt versioning, and plugin dependencies. | 4.1% | `red` | |

## Domain 3: Claude Code (3.1%)

| # | Task statement | Weight | Status | Evidence / day covered |
|---|---|---|---|---|
| **3.1** | **Claude Code Operation**: Claude Code core components (Rules, Skills, Commands, Agents, Agent Memory), features (session management, built-in and custom slash commands, headless mode, streaming mode, auto-mode), the CLAUDE.md hierarchy, repository initialization, and settings.json configuration. | 3.1% | `red` | |

## Domain 4: Eval, Testing, and Debugging (2.6%)

| # | Task statement | Weight | Status | Evidence / day covered |
|---|---|---|---|---|
| **4.1** | **Debugging and Error Handling**: Debugging and error handling techniques for Claude applications, including error type identification, recovery strategy selection, trace analysis to identify failure modes, and problem origin isolation between the integration layer and model output. | 2.6% | `red` | |

## Domain 5: Model Selection and Optimization (16.8%)

| # | Task statement | Weight | Status | Evidence / day covered |
|---|---|---|---|---|
| **5.1** | **LLM Fundamentals**: Basic understanding of LLMs (tokens, context windows, sampling, non-determinism, next-token generation), model options (fast mode, extended thinking, adaptive thinking, effort levels), and fundamental prompting techniques (zero-shot, single-shot, multi-shot). | 5.2% | `red` | |
| **5.2** | **Technical Fundamentals**: Foundational technical concepts supporting AI application development, including basic engineering practices (integrating with SDKs that wrap REST APIs, websockets). | 6.1% | `red` | |
| **5.3** | **Model Selection and Tradeoffs**: Claude model capabilities (Opus vs. Sonnet vs. Haiku use cases, adaptive thinking support), tradeoffs across quality/latency/cost parameters, and breaking behavior changes across model releases when selecting models for tasks. | 2.7% | `red` | |
| **5.4** | **Cost and Token Management**: Token budgeting and cost management techniques for Claude applications, including token usage tracking, cost modeling, and caching techniques (prompt caching, cache check-pointing) for cost optimization. | 2.8% | `red` | |

## Domain 6: Prompt and Context Engineering (11.0%)

| # | Task statement | Weight | Status | Evidence / day covered |
|---|---|---|---|---|
| **6.1** | **Context Engineering**: Context and memory management techniques for Claude applications, including context window management, prevention of context drift and bloat (tool output pruning, compaction), and context isolation through subagents or multi-step agentic workflows. | 3.8% | `red` | |
| **6.2** | **Prompt Engineering**: Prompt engineering principles and methods (instruction clarity, few-shot examples, system versus user placement, output constraints, prompt and instruction placement across components, iterative refinement, prompt adjustment, input sanitization) when writing and iterating on prompts for Claude. | 4.6% | `red` | |
| **6.3** | **Output Handling**: Established patterns and techniques for producing, validating, and consuming Claude output, including structured output patterns, response validation, defensive parsing, and skepticism toward confident output. | 2.6% | `red` | |

## Domain 7: Security and Safety (8.1%)

| # | Task statement | Weight | Status | Evidence / day covered |
|---|---|---|---|---|
| **7.1** | **AI Application Security**: Data privacy and security best practices, including prompt injection awareness and mitigation, jailbreak defense, untrusted input handling, data leakage prevention, PII handling, and ensuring authentication, authorization, confidentiality, privacy, and integrity. | 3.2% | `red` | |
| **7.2** | **Guardrails and Safe Deployment**: Safe and responsible deployment practices (content policy, guardrail layering) and secure-by-design principles (privacy, identity and access management, least privilege). | 2.3% | `red` | |
| **7.3** | **Claude Hooks**: Leveraging hooks for guardrails and safety controls to prevent destructive actions within Claude applications. | 1.0% | `red` | |
| **7.4** | **Identity, Secrets, and Key Management**: Managing secrets, credentials, and API keys across Claude development and production environments, including identity validation and authentication, access approval and level verification, and authorized access monitoring. | 1.6% | `red` | |

## Domain 8: Tools and MCPs (10.6%)

| # | Task statement | Weight | Status | Evidence / day covered |
|---|---|---|---|---|
| **8.1** | **Tool Implementation**: Tool implementation practices for Claude applications, including tool use and function calling, configuration for external system interaction, tool description writing, error handling, tool usage patterns (agentic harness dispatch, client-side vs. server-side tools, approval patterns), and tool set construction best practices. | 4.4% | `red` | |
| **8.2** | **MCP Server Development**: MCP server development practices, including server authoring, deployment, integration with Claude applications, MCP resources, tools, and prompts, and communication patterns (stdio, sockets, client vs. server). | 2.1% | `red` | |
| **8.3** | **Agentic Customization**: Tradeoffs among built-in Tools, custom Tools, Skills, and MCPs for selecting and applying the appropriate approach for a given use case. | 4.1% | `red` | |
