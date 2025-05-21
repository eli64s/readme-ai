"""Unit tests for Java-based dependency parsers."""

import re
from unittest.mock import patch

from readmeai.parsers.maven import MavenParser

content = """
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
<modelVersion>4.0.0</modelVersion>

<groupId>com.mt</groupId>
<artifactId>java-web-app</artifactId>
<packaging>war</packaging>
<version>1.0</version>

<name>Maven Web Application</name>
<url>http://mithuntechnologies.com</url>

<description>Maven Web Project</description>

<organization>
<name>Mithun Technologies</name>
<url>http://mithuntechnologies.com/</url>
</organization>

<properties>
<!-- versions -->

<spring.version>5.0.7.RELEASE</spring.version>
<junit.version>4.12</junit.version>
<log4j.version>1.2.17</log4j.version>
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
</properties>

<dependencies>

<!-- test dependencies -->
<dependency>
<groupId>junit</groupId>
<artifactId>junit</artifactId>
<version>${junit.version}</version>
<scope>test</scope>
</dependency>

<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-test</artifactId>
<version>3.2.3.RELEASE</version>
<scope>test</scope>
</dependency>

<dependency>
<groupId>org.mockito</groupId>
<artifactId>mockito-core</artifactId>
<version>1.9.5</version>
<scope>test</scope>
</dependency>

<!-- compile dependencies -->

<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-core</artifactId>
<version>${spring.version}</version>
</dependency>
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-web</artifactId>
<version>${spring.version}</version>
</dependency>
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-webmvc</artifactId>
<version>${spring.version}</version>
</dependency>
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-context</artifactId>
<version>${spring.version}</version>
</dependency>

<!-- provided dependencies -->

<dependency>
<groupId>javax.servlet</groupId>
<artifactId>javax.servlet-api</artifactId>
<version>3.1.0</version>
<scope>provided</scope>
</dependency>

<dependency>
<groupId>javax.servlet</groupId>
<artifactId>jstl</artifactId>
<version>1.2</version>
</dependency>

<!-- https://mvnrepository.com/artifact/ch.qos.logback/logback-classic -->
<dependency>
<groupId>ch.qos.logback</groupId>
<artifactId>logback-classic</artifactId>
<version>1.2.3</version>
</dependency>

</dependencies>

<!-- <distributionManagement>
<repository>
<id>nexus</id>
<name>Mithun Technologies Releases Nexus Repository</name>
<url>http://13.235.8.113:8081/repository/flipkart-release/</url>
</repository>
<snapshotRepository>
<id>nexus</id>
<name>Mithun Technologies Snapshot Nexus Repository </name>
<url>http://13.235.8.113:8081/repository/flipkart-snapshot/</url>
</snapshotRepository>
</distributionManagement> -->

<build>
<plugins>
<plugin>
<groupId>org.apache.maven.plugins</groupId>
<artifactId>maven-compiler-plugin</artifactId>
<version>2.5.1</version>
<inherited>true</inherited>
<configuration>
<source>1.8</source>
<target>1.8</target>
</configuration>
</plugin>
</plugins>
</build>


</project>
"""


def test_maven_parser():
    """Tests the Maven parser for pom.xml files."""
    parser = MavenParser()
    expected_dependencies = [
        "spring",
        "junit",
        "spring-test",
        "mockito-core",
        "spring-core",
        "spring-web",
        "spring-webmvc",
        "spring-context",
        "javax.servlet-api",
        "jstl",
        "logback-classic",
    ]
    assert sorted(parser.parse(content)) == sorted(expected_dependencies)


def test_maven_parser_exception_handling():
    """Test the Maven parser's exception handling."""
    parser = MavenParser()

    with patch("re.compile") as mock_compile:
        mock_compile.side_effect = re.error("Test Exception")
        with patch.object(parser, "handle_parsing_error") as mock_handle:
            parser.parse(content)
            mock_handle.assert_called_once_with("pom.xml: Test Exception")
