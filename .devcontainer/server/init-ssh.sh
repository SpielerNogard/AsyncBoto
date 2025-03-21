#!/bin/sh
set -e

# Copy generated keys
mkdir -p $HOME/.ssh
cat /server/temp-ssh-key.pub > $HOME/.ssh/authorized_keys
chmod 644 $HOME/.ssh/authorized_keys
chmod 700 $HOME/.ssh