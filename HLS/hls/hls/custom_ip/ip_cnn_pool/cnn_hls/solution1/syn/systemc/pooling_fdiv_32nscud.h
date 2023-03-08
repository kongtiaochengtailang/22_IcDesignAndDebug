// ==============================================================
// File generated on Thu Jan 19 10:47:49 +0800 2023
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2018.3 (64-bit)
// SW Build 2405991 on Thu Dec  6 23:38:27 MST 2018
// IP Build 2404404 on Fri Dec  7 01:43:56 MST 2018
// Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __pooling_fdiv_32nscud__HH__
#define __pooling_fdiv_32nscud__HH__
#include "ACMP_fdiv.h"
#include <systemc>

template<
    int ID,
    int NUM_STAGE,
    int din0_WIDTH,
    int din1_WIDTH,
    int dout_WIDTH>
SC_MODULE(pooling_fdiv_32nscud) {
    sc_core::sc_in_clk clk;
    sc_core::sc_in<sc_dt::sc_logic> reset;
    sc_core::sc_in<sc_dt::sc_logic> ce;
    sc_core::sc_in< sc_dt::sc_lv<din0_WIDTH> >   din0;
    sc_core::sc_in< sc_dt::sc_lv<din1_WIDTH> >   din1;
    sc_core::sc_out< sc_dt::sc_lv<dout_WIDTH> >   dout;



    ACMP_fdiv<ID, 16, din0_WIDTH, din1_WIDTH, dout_WIDTH> ACMP_fdiv_U;

    SC_CTOR(pooling_fdiv_32nscud):  ACMP_fdiv_U ("ACMP_fdiv_U") {
        ACMP_fdiv_U.clk(clk);
        ACMP_fdiv_U.reset(reset);
        ACMP_fdiv_U.ce(ce);
        ACMP_fdiv_U.din0(din0);
        ACMP_fdiv_U.din1(din1);
        ACMP_fdiv_U.dout(dout);

    }

};

#endif //
