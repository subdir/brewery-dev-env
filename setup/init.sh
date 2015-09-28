#!/bin/bash

set -e
set -o pipefail

apt-get update
apt-get install --yes --no-install-recommends sudo runit
echo "user ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/user

