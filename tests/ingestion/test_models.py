from readmeai.ingestion.models import RepositoryContext


def test_repository_context(repository_context_fixture: RepositoryContext):
    context = repository_context_fixture
    assert len(context.files) > 0
    assert "python" in context.languages
    assert context.quickstart.primary_language == "Python"
