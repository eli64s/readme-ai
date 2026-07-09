from readmeai.models.azure import AzureOpenAIHandler


def test_azure_openai_handler_sets_attributes(azure_openai_handler: AzureOpenAIHandler):
    """Test that the Azure Openai handler sets the correct attributes."""
    assert hasattr(azure_openai_handler, "host_name")
    assert hasattr(azure_openai_handler, "model")
    assert hasattr(azure_openai_handler, "max_tokens")
    assert hasattr(azure_openai_handler, "top_p")
    assert hasattr(azure_openai_handler, "client")
