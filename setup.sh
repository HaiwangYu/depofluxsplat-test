#!/bin/bash

source ~/.bash_profile

source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
setup dunesw v10_04_07d01 -q e26:prof

path-prepend /exp/dune/app/users/yuhw/opt/lib64 LD_LIBRARY_PATH
path-prepend /exp/dune/data/users/sergeym/PDHD_data_DNNROI/largeSample/test/wire-cell-cfg WIRECELL_PATH
