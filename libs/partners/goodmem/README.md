# langchain-goodmem

An integration package connecting [GoodMem](https://goodmem.ai) and [LangChain](https://github.com/langchain-ai/langchain).

GoodMem provides vector-based memory storage and semantic retrieval. This package exposes GoodMem operations as LangChain tools that can be used with any LangChain agent.

## Installation

```bash
pip install langchain-goodmem
```

## Tools

| Tool | Description |
|---|---|
| `GoodMemCreateSpace` | Create a new space or reuse an existing one |
| `GoodMemListSpaces` | List all spaces in your account |
| `GoodMemCreateMemory` | Store text or files as memories |
| `GoodMemRetrieveMemories` | Semantic similarity search across spaces |
| `GoodMemGetMemory` | Fetch a specific memory by ID |
| `GoodMemDeleteMemory` | Permanently delete a memory |
| `GoodMemListEmbedders` | List available embedder models |

## Quick start

```python
from langchain_goodmem import GoodMemCreateSpace, GoodMemCreateMemory, GoodMemRetrieveMemories

# Create tools with your credentials
create_space = GoodMemCreateSpace(
    goodmem_base_url="http://localhost:8080",
    goodmem_api_key="your-api-key",
)

create_memory = GoodMemCreateMemory(
    goodmem_base_url="http://localhost:8080",
    goodmem_api_key="your-api-key",
)

retrieve = GoodMemRetrieveMemories(
    goodmem_base_url="http://localhost:8080",
    goodmem_api_key="your-api-key",
)

# Use with an agent
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model="gpt-4o",
    tools=[create_space, create_memory, retrieve],
)
```
