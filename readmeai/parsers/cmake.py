"""Dependency file parsers for C/C++ projects."""

import re
from typing import List

from readmeai.core.logger import Logger
from readmeai.parsers.base_parser import FileParser

logger = Logger(__name__)


class CMakeParser(FileParser):
    """Parser for CMake dependency files."""

    def parse(self, content: str) -> List[str]:
        """Extracts dependencies, libraries, and software from a CMakeLists.txt file."""
        try:
            dependencies = []
            # Patterns to capture different CMake commands related to dependencies
            patterns = [
                r"find_package\(([^)]+)\)",
                r"add_library\((\S+)",
                r"target_link_libraries\((\S+)",
                # Add more patterns as needed
            ]
            for pattern in patterns:
                regex = re.compile(pattern)
                matches = regex.findall(content)
                dependencies.extend(matches)
            # Clean and return unique dependencies
            return list(set(dep.strip() for dep in dependencies))
        except re.error as exc:
            self.log_error(f"Error parsing CMakeLists.txt: {str(exc)}")
            return []


class MakefileAmParser(FileParser):
    """Parser for Makefile dependency files."""

    def parse(self, content: str) -> List[str]:
        """Extracts package names from a Makefile.am file."""
        try:
            regex = re.compile(r"bin_PROGRAMS\s*=\s*(.+)")
            matches = regex.findall(content)
            package_names = [
                dep for match in matches for dep in filter(None, match.split())
            ]
            return package_names
        except re.error as exc:
            self.log_error(f"Error parsing Makefile.am: {str(exc)}")
            return []


class ConfigureAcParser(FileParser):
    """Parser for configure.ac dependency files."""

    def parse(self, content: str) -> List[str]:
        """Extracts package names from a configure.ac file."""
        try:
            regex = re.compile(r"AC_CHECK_LIB\([^)]+\s+([^)]+)\)")
            return regex.findall(content)
        except re.error as exc:
            self.log_error(f"Error parsing configure.ac: {str(exc)}")
            return []
