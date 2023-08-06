#!/usr/bin/env bash
pcap_filename="$1"
output_path="$2"

java NetworkDataParser "${pcap_filename}" "${output_path}"