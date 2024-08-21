"""
Tests for parsing cargo.toml Rust files.
"""

from readmeai.parsers.rust import CargoTomlParser

content = """
[package]
name = "lightning-invoice"

[package.metadata.docs.rs]

[features]
default = ["std"]
no-std = ["hashbrown", "lightning/no-std"]
std = ["bitcoin_hashes/std", "num-traits/std", "lightning/std", "bech32/std"]

[dependencies]
bech32 = { version = "0.9.0", default-features = false }
lightning = { version = "0.0.118", path = "../lightning", default-features = false }
secp256k1 = { version = "0.27.0", default-features = false, features = ["recovery", "alloc"] }
num-traits = { version = "0.2.8", default-features = false }
bitcoin_hashes = { version = "0.12.0", default-features = false }
hashbrown = { version = "0.8", optional = true }
serde = { version = "1.0.118", optional = true }
bitcoin = { version = "0.30.2", default-features = false }

[dev-dependencies]
lightning = { version = "0.0.118", path = "../lightning", default-features = false, features = ["_test_utils"] }
hex = { package = "hex-conservative", version = "0.1.1", default-features = false }
serde_json = { version = "1"}
"""


def test_cargo_toml_parser():
    """Tests the Cargo.toml parser."""
    parser = CargoTomlParser()
    expected_dependencies = [
        "bech32",
        "lightning",
        "secp256k1",
        "num-traits",
        "bitcoin_hashes",
        "hashbrown",
        "serde",
        "bitcoin",
        "lightning",
        "hex",
        "serde_json",
    ]
    assert parser.parse(content) == expected_dependencies


def test_cargo_toml_parser_missing_section():
    parser = CargoTomlParser()
    content = """
    [dependencies]
    packageA = "1.0.0"
    """
    result = parser.parse(content)
    assert set(result) == {"packageA"}


def test_cargo_toml_parser_extended_dependency_tables():
    parser = CargoTomlParser()
    content = """
    [dependencies]
    packageA = "1.0.0"

    [dev-dependencies]
    packageC = "3.0.0"
    """
    result = parser.parse(content)
    assert set(result) == {"packageA", "packageC"}


def test_cargo_toml_parser_invalid_toml():
    parser = CargoTomlParser()
    content = "This is not a valid TOML"
    data = parser.parse(content)
    assert isinstance(data, list)
    assert data == []
