#!/usr/bin/env bash
filename="$1"
output_path="$2"
clicks_dir="$3"

java KeysToJSON "${filename}" "${output_path}"
java ClicksToJSON "${clicks_dir}" "${output_path}"