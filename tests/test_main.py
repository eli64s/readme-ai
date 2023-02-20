# test_main.py
import os
import shutil
import tempfile
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from main import SingletonLogger
from main import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.conf_path = os.path.join(self.test_dir, "conf.toml")
        with open(self.conf_path, "w") as f:
            f.write(
                '[api]\nengine = "test_engine"\nsk_key = "test_key"\n\n[html]\nhead = "<head>"\nbody = "<body>"\nclose = "</html>"\n\n[paths]\ndocs = "test_docs.csv"\nhtml = "test_html.html"\nmrkd = "test_output.md"\npkgs = "test_icons.json"\n\n[store]\nurl = "https://github.com/myrepo"'
            )

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    @patch("main.dacite")
    @patch("main.processor.clone_codebase")
    @patch("main.builder.create_html")
    @patch.object(SingletonLogger, "info")
    def test_main(self, mock_info, mock_create_html, mock_clone_codebase, mock_dacite):
        mock_conf_objs = MagicMock()
        mock_conf_objs.store.url = "https://github.com/myrepo"
        mock_dacite.from_dict.return_value = mock_conf_objs
        mock_clone_codebase.return_value = {
            "packages": ["test_pkg1", "test_pkg2"],
            "extensions": [],
        }
        mock_html = "<html>test_html</html>"
        mock_create_html.return_value = mock_html

        main()

        mock_dacite.from_dict.assert_called_once()
        mock_clone_codebase.assert_called_once_with("https://github.com/myrepo")
        mock_create_html.assert_called_once()
        mock_info.assert_called_with("\nTotal files to document: 0\n")
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "test_html.html")))
