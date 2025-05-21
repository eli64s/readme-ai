"""
Dependency file parsers for C/C++ projects.
"""

import re

from readmeai.parsers.base import BaseFileParser


class CMakeParser(BaseFileParser):
    """
    Parser for CMake dependency files.
    """

    def __init__(self) -> None:
        """Initializes the handler with given configuration."""
        super().__init__()

    def parse(self, content: str) -> list[str]:
        """Extracts dependencies, libs, and software from a CMakeLists.txt."""
        try:
            extracted_dependencies = []
            for line in content.splitlines():
                line = line.strip()
                if (
                    line.startswith("find_package")
                    or "target_link_libraries" in line
                ):
                    dependencies = re.findall(
                        r"(?:find_package\(|target_link_libraries\()\s*(\w+)",
                        line,
                    )
                    extracted_dependencies.extend(dependencies)

                if line.startswith("target_link_libraries") or line.startswith(
                    "find_package",
                ):
                    libs = re.findall(
                        r"target_link_libraries\([^)]+\s+([^)]+)\)",
                        line,
                    )
                    extracted_dependencies.extend(libs)

            return list(set(extracted_dependencies))

        except re.error as exc:
            return self.handle_parsing_error(f"CMakeLists.txt: {exc!s}")


class ConfigureAcParser(BaseFileParser):
    """
    Parser for configure.ac dependency files.
    """

    def parse(self, content: str) -> list[str]:
        """Extracts package names from a configure.ac file."""
        try:
            regex = re.compile(r"AC_CHECK_LIB\([^)]+\s+([^)]+)\)")
            return regex.findall(content)
        except re.error as exc:
            return self.handle_parsing_error(f"configure.ac: {exc!s}")


class MakefileAmParser(BaseFileParser):
    """
    Parser for Makefile dependency files.
    """

    def parse(self, content: str) -> list[str]:
        """Extracts dependencies from Makefile.am files."""
        try:
            extracted_packages = []
            bin_programs_regex = r"bin_PROGRAMS\s*=\s*(.*)"
            match = re.search(bin_programs_regex, content)

            if match:
                programs = match.group(1).split()
                extracted_packages.extend(programs)

            lib_sources_regex = r"libfoo_la_SOURCES\s*=\s*(.*)"
            match = re.search(lib_sources_regex, content)

            if match:
                sources = match.group(1).split()
                extracted_packages.extend(sources)

            check_programs_regex = r"check_PROGRAMS\s*=\s*(.*)"
            match = re.search(check_programs_regex, content)

            if match:
                programs = match.group(1).split()
                extracted_packages.extend(programs)

            check_libs_regex = r"check_LTLIBRARIES\s*=\s*(.*)"
            match = re.search(check_libs_regex, content)

            return list(set(extracted_packages))

        except re.error as exc:
            return self.handle_parsing_error(f"Makefile.am: {exc!s}")
