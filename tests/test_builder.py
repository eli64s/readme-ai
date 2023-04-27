"""Unit tests for the builder module."""

import os
import tempfile
from pathlib import Path

import pandas as pd
import pytest

from src.builder import build, create_directory_tree, create_tables, get_badges
