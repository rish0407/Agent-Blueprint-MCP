#  Agent Blueprint MCP | Build AI Agents Instantly

**Create structured, domain-specific AI assistants using a single prompt. Powered by OpenAI. Integrated with [Puch AI](https://puch.ai/) via MCP.**

---

`Agent Blueprint MCP` is a lightweight backend service that helps you **generate complete AI assistant specifications**, including:

- A system prompt
- Required tools
- Example user interactions

This is done using your own [OpenAI API key](https://platform.openai.com/), and exposed to Puch AI through a secure MCP interface.

---

##  What is Puch AI? How Does It Help?

[Puch AI](https://puch.ai/) is a WhatsApp-based assistant platform that lets you:

- Build, test, and run AI agents conversationally.
- Integrate tools you write locally using **MCP (Modular Custom Protocol)**.
- Call your tool via `/commands` in WhatsApp—no frontend needed.

This repo uses FastMCP to host a custom tool, and exposes it securely to Puch AI via `localtunnel` or `ngrok`. When you send `/mcp connect` in WhatsApp, your MCP tools are now accessible to the Puch agent!

---

##  Features

-  `onboard_agent`: Generate an AI assistant blueprint from a job description.
-  `validate`: Required for Puch AI to verify your tool.
-  Uses OpenAI securely via `.env`.
-  Powered by FastMCP and securely callable through Puch AI via HTTP tunnel.
.

---

##  Setup Instructions

### 1. Clone This Repository
```bash
git clone https://github.com/yourusername/agent-blueprint-mcp.git
cd agent-blueprint-mcp
### 2. Install Dependencies
pip install -r requirements.txt
### 3. Create a .env File
OPENAI_API_KEY=sk-...
### 4. Run the MCP Server Locally
Start your MCP server with:
python main.py

Puch AI needs your local server to be accessible over the internet.
You can use either localtunnel or ngrok to do that.
Once you have your public tunnel URL, open your WhatsApp chat with Puch AI and send:
/mcp connect https://your-url-here 16e5a4be404d

You can now trigger your tool with:
/onboard_agent An AI assistant that helps lawyers write contracts. prof
