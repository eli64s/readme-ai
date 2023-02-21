# test_model.py
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from model import code_to_text


class TestCodeToText(unittest.TestCase):
    def setUp(self):
        self.files = {
            "test_file1.py": "print('hello world!')",
            "test_file2.py": "import numpy as np\nx = np.array([1, 2, 3])\nprint(x)",
        }

    @patch("model.openai.Completion.create")
    def test_code_to_text(self, mock_create):
        mock_response1 = MagicMock()
        mock_response1["choices"][0]["text"].strip.return_value = "Print 'hello world!'"
        mock_response2 = MagicMock()
        mock_response2["choices"][0][
            "text"
        ].strip.return_value = "Create a numpy array and print it"
        mock_create.side_effect = [mock_response1, mock_response2]

        result = code_to_text("test_engine", self.files)

        mock_create.assert_has_calls(
            [
                unittest.mock.call(
                    model="test_engine",
                    prompt="Summarize the code in the following Python script: print('hello world!')",
                    temperature=0,
                    max_tokens=100,
                    top_p=1,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                ),
                unittest.mock.call(
                    model="test_engine",
                    prompt="Summarize the code in the following Python script: import numpy as np\nx = np.array([1, 2, 3])\nprint(x)",
                    temperature=0,
                    max_tokens=100,
                    top_p=1,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                ),
            ]
        )

        self.assertEqual(
            result,
            [
                ("test_file1.py", "Print 'hello world!'"),
                ("test_file2.py", "Create a numpy array and print it"),
            ],
        )
