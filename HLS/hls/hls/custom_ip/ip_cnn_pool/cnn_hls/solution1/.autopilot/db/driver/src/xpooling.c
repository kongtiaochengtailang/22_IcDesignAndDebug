// ==============================================================
// File generated on Thu Jan 19 10:47:49 +0800 2023
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2018.3 (64-bit)
// SW Build 2405991 on Thu Dec  6 23:38:27 MST 2018
// IP Build 2404404 on Fri Dec  7 01:43:56 MST 2018
// Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
// ==============================================================
/***************************** Include Files *********************************/
#include "xpooling.h"

/************************** Function Implementation *************************/
#ifndef __linux__
int XPooling_CfgInitialize(XPooling *InstancePtr, XPooling_Config *ConfigPtr) {
    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(ConfigPtr != NULL);

    InstancePtr->Axilites_BaseAddress = ConfigPtr->Axilites_BaseAddress;
    InstancePtr->IsReady = XIL_COMPONENT_IS_READY;

    return XST_SUCCESS;
}
#endif

void XPooling_Start(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_AP_CTRL) & 0x80;
    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_AP_CTRL, Data | 0x01);
}

u32 XPooling_IsDone(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_AP_CTRL);
    return (Data >> 1) & 0x1;
}

u32 XPooling_IsIdle(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_AP_CTRL);
    return (Data >> 2) & 0x1;
}

u32 XPooling_IsReady(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_AP_CTRL);
    // check ap_start to see if the pcore is ready for next input
    return !(Data & 0x1);
}

void XPooling_EnableAutoRestart(XPooling *InstancePtr) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_AP_CTRL, 0x80);
}

void XPooling_DisableAutoRestart(XPooling *InstancePtr) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_AP_CTRL, 0);
}

void XPooling_Set_CHin_V(XPooling *InstancePtr, u32 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_CHIN_V_DATA, Data);
}

u32 XPooling_Get_CHin_V(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_CHIN_V_DATA);
    return Data;
}

void XPooling_Set_Hin_V(XPooling *InstancePtr, u32 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_HIN_V_DATA, Data);
}

u32 XPooling_Get_Hin_V(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_HIN_V_DATA);
    return Data;
}

void XPooling_Set_Win_V(XPooling *InstancePtr, u32 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_WIN_V_DATA, Data);
}

u32 XPooling_Get_Win_V(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_WIN_V_DATA);
    return Data;
}

void XPooling_Set_Kx_V(XPooling *InstancePtr, u32 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_KX_V_DATA, Data);
}

u32 XPooling_Get_Kx_V(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_KX_V_DATA);
    return Data;
}

void XPooling_Set_Ky_V(XPooling *InstancePtr, u32 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_KY_V_DATA, Data);
}

u32 XPooling_Get_Ky_V(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_KY_V_DATA);
    return Data;
}

void XPooling_Set_Sc_V(XPooling *InstancePtr, u32 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_SC_V_DATA, Data);
}

u32 XPooling_Get_Sc_V(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_SC_V_DATA);
    return Data;
}

void XPooling_Set_Sx_V(XPooling *InstancePtr, u32 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_SX_V_DATA, Data);
}

u32 XPooling_Get_Sx_V(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_SX_V_DATA);
    return Data;
}

void XPooling_Set_Sy_V(XPooling *InstancePtr, u32 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_SY_V_DATA, Data);
}

u32 XPooling_Get_Sy_V(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_SY_V_DATA);
    return Data;
}

void XPooling_Set_mode_V(XPooling *InstancePtr, u32 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_MODE_V_DATA, Data);
}

u32 XPooling_Get_mode_V(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_MODE_V_DATA);
    return Data;
}

void XPooling_Set_feature_in(XPooling *InstancePtr, u32 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_FEATURE_IN_DATA, Data);
}

u32 XPooling_Get_feature_in(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_FEATURE_IN_DATA);
    return Data;
}

void XPooling_Set_feature_out(XPooling *InstancePtr, u32 Data) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_FEATURE_OUT_DATA, Data);
}

u32 XPooling_Get_feature_out(XPooling *InstancePtr) {
    u32 Data;

    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Data = XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_FEATURE_OUT_DATA);
    return Data;
}

void XPooling_InterruptGlobalEnable(XPooling *InstancePtr) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_GIE, 1);
}

void XPooling_InterruptGlobalDisable(XPooling *InstancePtr) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_GIE, 0);
}

void XPooling_InterruptEnable(XPooling *InstancePtr, u32 Mask) {
    u32 Register;

    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Register =  XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_IER);
    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_IER, Register | Mask);
}

void XPooling_InterruptDisable(XPooling *InstancePtr, u32 Mask) {
    u32 Register;

    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    Register =  XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_IER);
    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_IER, Register & (~Mask));
}

void XPooling_InterruptClear(XPooling *InstancePtr, u32 Mask) {
    Xil_AssertVoid(InstancePtr != NULL);
    Xil_AssertVoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    XPooling_WriteReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_ISR, Mask);
}

u32 XPooling_InterruptGetEnabled(XPooling *InstancePtr) {
    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    return XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_IER);
}

u32 XPooling_InterruptGetStatus(XPooling *InstancePtr) {
    Xil_AssertNonvoid(InstancePtr != NULL);
    Xil_AssertNonvoid(InstancePtr->IsReady == XIL_COMPONENT_IS_READY);

    return XPooling_ReadReg(InstancePtr->Axilites_BaseAddress, XPOOLING_AXILITES_ADDR_ISR);
}

