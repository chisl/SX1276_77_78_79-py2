#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""SX1276_77_78_79: 137 MHz to 1020 MHz Low Power Long Range Transceiver featuring the LoRa (TM) long range modem"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Semtech"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

class REG:
	Fifo = 0
	OpMode = 1
	Fr = 6
	PaConfig = 9
	PaRamp = 10
	Ocp = 11
	Lna = 12
	FifoAddrPtr = 13
	FifoTxBaseAddr = 14
	FifoRxBaseAddr = 15
	FifoRxCurrentAddr = 16
	IrqFlagsMask = 17
	IrqFlags = 18
	RxNbBytes = 19
	RxHeaderCntValue = 20
	RxPacketCntValue = 22
	ModemStat = 24
	PktSnrValue = 25
	PktRssiValue = 26
	RssiValue = 27
	HopChannel = 28
	ModemConfig1 = 29
	ModemConfig2 = 30
	SymbTimeoutLsb = 31
	Preamble = 32
	PayloadLength = 34
	MaxPayloadLength = 35
	HopPeriod = 36
	FifoRxByteAddr = 37
	ModemConfig3 = 38
	PpmCorrection = 39
	Fei = 40
	RssiWideband = 44
	DetectOptimize = 49
	InvertIQ = 51
	DetectionThreshold = 55
	SyncWord = 57
