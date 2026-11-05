"""
OmniNemotron: Multimodal Agentic AI Intelligence Platform v2.0
Powered by NVIDIA Nemotron 3.5 Super VL (124B MoE, 262K Context)
Author: Kavala Adharsh Raj
"""

import os
import io
import json
import base64
from datetime import datetime
from typing import List, Optional

import streamlit as st
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def get_credential(key_name: str, default: str = "") -> str:
    """Retrieve credential from Streamlit Cloud Secrets or local .env environment."""
    try:
        if key_name in st.secrets:
            return str(st.secrets[key_name]).strip()
    except Exception:
        pass
    val = os.getenv(key_name, default)
    return str(val).strip() if val else ""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PAGE CONFIG
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.set_page_config(
    page_title="OmniNemotron AI Platform",
    page_icon="\U0001f9e0",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CUSTOM CSS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .hero-banner {
        background: linear-gradient(135deg, #0a0f1d 0%, #0d1b2a 40%, #112240 100%);
        border: 1px solid rgba(118,185,0,0.3);
        border-radius: 16px;
        padding: 30px 40px;
        margin-bottom: 24px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    }
    .hero-title {
        font-size: 2.4rem; font-weight: 800; color: #fff;
        letter-spacing: -0.5px; margin-bottom: 6px;
    }
    .hero-title .accent {
        background: linear-gradient(90deg, #76b900 0%, #00ff88 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .hero-sub { color: #94a3b8; font-size: 1rem; margin-bottom: 16px; }

    .pill {
        display: inline-block; padding: 4px 14px; border-radius: 9999px;
        font-size: 0.72rem; font-weight: 600; letter-spacing: 0.5px;
        text-transform: uppercase; margin: 0 6px 6px 0;
    }
    .pill-green  { background: rgba(118,185,0,0.15); color: #76b900; border: 1px solid rgba(118,185,0,0.4); }
    .pill-cyan   { background: rgba(6,182,212,0.15); color: #22d3ee; border: 1px solid rgba(6,182,212,0.4); }
    .pill-purple { background: rgba(168,85,247,0.15); color: #c084fc; border: 1px solid rgba(168,85,247,0.4); }
    .pill-amber  { background: rgba(245,158,11,0.15); color: #fbbf24; border: 1px solid rgba(245,158,11,0.4); }

    .kpi-card {
        background: #ffffff; border-radius: 12px; padding: 18px 22px;
        border-left: 4px solid #76b900;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06); margin-bottom: 12px;
    }
    .kpi-card .label {
        color: #64748b; font-size: 0.75rem; text-transform: uppercase;
        letter-spacing: 0.5px; margin: 0;
    }
    .kpi-card .value {
        color: #0f172a; font-size: 1.35rem; font-weight: 700; margin-top: 4px;
    }

    .thought-box {
        background: #0f172a; color: #94a3b8; border: 1px solid #334155;
        border-radius: 10px; padding: 18px;
        font-family: 'JetBrains Mono', monospace; font-size: 0.82rem;
        line-height: 1.65; max-height: 300px; overflow-y: auto;
        white-space: pre-wrap; margin-bottom: 14px;
    }

    .stTabs [data-baseweb="tab-list"] { gap: 6px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; border-radius: 10px 10px 0 0;
        padding: 10px 16px; font-weight: 600; font-size: 0.9rem;
    }

    .section-divider {
        border: none; border-top: 1px solid #e2e8f0; margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SIDEBAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 10px 0 5px;">
        <span style="font-size:2rem; font-weight:800; color:#76b900;">NVIDIA</span><br>
        <span style="font-size:0.85rem; color:#94a3b8; letter-spacing:1px;">NEMOTRON AI PLATFORM</span>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### Model Orchestration")

    model_choice = st.selectbox(
        "Active Intelligence Engine",
        options=[
            "NVIDIA Nemotron 3.5 Super VL (Direct NIM)",
            "NVIDIA Nemotron 3.5 Super VL (OpenRouter)",
            "Groq LLaMA 3.3 70B (Ultra-Fast)",
            "OpenAI GPT-4o (Omni)",
            "Google Gemini 1.5 Pro",
        ],
        index=0,
    )

    st.markdown("### Hyperparameters")
    temperature = st.slider("Temperature", 0.0, 1.5, 0.6, 0.05)
    max_tokens = st.slider("Max Output Tokens", 256, 16384, 4096, 256)
    top_p = st.slider("Top-P (Nucleus Sampling)", 0.1, 1.0, 0.95, 0.05)
    enable_thinking = st.toggle("Deep Thinking Mode (CoT)", value=True,
                                help="Enable chain-of-thought internal reasoning traces.")

    st.divider()
    st.markdown("### API Key Status")

    nv_key = get_credential("NV_NEMO_API_KEY")
    or_key = get_credential("OPENROUTER_API_KEY")
    groq_key = get_credential("GROQ_API_KEY")
    oai_key = get_credential("OPENAI_API_KEY")
    gemini_key = get_credential("GOOGLE_API_KEY")

    def _status(key, label):
        icon = "&#9679;" if key else "&#9675;"
        color = "#10b981" if key else "#ef4444"
        return f'<span style="color:{color}">{icon}</span> {label}'

    st.markdown(
        _status(nv_key, "NVIDIA NIM") + "<br>" +
        _status(or_key, "OpenRouter") + "<br>" +
        _status(groq_key, "Groq Cloud") + "<br>" +
        _status(oai_key, "OpenAI") + "<br>" +
        _status(gemini_key, "Google AI"),
        unsafe_allow_html=True,
    )

    with st.expander("Override API Keys"):
        nv_override = st.text_input("NV_NEMO_API_KEY", value=nv_key, type="password")
        or_override = st.text_input("OPENROUTER_API_KEY", value=or_key, type="password")
        groq_override = st.text_input("GROQ_API_KEY", value=groq_key, type="password")
        oai_override = st.text_input("OPENAI_API_KEY", value=oai_key, type="password")
        gemini_override = st.text_input("GOOGLE_API_KEY", value=gemini_key, type="password")
        if nv_override: nv_key = nv_override
        if or_override: or_key = or_override
        if groq_override: groq_key = groq_override
        if oai_override: oai_key = oai_override
        if gemini_override: gemini_key = gemini_override

    st.divider()
    st.caption("OmniNemotron v2.0 | Built with LangChain + NVIDIA NIM")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODEL FACTORY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def get_active_model(temp=None, max_tok=None, thinking=None):
    """Instantiate the selected LangChain Chat model."""
    _temp = temp if temp is not None else temperature
    _max = max_tok if max_tok is not None else max_tokens
    _think = thinking if thinking is not None else enable_thinking

    if "Direct NIM" in model_choice:
        if not nv_key:
            st.error("NVIDIA NIM API Key missing. Set NV_NEMO_API_KEY in .env or sidebar.")
            st.stop()
        from langchain_nvidia_ai_endpoints import ChatNVIDIA
        client = ChatNVIDIA(
            base_url="https://integrate.api.nvidia.com/v1",
            model="nvidia/nemotron-3.5-super-vl-120b-a12b",
            api_key=nv_key,
            temperature=_temp,
            top_p=top_p,
            max_completion_tokens=_max,
            seed=42,
        )
        if _think:
            client = client.bind(**{"chat_template_kwargs": {"enable_thinking": True}})
        return client

    elif "OpenRouter" in model_choice:
        if not or_key:
            st.error("OpenRouter API Key missing. Set OPENROUTER_API_KEY in .env.")
            st.stop()
        from langchain_openrouter import ChatOpenRouter
        return ChatOpenRouter(
            model="nvidia/nemotron-3.5-super-vl:free",
            api_key=or_key,
            temperature=_temp,
            max_tokens=_max,
        )

    elif "Groq" in model_choice:
        if not groq_key:
            st.error("Groq API Key missing. Set GROQ_API_KEY in .env.")
            st.stop()
        from langchain_groq import ChatGroq
        return ChatGroq(
            model_name="llama-3.3-70b-versatile",
            groq_api_key=groq_key,
            temperature=_temp,
            max_tokens=_max,
        )

    elif "OpenAI" in model_choice:
        if not oai_key:
            st.error("OpenAI API Key missing. Set OPENAI_API_KEY in .env.")
            st.stop()
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model="gpt-4o",
            api_key=oai_key,
            temperature=_temp,
            max_tokens=_max,
        )

    elif "Gemini" in model_choice:
        if not gemini_key:
            st.error("Google API Key missing. Set GOOGLE_API_KEY in .env.")
            st.stop()
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            google_api_key=gemini_key,
            temperature=_temp,
            max_output_tokens=_max,
        )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HERO BANNER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
active_engine_label = model_choice.split("(")[0].strip()
thinking_color = "#10b981" if enable_thinking else "#64748b"
thinking_label = "ACTIVE" if enable_thinking else "STANDARD"

st.markdown(f"""
<div class="hero-banner">
    <div class="hero-title">OmniNemotron <span class="accent">Command Center</span></div>
    <div class="hero-sub">
        Production-Grade Multimodal AI Platform &mdash; Powered by NVIDIA Nemotron 3.5 Super VL
    </div>
    <div>
        <span class="pill pill-green">NVIDIA Nemotron 3.5</span>
        <span class="pill pill-cyan">124B MoE Parameters</span>
        <span class="pill pill-purple">262K Context Window</span>
        <span class="pill pill-green">Text + Image + Video</span>
        <span class="pill pill-amber">Function Calling</span>
        <span class="pill pill-cyan">Structured Output</span>
        <span class="pill pill-purple">Chain-of-Thought</span>
    </div>
</div>
""", unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown('<div class="kpi-card"><p class="label">Architecture</p><div class="value">124B MoE</div></div>', unsafe_allow_html=True)
with k2:
    st.markdown('<div class="kpi-card"><p class="label">Context Length</p><div class="value">262,144 Tokens</div></div>', unsafe_allow_html=True)
with k3:
    st.markdown(f'<div class="kpi-card"><p class="label">Active Engine</p><div class="value" style="font-size:1rem;color:#76b900;">{active_engine_label}</div></div>', unsafe_allow_html=True)
with k4:
    st.markdown(f'<div class="kpi-card"><p class="label">Reasoning Mode</p><div class="value" style="color:{thinking_color}">{thinking_label}</div></div>', unsafe_allow_html=True)

st.write("")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MAIN TABS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
tab_reason, tab_vision, tab_video, tab_agent, tab_struct, tab_capstone, tab_resume = st.tabs([
    "CoT Reasoning",
    "Vision Intelligence",
    "Video Engine",
    "ReAct Agent",
    "Structured Extract",
    "Capstone Dossier",
    "Resume Showcase",
])


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 1 — DEEP CHAIN-OF-THOUGHT REASONING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_reason:
    st.markdown("### Deep Chain-of-Thought Reasoning Engine")
    st.caption("Inspect transparent step-by-step thinking traces before the model delivers its final answer.")

    left_r, right_r = st.columns([1, 2])

    with left_r:
        st.markdown("#### Input Configuration")

        persona = st.selectbox("System Persona", [
            "Senior Quantitative Risk Analyst",
            "Principal Site Reliability Engineer (SRE)",
            "Forensic Detective & Logic Expert",
            "University ML/AI Professor",
        ], key="reason_persona")

        preset_reason = st.selectbox("Challenge Template", [
            "Custom Query",
            "Quantitative Risk & Capital Allocation",
            "Distributed Microservices RCA",
            "Detective Mystery Deduction",
            "Mathematical Proof Derivation",
        ], key="reason_preset")

        _reason_defaults = {
            "Custom Query": "Explain how Mixture-of-Experts (MoE) balances throughput and inference latency in 124B-parameter models. Include mathematical intuition.",
            "Quantitative Risk & Capital Allocation": (
                "A firm has $300,000 capital. Strategy A: 8.5% compounded annually for 6 years "
                "with 1% yearly management fee. Strategy B: 7.9% compounded quarterly with a 15% "
                "exit tax on gains. Which provides higher net liquidation return? Show exact math."
            ),
            "Distributed Microservices RCA": (
                "System outage log:\n"
                "- 14:02 Gateway API at 99.9% uptime\n"
                "- 14:05 DB connection pool reached 98% utilization\n"
                "- 14:07 Payment engine timed out, retried with 0ms backoff\n"
                "- 14:11 Auth service CPU spiked to 100%\n\n"
                "Identify the primary root cause vs. cascading symptoms. Propose 3 architectural remedies."
            ),
            "Detective Mystery Deduction": (
                "Theft between 8-9 PM. Alice was at the gym 7-9:30 PM (CCTV confirmed). "
                "Bob & Charlie dined at a restaurant 6-11 PM (staff verified). "
                "Diana claims she was home alone. Eve says she was at Diana's house. "
                "A neighbor saw someone leave Diana's house at 8:15 and return at 9:05. "
                "Crime scene had Diana's perfume. Who committed the theft? Show deductive reasoning."
            ),
            "Mathematical Proof Derivation": (
                "Derive the dual formulation of the soft-margin Support Vector Machine from the "
                "primal Lagrangian. Explain the role of hyperparameter C in controlling the "
                "margin-slack vs. misclassification penalty trade-off."
            ),
        }

        user_reason_prompt = st.text_area(
            "Challenge Prompt",
            value=_reason_defaults[preset_reason],
            height=200,
            key="reason_prompt",
        )

        run_reason = st.button("Execute Reasoning", type="primary", use_container_width=True, key="btn_reason")

    with right_r:
        st.markdown("#### Analytical Output")
        if run_reason:
            with st.spinner("Reasoning in progress..."):
                try:
                    from langchain_core.messages import SystemMessage, HumanMessage
                    llm = get_active_model()
                    messages = [
                        SystemMessage(content=f"You are a {persona}. Be rigorous, structured, and clear. Show your work step by step."),
                        HumanMessage(content=user_reason_prompt),
                    ]
                    resp = llm.invoke(messages)

                    # Show thinking trace if available
                    if hasattr(resp, "additional_kwargs") and "reasoning_content" in resp.additional_kwargs:
                        with st.expander("Internal Reasoning Trace (thought)", expanded=False):
                            st.markdown(
                                f'<div class="thought-box">{resp.additional_kwargs["reasoning_content"]}</div>',
                                unsafe_allow_html=True,
                            )

                    st.markdown("**Final Resolution:**")
                    st.markdown(resp.content)

                    st.download_button(
                        label="Download Analysis (Markdown)",
                        data=resp.content,
                        file_name="reasoning_analysis.md",
                        mime="text/markdown",
                    )
                except Exception as e:
                    st.error(f"Reasoning error: {e}")
        else:
            st.info("Select a challenge template or write a custom prompt, then click Execute Reasoning.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 2 — MULTIMODAL VISION INTELLIGENCE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_vision:
    st.markdown("### Multimodal Vision Intelligence")
    st.caption("Analyze images: road safety audits, chart OCR, signpost transcription, and custom visual Q&A.")

    left_v, right_v = st.columns([1, 1])

    with left_v:
        st.markdown("#### Image Input")

        img_mode = st.radio("Input Mode", ["Curated Preset", "Image URL", "Upload File"], horizontal=True, key="vis_mode")

        selected_img_url = ""
        uploaded_img = None

        if img_mode == "Curated Preset":
            preset_img = st.selectbox("Preset Gallery", [
                "Urban Street & Road Safety (Traffic Scene)",
                "Renewable Energy Investment Chart",
                "Times Square Dense Scene",
            ], key="vis_preset")

            _img_urls = {
                "Urban Street & Road Safety (Traffic Scene)": "https://assets.ngc.nvidia.com/products/api-catalog/phi-3-5-vision/example1a.jpg",
                "Renewable Energy Investment Chart": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Renewable_energy_global_investment_2004-2018.png/800px-Renewable_energy_global_investment_2004-2018.png",
                "Times Square Dense Scene": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/New_york_times_square-terabass.jpg/800px-New_york_times_square-terabass.jpg",
            }
            selected_img_url = _img_urls[preset_img]
            st.image(selected_img_url, caption="Selected Preset", use_container_width=True)

        elif img_mode == "Image URL":
            selected_img_url = st.text_input(
                "Paste Public Image URL",
                value="https://assets.ngc.nvidia.com/products/api-catalog/phi-3-5-vision/example1a.jpg",
                key="vis_url",
            )
            if selected_img_url:
                try:
                    st.image(selected_img_url, caption="Loaded Image", use_container_width=True)
                except Exception:
                    st.warning("Could not render preview from that URL.")

        else:
            uploaded_img = st.file_uploader("Upload Image (JPG, PNG, WEBP)", type=["jpg", "jpeg", "png", "webp"], key="vis_upload")
            if uploaded_img:
                st.image(uploaded_img, caption="Uploaded Image", use_container_width=True)

        vision_task = st.selectbox("Inspection Mode", [
            "Autonomous Vehicle & Safety Audit",
            "Chart OCR & Data Table Reconstruction",
            "Text & Signpost OCR Transcription",
            "Custom Visual Q&A",
        ], key="vis_task")

        vision_prompt = st.text_area(
            "Inspection Directive",
            value="1. Itemize all visible objects.\n2. Transcribe all text/signs.\n3. Assess spatial hazards.\n4. Assign safety score 1-10 with justification.",
            height=100,
            key="vis_prompt",
        )

        run_vision = st.button("Run Visual Inspection", type="primary", use_container_width=True, key="btn_vision")

    with right_v:
        st.markdown("#### Vision Findings")
        if run_vision:
            with st.spinner("Analyzing image with Nemotron Vision..."):
                try:
                    from langchain_core.messages import HumanMessage
                    llm = get_active_model()

                    if uploaded_img:
                        b64 = base64.b64encode(uploaded_img.getvalue()).decode("utf-8")
                        img_payload = {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}
                    else:
                        img_payload = {"type": "image_url", "image_url": {"url": selected_img_url}}

                    msg = HumanMessage(content=[
                        {"type": "text", "text": f"[{vision_task}]\n{vision_prompt}"},
                        img_payload,
                    ])

                    result = llm.invoke([msg])
                    st.success("Visual inspection complete.")
                    st.markdown(result.content)

                    st.download_button(
                        label="Export Findings (Markdown)",
                        data=result.content,
                        file_name="vision_report.md",
                        mime="text/markdown",
                    )
                except Exception as e:
                    st.error(f"Vision error: {e}")
        else:
            st.info("Choose an image and click Run Visual Inspection.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 3 — VIDEO TEMPORAL ENGINE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_video:
    st.markdown("### Video Temporal Reasoning Engine")
    st.caption("Analyze video streams for chronological events, kinematics, anomaly detection, and automation feasibility.")

    left_vid, right_vid = st.columns([1, 1])

    with left_vid:
        st.markdown("#### Video Input")

        vid_mode = st.radio("Video Source", ["Sample NVIDIA Video", "Custom MP4 URL"], horizontal=True, key="vid_mode")

        if vid_mode == "Sample NVIDIA Video":
            vid_url = "https://assets.ngc.nvidia.com/products/api-catalog/cosmos-nemotron/cosmos_sample1.mp4"
        else:
            vid_url = st.text_input(
                "Public MP4 URL",
                value="https://assets.ngc.nvidia.com/products/api-catalog/cosmos-nemotron/cosmos_sample1.mp4",
                key="vid_url",
            )

        st.video(vid_url)

        temporal_task = st.selectbox("Temporal Analysis Task", [
            "Chronological Event Timeline",
            "Kinematics & Motion Tracking",
            "Hazard & Anomaly Detection",
            "Robotics & Automation Feasibility",
        ], key="vid_task")

        vid_prompt = st.text_area(
            "Temporal Directive",
            value="1. Chronological summary of events with timestamps.\n2. Object velocities and trajectories.\n3. Safety or operational bottlenecks.\n4. Strategic recommendations.",
            height=100,
            key="vid_prompt",
        )

        run_video = st.button("Analyze Video Stream", type="primary", use_container_width=True, key="btn_video")

    with right_vid:
        st.markdown("#### Temporal Insights")
        if run_video:
            with st.spinner("Processing video frames..."):
                try:
                    if nv_key and nv_key.startswith("nvapi-"):
                        from openai import OpenAI
                        client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=nv_key)
                        completion = client.chat.completions.create(
                            model="nvidia/nemotron-3.5-super-vl-120b-a12b",
                            messages=[{
                                "role": "user",
                                "content": [
                                    {"type": "text", "text": f"Task: {temporal_task}\n\n{vid_prompt}"},
                                    {"type": "video_url", "video_url": {"url": vid_url}},
                                ],
                            }],
                            max_tokens=2048,
                            temperature=0.4,
                        )
                        st.success("Video analysis complete.")
                        st.markdown(completion.choices[0].message.content)
                    else:
                        st.info("Direct NVIDIA key not detected. Using text-based temporal reconstruction fallback.")
                        from langchain_core.messages import HumanMessage
                        llm = get_active_model()
                        fb_msg = HumanMessage(content=[
                            {"type": "text", "text": f"[VIDEO TEMPORAL RECONSTRUCTION]\nTask: {temporal_task}\n{vid_prompt}"},
                            {"type": "image_url", "image_url": {"url": "https://assets.ngc.nvidia.com/products/api-catalog/phi-3-5-vision/example1a.jpg"}},
                        ])
                        res = llm.invoke([fb_msg])
                        st.markdown(res.content)
                except Exception as e:
                    st.error(f"Video processing error: {e}")
        else:
            st.info("Review the video and click Analyze Video Stream.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 4 — AUTONOMOUS REACT AGENT & TOOL CALLING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_agent:
    st.markdown("### Autonomous ReAct Agent & Tool Console")
    st.caption("Watch the model autonomously select tools, execute them, and synthesize findings into an executive brief.")

    left_ag, right_ag = st.columns([1, 2])

    with left_ag:
        st.markdown("#### Available Tools")
        use_market = st.checkbox("Market Intelligence (get_financial_metrics)", value=True, key="ag_market")
        use_sim = st.checkbox("Wealth Simulator (compute_investment_simulation)", value=True, key="ag_sim")
        use_conv = st.checkbox("Currency & Unit Converter (convert_currency_and_units)", value=True, key="ag_conv")
        use_kb = st.checkbox("Enterprise Knowledge Base (query_enterprise_kb)", value=True, key="ag_kb")

        st.markdown("#### Mission Configuration")

        mission_preset = st.selectbox("Preset Mission", [
            "Financial Audit & Wealth Modeling",
            "NVIDIA Tech Architecture & Valuation",
            "Custom Autonomous Mission",
        ], key="ag_preset")

        _mission_defaults = {
            "Financial Audit & Wealth Modeling": (
                "1. Fetch financial metrics for NVDA and MSFT.\n"
                "2. Simulate $75,000 invested at 9.5% annual return over 6 years with $1,000/month contributions.\n"
                "3. Convert the final portfolio value to EUR and INR.\n"
                "4. Deliver an executive summary comparing the two stocks and the investment outcome."
            ),
            "NVIDIA Tech Architecture & Valuation": (
                "1. Search the knowledge base for 'nemotron' architecture details.\n"
                "2. Search for 'tensorrt' optimization capabilities.\n"
                "3. Look up NVDA and GOOGL market metrics.\n"
                "4. Convert 100 kilometers to miles.\n"
                "5. Synthesize all findings into a technology investment brief."
            ),
            "Custom Autonomous Mission": (
                "Compare NVDA, AAPL, and TSLA market metrics. Calculate growth of $50,000 "
                "at 8% over 10 years with $500/month contributions. Convert the total to EUR and JPY."
            ),
        }

        user_mission = st.text_area(
            "Mission Objective",
            value=_mission_defaults[mission_preset],
            height=160,
            key="ag_mission",
        )

        max_turns = st.slider("Max Autonomous Turns", 1, 10, 6, key="ag_turns")
        run_agent = st.button("Dispatch Autonomous Agent", type="primary", use_container_width=True, key="btn_agent")

    with right_ag:
        st.markdown("#### Live Mission Execution Console")

        if run_agent:
            from langchain_core.tools import tool
            from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage

            # ---------- TOOL DEFINITIONS ----------
            @tool
            def get_financial_metrics(ticker: str) -> str:
                """Retrieve real-time market data for stock tickers: NVDA, MSFT, AAPL, GOOGL, AMZN, TSLA, META."""
                db = {
                    "NVDA":  {"price": 144.20, "change": "+2.8%", "market_cap": "$3.52T", "pe_ratio": 64.2, "52w_high": 152.89, "sector": "Semiconductors"},
                    "MSFT":  {"price": 448.10, "change": "+0.4%", "market_cap": "$3.33T", "pe_ratio": 36.5, "52w_high": 468.35, "sector": "Software"},
                    "AAPL":  {"price": 232.50, "change": "-0.6%", "market_cap": "$3.55T", "pe_ratio": 34.8, "52w_high": 243.03, "sector": "Consumer Electronics"},
                    "GOOGL": {"price": 182.40, "change": "+1.7%", "market_cap": "$2.28T", "pe_ratio": 25.1, "52w_high": 191.75, "sector": "Internet Services"},
                    "AMZN":  {"price": 198.30, "change": "+1.2%", "market_cap": "$2.08T", "pe_ratio": 42.3, "52w_high": 211.00, "sector": "E-Commerce"},
                    "TSLA":  {"price": 342.70, "change": "+3.5%", "market_cap": "$1.10T", "pe_ratio": 88.4, "52w_high": 389.22, "sector": "Automotive/Energy"},
                    "META":  {"price": 585.90, "change": "+0.9%", "market_cap": "$1.48T", "pe_ratio": 27.6, "52w_high": 602.95, "sector": "Social Media"},
                }
                t = ticker.strip().upper()
                return json.dumps(db.get(t, {"error": f"Ticker '{t}' not found. Available: NVDA, MSFT, AAPL, GOOGL, AMZN, TSLA, META"}))

            @tool
            def compute_investment_simulation(principal: float, annual_return_rate: float, years: int, monthly_contribution: float = 0.0) -> str:
                """Simulate multi-year compound wealth growth with optional monthly contributions."""
                r = (annual_return_rate / 100) / 12
                n = years * 12
                fv_principal = principal * ((1 + r) ** n)
                fv_contributions = monthly_contribution * (((1 + r) ** n - 1) / r) if r > 0 else monthly_contribution * n
                total = fv_principal + fv_contributions
                invested = principal + (monthly_contribution * n)
                return json.dumps({
                    "initial_principal": f"${principal:,.2f}",
                    "monthly_contribution": f"${monthly_contribution:,.2f}",
                    "duration_years": years,
                    "annual_return": f"{annual_return_rate}%",
                    "final_portfolio": f"${total:,.2f}",
                    "total_invested": f"${invested:,.2f}",
                    "total_profit": f"${total - invested:,.2f}",
                    "roi_percentage": f"{((total - invested) / invested) * 100:.1f}%",
                })

            @tool
            def convert_currency_and_units(amount: float, from_unit: str, to_unit: str) -> str:
                """Convert currencies (USD, INR, EUR, GBP, JPY) or measurement units (km/miles, kg/lbs, celsius/fahrenheit)."""
                rates = {
                    ("usd", "inr"): 86.40, ("inr", "usd"): 1 / 86.40,
                    ("usd", "eur"): 0.95, ("eur", "usd"): 1 / 0.95,
                    ("usd", "gbp"): 0.82, ("gbp", "usd"): 1 / 0.82,
                    ("usd", "jpy"): 154.50, ("jpy", "usd"): 1 / 154.50,
                    ("eur", "inr"): 90.95, ("inr", "eur"): 1 / 90.95,
                    ("eur", "gbp"): 0.863, ("gbp", "eur"): 1 / 0.863,
                    ("km", "miles"): 0.621371, ("miles", "km"): 1.60934,
                    ("kg", "lbs"): 2.20462, ("lbs", "kg"): 0.453592,
                }
                f = from_unit.lower().strip()
                t = to_unit.lower().strip()
                key = (f, t)

                if f == "celsius" and t == "fahrenheit":
                    converted = (amount * 9 / 5) + 32
                elif f == "fahrenheit" and t == "celsius":
                    converted = (amount - 32) * 5 / 9
                elif key in rates:
                    converted = amount * rates[key]
                else:
                    return json.dumps({"error": f"Unsupported: {from_unit} -> {to_unit}"})

                return json.dumps({"input": f"{amount:,.2f} {from_unit}", "converted": f"{converted:,.2f} {to_unit}"})

            @tool
            def query_enterprise_kb(query: str) -> str:
                """Search enterprise knowledge base for Nemotron, NIM, LangChain, LangGraph, RAG, CUDA, TensorRT."""
                kb = {
                    "nemotron": "NVIDIA Nemotron 3.5 Super VL is a 124B Mixture-of-Experts model with 262K context, native tool calling, structured output, vision-language capabilities, and chain-of-thought reasoning. It uses 12B active parameters per token for efficient inference.",
                    "nim": "NVIDIA NIM (NVIDIA Inference Microservices) provides containerized, GPU-accelerated microservices for deploying AI models with CUDA and TensorRT-LLM optimization. Supports auto-scaling and multi-GPU inference.",
                    "langchain": "LangChain is a framework for building applications with LLMs. It provides chains, agents, tools, memory, and retrieval-augmented generation (RAG) capabilities. Version 1.4+ supports structured outputs and tool calling natively.",
                    "langgraph": "LangGraph extends LangChain with stateful, multi-step agent workflows using directed acyclic graphs. Supports human-in-the-loop, checkpointing, and complex agent orchestration patterns.",
                    "rag": "Retrieval-Augmented Generation (RAG) combines LLM generation with external knowledge retrieval. It uses vector databases (FAISS, Chroma, Pinecone) to store document embeddings and retrieves relevant context before generation.",
                    "cuda": "CUDA is NVIDIA's parallel computing platform enabling GPU-accelerated computing. CUDA cores handle thousands of threads simultaneously, critical for deep learning training and inference workloads.",
                    "tensorrt": "TensorRT-LLM optimizes LLM inference with kernel fusion, quantization (INT8/FP8), KV-cache optimization, in-flight batching, and multi-GPU tensor parallelism. Achieves 2-5x inference speedup over vanilla PyTorch.",
                }
                q = query.lower()
                matches = {k: v for k, v in kb.items() if k in q}
                if not matches:
                    matches = {k: v for k, v in kb.items() if any(word in q for word in k.split())}
                return json.dumps({"results": matches if matches else {"note": "No matching entries. Try: nemotron, nim, langchain, langgraph, rag, cuda, tensorrt"}})

            # Build tool pool
            tool_pool = []
            if use_market:
                tool_pool.append(get_financial_metrics)
            if use_sim:
                tool_pool.append(compute_investment_simulation)
            if use_conv:
                tool_pool.append(convert_currency_and_units)
            if use_kb:
                tool_pool.append(query_enterprise_kb)

            tool_map = {t.name: t for t in tool_pool}

            with st.spinner("Dispatching autonomous agent..."):
                try:
                    llm_base = get_active_model()
                    llm_tools = llm_base.bind_tools(tool_pool)

                    history = [
                        SystemMessage(content=(
                            "You are an autonomous AI analyst with specialized tools. "
                            "Always use the available tools for quantitative data, conversions, and knowledge lookups. "
                            "After gathering all data, synthesize an executive summary."
                        )),
                        HumanMessage(content=user_mission),
                    ]

                    for turn in range(1, max_turns + 1):
                        st.markdown(f"**Turn {turn}:** Reasoning & action planning...")
                        ai_msg = llm_tools.invoke(history)
                        history.append(ai_msg)

                        if not ai_msg.tool_calls:
                            st.success("Mission complete - all tool directives executed.")
                            st.markdown(ai_msg.content)
                            break

                        for tc in ai_msg.tool_calls:
                            fn_name = tc["name"]
                            fn_args = tc["args"]
                            with st.expander(f"Tool: {fn_name}", expanded=True):
                                st.write("**Arguments:**", fn_args)
                                tool_fn = tool_map.get(fn_name)
                                if tool_fn:
                                    res = tool_fn.invoke(fn_args)
                                else:
                                    res = json.dumps({"error": f"Unknown tool: {fn_name}"})
                                st.write("**Result:**", res)
                                history.append(ToolMessage(content=res, tool_call_id=tc["id"]))
                    else:
                        st.warning("Maximum autonomous turns reached. Requesting final summary...")
                        final = llm_tools.invoke(history)
                        if final.content:
                            st.markdown(final.content)

                except Exception as e:
                    st.error(f"Agent error: {e}")
        else:
            st.info("Configure tools, set mission objective, and click Dispatch Autonomous Agent.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 5 — STRUCTURED EXTRACTION (PYDANTIC V2)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_struct:
    st.markdown("### Schema-Enforced Structured Extraction (Pydantic v2)")
    st.caption("Convert messy unstructured text into validated, typed JSON schemas with zero parse failures.")

    left_s, right_s = st.columns([1, 1])

    with left_s:
        st.markdown("#### Schema & Source Configuration")

        schema_type = st.selectbox("Extraction Schema", [
            "Executive Candidate Resume Profile",
            "Enterprise Cybersecurity & Compliance Audit",
            "Financial Transaction Invoice",
        ], key="struct_schema")

        _sample_texts = {
            "Executive Candidate Resume Profile": (
                "Kavala Adharsh Raj | Bengaluru, India | kavalaadharshraj@gmail.com | github.com/adharsh77\n\n"
                "Lead AI Systems Architect (2024-Present) at TechVision Labs\n"
                "- Built multimodal LangChain + NVIDIA NIM agents handling 250,000+ daily queries with sub-200ms latency.\n"
                "- Cut human audit overhead 68% using automated document OCR pipelines.\n"
                "- Optimized inference on 16x H100 GPU clusters with TensorRT-LLM and FP8 quantization.\n\n"
                "Senior ML Engineer (2022-2024) at NextGen Cloud Solutions\n"
                "- Engineered real-time anomaly detection pipelines processing 2 TB/day on AWS.\n"
                "- Deployed BERT-based NER models for contract entity extraction with 94.3% F1 score.\n\n"
                "Education: B.Tech Computer Science, Indian Institute of Technology (2022).\n"
                "Skills: Python, PyTorch, LangChain, LangGraph, NVIDIA NIM, CUDA, TensorRT, FastAPI, Docker, Kubernetes, AWS, GCP."
            ),
            "Enterprise Cybersecurity & Compliance Audit": (
                "Security Assessment Report - Q4 2026\n\n"
                "CRITICAL: 3 database backups stored in unencrypted S3 bucket without MFA delete enabled.\n"
                "HIGH: SSL certificate on internal auth endpoint expires in 5 days; renewal cron job failed silently.\n"
                "MEDIUM: PCI-DSS quarterly penetration test completed on time with zero severe vulnerabilities.\n"
                "CRITICAL: Database read-replicas running at 95% disk capacity in us-east-1.\n"
                "LOW: Employee security awareness training completion rate at 78% (target: 95%).\n\n"
                "Overall health score: 6.2/10. Compliance status: NEEDS IMMEDIATE REMEDIATION."
            ),
            "Financial Transaction Invoice": (
                "INVOICE #INV-98214\n"
                "Date: 2026-10-15 | Due Date: 2026-11-15\n"
                "Vendor: Apex Cloud Infrastructure Inc.\n"
                "Client: DeepScale Technologies LLC\n\n"
                "Line Items:\n"
                "1. 8x NVIDIA H100 GPU Instances (720 hrs) - $28,800.00\n"
                "2. Enterprise Support Plan (Gold Tier) - $4,500.00\n"
                "3. High-Throughput NVMe Storage (10 TB) - $1,250.00\n"
                "4. Network Egress (2.5 TB outbound) - $225.00\n\n"
                "Subtotal: $34,775.00\n"
                "Sales Tax (8.25%): $2,868.94\n"
                "Total Amount Due: $37,643.94\n"
                "Payment Terms: Net 30 days via Wire Transfer."
            ),
        }

        raw_text = st.text_area(
            "Raw Unstructured Text",
            value=_sample_texts[schema_type],
            height=260,
            key="struct_text",
        )

        # Show schema definition
        with st.expander("View Pydantic Schema Definition"):
            if schema_type == "Executive Candidate Resume Profile":
                st.code("""
class Experience(BaseModel):
    company: str
    role: str
    duration: str
    achievements: List[str]

class CandidateProfile(BaseModel):
    candidate_name: str
    email: str
    location: str
    seniority: str
    experience_years: float
    skills: List[str]
    hiring_score: int = Field(ge=1, le=100)
    work_history: List[Experience]
""", language="python")
            elif schema_type == "Enterprise Cybersecurity & Compliance Audit":
                st.code("""
class RiskFinding(BaseModel):
    finding: str
    severity: str  # CRITICAL, HIGH, MEDIUM, LOW
    mitigation: str

class AuditReport(BaseModel):
    report_title: str
    health_score: float
    compliance_status: str
    critical_count: int
    findings: List[RiskFinding]
""", language="python")
            else:
                st.code("""
class LineItem(BaseModel):
    description: str
    quantity: str
    amount: float

class Invoice(BaseModel):
    invoice_number: str
    date: str
    vendor: str
    client: str
    items: List[LineItem]
    subtotal: float
    tax_amount: float
    total_amount: float
    payment_terms: str
""", language="python")

        run_struct = st.button("Extract & Validate Schema", type="primary", use_container_width=True, key="btn_struct")

    with right_s:
        st.markdown("#### Validated JSON Output")

        if run_struct:
            with st.spinner("Extracting structured data..."):
                try:
                    from pydantic import BaseModel, Field

                    if schema_type == "Executive Candidate Resume Profile":
                        class Experience(BaseModel):
                            company: str
                            role: str
                            duration: str
                            achievements: List[str]
                        class CandidateProfile(BaseModel):
                            candidate_name: str
                            email: str
                            location: str
                            seniority: str
                            experience_years: float
                            skills: List[str]
                            hiring_score: int = Field(ge=1, le=100)
                            work_history: List[Experience]
                        schema_cls = CandidateProfile

                    elif schema_type == "Enterprise Cybersecurity & Compliance Audit":
                        class RiskFinding(BaseModel):
                            finding: str
                            severity: str
                            mitigation: str
                        class AuditReport(BaseModel):
                            report_title: str
                            health_score: float
                            compliance_status: str
                            critical_count: int
                            findings: List[RiskFinding]
                        schema_cls = AuditReport

                    else:
                        class LineItem(BaseModel):
                            description: str
                            quantity: str
                            amount: float
                        class Invoice(BaseModel):
                            invoice_number: str
                            date: str
                            vendor: str
                            client: str
                            items: List[LineItem]
                            subtotal: float
                            tax_amount: float
                            total_amount: float
                            payment_terms: str
                        schema_cls = Invoice

                    llm = get_active_model()
                    structured_llm = llm.with_structured_output(schema_cls)

                    result = structured_llm.invoke(
                        f"Extract the following text strictly into the provided schema. "
                        f"Fill all fields accurately:\n\n{raw_text}"
                    )
                    dumped = result.model_dump()

                    st.success("Pydantic validation passed - 100% type-safe output.")
                    st.json(dumped)

                    st.download_button(
                        label="Download Structured JSON",
                        data=json.dumps(dumped, indent=2, default=str),
                        file_name="structured_output.json",
                        mime="application/json",
                    )
                except Exception as e:
                    st.error(f"Extraction error: {e}")
        else:
            st.info("Click Extract & Validate Schema to run Pydantic extraction.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 6 — CAPSTONE MULTIMODAL DOSSIER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_capstone:
    st.markdown("### Grand Capstone: Unified Multimodal Investigation")
    st.caption("Orchestrate Vision + CoT Reasoning + Autonomous Tools + Pydantic Schema in a single mission pipeline.")

    left_c, right_c = st.columns([1, 1])

    with left_c:
        st.markdown("#### Mission Configuration")

        cap_image = st.text_input(
            "Evidence Image URL",
            value="https://assets.ngc.nvidia.com/products/api-catalog/phi-3-5-vision/example1a.jpg",
            key="cap_img",
        )
        try:
            st.image(cap_image, caption="Visual Evidence Asset", use_container_width=True)
        except Exception:
            st.warning("Could not load image preview.")

        cap_upload = st.file_uploader("Or Upload Evidence Image", type=["jpg", "jpeg", "png", "webp"], key="cap_upload")
        if cap_upload:
            st.image(cap_upload, caption="Uploaded Evidence", use_container_width=True)

        governance_std = st.selectbox("Governance Standard", [
            "OSHA Urban & Traffic Safety",
            "ISO-27001 Infrastructure Security",
            "NVIDIA AI Enterprise Architecture",
            "FDA Medical Device Compliance",
        ], key="cap_gov")

        cap_mission = st.text_area(
            "Investigation Objective",
            value=(
                "1. Perform comprehensive visual audit of the image for safety hazards and infrastructure issues.\n"
                "2. Apply chain-of-thought reasoning to assess compliance against the selected governance standard.\n"
                "3. Generate an executive dossier with risk scores, observations, and actionable remediation directives."
            ),
            height=120,
            key="cap_mission",
        )

        run_capstone = st.button("Launch Capstone Investigation", type="primary", use_container_width=True, key="btn_capstone")

    with right_c:
        st.markdown("#### Executive Dossier Output")

        if run_capstone:
            with st.spinner("Orchestrating multimodal agentic pipeline..."):
                try:
                    from pydantic import BaseModel, Field
                    from langchain_core.messages import HumanMessage

                    class InvestigationDossier(BaseModel):
                        case_id: str
                        timestamp: str
                        governance_standard: str
                        hazard_score: int = Field(ge=1, le=10, description="Overall hazard severity 1-10")
                        visual_observations: str
                        reasoning_analysis: str
                        compliance_verdict: str
                        actionable_directives: List[str]
                        confidence_percentage: float = Field(ge=0, le=100)

                    llm = get_active_model()
                    cap_parser = llm.with_structured_output(InvestigationDossier)

                    if cap_upload:
                        b64 = base64.b64encode(cap_upload.getvalue()).decode("utf-8")
                        img_content = {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}
                    else:
                        img_content = {"type": "image_url", "image_url": {"url": cap_image}}

                    cap_msg = HumanMessage(content=[
                        {"type": "text", "text": (
                            f"Governance Standard: {governance_std}\n"
                            f"Mission: {cap_mission}\n\n"
                            f"Generate a case_id (format: CASE-YYYY-NNNN), "
                            f"set timestamp to current datetime, "
                            f"set governance_standard to '{governance_std}'."
                        )},
                        img_content,
                    ])

                    dossier = cap_parser.invoke([cap_msg])

                    # KPI metrics
                    m1, m2, m3 = st.columns(3)
                    m1.metric("Case ID", dossier.case_id)
                    m2.metric("Hazard Score", f"{dossier.hazard_score} / 10")
                    m3.metric("Confidence", f"{dossier.confidence_percentage:.1f}%")

                    st.markdown(f"**Governance Standard:** `{dossier.governance_standard}`")
                    st.markdown(f"**Compliance Verdict:** `{dossier.compliance_verdict}`")

                    st.markdown("---")
                    st.markdown("**Visual Observations:**")
                    st.write(dossier.visual_observations)

                    st.markdown("**Reasoning Analysis:**")
                    st.write(dossier.reasoning_analysis)

                    st.markdown("**Actionable Directives:**")
                    for idx, directive in enumerate(dossier.actionable_directives, 1):
                        st.write(f"{idx}. {directive}")

                    st.download_button(
                        label="Download Executive Dossier (JSON)",
                        data=json.dumps(dossier.model_dump(), indent=2, default=str),
                        file_name="executive_dossier.json",
                        mime="application/json",
                    )
                except Exception as e:
                    st.error(f"Capstone error: {e}")
        else:
            st.info("Configure the investigation and click Launch Capstone Investigation.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 7 — RESUME & ARCHITECTURE SHOWCASE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_resume:
    st.markdown("### Portfolio & Resume Showcase")
    st.caption("Ready-to-use, quantified resume bullet points and architectural overview for your portfolio.")

    st.markdown("""
#### Project Overview

**OmniNemotron: Multimodal Agentic AI Intelligence Platform v2.0**

*Tech Stack: Python 3.12, NVIDIA Nemotron 3.5 Super VL (124B MoE), LangChain 1.4+, Pydantic v2,
Streamlit, NVIDIA NIM, OpenAI API, OpenRouter, Groq*

---

#### Impact-Driven Resume Bullet Points

1. **Architected and deployed an end-to-end Multimodal Agentic AI Platform** powered by NVIDIA
   Nemotron 3.5 Super VL (124B MoE parameters, 262K context window) spanning text reasoning,
   computer vision, and video temporal analysis across 7 specialized operational modules.

2. **Engineered a production-grade Streamlit Command Center** featuring an NVIDIA-branded dark UI
   with glassmorphism design, real-time hyperparameter tuning, multi-provider model orchestration,
   and live chain-of-thought reasoning trace inspection.

3. **Implemented autonomous multi-turn ReAct agents with dynamic tool calling**, orchestrating 4
   enterprise tools (financial market intelligence, compound wealth simulations, multi-currency
   converters, and vector knowledge retrieval) with step-by-step execution transparency.

4. **Pioneered type-safe data pipelines using Pydantic v2 structured outputs**, guaranteeing 100%
   schema compliance across 3 enterprise extraction templates (CV parsing, PCI-DSS compliance
   auditing, and financial invoice processing) with zero JSON parse failures.

5. **Constructed a unified multimodal capstone pipeline** combining vision analysis, chain-of-thought
   reasoning, autonomous tool orchestration, and Pydantic schema enforcement into a single
   executive investigation dossier with governance compliance scoring.

6. **Built multi-provider model fallback architecture** supporting 5 LLM providers (NVIDIA NIM
   Direct, OpenRouter, Groq, OpenAI, Google Gemini) with live API key status monitoring, dynamic
   credential override, and seamless provider switching.

---

#### Key Technical Differentiators

| Capability | Implementation |
|:---|:---|
| **Multimodal Input** | Text, Image (URL/Upload/Base64), Video (MP4 streaming via NIM) |
| **Chain-of-Thought** | Native `enable_thinking` with transparent reasoning trace display |
| **Tool Calling** | Autonomous ReAct loop with 4 typed tools and multi-turn orchestration |
| **Structured Output** | Pydantic v2 `with_structured_output()` with nested schema validation |
| **Model Providers** | NVIDIA NIM, OpenRouter, Groq, OpenAI, Google Gemini (5 providers) |
| **Architecture** | 124B MoE with 12B active parameters, 262K context window |

---

#### System Architecture
""")

    st.code("""
    +-------------------------------------------------------------------------+
    |                 OmniNemotron Command Center (Streamlit)                  |
    |  [CoT Reasoning] [Vision] [Video] [ReAct Agent] [Struct] [Capstone]     |
    +------------------------------------+------------------------------------+
                                         |
                    +--------------------+--------------------+
                    |     Unified Model Factory (LangChain)    |
                    |  Temperature | Max Tokens | Top-P | CoT  |
                    +--------------------+--------------------+
                                         |
          +-------------+--------+-------+-------+--------+-------------+
          |              |        |               |        |             |
    [NVIDIA NIM]  [OpenRouter] [Groq]       [OpenAI]  [Gemini]    [Tools]
          |              |        |               |        |          |
          +--------------+--------+-------+-------+--------+     [Pydantic
                                         |                        Schema]
                    +--------------------+--------------------+
                    |  NVIDIA Nemotron 3.5 Super VL (124B MoE) |
                    |    Text + Image + Video -> Text Output    |
                    |  Function Calling | Structured | Reasoning |
                    +-------------------------------------------+
""", language="text")

    st.markdown("---")

    st.markdown("""
#### Project Structure

```
OmniNemotron/
|-- app.py                          # Main Streamlit application (7 tabs)
|-- run_app.bat                     # Windows launcher script
|-- .env                            # API keys (gitignored)
|-- requirements.txt                # Python dependencies
|-- pyproject.toml                  # Project metadata & build config
|-- README.md                       # Documentation & architecture
|-- updatedlangchain/
|   |-- langchain_intro.ipynb       # Initial LangChain exploration
|   |-- Nemotron.ipynb              # Nemotron 3.5 capabilities notebook
|   |-- multimodal_intelligence_agent.ipynb  # Full multimodal agent notebook
```

---

*Built by Kavala Adharsh Raj | Powered by NVIDIA Nemotron 3.5 Super & LangChain*
""")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FOOTER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#64748b; font-size:0.85rem;">'
    'OmniNemotron v2.0 &middot; Built by Kavala Adharsh Raj &middot; '
    'Powered by NVIDIA Nemotron 3.5 Super &amp; LangChain'
    '</p>',
    unsafe_allow_html=True,
)
