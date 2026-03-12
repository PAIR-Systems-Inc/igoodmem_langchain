"""Unit tests for GoodMem tool schemas and instantiation."""

from langchain_goodmem import (
    GoodMemCreateMemory,
    GoodMemCreateSpace,
    GoodMemDeleteMemory,
    GoodMemGetMemory,
    GoodMemListEmbedders,
    GoodMemListSpaces,
    GoodMemRetrieveMemories,
)


_COMMON_KWARGS = {
    "goodmem_base_url": "http://localhost:8080",
    "goodmem_api_key": "test-key",
}


def test_create_space_schema() -> None:
    tool = GoodMemCreateSpace(**_COMMON_KWARGS)
    assert tool.name == "goodmem_create_space"
    schema = tool.args_schema.model_json_schema()
    assert "name" in schema["properties"]
    assert "embedder_id" in schema["properties"]
    required = schema.get("required", [])
    assert "name" in required
    assert "embedder_id" in required


def test_create_memory_schema() -> None:
    tool = GoodMemCreateMemory(**_COMMON_KWARGS)
    assert tool.name == "goodmem_create_memory"
    schema = tool.args_schema.model_json_schema()
    assert "space_id" in schema["properties"]
    assert "text_content" in schema["properties"]
    assert "file_path" in schema["properties"]
    assert "source" in schema["properties"]
    assert "author" in schema["properties"]
    assert "tags" in schema["properties"]
    assert "metadata" in schema["properties"]


def test_retrieve_memories_schema() -> None:
    tool = GoodMemRetrieveMemories(**_COMMON_KWARGS)
    assert tool.name == "goodmem_retrieve_memories"
    schema = tool.args_schema.model_json_schema()
    assert "query" in schema["properties"]
    assert "space_ids" in schema["properties"]
    assert "max_results" in schema["properties"]
    assert "include_memory_definition" in schema["properties"]
    assert "wait_for_indexing" in schema["properties"]


def test_get_memory_schema() -> None:
    tool = GoodMemGetMemory(**_COMMON_KWARGS)
    assert tool.name == "goodmem_get_memory"
    schema = tool.args_schema.model_json_schema()
    assert "memory_id" in schema["properties"]
    assert "include_content" in schema["properties"]


def test_delete_memory_schema() -> None:
    tool = GoodMemDeleteMemory(**_COMMON_KWARGS)
    assert tool.name == "goodmem_delete_memory"
    schema = tool.args_schema.model_json_schema()
    assert "memory_id" in schema["properties"]


def test_list_embedders_schema() -> None:
    tool = GoodMemListEmbedders(**_COMMON_KWARGS)
    assert tool.name == "goodmem_list_embedders"


def test_list_spaces_schema() -> None:
    tool = GoodMemListSpaces(**_COMMON_KWARGS)
    assert tool.name == "goodmem_list_spaces"


def test_tools_are_base_tool_instances() -> None:
    from langchain_core.tools import BaseTool

    for cls in (
        GoodMemCreateSpace,
        GoodMemCreateMemory,
        GoodMemRetrieveMemories,
        GoodMemGetMemory,
        GoodMemDeleteMemory,
        GoodMemListEmbedders,
        GoodMemListSpaces,
    ):
        tool = cls(**_COMMON_KWARGS)
        assert isinstance(tool, BaseTool)
