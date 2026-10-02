"""Tests for the .readmeaiignore file filter functionality."""

from readmeai.preprocessor.file_filter import is_excluded
from readmeai.preprocessor.ignore_handler import IgnoreHandler


class TestIgnoreHandler:
    """Test cases for IgnoreHandler class."""

    def test_no_ignore_file(self, tmp_path, monkeypatch):
        """Test with no ignore file."""
        # Change to tmp_path to avoid loading actual .readmeaiignore
        monkeypatch.chdir(tmp_path)

        default_rules = {"directories": [], "extensions": [], "files": []}
        handler = IgnoreHandler(default_rules)
        handler.load_user_rules(tmp_path)
        assert handler.ignore_rules == default_rules

    def test_basic_patterns(self, tmp_path, monkeypatch):
        """Test basic pattern loading."""
        # Change to tmp_path to avoid conflicts with existing files
        monkeypatch.chdir(tmp_path)

        # Create .readmeaiignore file in tmp_path
        ignore_file = tmp_path / ".readmeaiignore"
        ignore_file.write_text("""
# This is a comment
*.log
temp.txt
# Another comment

src/markitecture/
""")

        try:
            default_rules = {"directories": [], "extensions": [], "files": []}
            handler = IgnoreHandler(default_rules)
            handler.load_user_rules(tmp_path)

            # Check that patterns were parsed correctly
            assert "log" in handler.ignore_rules["extensions"]
            assert "temp.txt" in handler.ignore_rules["files"]
            assert "src/markitecture" in handler.ignore_rules["directories"]
        finally:
            # Clean up
            if ignore_file.exists():
                ignore_file.unlink()

    def test_basic_integration(self, tmp_path):
        """Test basic integration of ignore handler."""
        default_rules = {
            "directories": ["build"],
            "extensions": ["log"],
            "files": [".DS_Store"],
        }
        handler = IgnoreHandler(default_rules)
        handler.load_user_rules(tmp_path)  # No user rules, just test default

        # Create test files
        (tmp_path / "build").mkdir()
        (tmp_path / "build" / "output.txt").touch()
        (tmp_path / "debug.log").touch()
        (tmp_path / ".DS_Store").touch()
        (tmp_path / "main.py").touch()

        build_file = tmp_path / "build" / "output.txt"
        log_file = tmp_path / "debug.log"
        ds_store = tmp_path / ".DS_Store"
        main_file = tmp_path / "main.py"

        assert handler.is_excluded(build_file, tmp_path) is True
        assert handler.is_excluded(log_file, tmp_path) is True
        assert handler.is_excluded(ds_store, tmp_path) is True
        assert handler.is_excluded(main_file, tmp_path) is False

    def test_node_modules_and_directory_exclusion(self, tmp_path):
        """Test that node_modules and directory patterns in .readmeaiignore exclude nested files."""
        ignore_file = tmp_path / ".readmeaiignore"
        ignore_file.write_text("node_modules/\nsrc/markitecture/\n")

        default_rules = {"directories": [], "extensions": [], "files": []}
        handler = IgnoreHandler(default_rules)
        handler.load_user_rules(tmp_path)

        nm_file = tmp_path / "node_modules" / "axios" / "index.js"
        nm_file.parent.mkdir(parents=True)
        nm_file.touch()

        nested_nm_file = tmp_path / "frontend" / "node_modules" / "lodash" / "package.json"
        nested_nm_file.parent.mkdir(parents=True)
        nested_nm_file.touch()

        markitecture_file = tmp_path / "src" / "markitecture" / "main.py"
        markitecture_file.parent.mkdir(parents=True)
        markitecture_file.touch()

        valid_file = tmp_path / "src" / "other" / "main.py"
        valid_file.parent.mkdir(parents=True)
        valid_file.touch()

        assert handler.is_excluded(nm_file, tmp_path) is True
        assert handler.is_excluded(nested_nm_file, tmp_path) is True
        assert handler.is_excluded(markitecture_file, tmp_path) is True
        assert handler.is_excluded(valid_file, tmp_path) is False

    def test_node_modules_pattern_without_trailing_slash(self, tmp_path):
        """Test node_modules pattern specified without trailing slash."""
        ignore_file = tmp_path / ".readmeaiignore"
        ignore_file.write_text("node_modules\n")

        default_rules = {"directories": [], "extensions": [], "files": []}
        handler = IgnoreHandler(default_rules)
        handler.load_user_rules(tmp_path)

        nm_file = tmp_path / "node_modules" / "pkg" / "index.js"
        nm_file.parent.mkdir(parents=True)
        nm_file.touch()

        valid_file = tmp_path / "src" / "index.js"
        valid_file.parent.mkdir(parents=True)
        valid_file.touch()

        assert handler.is_excluded(nm_file, tmp_path) is True
        assert handler.is_excluded(valid_file, tmp_path) is False


