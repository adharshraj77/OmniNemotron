# 🚀 Streamlit Community Cloud Deployment Guide

This guide walks you through deploying **OmniNemotron** to [Streamlit Community Cloud](https://share.streamlit.io/) for free in under 5 minutes.

---

## 📋 Pre-Deployment Checklist

Before deploying, ensure you have:
- [x] A [GitHub](https://github.com/) account.
- [x] A [Streamlit Community Cloud](https://share.streamlit.io/) account (sign in with your GitHub account).
- [x] Your API keys ready:
  - `NV_NEMO_API_KEY` (from [NVIDIA Build](https://build.nvidia.com))
  - `OPENROUTER_API_KEY` (from [OpenRouter](https://openrouter.ai))
  - `OPENAI_API_KEY` / `GROQ_API_KEY` / `GOOGLE_API_KEY` (optional)

---

## Step 1: Push Code to GitHub

Open PowerShell or Command Prompt in `d:\LangChain` and run:

```bash
# 1. Stage all deployment files
git add .

# 2. Commit the changes
git commit -m "feat: complete production-ready OmniNemotron platform for Streamlit Cloud"

# 3. Rename branch to main
git branch -M main

# 4. Add your GitHub remote repository (replace with your repo URL)
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/OmniNemotron.git

# 5. Push to GitHub
git push -u origin main
```

> **Security Note:** Your `.env` and `.streamlit/secrets.toml` files are included in `.gitignore` and will **never** be pushed to GitHub. Your private API keys remain secure.

---

## Step 2: Deploy on Streamlit Community Cloud

1. Go to **[share.streamlit.io](https://share.streamlit.io)** and log in with GitHub.
2. Click the **"New app"** (or **"Create app"**) button.
3. Fill in the repository settings:
   - **Repository:** `YOUR_GITHUB_USERNAME/OmniNemotron`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL:** (Choose your custom subdomain, e.g. `omni-nemotron.streamlit.app`)

---

## Step 3: Add Your Secrets in Streamlit Cloud

1. In the deployment screen, click **"Advanced settings..."** before deploying (or go to **App Settings → Secrets** after deploying).
2. Paste the following into the **Secrets** text box (replace with your actual API keys):

```toml
NV_NEMO_API_KEY = "nvapi-your-nvidia-api-key-here"
OPENROUTER_API_KEY = "sk-or-v1-your-openrouter-key-here"
OPENAI_API_KEY = "sk-your-openai-key-here"
GROQ_API_KEY = "gsk_your-groq-key-here"
GOOGLE_API_KEY = "your-google-ai-key-here"
```

3. Click **"Save"**.
4. Click **"Deploy!"**.

---

## Step 4: Verification & Live Link

Streamlit Cloud will:
1. Spin up a container using Debian Linux & Python 3.12.
2. Install dependencies automatically from `requirements.txt`.
3. Apply the custom dark NVIDIA theme from `.streamlit/config.toml`.
4. Inject your secrets into the app via `st.secrets`.
5. Launch your app at your public URL (e.g. `https://omni-nemotron.streamlit.app`).

---

## 🛠️ Deployment Troubleshooting

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| **"API Key missing" warning on cloud** | Secrets not saved in Streamlit Cloud | Open App settings → Secrets, paste keys from `.streamlit/secrets.toml.example`, and save. |
| **Build timeout on dependencies** | Heavy unnecessary packages | `requirements.txt` is already streamlined without `ipykernel` for fast cloud builds. |
| **Visual assets fail to load** | External images blocked or offline | All images use reliable HTTPS CDN endpoints or direct user upload. |
| **Theme reset to light mode** | Browser overrides | `.streamlit/config.toml` enforces the custom dark NVIDIA theme by default. |

---

*OmniNemotron &middot; Built by Kavala Adharsh Raj &middot; Powered by NVIDIA Nemotron & LangChain*

