"""Dependency file parsers for Swift projects."""

import re
from typing import List

from readmeai.core.base_parser import FileParser


class SwiftPackageParser(FileParser):
    """Parser for Swift Package.swift files."""

    def parse(self, content: str) -> List[str]:
        """Extracts package names from a Package.swift file."""
        try:
            package_names = set()
            lines = content.splitlines()

            for line in lines:
                line = line.strip()

                if ".package(url:" in line or ".package(name:" in line:
                    url_match = re.search(r'url:\s*"([^"]+)"', line)
                    name_match = re.search(r'name:\s*"([^"]+)"', line)

                    if url_match:
                        url = url_match.group(1)
                        package_name = self.extract_package_name_from_url(url)
                        package_names.add(package_name)
                    elif name_match:
                        package_name = name_match.group(1)
                        package_names.add(package_name)

                elif "dependencies:" in line:
                    dep_match = re.findall(r"\"([^\"]+)\"", line)
                    package_names.update(dep_match)

            return list(package_names)

        except Exception as exc:
            return self.handle_parsing_error(f"Package.swift: {str(exc)}")

    @staticmethod
    def extract_package_name_from_url(url: str) -> str:
        """Extracts the package name from a GitHub URL."""
        package_name = url.split("/")[-1]
        if package_name.endswith(".git"):
            package_name = package_name[:-4]
        return package_name
