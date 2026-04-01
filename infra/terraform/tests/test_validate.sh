#!/bin/bash
set -e
cd ../
terraform init -backend=false
terraform validate
