@echo off
cd /d "%~dp0"
title OmniNemotron AI Platform v2.0
echo.
echo  ============================================================
echo     OmniNemotron: Multimodal Intelligence Platform v2.0
echo     Powered by NVIDIA Nemotron 3.5 Super VL (124B MoE)
echo  ============================================================
echo.
echo  Starting Streamlit server...
echo  Dashboard will open at: http://localhost:8501
echo.
echo  Press Ctrl+C to stop the server.
echo  ============================================================
echo.
.\.venv\Scripts\streamlit.exe run app.py --server.headless=false --browser.gatherUsageStats=false
pause
