#!/bin/bash
sphinx-apidoc -f -o source ../../models -t _templates
make clean html