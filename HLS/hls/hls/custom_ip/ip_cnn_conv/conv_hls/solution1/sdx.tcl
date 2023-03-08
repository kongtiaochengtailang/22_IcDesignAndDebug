# ==============================================================
# File generated on Tue Feb 05 22:46:40 +0800 2019
# Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2018.3 (64-bit)
# SW Build 2405991 on Thu Dec  6 23:38:27 MST 2018
# IP Build 2404404 on Fri Dec  7 01:43:56 MST 2018
# Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
# ==============================================================
add_files -tb ../../../../../googledownload/hls_for_cnn_mnist-main/hls_for_cnn_mnist-main/conv_core_hls/main.cpp -cflags { -Wno-unknown-pragmas}
add_files ../../Fpga-accelerator-demos-main/Fpga-accelerator-demos-main/conv_core.cpp
add_files ../../Fpga-accelerator-demos-main/Fpga-accelerator-demos-main/conv_core.h
set_part xc7z020clg400-1
create_clock -name default -period 10
config_export -format=ip_catalog
config_export -rtl=verilog
