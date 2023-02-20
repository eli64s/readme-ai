# test_utils.py
import os
import shutil
import tempfile
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from utils import clone_codebase
from utils import get_extensions
from utils import get_packages
from utils import make_temp_directory
from utils import parse_codebase


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        os.mkdir(os.path.join(self.test_dir, "test_repo"))
        with open(os.path.join(self.test_dir, "test_repo", "test_file1.py"), "w") as f:
            f.write("print('hello world!')")
        with open(os.path.join(self.test_dir, "test_repo", "test_file2.py"), "w") as f:
            f.write("import numpy as np\nx = np.array([1, 2, 3])\nprint(x)")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_make_temp_directory(self):
        with make_temp_directory() as temp_dir:
            self.assertTrue(os.path.isdir(temp_dir))
        self.assertFalse(os.path.isdir(temp_dir))

    @patch("utils.git.Repo.clone_from")
    @patch("utils.parse_codebase")
    @patch("utils.get_packages")
    @patch("utils.get_extensions")
    def test_clone_codebase(
        self,
        mock_get_extensions,
        mock_get_packages,
        mock_parse_codebase,
        mock_clone_from,
    ):
        mock_get_extensions.return_value = ["py", "txt"]
        mock_get_packages.return_value = ["numpy", "pandas"]
        mock_parse_codebase.return_value = {
            "test_file1.py": "print('hello world!')",
            "test_file2.py": "import numpy as np\nx = np.array([1, 2, 3])\nprint(x)",
        }

        result = clone_codebase("https://github.com/myrepo")

        mock_clone_from.assert_called_once_with(
            "https://github.com/myrepo", unittest.mock.ANY
        )
        mock_get_extensions.assert_called_once_with(unittest.mock.ANY)
        mock_get_packages.assert_called_once()
        mock_parse_codebase.assert_called_once_with(unittest.mock.ANY)
        self.assertEqual(
            result,
            {
                "test_file1.py": "print('hello world!')",
                "test_file2.py": "import numpy as np\nx = np.array([1, 2, 3])\nprint(x)",
                "packages": ["numpy", "pandas"],
                "extensions": ["py", "txt"],
            },
        )

    def test_get_extensions(self):
        result = get_extensions(os.path.join(self.test_dir, "test_repo"))
        self.assertEqual(result, ["py"])

    def test_get_packages(self):
        with open(os.path.join(self.test_dir, "requirements.txt"), "w") as f:
            f.write("numpy==1.19.0\npandas==1.2.3")
        result = get_packages()
        self.assertEqual(result, ["numpy", "pandas"])

    def test_parse_codebase(self):
        result = parse_codebase(os.path.join(self.test_dir, "test_repo"))
        self.assertEqual(
            result,
            {
                "test_file1.py": "print('hello world!')",
                "test_file2.py": "import numpy as np\nx = np.array([1, 2, 3])\nprint(x)",
            },
        )
