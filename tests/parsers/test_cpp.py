"""Unit tests for C/C++ parsers."""

import pytest

from readmeai.parsers.cpp import (
    CMakeParser,
    ConfigureAcParser,
    MakefileAmParser,
)

cmake_file = """
cmake_minimum_required(VERSION 2.8.12)

# Set extension name here
set(TARGET_NAME arrow)

set(EXTENSION_NAME ${TARGET_NAME}_extension)
project(${TARGET_NAME})
include_directories(src/include)

set(EXTENSION_SOURCES
        src/arrow_extension.cpp
        src/arrow_stream_buffer.cpp
        src/arrow_scan_ipc.cpp
        src/arrow_to_ipc.cpp)

if(NOT "${OSX_BUILD_ARCH}" STREQUAL "")
    set(OSX_ARCH_FLAG -DCMAKE_OSX_ARCHITECTURES=${OSX_BUILD_ARCH})
else()
    set(OSX_ARCH_FLAG "")
endif()

# Building Arrow
include(ExternalProject)
ExternalProject_Add(
        ARROW_EP
        GIT_REPOSITORY "https://github.com/apache/arrow"
        GIT_TAG ea6875fd2a3ac66547a9a33c5506da94f3ff07f2
        PREFIX "${CMAKE_BINARY_DIR}/third_party/arrow"
        INSTALL_DIR "${CMAKE_BINARY_DIR}/third_party/arrow/install"
        BUILD_BYPRODUCTS <INSTALL_DIR>/lib/libarrow.a
        CONFIGURE_COMMAND
        ${CMAKE_COMMAND} -G${CMAKE_GENERATOR} ${OSX_ARCH_FLAG}
        -DCMAKE_BUILD_TYPE=Release
        -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/third_party/arrow/install
        -DCMAKE_INSTALL_LIBDIR=lib -DARROW_BUILD_STATIC=ON -DARROW_BUILD_SHARED=OFF
        -DARROW_NO_DEPRECATED_API=ON -DARROW_POSITION_INDEPENDENT_CODE=ON
        -DARROW_SIMD_LEVEL=NONE -DARROW_ENABLE_TIMING_TESTS=OFF -DARROW_IPC=ON
        -DARROW_JEMALLOC=OFF -DARROW_DEPENDENCY_SOURCE=BUNDLED
        -DARROW_VERBOSE_THIRDPARTY_BUILD=OFF -DARROW_DEPENDENCY_USE_SHARED=OFF
        -DARROW_BOOST_USE_SHARED=OFF -DARROW_BROTLI_USE_SHARED=OFF
        -DARROW_BZ2_USE_SHARED=OFF -DARROW_GFLAGS_USE_SHARED=OFF
        -DARROW_GRPC_USE_SHARED=OFF -DARROW_JEMALLOC_USE_SHARED=OFF
        -DARROW_LZ4_USE_SHARED=OFF -DARROW_OPENSSL_USE_SHARED=OFF
        -DARROW_PROTOBUF_USE_SHARED=OFF -DARROW_SNAPPY_USE_SHARED=OFF
        -DARROW_THRIFT_USE_SHARED=OFF -DARROW_UTF8PROC_USE_SHARED=OFF
        -DARROW_ZSTD_USE_SHARED=OFF -DARROW_USE_GLOG=OFF -DARROW_WITH_BACKTRACE=OFF
        -DARROW_WITH_OPENTELEMETRY=OFF -DARROW_WITH_BROTLI=OFF -DARROW_WITH_BZ2=OFF
        -DARROW_WITH_LZ4=OFF -DARROW_WITH_SNAPPY=OFF -DARROW_WITH_ZLIB=OFF
        -DARROW_WITH_ZSTD=OFF -DARROW_WITH_UCX=OFF -DARROW_WITH_UTF8PROC=OFF
        -DARROW_WITH_RE2=OFF <SOURCE_DIR>/cpp
        CMAKE_ARGS -Wno-dev
        UPDATE_COMMAND "")

ExternalProject_Get_Property(ARROW_EP install_dir)
add_library(arrow STATIC IMPORTED GLOBAL)
if(WIN32)
    set_target_properties(arrow PROPERTIES IMPORTED_LOCATION ${install_dir}/lib/arrow_static.lib)
else()
    set_target_properties(arrow PROPERTIES IMPORTED_LOCATION ${install_dir}/lib/libarrow.a)
endif()

# create static library
add_library(${EXTENSION_NAME} STATIC ${EXTENSION_SOURCES})
add_dependencies(${EXTENSION_NAME} ARROW_EP)
target_link_libraries(${EXTENSION_NAME} PUBLIC arrow)
target_include_directories(${EXTENSION_NAME} PRIVATE ${install_dir}/include)

# create loadable extension
set(PARAMETERS "-warnings")
build_loadable_extension(${TARGET_NAME} ${PARAMETERS} ${EXTENSION_SOURCES})
add_dependencies(${TARGET_NAME}_loadable_extension ARROW_EP)
target_link_libraries(${TARGET_NAME}_loadable_extension arrow)
if(WIN32)
    target_compile_definitions(${TARGET_NAME}_loadable_extension PUBLIC ARROW_STATIC)
endif()
target_include_directories(${TARGET_NAME}_loadable_extension PRIVATE ${install_dir}/include)

install(
        TARGETS ${EXTENSION_NAME}
        EXPORT "${DUCKDB_EXPORT_SET}"
        LIBRARY DESTINATION "${INSTALL_LIB_DIR}"
        ARCHIVE DESTINATION "${INSTALL_LIB_DIR}")
"""

