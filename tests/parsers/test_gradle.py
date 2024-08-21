"""Unit tests for parsing build.gradle files."""

from readmeai.parsers.gradle import (
    BuildGradleKtsParser,
    BuildGradleParser,
)

build_gradle = """
buildscript {
    repositories {
        jcenter()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:2.1.0-beta3'
        classpath 'com.github.dcendents:android-maven-gradle-plugin:1.3'
        classpath "com.jfrog.bintray.gradle:gradle-bintray-plugin:1.1"

        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }
}

allprojects {
    repositories {
        jcenter()
    }
}

ext {
    compileSdkVersion = 22
    buildToolsVersion = '22.0.1'
    targetSdkVersion = 22
    minSdkVersion = 16
    versionCode = 28
    versionName = "0.3.2"
}
"""

build_gradle_kts = """
plugins {
    id("com.android.test")
    id("kotlin-android")
}

android {
    compileSdk = 31

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }

    defaultConfig {
        minSdk = 29
        targetSdk = 30

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        // This benchmark buildType is used for benchmarking, and should function like your
        // release build (for example, with minification on). It's signed with a debug key
        // for easy local/CI testing.
        create("benchmark") {
            isDebuggable = true
            signingConfig = signingConfigs.getByName("debug")
        }
    }

    targetProjectPath = ":wearApp"
    namespace = "com.surrus.peopleinspace.benchmark"
    experimentalProperties["android.experimental.self-instrumenting"] = true

    variantFilter {
        if (buildType.name.contains("release") || buildType.name.contains("debug")) {
            ignore = true
        }
    }
}

dependencies {

    implementation("androidx.benchmark:benchmark-macro-junit4:1.2.2")
    implementation("androidx.benchmark:benchmark-junit4:1.2.2")
    implementation("androidx.test.espresso:espresso-core:3.5.1")
    implementation("androidx.test.ext:junit:1.1.5")
    implementation("androidx.test.uiautomator:uiautomator:2.2.0")
}

androidComponents {
    beforeVariants(selector().all()) { variant ->
        variant.enable = variant.buildType == "benchmark"
    }
}
"""


def test_build_gradle():
    """Test parsing build.gradle files."""
    parser = BuildGradleParser()
    dependencies = parser.parse(build_gradle)
    assert sorted(dependencies) == sorted(
        [
            "android",
            "bintray",
            "build",
            "com",
            "dcendents",
            "github",
            "gradle",
            "jfrog",
            "tools",
        ],
    )


def test_build_gradle_kts():
    """Test parsing build.gradle.kts files."""
    parser = BuildGradleKtsParser()
    dependencies = parser.parse(build_gradle_kts)
    assert sorted(dependencies) == sorted(
        [
            "junit",
            "test",
            "uiautomator",
            "espresso",
            "ext",
            "androidx",
            "benchmark",
        ],
    )
