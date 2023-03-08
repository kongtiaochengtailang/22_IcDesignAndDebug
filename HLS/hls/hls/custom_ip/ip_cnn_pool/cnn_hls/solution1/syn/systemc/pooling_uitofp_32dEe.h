// ==============================================================
// File generated on Thu Jan 19 10:47:49 +0800 2023
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2018.3 (64-bit)
// SW Build 2405991 on Thu Dec  6 23:38:27 MST 2018
// IP Build 2404404 on Fri Dec  7 01:43:56 MST 2018
// Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __pooling_uitofp_32dEe__HH__
#define __pooling_uitofp_32dEe__HH__
#include "ACMP_uitofp.h"
#include <systemc>

template<
    int ID,
    int NUM_STAGE,
    int din0_WIDTH,
    int dout_WIDTH>
SC_MODULE(pooling_uitofp_32dEe) {
    sc_core::sc_in_clk clk;
    sc_core::sc_in<sc_dt::sc_logic> reset;
    sc_core::sc_in<sc_dt::sc_logic> ce;
    sc_core::sc_in< sc_dt::sc_lv<din0_WIDTH> >   din0;
    sc_core::sc_out< sc_dt::sc_lv<dout_WIDTH> >   dout;



    ACMP_uitofp<ID, 6, din0_WIDTH, dout_WIDTH> ACMP_uitofp_U;

    SC_CTOR(pooling_uitofp_32dEe):  ACMP_uitofp_U ("ACMP_uitofp_U") {
        ACMP_uitofp_U.clk(clk);
        ACMP_uitofp_U.reset(reset);
        ACMP_uitofp_U.ce(ce);
        ACMP_uitofp_U.din0(din0);
        ACMP_uitofp_U.dout(dout);

    }

};

#endif //