SAMPLE_CONTENT_CMAKELISTSTXT = """
find_package(Qt5Widgets REQUIRED)
find_package(Boost COMPONENTES system thread filesystem)
add_executable(main main.cpp)
target_link_libraries(main Qt5::Widgets Boost::system Boost::thread Boost::filesystem)"""

SAMPLE_CONTENT_CONFIGUREAC = """
AC_PROG_CC
AC_PROG_RANLIB
AC_PATH_XSPELL
AC_CHECK_HEADER(stdc-predefined.h, AC_FAIL("Need stdc-predefined.h"))
AC_CHECK_HEADERS([time.h sys/types.h],[])
AC_CHECK_LIBS([m pthread dl rt clock_gettime gmon mp],[],
              [AX_BOOST_REQUIRE_LIBRARY(threads, [], [have_pthread_mutexattr_setpshared])])
"""

SAMPLE_CONTENT_MAKEFILEAM = """
bin_PROGRAMS = my_program
my_program_SOURCES = main.c utils.c
noinst_LTLIBRARIES = libfoo.la
libfoo_la_LDFLAGS = -module -avoid-version
libfoo_la_SOURCES = foo.c bar.c baz.c
nobase_include_HEADERS = header.h
check_PROGRAMS = check
check_SOURCES = check.c
EXTRA_DIST = doc/*.png
dist_doc_DATA = $(wildcard doc/*.html)
BUILT_SOURCES = stamp-vti
CLEANFILES += $(srcdir)/Makefile.in
MOSTLYCLEANFILES += Makefile.in
"""


def test_cmake_parser():
    """Test the CMake parser."""
    parser = CMakeParser()
    expected = "arrow"
    result = parser.parse(cmake_file)
    assert expected in result


@pytest.fixture
def cmake_parser():
    return CMakeParser()


@pytest.fixture
def makefile_am_parser():
    return MakefileAmParser()


@pytest.fixture
def configureac_parser():
    return ConfigureAcParser()


@pytest.fixture
def content_cmakelists(tmp_path):
    cmakelists_file = tmp_path / "CMakeLists.txt"
    cmakelists_file.write_text(SAMPLE_CONTENT_CMAKELISTSTXT)
    return cmakelists_file


@pytest.fixture
def content_configureac(tmp_path):
    configureac_file = tmp_path / "configure.ac"
    configureac_file.write_text(SAMPLE_CONTENT_CONFIGUREAC)
    return configureac_file


@pytest.fixture
def content_makefileam(tmp_path):
    makefileam_file = tmp_path / "Makefile.am"
    makefileam_file.write_text(SAMPLE_CONTENT_MAKEFILEAM)
    return makefileam_file


def test_cmake_parser_valid(cmake_parser, content_cmakelists):
    extracted_dependencies = cmake_parser.parse(content_cmakelists.read_text())
    """
    expected_dependencies = [
        "Qt5Widgets",
        "Boost::system",
        "Boost::thread",
        "Boost::filesystem",
    ]
    """
    assert "Qt5Widgets" in extracted_dependencies


def test_cmake_parser_invalid(cmake_parser):
    extracted_dependencies = cmake_parser.parse("Invalid Content")
    assert extracted_dependencies == []


@pytest.mark.skip
def test_configureac_parser_valid(configureac_parser, content_configureac):
    extracted_packages = configureac_parser.parse(
        content_configureac.read_text(),
    )
    expected_packages = ["mp", "clock_gettime", "rt", "dl", "pthread"]
    assert sorted(extracted_packages) == sorted(expected_packages)


def test_configureac_parser_invalid(configureac_parser):
    extracted_packages = configureac_parser.parse("Invalid Content")
    assert extracted_packages == []


def test_makefile_am_parser_valid(makefile_am_parser, content_makefileam):
    extracted_packages = makefile_am_parser.parse(
        content_makefileam.read_text(),
    )
    # expected_packages = ["my_program", "libfoo", "check"]
    assert "my_program" in extracted_packages


def test_makefile_am_parser_invalid(makefile_am_parser):
    extracted_packages = makefile_am_parser.parse("Invalid Content")
    assert extracted_packages == []
