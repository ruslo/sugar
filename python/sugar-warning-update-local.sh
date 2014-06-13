#!/bin/bash -e

set -x

./sugar-generate-warnings.py

trash.py ${GITENV_ROOT}/ruslo/leathers/Source/leathers
mkdir ${GITENV_ROOT}/ruslo/leathers/Source/leathers

mv leathers/* ${GITENV_ROOT}/ruslo/leathers/Source/leathers

rmdir leathers

rm wiki-table.txt

mv sugar_generate_warning_flag_by_name.cmake ../cmake/utility/

git status
