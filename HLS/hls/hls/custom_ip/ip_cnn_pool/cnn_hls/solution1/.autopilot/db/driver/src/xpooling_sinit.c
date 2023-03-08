// ==============================================================
// File generated on Thu Jan 19 10:47:49 +0800 2023
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2018.3 (64-bit)
// SW Build 2405991 on Thu Dec  6 23:38:27 MST 2018
// IP Build 2404404 on Fri Dec  7 01:43:56 MST 2018
// Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __linux__

#include "xstatus.h"
#include "xparameters.h"
#include "xpooling.h"

extern XPooling_Config XPooling_ConfigTable[];

XPooling_Config *XPooling_LookupConfig(u16 DeviceId) {
	XPooling_Config *ConfigPtr = NULL;

	int Index;

	for (Index = 0; Index < XPAR_XPOOLING_NUM_INSTANCES; Index++) {
		if (XPooling_ConfigTable[Index].DeviceId == DeviceId) {
			ConfigPtr = &XPooling_ConfigTable[Index];
			break;
		}
	}

	return ConfigPtr;
}

int XPooling_Initialize(XPooling *InstancePtr, u16 DeviceId) {
	XPooling_Config *ConfigPtr;

	Xil_AssertNonvoid(InstancePtr != NULL);

	ConfigPtr = XPooling_LookupConfig(DeviceId);
	if (ConfigPtr == NULL) {
		InstancePtr->IsReady = 0;
		return (XST_DEVICE_NOT_FOUND);
	}

	return XPooling_CfgInitialize(InstancePtr, ConfigPtr);
}

#endif

