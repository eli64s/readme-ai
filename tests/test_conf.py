"""tests/test_conf.py"""

import unittest

from conf import AppConfig
from conf import GitHub
from conf import HtmlObjs
from conf import OpenAI
from conf import Paths


class TestAppConfig(unittest.TestCase):
    def test_create_app_config(self):
        api = OpenAI(engine="davinci", sk_key="my-secret-key")
        html = HtmlObjs(head="<head>", body="<body>", close="</html>")
        paths = Paths(
            docs="test_docs.csv",
            html="test_html.html",
            mrkd="test_output.md",
            pkgs="test_icons.json",
        )
        store = GitHub(url="https://github.com/myrepo")

        app_config = AppConfig(api=api, html=html, paths=paths, store=store)

        self.assertIsInstance(app_config, AppConfig)
        self.assertEqual(app_config.api.engine, "davinci")
        self.assertEqual(app_config.api.sk_key, "my-secret-key")
        self.assertEqual(app_config.html.head, "<head>")
        self.assertEqual(app_config.html.body, "<body>")
        self.assertEqual(app_config.html.close, "</html>")
        self.assertEqual(app_config.paths.docs, "test_docs.csv")
        self.assertEqual(app_config.paths.html, "test_html.html")
        self.assertEqual(app_config.paths.mrkd, "test_output.md")
        self.assertEqual(app_config.paths.pkgs, "test_icons.json")
        self.assertEqual(app_config.store.url, "https://github.com/myrepo")
