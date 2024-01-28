"""Parser for Rust dependency files."""

from typing import List

import toml

from readmeai.core.base_parser import FileParser


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
                dependencies.extend(data["dependencies"].keys())
            if "dev-dependencies" in data:
                dependencies.extend(data["dev-dependencies"].keys())

            for key in data:
                if key.startswith("dependencies.") and isinstance(
                    data[key], dict
                ):
                    dependencies.extend(data[key].keys())

            return dependencies

        except toml.TomlDecodeError as exc:
            return self.handle_parsing_error(f"cargo.toml: {str(exc)}")
