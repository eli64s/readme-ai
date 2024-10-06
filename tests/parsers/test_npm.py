import json

from readmeai.parsers.npm import PackageJsonParser

package_json_file = """
{
  "name": "chatgpt-app",
  "version": "1.0.0",
  "main": "node_modules/expo/AppEntry.js",
  "scripts": {
    "start": "expo start",
    "android": "expo start --android",
    "ios": "expo start --ios",
    "web": "expo start --web"
  },
  "dependencies": {
    "@react-navigation/native": "^6.1.1",
    "@react-navigation/native-stack": "^6.9.7",
    "expo": "~47.0.9",
    "expo-clipboard": "~4.0.1",
    "expo-status-bar": "~1.4.2",
    "react": "18.1.0",
    "react-dom": "18.1.0",
    "react-native": "0.70.5",
    "react-native-safe-area-context": "4.4.1",
    "react-native-screens": "~3.18.0",
    "react-native-web": "~0.18.9",
    "react-uuid": "^2.0.0"
  },
  "devDependencies": {
    "@babel/core": "^7.12.9",
    "@types/react": "~18.0.14",
    "@types/react-native": "~0.70.6",
    "typescript": "^4.6.3"
  },
  "private": true
}
"""


def test_package_json_parser():
    """Tests the JSON parser."""
    parser = PackageJsonParser()
    dependencies = parser.parse(package_json_file)
    assert dependencies == [
        "@react-navigation/native",
        "@react-navigation/native-stack",
        "expo",
        "expo-clipboard",
        "expo-status-bar",
        "react",
        "react-dom",
        "react-native",
        "react-native-safe-area-context",
        "react-native-screens",
        "react-native-web",
        "react-uuid",
        "@babel/core",
        "@types/react",
        "@types/react-native",
        "typescript",
    ]


def test_package_json_parser_success():
    parser = PackageJsonParser()
    content = json.dumps(
        {
            "dependencies": {"packageA": "1.0.0"},
            "devDependencies": {"packageB": "2.0.0"},
            "peerDependencies": {"packageC": "3.0.0"},
        },
    )
    result = parser.parse(content)
    assert set(result) == {"packageA", "packageB", "packageC"}


def test_package_json_parser_no_dependencies():
    parser = PackageJsonParser()
    content = json.dumps({})
    result = parser.parse(content)
    assert result == []


def test_package_json_parser_invalid_json():
    parser = PackageJsonParser()
    content = '{"dependencies": {"packageA": "1.0.0", invalid json}'
    data = parser.parse(content)
    assert isinstance(data, list)
    assert data == []
