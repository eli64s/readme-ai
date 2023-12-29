"""Test automation with nox and pytest."""

import nox


def install(session, groups, root=True):
    """Install the package in the current session."""
    if root:
        groups = ["main", *groups]

    session.run_always(
        "poetry",
        "install",
        "--no-root",
        "--sync",
        f"--only={','.join(groups)}",
        external=True,
    )
    if root:
        session.install(".")


@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
def tests(session):
    """Run the test suite across Python versions"""
    session.install(".")
    session.install(".[test]")
    session.run("pytest", "--cov=./", "--cov-report=term-missing")
