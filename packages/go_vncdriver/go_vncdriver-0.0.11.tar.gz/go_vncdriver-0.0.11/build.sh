#!/bin/sh

# Builds against your current Python version. You must have numpy installed.

set -ex

cd "$(dirname "$0")"

# Clear .build
rm -rf .build
trap 'rm -rf .build' EXIT

mkdir -p .build/src/github.com/openai/gym-vnc
ln -s ../../../../.. .build/src/github.com/openai/gym-vnc/go-vncdriver
ln -s ../../../vendor/github.com/go-gl .build/src/github.com
ln -s ../../../vendor/github.com/op .build/src/github.com
ln -s ../../../vendor/github.com/juju .build/src/github.com

export GOPATH="$(pwd)/.build"
export CGO_CFLAGS=$(
    python -c "import numpy, sysconfig
print('-I{} -I{}\n'.format(numpy.get_include(), sysconfig.get_config_var('INCLUDEPY')))"
)
export CGO_LDFLAGS=$(python -c "import re, sysconfig;
library = sysconfig.get_config_var('LIBRARY')
match = re.search('^lib(.*)\.a', library)
if match is None:
  raise RuntimeError('Could not parse LIBRARY: {}'.format(library))
print('-L{} -l{}\n'.format(sysconfig.get_config_var('LIBDIR'), match.group(1)))
")

cd "$(pwd)/.build/src/github.com/openai/gym-vnc/go-vncdriver"
go build -buildmode=c-shared -o go_vncdriver.so
