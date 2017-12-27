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

from SX1276_77_78_79_constants import *

# name:        SX1276_77_78_79
# description: 137 MHz to 1020 MHz Low Power Long Range Transceiver featuring the LoRa (TM) long range modem
# manuf:       Semtech
# version:     0.1
# url:         http://www.semtech.com/images/datasheet/sx1276_77_78_79.pdf
# date:        2016-08-01


# Derive from this class and implement read and write
class SX1276_77_78_79_Base:
	"""137 MHz to 1020 MHz Low Power Long Range Transceiver featuring the LoRa (TM) long range modem"""
	# Register Fifo
	# LoRaTM base-band FIFO data input/output.
	#       FIFO is cleared an not accessible when device is in SLEEP mode 
	
	
	def setFifo(self, val):
		"""Set register Fifo"""
		self.write(REG.Fifo, val, 8)
	
	def getFifo(self):
		"""Get register Fifo"""
		return self.read(REG.Fifo, 8)
	
	# Bits Fifo
	# Register OpMode
	
	
	def setOpMode(self, val):
		"""Set register OpMode"""
		self.write(REG.OpMode, val, 8)
	
	def getOpMode(self):
		"""Get register OpMode"""
		return self.read(REG.OpMode, 8)
	
	# Bits LongRangeMode
	# 0 = FSK/OOK Mode
	#           1 = LoRaTM Mode
	#           This bit can be modified only in Sleep mode. A write operation on other device modes is ignored. 
	
	# Bits AccessSharedReg
	# This bit operates when device is in Lora mode; if set it allows access to FSK registers page located in address space (0x0D:0x3F) while in LoRa mode
	#           0 = Access LoRa registers page 0x0D: 0x3F
	#           1 = Access FSK registers page (in mode LoRa) 0x0D: 0x3F 
	
	# Bits reserved_0
	# reserved 
	# Bits LowFrequencyModeOn
	# Access Low Frequency Mode registers 
	# Bits Mode
	# Device modes 
	# Register Fr
	# RF carrier frequency
	#       Resolution is 61.035 Hz if F(XOSC) = 32 MHz.
	#       Default value is 0x6c8000 = 434 MHz.
	#       Register values must be modified only when device is in SLEEP or STAND-BY mode. 
	
	
	def setFr(self, val):
		"""Set register Fr"""
		self.write(REG.Fr, val, 24)
	
	def getFr(self):
		"""Get register Fr"""
		return self.read(REG.Fr, 24)
	
	# Bits Fr
	# Register PaConfig
	
	
	def setPaConfig(self, val):
		"""Set register PaConfig"""
		self.write(REG.PaConfig, val, 8)
	
	def getPaConfig(self):
		"""Get register PaConfig"""
		return self.read(REG.PaConfig, 8)
	
	# Bits PaSelect
	# Selects PA output pin 
	# Bits MaxPower
	# Select max output power: Pmax=10.8+0.6*MaxPower [dBm] 
	# Bits OutputPower
	# Pout=Pmax-(15-OutputPower) if PaSelect = 0 (RFO pin)
	#           Pout=17-(15-OutputPower)   if PaSelect = 1 (PA_BOOST pin) 
	
	# Register PaRamp
	
	
	def setPaRamp(self, val):
		"""Set register PaRamp"""
		self.write(REG.PaRamp, val, 8)
	
	def getPaRamp(self):
		"""Get register PaRamp"""
		return self.read(REG.PaRamp, 8)
	
	# Bits unused_0
	# unused 
	# Bits reserved_1
	# Bits PaRamp
	# Rise/Fall time of ramp up/down in FSK 0000 = 3.4 ms 
	# Register Ocp
	
	
	def setOcp(self, val):
		"""Set register Ocp"""
		self.write(REG.Ocp, val, 8)
	
	def getOcp(self):
		"""Get register Ocp"""
		return self.read(REG.Ocp, 8)
	
	# Bits unused_0
	# Bits OcpOn
	# Enables overload current protection (OCP) for PA:
	#           0 = OCP disabled
	#           1 = OCP enabled 
	
	# Bits OcpTrim
	# Trimming of OCP current:
	#           Imax = 45+5*OcpTrim [mA] if OcpTrim <= 15 (120 mA)
	#           Imax = -30+10*OcpTrim [mA] if 15 < OcpTrim <= 27 (130 to 240 mA)
	#           Imax = 240mA for higher settings
	#           Default Imax = 100mA 
	
	# Register Lna
	
	
	def setLna(self, val):
		"""Set register Lna"""
		self.write(REG.Lna, val, 8)
	
	def getLna(self):
		"""Get register Lna"""
		return self.read(REG.Lna, 8)
	
	# Bits LnaGain
	# LNA gain setting:
	#           b000 not used 
	# b111 not used 
	
	# Bits LnaBoostLf
	# Low Frequency (RFI_LF) LNA current adjustment
	#           00 = Default LNA current
	#           Other = Reserved 
	
	# Bits reserved_0
	# Bits LnaBoostHf
	# High Frequency (RFI_HF) LNA current adjustment
	#           0 = Default;     -- Default LNA current
	#           1 = Boost_on; -- Boost on, 150% LNA current 
	
	# Register FifoAddrPtr
	# SPI interface address pointer in FIFO data buffer. 
	
	def setFifoAddrPtr(self, val):
		"""Set register FifoAddrPtr"""
		self.write(REG.FifoAddrPtr, val, 8)
	
	def getFifoAddrPtr(self):
		"""Get register FifoAddrPtr"""
		return self.read(REG.FifoAddrPtr, 8)
	
	# Bits FifoAddrPtr
	# Register FifoTxBaseAddr
	# write base address in FIFO data buffer for TX modulator 
	
	def setFifoTxBaseAddr(self, val):
		"""Set register FifoTxBaseAddr"""
		self.write(REG.FifoTxBaseAddr, val, 8)
	
	def getFifoTxBaseAddr(self):
		"""Get register FifoTxBaseAddr"""
		return self.read(REG.FifoTxBaseAddr, 8)
	
	# Bits FifoTxBaseAddr
	# Register FifoRxBaseAddr
	# read base address in FIFO data buffer for RX demodulator 
	
	def setFifoRxBaseAddr(self, val):
		"""Set register FifoRxBaseAddr"""
		self.write(REG.FifoRxBaseAddr, val, 8)
	
	def getFifoRxBaseAddr(self):
		"""Get register FifoRxBaseAddr"""
		return self.read(REG.FifoRxBaseAddr, 8)
	
	# Bits FifoRxBaseAddr
	# Register FifoRxCurrentAddr
	# Start address (in data buffer) of last packet received 
	
	def setFifoRxCurrentAddr(self, val):
		"""Set register FifoRxCurrentAddr"""
		self.write(REG.FifoRxCurrentAddr, val, 8)
	
	def getFifoRxCurrentAddr(self):
		"""Get register FifoRxCurrentAddr"""
		return self.read(REG.FifoRxCurrentAddr, 8)
	
	# Bits FifoRxCurrentAddr
	# Register IrqFlagsMask
	
	
	def setIrqFlagsMask(self, val):
		"""Set register IrqFlagsMask"""
		self.write(REG.IrqFlagsMask, val, 8)
	
	def getIrqFlagsMask(self):
		"""Get register IrqFlagsMask"""
		return self.read(REG.IrqFlagsMask, 8)
	
	# Bits RxTimeoutMask
	# Timeout interrupt mask: setting this bit masks the corresponding IRQ in RegIrqFlags 
	# Bits RxDoneMask
	# Packet reception complete interrupt mask: setting this bit masks the
	#           corresponding IRQ in RegIrqFlags 
	
	# Bits PayloadCrcErrorMask
	# Payload CRC error interrupt mask: setting this bit masks the
	#           corresponding IRQ in RegIrqFlags 
	
	# Bits ValidHeaderMask
	# Valid header received in Rx mask: setting this bit masks the
	#           corresponding IRQ in RegIrqFlags 
	
	# Bits TxDoneMask
	# FIFO Payload transmission complete interrupt mask: setting this bit masks
	#           the corresponding IRQ in RegIrqFlags 
	
	# Bits CadDoneMask
	# CAD complete interrupt mask: setting this bit masks the corresponding
	#           IRQ in RegIrqFlags 
	
	# Bits FhssChangeChannelMask
	# FHSS change channel interrupt mask: setting this bit masks the
	#           corresponding IRQ in RegIrqFlags 
	
	# Bits CadDetectedMask
	# Cad Detected Interrupt Mask: setting this bit masks the corresponding
	#           IRQ in RegIrqFlags 
	
	# Register IrqFlags
	
	
	def setIrqFlags(self, val):
		"""Set register IrqFlags"""
		self.write(REG.IrqFlags, val, 8)
	
	def getIrqFlags(self):
		"""Get register IrqFlags"""
		return self.read(REG.IrqFlags, 8)
	
	# Bits RxTimeout
	# Timeout interrupt: writing a 1 clears the IRQ 
	# Bits RxDone
	# Packet reception complete interrupt: writing a 1 clears the IRQ 
	# Bits PayloadCrcError
	# Payload CRC error interrupt: writing a 1 clears the IRQ 
	# Bits ValidHeader
	# Valid header received in Rx: writing a 1 clears the IRQ 
	# Bits TxDone
	# FIFO Payload transmission complete interrupt: writing a 1 clears the IRQ 
	# Bits CadDone
	# CAD complete: write to clear: writing a 1 clears the IRQ 
	# Bits FhssChangeChannel
	# FHSS change channel interrupt: writing a 1 clears the IRQ 
	# Bits CadDetected
	# Valid Lora signal detected during CAD operation: writing a 1 clears the IRQ 
	# Register RxNbBytes
	# Number of payload bytes of latest packet received 
	
	def setRxNbBytes(self, val):
		"""Set register RxNbBytes"""
		self.write(REG.RxNbBytes, val, 8)
	
	def getRxNbBytes(self):
		"""Get register RxNbBytes"""
		return self.read(REG.RxNbBytes, 8)
	
	# Bits RxNbBytes
	# Register RxHeaderCntValue
	# Number of valid headers received since last transition into Rx mode.
	#       Header and packet counters are reseted in Sleep mode. 
	
	
	def setRxHeaderCntValue(self, val):
		"""Set register RxHeaderCntValue"""
		self.write(REG.RxHeaderCntValue, val, 16)
	
	def getRxHeaderCntValue(self):
		"""Get register RxHeaderCntValue"""
		return self.read(REG.RxHeaderCntValue, 16)
	
	# Bits RxHeaderCntValue
	# Register RxPacketCntValue
	# Number of valid packets received since last transition into Rx mode.
	#       Header and packet counters are reseted in Sleep mode. 
	
	
	def setRxPacketCntValue(self, val):
		"""Set register RxPacketCntValue"""
		self.write(REG.RxPacketCntValue, val, 16)
	
	def getRxPacketCntValue(self):
		"""Get register RxPacketCntValue"""
		return self.read(REG.RxPacketCntValue, 16)
	
	# Bits RxPacketCntValue
	# Register ModemStat
	
	
	def setModemStat(self, val):
		"""Set register ModemStat"""
		self.write(REG.ModemStat, val, 8)
	
	def getModemStat(self):
		"""Get register ModemStat"""
		return self.read(REG.ModemStat, 8)
	
	# Bits RxCodingRate
	# Coding rate of last header received 
	# Bits ModemClear
	# Modem clear 
	# Bits HeaderInfoValid
	# Header info valid 
	# Bits RxOngoing
	# RX on-going 
	# Bits SignalSynchronized
	# Signal synchronized 
	# Bits SignalDetected
	# Signal detected 
	# Register PktSnrValue
	# Estimation of SNR on last packet received.In two's compliment format mutiplied by 4.
	#       SNR[dB] = PacketSnr[twos complement-] / 4 
	
	
	def setPktSnrValue(self, val):
		"""Set register PktSnrValue"""
		self.write(REG.PktSnrValue, val, 8)
	
	def getPktSnrValue(self):
		"""Get register PktSnrValue"""
		return self.read(REG.PktSnrValue, 8)
	
	# Bits PktSnrValue
	# Register PktRssiValue
	# RSSI of the latest packet received (dBm):
	#       RSSI[dBm] = -157 + Rssi (using HF output port, SNR >= 0) or
	#       RSSI[dBm] = -164 + Rssi (using LF output port, SNR >= 0)
	#       (see section 5.5.5 for details) 
	
	
	def setPktRssiValue(self, val):
		"""Set register PktRssiValue"""
		self.write(REG.PktRssiValue, val, 8)
	
	def getPktRssiValue(self):
		"""Get register PktRssiValue"""
		return self.read(REG.PktRssiValue, 8)
	
	# Bits PktRssiValue
	# Register RssiValue
	# Current RSSI value (dBm)
	#       RSSI[dBm] = -157 + Rssi (using HF output port) or
	#       RSSI[dBm] = -164 + Rssi (using LF output port)
	#       (see section 5.5.5 for details) 
	
	
	def setRssiValue(self, val):
		"""Set register RssiValue"""
		self.write(REG.RssiValue, val, 8)
	
	def getRssiValue(self):
		"""Get register RssiValue"""
		return self.read(REG.RssiValue, 8)
	
	# Bits RssiValue
	# Register HopChannel
	
	
	def setHopChannel(self, val):
		"""Set register HopChannel"""
		self.write(REG.HopChannel, val, 8)
	
	def getHopChannel(self):
		"""Get register HopChannel"""
		return self.read(REG.HopChannel, 8)
	
	# Bits PllTimeout
	# PLL failed to lock while attempting a TX/RX/CAD operation 1 = PLL did not lock
	#           0 = PLL did lock 
	
	# Bits CrcOnPayload
	# CRC Information extracted from the received packet header (Explicit header mode only)
	#           0 = Header indicates CRC off
	#           1 = Header indicates CRC on 
	
	# Bits FhssPresentChannel
	# Current value of frequency hopping channel in use. 
	# Register ModemConfig1
	
	
	def setModemConfig1(self, val):
		"""Set register ModemConfig1"""
		self.write(REG.ModemConfig1, val, 8)
	
	def getModemConfig1(self):
		"""Get register ModemConfig1"""
		return self.read(REG.ModemConfig1, 8)
	
	# Bits BW
	# Signal bandwidth:
	#           In the lower band (169MHz), signal bandwidths 8&9 are not supported) 
	# other values = reserved 
	
	# Bits CodingRate
	# Error coding rate
	#           In implicit header mode should be set on receiver to determine
	#           expected coding rate. See 4.1.1.3 
	# All other values = reserved 
	
	# Bits ImplicitHeaderModeOn
	# 0 = Explicit Header mode
	#           1 = Implicit Header mode 
	
	# Register ModemConfig2
	
	
	def setModemConfig2(self, val):
		"""Set register ModemConfig2"""
		self.write(REG.ModemConfig2, val, 8)
	
	def getModemConfig2(self):
		"""Get register ModemConfig2"""
		return self.read(REG.ModemConfig2, 8)
	
	# Bits SpreadingFactor
	# SF rate (expressed as a base-2 logarithm) 
	# Bits TxContinuousMode
	# 0 = normal mode, a single packet is sent
	#           1 = continuous mode, send multiple packets across the FIFO (used for spectral analysis) 
	
	# Bits RxPayloadCrcOn
	# Enable CRC generation and check on payload: 0 = CRC disable
	#           1 = CRC enable
	#           If CRC is needed, RxPayloadCrcOn should be set:
	#           - in Implicit header mode: on Tx and Rx side
	#           - in Explicit header mode: on the Tx side alone (recovered from the header in Rx side) 
	
	# Bits SymbTimeout
	# RX Time-Out MSB (bits 9:8) 
	# Register SymbTimeoutLsb
	# RX Time-Out LSB
	#       RX operation time-out value expressed as number of symbols:
	#       TimeOut = SymbTimeout / Ts 
	
	
	def setSymbTimeoutLsb(self, val):
		"""Set register SymbTimeoutLsb"""
		self.write(REG.SymbTimeoutLsb, val, 8)
	
	def getSymbTimeoutLsb(self):
		"""Get register SymbTimeoutLsb"""
		return self.read(REG.SymbTimeoutLsb, 8)
	
	# Bits SymbTimeoutLsb
	# Register Preamble
	# Preamble length MSB, = PreambleLength + 4.25 Symbols See 4.1.1 for more details. 
	
	def setPreamble(self, val):
		"""Set register Preamble"""
		self.write(REG.Preamble, val, 16)
	
	def getPreamble(self):
		"""Get register Preamble"""
		return self.read(REG.Preamble, 16)
	
	# Bits Preamble
	# Register PayloadLength
	# Payload length in bytes. The register needs to be set in implicit header
	#       mode for the expected packet length. A 0 value is not permitted 
	
	
	def setPayloadLength(self, val):
		"""Set register PayloadLength"""
		self.write(REG.PayloadLength, val, 8)
	
	def getPayloadLength(self):
		"""Get register PayloadLength"""
		return self.read(REG.PayloadLength, 8)
	
	# Bits PayloadLength
	# Register MaxPayloadLength
	# Maximum payload length; if header payload length exceeds value a header
	#       CRC error is generated. Allows filtering of packet with a bad size. 
	
	
	def setMaxPayloadLength(self, val):
		"""Set register MaxPayloadLength"""
		self.write(REG.MaxPayloadLength, val, 8)
	
	def getMaxPayloadLength(self):
		"""Get register MaxPayloadLength"""
		return self.read(REG.MaxPayloadLength, 8)
	
	# Bits MaxPayloadLength
	# Register HopPeriod
	# Symbol periods between frequency hops. (0 = disabled).
	#       1st hop always happen after the 1st header symbol 
	
	
	def setHopPeriod(self, val):
		"""Set register HopPeriod"""
		self.write(REG.HopPeriod, val, 8)
	
	def getHopPeriod(self):
		"""Get register HopPeriod"""
		return self.read(REG.HopPeriod, 8)
	
	# Bits HopPeriod
	# Register FifoRxByteAddr
	# Current value of RX databuffer pointer
	#       (address of last byte written by Lora receiver) 
	
	
	def setFifoRxByteAddr(self, val):
		"""Set register FifoRxByteAddr"""
		self.write(REG.FifoRxByteAddr, val, 8)
	
	def getFifoRxByteAddr(self):
		"""Get register FifoRxByteAddr"""
		return self.read(REG.FifoRxByteAddr, 8)
	
	# Bits FifoRxByteAddr
	# Register ModemConfig3
	
	
	def setModemConfig3(self, val):
		"""Set register ModemConfig3"""
		self.write(REG.ModemConfig3, val, 8)
	
	def getModemConfig3(self):
		"""Get register ModemConfig3"""
		return self.read(REG.ModemConfig3, 8)
	
	# Bits Unused_0
	# None 
	# Bits LowDataRateOptimize
	# 0 = Disabled
	#           1 = Enabled; mandated for when the symbol length exceeds 16ms 
	
	# Bits AgcAutoOn
	# 0 = LNA gain set by register LnaGain
	#           1 = LNA gain set by the internal AGC loop 
	
	# Bits Reserved_1
	# Register PpmCorrection
	# Data rate offset value, used in conjunction with AFC 
	
	def setPpmCorrection(self, val):
		"""Set register PpmCorrection"""
		self.write(REG.PpmCorrection, val, 8)
	
	def getPpmCorrection(self):
		"""Get register PpmCorrection"""
		return self.read(REG.PpmCorrection, 8)
	
	# Bits PpmCorrection
	# Register Fei
	
	
	def setFei(self, val):
		"""Set register Fei"""
		self.write(REG.Fei, val, 24)
	
	def getFei(self):
		"""Get register Fei"""
		return self.read(REG.Fei, 24)
	
	# Bits Reserved_0
	# Bits FreqError
	# Estimated frequency error from modem MSB of RF Frequency Error 
	# Register RssiWideband
	# Wideband RSSI measurement used to locally generate a random number 
	
	def setRssiWideband(self, val):
		"""Set register RssiWideband"""
		self.write(REG.RssiWideband, val, 8)
	
	def getRssiWideband(self):
		"""Get register RssiWideband"""
		return self.read(REG.RssiWideband, 8)
	
	# Bits RssiWideband
	# Register DetectOptimize
	
	
	def setDetectOptimize(self, val):
		"""Set register DetectOptimize"""
		self.write(REG.DetectOptimize, val, 8)
	
	def getDetectOptimize(self):
		"""Get register DetectOptimize"""
		return self.read(REG.DetectOptimize, 8)
	
	# Bits Reserved_0
	# Reserved 
	# Bits DetectionOptimize
	# LoRa Detection Optimize 
	# Register InvertIQ
	
	
	def setInvertIQ(self, val):
		"""Set register InvertIQ"""
		self.write(REG.InvertIQ, val, 8)
	
	def getInvertIQ(self):
		"""Get register InvertIQ"""
		return self.read(REG.InvertIQ, 8)
	
	# Bits Reserved_0
	# Reserved 
	# Bits InvertIQ
	# Invert the LoRa I and Q signals 0 = normal mode
	#           1 = I and Q signals are inverted 
	
	# Bits Reserved_1
	# Reserved 
	# Register DetectionThreshold
	# LoRa detection threshold 
	
	def setDetectionThreshold(self, val):
		"""Set register DetectionThreshold"""
		self.write(REG.DetectionThreshold, val, 8)
	
	def getDetectionThreshold(self):
		"""Get register DetectionThreshold"""
		return self.read(REG.DetectionThreshold, 8)
	
	# Bits Threshold
	# Register SyncWord
	# LoRa Sync Word
	#       Value 0x34 is reserved for LoRaWAN networks 
	
	
	def setSyncWord(self, val):
		"""Set register SyncWord"""
		self.write(REG.SyncWord, val, 8)
	
	def getSyncWord(self):
		"""Get register SyncWord"""
		return self.read(REG.SyncWord, 8)
	
	# Bits SyncWord
