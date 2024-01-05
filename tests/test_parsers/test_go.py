"""Unit tests for Go-based dependency parsers."""

from readmeai.parsers.go import GoModParser

content = """
module geekdemo

go 1.19

require (
github.com/google/uuid v1.1.2
)

require (
github.com/dop251/goja_nodejs v0.0.0-20230226152057-060fa99b809f // indirect
)

require (
github.com/go-sql-driver/mysql v1.7.0 // indirect
)
"""


def test_go_mod():
    """Tests the go.mod parser."""
    parser = GoModParser()
    expected_dependencies = ["uuid", "goja_nodejs", "mysql"]
    assert parser.parse(content) == expected_dependencies
