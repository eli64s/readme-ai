import unittest
from unittest.mock import Mock, patch

from src import main


class TestReadmeAI(unittest.TestCase):
    def test_parse_arguments(self):
        with patch("argparse.ArgumentParser.parse_args") as mock_parse_args:
            mock_parse_args.return_value = Mock(
                api_key="test_key",
                local="test_path",
                output="output_path",
                remote="remote_repo",
            )
            args = main.parse_arguments()
            self.assertEqual(args.api_key, "test_key")
            self.assertEqual(args.local, "test_path")
            self.assertEqual(args.output, "output_path")
            self.assertEqual(args.remote, "remote_repo")

    def test_load_configuration(self):
        test_conf = {
            "api": {"endpoint": "test_endpoint"},
            "paths": {"md": "test_md_path"},
            "github": {"local": "test_local"},
        }

        with patch("main.FileHandler.read") as mock_read:
            mock_read.return_value = test_conf
            conf = main.load_configuration("test_config_path")
            self.assertEqual(conf.api.endpoint, "test_endpoint")
            self.assertEqual(conf.paths.md, "test_md_path")
            self.assertEqual(conf.github.local, "test_local")

    def test_main(self):
        with patch("main.load_configuration") as mock_load_configuration:
            with patch("main.parse_arguments") as mock_parse_arguments:
                with patch(
                    "main.preprocess.get_local_codebase"
                ) as mock_get_local_codebase:
                    with patch("main.preprocess.get_repo_name") as mock_get_repo_name:
                        with patch(
                            "main.preprocess.get_project_dependencies"
                        ) as mock_get_project_dependencies:
                            with patch("main.model.code_to_text") as mock_code_to_text:
                                with patch(
                                    "main.model.generate_summary_text"
                                ) as mock_generate_summary_text:
                                    with patch(
                                        "main.builder.build"
                                    ) as mock_builder_build:
                                        # Setup mocks
                                        mock_load_configuration.return_value = Mock()
                                        mock_parse_arguments.return_value = Mock(
                                            local="test_path"
                                        )
                                        mock_get_local_codebase.return_value = []
                                        mock_get_repo_name.return_value = "test_repo"
                                        mock_get_project_dependencies.return_value = []
                                        mock_code_to_text.return_value = []
                                        mock_generate_summary_text.side_effect = [
                                            "test_introduction",
                                            "test_intro_slogan",
                                        ]
                                        mock_builder_build.return_value = None

                                        # Execute main function
                                        main.asyncio.run(main.main())

                                        # Check if all mocks have been called
                                        mock_load_configuration.assert_called_once()
                                        mock_parse_arguments.assert_called_once()
                                        mock_get_local_codebase.assert_called_once()
                                        mock_get_repo_name.assert_called_once()
                                        mock_get_project_dependencies.assert_called_once()
                                        mock_code_to_text.assert_called_once()
                                        self.assertEqual(
                                            mock_generate_summary_text.call_count, 2
                                        )
                                        mock_builder_build.assert_called_once()


if __name__ == "__main__":
    unittest.main()
