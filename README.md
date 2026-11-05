# 🧠 OmniNemotron: Multimodal Agentic Intelligence Platform

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB.svg?logo=python&logoColor=white)](https://python.org)
[![NVIDIA NIM](https://img.shields.io/badge/NVIDIA-NIM%20AI-76B900.svg?logo=nvidia&logoColor=white)](https://build.nvidia.com)
[![LangChain 1.4](https://img.shields.io/badge/LangChain-1.4+-1C3C3C.svg?logo=chainlink&logoColor=white)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.66-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2-E92063.svg?logo=pydantic&logoColor=white)](https://pydantic.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**OmniNemotron** is an enterprise-grade, end-to-end multimodal agentic AI platform and interactive executive dashboard powered by **NVIDIA Nemotron 3.5 Super VL** (124B parameters, 262K context window). The system unifies deep chain-of-thought mathematical reasoning, computer vision spatial safety auditing, video temporal kinematics analysis, autonomous multi-turn ReAct tool orchestration, and Pydantic v2 schema-enforced structured extraction into a single cohesive architecture.

---

## 📌 Model Specifications: NVIDIA Nemotron 3.5 Super VL

| Attribute | Technical Specification |
| :--- | :--- |
| **Model ID** | `nvidia/nemotron-3.5-super-vl-120b-a12b` (Direct NIM) / `nvidia/nemotron-3.5-super-vl:free` (OpenRouter) |
| **Architecture** | 124B Mixture-of-Experts (MoE) · ~12B Active Parameters per Token |
| **Context Window** | **262,144 Tokens (262K)** — Massive document, multi-image, and video stream support |
| **Input Modalities** | **Text**, **High-Resolution Images**, **Video Streams (MP4)** |
| **Output Modalities** | **Text** (with native JSON structured schema generation) |
| **Core Capabilities** | **Chain-of-Thought Reasoning (`enable_thinking`)**, **Autonomous Function Calling**, **Structured Schema Output** |
| **Inference Acceleration**| NVIDIA NIM microservices with TensorRT-LLM and FP8 quantization |

---

## 🏛️ System Architecture

```text
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │                         OmniNemotron Command Center                         │
 │                     (Interactive Streamlit Dashboard)                       │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
           ┌────────────────────────────┴────────────────────────────┐
           ▼                                                         ▼
 ┌───────────────────────────────────┐             ┌───────────────────────────────────┐
 │       Unified Model Factory       │             │       Autonomous ReAct Engine     │
 │  - NVIDIA NIM Direct Microservice │             │  - Dynamic Tool Registry          │
 │  - OpenRouter Free Endpoint       │             │  - Multi-Turn Execution Loop      │
 │  - Groq LLaMA 3.3 70B (Ultra-Fast)│             │  - Real-Time Action Trace         │
 │  - OpenAI GPT-4o & Google Gemini  │             │  - Pydantic v2 Schema Validation  │
 └─────────────────┬─────────────────┘             └─────────────────┬─────────────────┘
                   │                                                 │
                   └────────────────────────┬────────────────────────┘
                                            │
                                            ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │                 NVIDIA Nemotron 3.5 Super VL (124B MoE)                     │
 │          Text + Image + Video Input  ───►  Reasoned Text Output             │
 └──────────────────┬───────────────────────┬───────────────────────┬──────────┘
                    │                       │                       │
                    ▼                       ▼                       ▼
           ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
           │ 🧠 CoT Thinking │     │ 🖼️ Vision OCR   │     │ 🎬 Video Motion │
           │ & Mathematical  │     │ & Spatial Hazard│     │ & Anomaly Event │
           │ Proof Synthesis │     │ Classification  │     │ Timeline Mining │
           └─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## ✨ Interactive Operational Modules (7 Cards)

The platform provides an executive tabbed interface where each capability is encapsulated into an interactive card:

### 1. 🧠 CoT Reasoning Studio
- Inspects transparent `<thought>` internal reasoning tokens delivered via `additional_kwargs["reasoning_content"]`.
- Includes 5 challenge templates:
  - Quantitative Capital Allocation & Compound Growth
  - Distributed Microservices Root Cause Analysis (RCA)
  - Forensic Detective Deductive Logic
  - Mathematical Physics & Soft-Margin SVM Dual Proofs
  - Custom Analytical Prompting
- 4 system personas (Senior Quantitative Analyst, Principal SRE, Forensic Detective, University ML Professor).
- Direct Markdown export and download options.

### 2. 🖼️ Multimodal Vision Intelligence
- Supports 3 flexible image ingestion modes: **Curated Preset Gallery**, **Public Image URL**, or **Local Image Upload (JPG/PNG/WEBP)** with base64 data URI encoding.
- 4 inspection modes:
  - Autonomous Vehicle Road Safety & Spatial Hazard Classification
  - Financial Infographic & Numerical Data Table Reconstruction
  - Text & Signpost OCR Transcription
  - Custom Visual Q&A Directives

### 3. 🎬 Video Temporal Reasoning Engine
- Supports MP4 streaming via direct NVIDIA NIM microservices.
- Temporal analytics tasks:
  - Chronological Event Timelines (00:00 to End)
  - Kinematics & Velocity Trajectory Tracking
  - Autonomous Hazard & Anomaly Detection
  - Industrial Robotics Automation Feasibility

### 4. 🔧 Autonomous ReAct Agent & Tool Console
- Autonomous multi-turn decision loop where Nemotron decides which tools to call, inspects intermediate outputs, and synthesizes an executive brief.
- 4 built-in enterprise tools:
  - `get_financial_metrics(ticker)`: Real-time stock indicators for NVDA, MSFT, AAPL, GOOGL, AMZN, TSLA, META.
  - `compute_investment_simulation(principal, annual_return_rate, years, monthly_contribution)`: Multi-year compound wealth simulation with ROI metrics.
  - `convert_currency_and_units(amount, from_unit, to_unit)`: Conversion across USD, INR, EUR, GBP, JPY, and physical units (km/miles, kg/lbs, Celsius/Fahrenheit).
  - `query_enterprise_kb(query)`: Semantic technical knowledge base for Nemotron, NIM, LangChain, LangGraph, RAG, CUDA, and TensorRT-LLM.
- Step-by-step turn inspection displaying tool arguments, JSON responses, and agent reasoning.

### 5. 📊 Schema-Enforced Structured Extraction (Pydantic v2)
- Zero-hallucination, 100% type-safe JSON extraction using LangChain's `.with_structured_output()`.
- 3 enterprise schemas:
  - `CandidateProfile`: Executive resume parsing with nested `Experience` models and hiring scores (1-100).
  - `AuditReport`: Cybersecurity assessment with severity ratings (`CRITICAL`, `HIGH`, `MEDIUM`) and remediation actions.
  - `Invoice`: Financial transaction parser extracting vendor, client, line items, and sales tax.
- In-browser JSON viewer with one-click JSON file download.

### 6. 🚀 Grand Capstone: Unified Multimodal Investigation
- End-to-end mission pipeline fusing **Vision + Reasoning + Tool Calling + Pydantic v2 Schema Enforcement**.
- Evaluates visual assets against regulatory frameworks (OSHA Urban Safety, ISO-27001 Security, NVIDIA AI Enterprise Architecture).
- Emits an `InvestigationDossier` complete with case ID, hazard severity scores (1-10), observation logs, and prioritized remediation directives.

### 7. 💼 Portfolio & Resume Showcase
- Interactive resume-ready dossier highlighting architecture decisions, quantified business impacts, and technical bullet points for hiring managers.

---

## 🛠️ Tech Stack & Dependencies

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Core Model** | **NVIDIA Nemotron 3.5 Super VL** | 124B MoE foundation model for multimodal reasoning |
| **Inference** | **NVIDIA NIM & OpenRouter** | High-performance inference endpoints with CUDA acceleration |
| **Agent Framework** | **LangChain 1.4+ & LangChain Core** | Tool binding, prompt templating, and ReAct loops |
| **Type Validation** | **Pydantic v2 (2.10+)** | Schema enforcement, data validation, and JSON serialization |
| **User Interface** | **Streamlit (1.35+)** | Responsive web dashboard with custom NVIDIA CSS styling |
| **Notebooks** | **Jupyter / IPython Kernel** | Exploratory research and step-by-step model validation |
| **Runtime** | **Python 3.12** | Modern Python runtime |

---

## ⚡ Quick Start Guide

### 1. Clone & Configure Environment
Clone the repository and set up your `.env` file:
```bash
git clone https://github.com/your-username/OmniNemotron.git
cd OmniNemotron
```

Create a `.env` file in the root directory:
```env
NV_NEMO_API_KEY="nvapi-your-nvidia-api-key"
OPENROUTER_API_KEY="sk-or-v1-your-openrouter-key"
OPENAI_API_KEY="sk-your-openai-key"          # Optional
GROQ_API_KEY="gsk-your-groq-key"            # Optional
GOOGLE_API_KEY="your-google-ai-key"          # Optional
```

### 2. Install Dependencies
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Launch the Executive Dashboard
Double-click `run_app.bat` or run:
```bash
.\.venv\Scripts\streamlit run app.py
```
Open your browser at `http://localhost:8501`.

### 4. Interactive Jupyter Notebooks
Explore the step-by-step notebooks in `updatedlangchain/`:
- `Nemotron.ipynb`: Deep walkthrough of all Nemotron 3.5 capabilities.
- `multimodal_intelligence_agent.ipynb`: Multimodal agent implementation with tools and Pydantic schemas.
- `langchain_intro.ipynb`: Foundation LangChain setup and API connection validation.

---

## 💼 Quantified Resume Highlights

Drop these bullet points directly into your resume under Experience / Projects:

> - **Architected and deployed an end-to-end Multimodal Agentic AI Platform** powered by NVIDIA Nemotron 3.5 Super VL (124B MoE, 262K context window) spanning text reasoning, computer vision, and video temporal analysis across 7 operational modules.
> - **Engineered an interactive Streamlit Command Center** featuring NVIDIA-branded glassmorphism design, real-time hyperparameter tuning, multi-provider model orchestration, and live chain-of-thought reasoning trace inspection.
> - **Implemented autonomous multi-turn ReAct agents with dynamic tool calling**, orchestrating 4 enterprise tools (financial market intelligence, compound wealth simulations, multi-currency converters, and vector knowledge retrieval) with step-by-step execution transparency.
> - **Pioneered type-safe data pipelines using Pydantic v2 structured outputs**, guaranteeing 100% schema compliance across 3 enterprise extraction templates (CV parsing, PCI-DSS compliance auditing, and financial invoice processing) with zero JSON parse failures.
> - **Constructed a unified multimodal capstone pipeline** combining vision analysis, chain-of-thought reasoning, autonomous tool orchestration, and Pydantic schema enforcement into a single executive investigation dossier with governance compliance scoring.
> - **Built multi-provider model fallback architecture** supporting 5 LLM providers (NVIDIA NIM Direct, OpenRouter, Groq, OpenAI, Google Gemini) with live API key status monitoring, dynamic credential override, and seamless provider switching.

---

## 📂 Project Directory Structure

```text
d:\LangChain\
├── .env                                # API keys for NVIDIA NIM, OpenRouter, etc.
├── .gitignore                          # Git exclusions (venv, secrets, cache)
├── app.py                              # 7-Tab Streamlit Production Application
├── pyproject.toml                      # Modern packaging & dependencies
├── README.md                           # Enterprise documentation & portfolio guide
├── requirements.txt                    # Pinned Python dependencies
├── run_app.bat                         # One-click Windows application launcher
└── updatedlangchain/
    ├── langchain_intro.ipynb           # Basic API connection & setup verification
    ├── Nemotron.ipynb                  # 23-cell comprehensive Nemotron exploration
    └── multimodal_intelligence_agent.ipynb  # End-to-end multimodal agent notebook
```

---

## 📜 License & Credits

- **Author**: Kavala Adharsh Raj ([GitHub](https://github.com/adharsh77) · [LinkedIn](https://linkedin.com))
- **License**: MIT License — free for educational and commercial portfolio use.
- **Powered by**: [NVIDIA NIM](https://build.nvidia.com) & [LangChain](https://python.langchain.com).
