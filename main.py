from typing import Annotated
from fastmcp import FastMCP
from fastmcp.server.auth.providers.bearer import BearerAuthProvider, RSAKeyPair
from mcp.server.auth.provider import AccessToken
from mcp.types import TextContent
from pydantic import BaseModel, Field
import openai
import os
from dotenv import load_dotenv

load_dotenv()

#  CONFIG
TOKEN = "16e5a4be404d"
MY_NUMBER = "919929108096"
openai.api_key = os.getenv("OPENAI_API_KEY")

#  Auth Provider
class SimpleBearerAuthProvider(BearerAuthProvider):
    def __init__(self, token: str):
        k = RSAKeyPair.generate()
        super().__init__(public_key=k.public_key)
        self.token = token

    async def load_access_token(self, token: str) -> AccessToken | None:
        if token == self.token:
            return AccessToken(token=token, client_id="puch_user")
        return None

# MCP Server 
mcp = FastMCP("Agent Blueprint MCP", auth=SimpleBearerAuthProvider(TOKEN))

# Tool Description 
class RichToolDescription(BaseModel):
    description: str
    use_when: str
    side_effects: str | None = None

async def _onboard_agent(job_description: str, tone: str = "professional", domain_knowledge: str = "general") -> str:
    prompt = f"""
You are an AI agent architect.

Given the following:

- Job Description: {job_description}
- Tone: {tone}
- Domain Knowledge: {domain_knowledge}

Generate the following as Markdown:

1. **System Prompt**: A short instruction defining the agent's behavior  
2. **Required Tools**: List any tools this agent should have access to  
3. **Example Interactions**: At least 2 realistic user prompts and the assistant’s ideal replies
"""
    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"<error>OpenAI API failed: {e}</error>"

#  Decorated Tool for MCP
@mcp.tool(description=RichToolDescription(
    description="Onboard an AI assistant given its job, tone, and knowledge domain.",
    use_when="User wants to design a new AI assistant or agent from scratch."
).model_dump_json())
async def onboard_agent(
    job_description: Annotated[str, Field(description="What is the agent supposed to do?")],
    tone: Annotated[str, Field(description="Preferred tone (professional, casual, etc.)")] = "professional",
    domain_knowledge: Annotated[str, Field(description="Domain knowledge focus (e.g. legal, tech)")] = "general"
) -> str:
    return await _onboard_agent(job_description, tone, domain_knowledge)

# Required Validation Tool 
@mcp.tool
async def validate() -> str:
    return MY_NUMBER

# Run Server 
async def main():
    await mcp.run_async("streamable-http", host="0.0.0.0", port=8089, path="/")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
