#  Agent Blueprint MCP | Build AI Agents Instantly

**Create structured, domain-specific AI assistants using a single prompt. Powered by OpenAI. Integrated with [Puch AI](https://puch.so) via MCP.**

---

`Agent Blueprint MCP` is a lightweight backend service that helps you **generate complete AI assistant specifications**—including:

- A system prompt
- Required tools
- Example user interactions

This is done using your own [OpenAI API key](https://platform.openai.com/), and exposed to Puch AI through a secure MCP interface.

---

##  What is Puch AI? How Does It Help?

[Puch AI](https://puch.so) is a WhatsApp-based assistant platform that lets you:

- Build, test, and run AI agents conversationally.
- Integrate tools you write locally using **MCP (Modular Custom Protocol)**.
- Call your tool via `/commands` in WhatsApp—no frontend needed.

This repo uses FastMCP to host a custom tool, and exposes it securely to Puch AI via `localtunnel` or `ngrok`. When you send `/mcp connect` in WhatsApp, your MCP tools are now accessible to the Puch agent!

---

##  Features

-  `onboard_agent`: Generate an AI assistant blueprint from a job description.
-  `validate`: Required for Puch AI to verify your tool.
-  Uses OpenAI securely via `.env`.
-  Exposed over HTTP (port 8087) with FastAPI via `FastMCP`.

---

##  Setup Instructions

### 1. Clone This Repository
```bash
git clone https://github.com/yourusername/agent-blueprint-mcp.git
cd agent-blueprint-mcp
