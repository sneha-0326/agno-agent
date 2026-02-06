Agno-Based AI Research Agent
Overview
This repository contains an autonomous AI agent implemented using the Agno agent framework. The agent integrates a Groq-hosted LLaMA 3.3 (70B) large language model as its reasoning and decision-making engine, along with DuckDuckGo web search tools for real-time information retrieval. The agent is designed to execute research-oriented tasks by dynamically determining when external web search is required and synthesizing retrieved information into structured summaries.

Architecture
The system follows a modular agent-oriented architecture:
Agent Orchestration:
Agno manages agent lifecycle, prompt routing, and tool invocation.
LLM Inference Layer:
A Groq-hosted LLaMA 3.3 (70B) model provides natural language understanding, reasoning, and task planning.
Tooling Layer:
DuckDuckGo search tools are exposed to the agent, enabling live web queries when the language model determines that external information is required.
Configuration Layer:
Runtime configuration and API credentials are supplied through environment variables to maintain separation between code and secrets.

Execution Flow
A user prompt is submitted to the agent.
The LLM analyzes the task and determine whether external information is required.
If necessary, the agent invokes the DuckDuckGo web search tool.
Retrieved search results are passed back to the LLM.
The LLM synthesizes the information and produces a structured, markdown-formatted response.

Environment Setup

Prerequisites
Python 3.9+
Groq API access

Dependency Installation
pip install -r requirements.txt

Environment Variables
Create a .env file in the project root:
GROQ_API_KEY=your_groq_api_key_here
Environment variables are loaded at runtime using python-dotenv.

Running the Agent
python main.py
The agent will execute a predefined research prompt and output a structured summary to the console.

Project Structure
.
├── main.py            # Agent definition and execution logic
├── requirements.txt   # Python dependencies
├── .gitignore         # Git ignore rules
├── .env               # Environment variables (not committed)
└── venv/              # Local virtual environment (not committed)

Notes
The project uses a Python virtual environment to ensure dependency isolation.
No persistent memory, database integration, or retrieval-augmented generation (RAG) mechanisms are implemented.
Tool usage is dynamically controlled by the language model rather than hardcoded logic.

License
This project is provided for educational and experimental purposes.
