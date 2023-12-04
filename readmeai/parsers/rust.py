"""Parser for Rust dependency files."""

from typing import List

import toml

from readmeai.parsers.base_parser import FileParser

TOM_DECODE_ERROR = "Error decoding TOML content: {0}"


class CargoTomlParser(FileParser):
    """
    Parser for Rust cargo.toml dependency files.
    """

    def parse(self, content: str) -> List[str]:
        """Extract packages names from Rust TOML files."""
        try:
            data = toml.loads(content)
            dependencies = []
            if "dependencies" in data:
                dependencies.extend(data.get("dependencies", {}).keys())
            if "dev-dependencies" in data:
                dependencies.extend(data.get("dev-dependencies", {}).keys())
            return dependencies

        except toml.TomlDecodeError as error:
            self.log_error(TOM_DECODE_ERROR.format(error))
            return dependencies
