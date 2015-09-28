#!/bin/bash

set -e
set -o pipefail

if ! [[ -v DEVENV ]]; then
    rm -f /etc/sudoers.d/user
fi

