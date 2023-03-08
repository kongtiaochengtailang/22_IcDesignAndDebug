############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 1986-2018 Xilinx, Inc. All Rights Reserved.
############################################################
open_project cnn_hls
set_top pooling
add_files ../../Fpga-accelerator-demos-main/Fpga-accelerator-demos-main/conv_core.cpp
add_files ../../Fpga-accelerator-demos-main/Fpga-accelerator-demos-main/conv_core.h
add_files ../../Fpga-accelerator-demos-main/Fpga-accelerator-demos-main/pooling.cpp
add_files ../../Fpga-accelerator-demos-main/Fpga-accelerator-demos-main/pooling.h
add_files -tb ../../../googledownload/hls_for_cnn_mnist-main/hls_for_cnn_mnist-main/conv_core_hls/main.cpp -cflags "-Wno-unknown-pragmas"
open_solution "solution1"
set_part {xc7z020clg400-1} -tool vivado
create_clock -period 10 -name default
config_export -format ip_catalog -rtl verilog
source "./cnn_hls/solution1/directives.tcl"
csim_design
csynth_design
cosim_design
export_design -rtl verilog -format ip_catalog
