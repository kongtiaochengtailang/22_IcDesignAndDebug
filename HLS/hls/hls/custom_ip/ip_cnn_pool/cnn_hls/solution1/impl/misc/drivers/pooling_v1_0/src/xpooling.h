// ==============================================================
// File generated on Thu Jan 19 10:47:49 +0800 2023
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2018.3 (64-bit)
// SW Build 2405991 on Thu Dec  6 23:38:27 MST 2018
// IP Build 2404404 on Fri Dec  7 01:43:56 MST 2018
// Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef XPOOLING_H
#define XPOOLING_H

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Include Files *********************************/
#ifndef __linux__
#include "xil_types.h"
#include "xil_assert.h"
#include "xstatus.h"
#include "xil_io.h"
#else
#include <stdint.h>
#include <assert.h>
#include <dirent.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <unistd.h>
#include <stddef.h>
#endif
#include "xpooling_hw.h"

/**************************** Type Definitions ******************************/
#ifdef __linux__
typedef uint8_t u8;
typedef uint16_t u16;
typedef uint32_t u32;
#else
typedef struct {
    u16 DeviceId;
    u32 Axilites_BaseAddress;
} XPooling_Config;
#endif

typedef struct {
    u32 Axilites_BaseAddress;
    u32 IsReady;
} XPooling;

/***************** Macros (Inline Functions) Definitions *********************/
#ifndef __linux__
#define XPooling_WriteReg(BaseAddress, RegOffset, Data) \
    Xil_Out32((BaseAddress) + (RegOffset), (u32)(Data))
#define XPooling_ReadReg(BaseAddress, RegOffset) \
    Xil_In32((BaseAddress) + (RegOffset))
#else
#define XPooling_WriteReg(BaseAddress, RegOffset, Data) \
    *(volatile u32*)((BaseAddress) + (RegOffset)) = (u32)(Data)
#define XPooling_ReadReg(BaseAddress, RegOffset) \
    *(volatile u32*)((BaseAddress) + (RegOffset))

#define Xil_AssertVoid(expr)    assert(expr)
#define Xil_AssertNonvoid(expr) assert(expr)

#define XST_SUCCESS             0
#define XST_DEVICE_NOT_FOUND    2
#define XST_OPEN_DEVICE_FAILED  3
#define XIL_COMPONENT_IS_READY  1
#endif

/************************** Function Prototypes *****************************/
#ifndef __linux__
int XPooling_Initialize(XPooling *InstancePtr, u16 DeviceId);
XPooling_Config* XPooling_LookupConfig(u16 DeviceId);
int XPooling_CfgInitialize(XPooling *InstancePtr, XPooling_Config *ConfigPtr);
#else
int XPooling_Initialize(XPooling *InstancePtr, const char* InstanceName);
int XPooling_Release(XPooling *InstancePtr);
#endif

void XPooling_Start(XPooling *InstancePtr);
u32 XPooling_IsDone(XPooling *InstancePtr);
u32 XPooling_IsIdle(XPooling *InstancePtr);
u32 XPooling_IsReady(XPooling *InstancePtr);
void XPooling_EnableAutoRestart(XPooling *InstancePtr);
void XPooling_DisableAutoRestart(XPooling *InstancePtr);

void XPooling_Set_CHin_V(XPooling *InstancePtr, u32 Data);
u32 XPooling_Get_CHin_V(XPooling *InstancePtr);
void XPooling_Set_Hin_V(XPooling *InstancePtr, u32 Data);
u32 XPooling_Get_Hin_V(XPooling *InstancePtr);
void XPooling_Set_Win_V(XPooling *InstancePtr, u32 Data);
u32 XPooling_Get_Win_V(XPooling *InstancePtr);
void XPooling_Set_Kx_V(XPooling *InstancePtr, u32 Data);
u32 XPooling_Get_Kx_V(XPooling *InstancePtr);
void XPooling_Set_Ky_V(XPooling *InstancePtr, u32 Data);
u32 XPooling_Get_Ky_V(XPooling *InstancePtr);
void XPooling_Set_Sc_V(XPooling *InstancePtr, u32 Data);
u32 XPooling_Get_Sc_V(XPooling *InstancePtr);
void XPooling_Set_Sx_V(XPooling *InstancePtr, u32 Data);
u32 XPooling_Get_Sx_V(XPooling *InstancePtr);
void XPooling_Set_Sy_V(XPooling *InstancePtr, u32 Data);
u32 XPooling_Get_Sy_V(XPooling *InstancePtr);
void XPooling_Set_mode_V(XPooling *InstancePtr, u32 Data);
u32 XPooling_Get_mode_V(XPooling *InstancePtr);
void XPooling_Set_feature_in(XPooling *InstancePtr, u32 Data);
u32 XPooling_Get_feature_in(XPooling *InstancePtr);
void XPooling_Set_feature_out(XPooling *InstancePtr, u32 Data);
u32 XPooling_Get_feature_out(XPooling *InstancePtr);

void XPooling_InterruptGlobalEnable(XPooling *InstancePtr);
void XPooling_InterruptGlobalDisable(XPooling *InstancePtr);
void XPooling_InterruptEnable(XPooling *InstancePtr, u32 Mask);
void XPooling_InterruptDisable(XPooling *InstancePtr, u32 Mask);
void XPooling_InterruptClear(XPooling *InstancePtr, u32 Mask);
u32 XPooling_InterruptGetEnabled(XPooling *InstancePtr);
u32 XPooling_InterruptGetStatus(XPooling *InstancePtr);

#ifdef __cplusplus
}
#endif

#endif