class TestFileFilterFunction:
    """Test cases for is_excluded function."""

    def test_directory_exclusion(self, tmp_path):
        """Test directory exclusion with basic ignore list."""
        # Create directory structure
        (tmp_path / "src").mkdir()
        (tmp_path / "src" / "markitecture").mkdir()
        (tmp_path / "src" / "markitecture" / "main.py").touch()
        (tmp_path / "src" / "other").mkdir()
        (tmp_path / "src" / "other" / "file.py").touch()
        (tmp_path / "README.md").touch()

        # Test filtering with ignore list
        ignore_list = {"directories": ["src"], "extensions": [], "files": []}

        src_markitecture_file = tmp_path / "src" / "markitecture" / "main.py"
        src_other_file = tmp_path / "src" / "other" / "file.py"
        readme_file = tmp_path / "README.md"

        assert is_excluded(ignore_list, src_markitecture_file, tmp_path) is True
        assert is_excluded(ignore_list, src_other_file, tmp_path) is True
        assert is_excluded(ignore_list, readme_file, tmp_path) is False

    def test_extension_exclusion(self, tmp_path):
        """Test file extension exclusion."""
        # Create test files
        (tmp_path / "debug.log").touch()
        (tmp_path / "cache.tmp").touch()
        (tmp_path / "main.py").touch()

        ignore_list = {"directories": [], "extensions": ["log", "tmp"], "files": []}

        log_file = tmp_path / "debug.log"
        tmp_file = tmp_path / "cache.tmp"
        py_file = tmp_path / "main.py"

        assert is_excluded(ignore_list, log_file, tmp_path) is True
        assert is_excluded(ignore_list, tmp_file, tmp_path) is True
        assert is_excluded(ignore_list, py_file, tmp_path) is False

    def test_file_exclusion(self, tmp_path):
        """Test specific file exclusion."""
        # Create test files
        (tmp_path / "config.local").touch()
        (tmp_path / "secrets.env").touch()
        (tmp_path / "config.py").touch()

        ignore_list = {
            "directories": [],
            "extensions": [],
            "files": ["config.local", "secrets.env"],
        }

        config_file = tmp_path / "config.local"
        secrets_file = tmp_path / "secrets.env"
        py_file = tmp_path / "config.py"

        assert is_excluded(ignore_list, config_file, tmp_path) is True
        assert is_excluded(ignore_list, secrets_file, tmp_path) is True
        assert is_excluded(ignore_list, py_file, tmp_path) is False

    def test_nested_directory_exclusion(self, tmp_path):
        """Test multi-part directory exclusion with is_excluded."""
        (tmp_path / "src" / "markitecture").mkdir(parents=True)
        file1 = tmp_path / "src" / "markitecture" / "main.py"
        file1.touch()
        (tmp_path / "src" / "other").mkdir(parents=True)
        file2 = tmp_path / "src" / "other" / "main.py"
        file2.touch()

        ignore_list = {
            "directories": ["src/markitecture"],
            "extensions": [],
            "files": [],
        }
        assert is_excluded(ignore_list, file1, tmp_path) is True
        assert is_excluded(ignore_list, file2, tmp_path) is False
