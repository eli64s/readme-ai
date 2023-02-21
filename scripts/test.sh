#!/bin/bash

conda activate myenv

pytest --verbose --junitxml=report.xml

conda deactivate