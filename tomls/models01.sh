#!/bin/sh
python /home/egil/gits_wsl/wl-coref-ncc/run.py train models01_000 --config-file /home/egil/gits_wsl/wl-coref-ncc/tomls/models01.toml
python /home/egil/gits_wsl/wl-coref-ncc/run.py train models01_001 --config-file /home/egil/gits_wsl/wl-coref-ncc/tomls/models01.toml
python /home/egil/gits_wsl/wl-coref-ncc/run.py train models01_002 --config-file /home/egil/gits_wsl/wl-coref-ncc/tomls/models01.toml
python /home/egil/gits_wsl/wl-coref-ncc/run.py train models01_003 --config-file /home/egil/gits_wsl/wl-coref-ncc/tomls/models01.toml