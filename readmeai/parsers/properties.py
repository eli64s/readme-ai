"""Parser for *.properties configuration files."""

import re

from .base import BaseFileParser


class PropertiesParser(BaseFileParser):
    def __init__(self):
        super().__init__()
        super().__init__()
        self.common_tech_keywords = {
            "spring",
            "gradle",
            "maven",
            "java",
            "kotlin",
            "python",
            "node",
            "react",
            "angular",
            "vue",
            "docker",
            "kubernetes",
            "aws",
            "azure",
            "gcp",
            "android",
            "ios",
            "swift",
            "flutter",
            "django",
            "flask",
            "fastapi",
            "express",
            "nest",
            "tensorflow",
            "pytorch",
            "pandas",
            "numpy",
            "scikit",
            "hadoop",
            "spark",
            "kafka",
            "redis",
            "mongodb",
            "postgresql",
            "mysql",
            "oracle",
            "elasticsearch",
            "graphql",
            "rest",
            "grpc",
            "protobuf",
            "openapi",
            "swagger",
            "selenium",
            "terraform",
            "ansible",
            "helm",
            "git",
            "svn",
            "cicd",
            "jenkins",
            "circleci",
            "gitlab",
            "github",
            "bitbucket",
            "travis",
            "webpack",
            "babel",
            "typescript",
            "ruby",
            "rails",
            "scala",
            "clojure",
            "erlang",
            "elixir",
            "phoenix",
            "laravel",
            "svelte",
            "webassembly",
            "rust",
            "go",
            "julia",
            "csharp",
            ".net",
            "asp.net",
            "qml",
            "unity",
            "unreal",
            "cryengine",
            "vulkan",
            "opengl",
            "threejs",
            "blender",
            "matlab",
            "octave",
            "fortran",
            "r",
            "tableau",
            "powerbi",
            "qlik",
            "sap",
            "salesforce",
            "dynamics",
            "stripe",
            "paypal",
            "braintree",
            "rabbitmq",
            "zeromq",
            "socket.io",
            "websockets",
            "webrtc",
            "oauth",
            "jwt",
            "saml",
            "openid",
            "hashicorp",
            "cassandra",
            "neo4j",
            "arangodb",
            "couchbase",
            "dynamodb",
            "memcached",
            "sphinx",
            "solr",
            "lucene",
            "next.js",
            "nuxt.js",
            "remix",
            "gatsby",
            "emotion",
            "styled-components",
            "tailwindcss",
            "bootstrap",
            "material-ui",
            "ant-design",
            "chakra-ui",
            "quasar",
            "primefaces",
            "vuetify",
            "fivem",
            "qt",
            "wxwidgets",
            "tkinter",
            "xamarin",
            "react-native",
            "electron",
            "cordova",
            "ionic",
            "nativescript",
            "appium",
            "xstate",
            "rxjs",
            "mobx",
            "redux",
            "vuex",
            "recoil",
            "pinia",
            "akka",
            "vert.x",
            "play",
            "quarkus",
            "micronaut",
            "spring-boot",
            "netty",
            "kotlinx.coroutines",
            "jetpack",
            "room",
            "workmanager",
            "compose",
            "pulumi",
            "boto3",
            "sdkman",
            "jvm",
            "graalvm",
            "openjdk",
            "v8",
            "spidermonkey",
            "webgl",
            "d3.js",
            "highcharts",
            "amcharts",
            "echarts",
            "plotly",
            "vega",
            "kendo-ui",
        }

    def parse(self, content: str) -> list[str]:
        lines = content.split("\n")
        dependencies = set()

        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            dependencies.update(self._extract_from_line(line))

        return sorted(list(dependencies))

    def _clean_word(self, word: str) -> str:
        word = word.lower()
        word = re.sub(
            r"^(lib|org|com|net|io|api|sdk|cli|ui|app|service|utils?|helpers?|core|base|impl|test|dev|prod)\.?",
            "",
            word,
        )
        word = re.sub(
            r"(version|tool|module|plugin|dependency|lib|framework|platform)s?$",
            "",
            word,
        )
        return word.strip()

    def _extract_from_line(self, line: str) -> set[str]:
        extracted = set()

        if "=" in line:
            key, value = line.split("=", 1)
            extracted.update(self._extract_words(key))
            extracted.update(self._extract_words(value))

            # Handle version-specific dependencies
            if "version" in key.lower():
                dep_name = re.sub(
                    r"version.*$", "", key, flags=re.IGNORECASE
                ).strip()
                extracted.add(f"{dep_name}: {value}")
        else:
            extracted.update(self._extract_words(line))

        return extracted

    def _extract_words(self, text: str) -> set[str]:
        words = {text.lower()}
        parts = re.split(r"[._-]", text)
        words.update(part.lower() for part in parts)

        for i in range(len(parts)):
            for j in range(i + 1, len(parts) + 1):
                words.add(".".join(parts[i:j]).lower())

        # Split camelCase
        for part in parts:
            words.update(self._split_camel_case(part))

        return words

    def _filter_technologies(self, words: set[str]) -> set[str]:
        return {
            word
            for word in words
            if word in self.common_tech_keywords or len(word) > 1
        }

    def _split_camel_case(self, text: str) -> set[str]:
        words = re.findall(
            r"[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+", text
        )
        return {word.lower() for word in words}
