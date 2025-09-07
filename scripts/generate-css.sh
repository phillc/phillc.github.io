#!/usr/bin/env bash

set -euxo pipefail

pushd themes/blowfish
npm ci
popd

./themes/blowfish/node_modules/@tailwindcss/cli/dist/index.mjs -c ./themes/blowfish/tailwind.config.js -i ./themes/blowfish/assets/css/main.css -o ./assets/css/compiled/main.css --jit