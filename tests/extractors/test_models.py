from readmeai.extractors.models import RepositoryContext


def test_repository_context(mock_repository_context: RepositoryContext):
    context = mock_repository_context
    assert len(context.files) > 0
    assert "python" in context.languages
    assert context.quickstart.primary_language == "Python"
