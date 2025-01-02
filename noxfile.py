"""Nox file for running tests against multiple Python versions."""

import nox


def install(session, groups=None, extras=None, root=True):
    """Install the project for the current session using Poetry."""
    groups = groups or []
    extras = extras or []

    if root and "main" not in groups:
        groups.insert(0, "main")

    only_arg = []
    if groups:
        only_arg = [f"--only={','.join(groups)}"]

    extras_args = []
    if extras:
        for extra in extras:
            extras_args.extend(["--extras", extra])

    session.run_always(
        "poetry",
        "install",
        "--no-root",
        "--sync",
        *only_arg,
        *extras_args,
        external=True,
    )

    if root:
        session.install(".")


@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
def tests(session):
    """Run test suite against Python versions 3.9, 3.10, 3.11, and 3.12."""
    install(
        session,
        groups=["test"],
        extras=["anthropic", "google-generativeai"],
    )
    session.install(
        "pytest",
        "pytest-asyncio",
        "pytest-cov",
        "pytest-mock",
        "pytest-pretty",
        "pytest-randomly",
        "pytest-sugar",
        "pytest-xdist",
    )
    session.run(
        "poetry",
        "run",
        "pytest",
        "--config-file=pyproject.toml",
        "--cov-config=pyproject.toml",
        external=True,
    )
