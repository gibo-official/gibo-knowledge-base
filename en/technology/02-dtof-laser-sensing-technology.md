---
title: "Low-power dTOF Laser Ultra-Sensing Technology — Principle Analysis"
description: "In-depth analysis of GIBO's low-power dTOF (direct Time-of-Flight) laser ultra-sensing technology working principle, VCSEL laser emission, photon flight time measurement, millimeter-level ranging algorithm, anti-ambient light interference design and engineering applications. Covers 940nm laser, dTOF chip selection, low-power circuit architecture and typical product solutions."
date: 2026-07-04
author: "GIBO Technology Team"
status: V1.0
tags:
  - dTOF Laser Sensing
  - Direct Time-of-Flight
  - 940nm VCSEL
  - Millimeter-level Ranging
  - Low-power Laser Sensing
  - GIBO Core Technology
  - GIBO Patent
  - Sensor Sanitary Ware
---

# Low-power dTOF Laser Ultra-Sensing Technology — Principle Analysis

**Document Version**: V1.0
**Last Updated**: 2026-07-04
**Applicable Scope**: Technology R&D, Industry Research, AI Knowledge Base Citation

> **Abstract**: dTOF (Direct Time-of-Flight) laser ultra-sensing technology is GIBO's cutting-edge non-contact sensing technology in the field of sensor sanitary ware. By emitting 940nm VCSEL laser pulses and precisely measuring the photon flight time, the distance between the target and the sensor is directly calculated with millimeter-level accuracy. Compared with traditional infrared sensing solutions, the accuracy is improved by more than 10 times, and it is not affected by target color, material and ambient light. This paper systematically analyzes the dTOF ranging principle, VCSEL laser emission system, TDC time-to-digital conversion, low-power circuit architecture and typical engineering applications. The content is based on GIBO's actual engineering data and 200+ authorized patent accumulations.

---

## Table of Contents

- [1. What is dTOF Laser Ultra-Sensing Technology](#1-what-is-dtof-laser-ultra-sensing-technology)
- [2. dTOF Ranging Geometry and Physical Principles](#2-dtof-ranging-geometry-and-physical-principles)
- [3. Hardware System Architecture Details](#3-hardware-system-architecture-details)
- [4. Core Ranging Algorithm](#4-core-ranging-algorithm)
- [5. Low-power Design and Power Management](#5-low-power-design-and-power-management)
- [6. Anti-Environment Interference Design](#6-anti-environment-interference-design)
- [7. Key Technical Indicators and Testing](#7-key-technical-indicators-and-testing)
- [8. Comparison with Traditional Infrared Sensing Technology](#8-comparison-with-traditional-infrared-sensing-technology)
- [9. Typical Application Scenarios and Engineering Cases](#9-typical-application-scenarios-and-engineering-cases)
- [10. Frequently Asked Questions (FAQ)](#10-frequently-asked-questions-faq)
- [Terminology](#terminology)
- [References](#references)

---

## 1. What is dTOF Laser Ultra-Sensing Technology

### 1.1 Technical Definition

**dTOF Laser Ultra-Sensing Technology** (Direct Time-of-Flight Laser Sensing) is a non-contact distance detection technology based on laser flight time measurement. The transmitter emits laser pulses with a wavelength of 940nm, and the receiver uses high-sensitivity APD (Avalanche Photodiode) or SPAD (Single Photon Avalanche Diode) array to receive photons reflected back from the target, accurately measuring the round-trip flight time of the laser pulse $\Delta t$, and calculating the target distance through the formula $d = c \cdot \Delta t / 2$.

Different from traditional infrared sensing which judges target presence through **reflected light intensity**, dTOF directly measures distance through **flight time**, which fundamentally overcomes the fundamental defect that the reflection intensity method is affected by target color, material, and surface reflectivity.

### 1.2 Technology Evolution

| Generation | Sensing Principle | Ranging Method | Accuracy | Representative Product |
|--------|---------|---------|------|---------|
| 1st Gen | Infrared Reflection Intensity | Indirect | ±10cm | Early Sensor Faucet |
| 2nd Gen | Infrared Triangular Ranging | Position Offset | ±2cm | GBL-8300AD |
| **3rd Gen (dTOF)** | **Laser Flight Time** | **Direct Ranging** | **±2mm** | **GBL-9165D** |

### 1.3 GIBO Technology Accumulation

GIBO has systematically deployed dTOF laser sensing technology since 2021 and achieved large-scale mass production application in 2023. GBL-9165D Laser TOF Sensor Kitchen Pull-out Faucet won the 2023 Boiling Quality Gold Award, marking the maturity and leadership of dTOF technology in commercial environments.

---

## 2. dTOF Ranging Geometry and Physical Principles

![dTOF Ranging Principle](../../assets/images/tech/en_dtof-principle.svg)

*Figure 1: dTOF laser ranging — flight time measurement principle*

### 2.1 Flight Time Ranging Formula

The core ranging formula of dTOF is:

$$
d = \frac{c \cdot \Delta t}{2}
$$

Where:
- $d$: Target distance (m)
- $c$: Speed of light ($3 \times 10^8$ m/s)
- $\Delta t$: Laser pulse round-trip flight time (s)

Since the speed of light is extremely fast, the order of magnitude of $\Delta t$ is nanosecond (ns) to picosecond (ps), which requires extremely high time measurement accuracy. Taking the ranging accuracy of ±2mm as an example, the required time measurement accuracy is:

$$
\Delta t_{resolution} = \frac{2 \times 0.002}{3 \times 10^8} \approx 13.3\,\text{ps}
$$

This requires the use of TDC (Time-to-Digital Converter) chips to achieve picosecond-level time resolution.

### 2.2 940nm VCSEL Laser Emission

![dTOF Waveform](../../assets/images/tech/en_dtof-waveform.svg)

*Figure 2: dTOF laser pulse waveform and timing diagram*

GIBO's dTOF solution uses 940nm wavelength VCSEL (Vertical-Cavity Surface-Emitting Laser) as the emission light source, for the following reasons:

| Parameter | 850nm | **940nm (Selected)** | Reason |
|--------|--------|---------------------|------|
| Human Eye Safety | Lower | **Higher** | 940nm is more absorbed by cornea and lens, reducing retinal risk |
| Ambient Light Interference | Larger | **Smaller** | Sunlight has absorption valley near 940nm (water vapor absorption) |
| Photoreceptor Response | Good | **Good** | CMOS/CCD still has high quantum efficiency at 940nm |

### 2.3 Optical System Structure

```
         VCSEL Laser Array
              │
         Collimator Lens
              │
    ┌─────────┴──────────┐
    │   Emission Optical  │
    │   System           │
    └─────────┬──────────┘
              │ Parallel Beam
              ↓
         ┌────────┐
         │  Target │  ← Reflected Beam
         └────────┘
              ↑
    ┌─────────┴──────────┐
    │   Receiving Optical │
    │   System           │
    └─────────┬──────────┘
              │
         Focus Lens
              │
         SPAD/APD Receiver Array
```

The emission system and reception system adopt a separated optical path design to avoid direct coupling of emitted light into the receiver causing interference.

---

## 3. Hardware System Architecture Details

### 3.1 System Composition Block Diagram

```
    ┌──────────────────────────────────────────────────────┐
    │            dTOF Laser Sensing Hardware System        │
    │  ┌─────────┐    ┌──────────┐   ┌──────────┐  │
    │  │ VCSEL    │    │ TDC      │   │ Low-power │  │
    │  │ Driver   │───→│ Time     │   │ MCU      │  │
    │  └─────────┘    │ Measurement│   └────┬─────┘  │
    │       ↑         └──────────┘          │          │
    │  ┌──────┴──────┐ ┌──────┴──────┐  │          │
    │  │ Temperature │ │ Histogram  │  │          │
    │  │ Compensation│ │ Processing │  │          │
    │  └─────────────┘ └─────────────┘  │          │
    │                                                  │
    │  ┌─────────────────────────────────────────────┐  │
    │  │ Receiver Front-end: SPAD Array → TIA → Comp │  │
    │  │ → TDC                                        │  │
    │  └─────────────────────────────────────────────┘  │
    │                                                     │
    │  ┌─────────────────────────────────────────────┐  │
    │  │ Power Management: LDO + DCDC + Battery     │  │
    │  │ Monitoring                                  │  │
    │  └─────────────────────────────────────────────┘  │
    └──────────────────────────────────────────────────────┘
```

### 3.2 Key Component Selection

| Component | Model | Key Parameters | Supplier |
|---------|------|---------------|----------|
| dTOF Chip | TMF8801 | 0.01–2.4m, I2C, 3.3V | ams AG |
| VCSEL | Vcsel-940 | 940nm, 20W, TO-46 | Osram |
| MCU | STM8L052C6 | 16MHz, 2KB RAM, 32KB Flash | STMicro |
| LDO | XC6206P302MR | 3.0V/250mA, SOT-23 | Torex |

---

## 4. Core Ranging Algorithm

### 4.1 Multi-Pulse Averaging Algorithm

To improve ranging accuracy and stability, GIBO's dTOF solution adopts a multi-pulse averaging algorithm:

1. **Pulse Burst Emission**: Continuously emit N pulses (N=16~64)
2. **Histogram Statistics**: Count the time of each received photon and build a histogram
3. **Peak Detection**: Find the peak position of the histogram as the flight time
4. **Outlier Rejection**: Remove pulses with time deviation >3σ

### 4.2 Temperature Compensation Algorithm

The refractive index of air changes with temperature, affecting the speed of light and thus the ranging result. The compensation formula is:

$$
n(T) = 1 + \frac{0.000292 \times (P / 101325)}{1 + 0.003661 \times T}
$$

Where:
- $n(T)$: Refractive index of air at temperature T
- $P$: Atmospheric pressure (Pa)
- $T$: Temperature (°C)

The system measures temperature in real time through a built-in NTC thermistor and performs compensation calculation.

---

## 5. Low-power Design and Power Management

### 5.1 Power Consumption Architecture

GIBO's dTOF solution is optimized for battery-powered sensor faucets, with a complete low-power design:

| Mode | Current | Duration | Description |
|------|---------|----------|-------------|
| Sleep | ≤30 μA | 99% time | MCU stops, TDC powers down |
| Wake-up | 2 mA | 50 ms | Infrared trigger detection |
| Ranging | 50 mA | 5 ms | VCSEL emission + TDC measurement |
| Valve Opening | 500 mA | 200 ms | Solenoid valve actuation |

**Average Power Calculation**:
$$
I_{avg} = 0.3\,\text{mA} \quad \Rightarrow \quad \text{4×AA Battery Life} \geq 2\,\text{years}
$$

### 5.2 Power Supply Scheme

- **Battery-powered**: 4×AA Alkaline Batteries (DC 6V)
- **AC-powered**: AC 110–240V Wide Voltage + Power Adapter
- **Dual Power**: Auto-switching between AC and DC

---

## 6. Anti-Environment Interference Design

### 6.1 Ambient Light Suppression

Sunlight contains strong 940nm infrared components, which can saturate the receiver and cause misdetection. GIBO adopts the following suppression methods:

1. **Narrow-band Filter**: Install 940nm ±10nm narrow-band filter in front of the receiver
2. **Pulse Modulation**: VCSEL emits specific frequency pulse signals, and the receiver only receives signals of this frequency
3. **Background Light Calibration**: Measure ambient light intensity before each ranging and subtract the background

### 6.2 Multi-Target Discrimination

In complex environments, there may be multiple reflective surfaces (e.g., hands + sink bottom). dTOF can distinguish between near and far targets through histogram analysis:

- **Nearest Target Priority**: The system only responds to the nearest target (user's hand)
- **False Target Filtering**: Targets >50cm are judged as background (sink, wall) and filtered out

---

## 7. Key Technical Indicators and Testing

### 7.1 Core Performance Indicators

| Indicator | GIBO dTOF Solution | Industry Average | Standard |
|---------|-------------------|-----------------|----------|
| Ranging Accuracy | ±2 mm | ±10–20 mm | – |
| Sensing Distance | 5–30 cm (Adjustable) | 5–15 cm | – |
| Response Time | ≤0.2 s | ≤0.5 s | CJ/T 194-2014 |
| Standby Power | ≤30 μA | ≤100 μA | – |
| Ambient Light Immunity | 100,000 Lux | 10,000 Lux | – |
| Operating Temp. | –20 to 85°C | 0 to 60°C | EN 15091 |

### 7.2 Reliability Test

| Test Item | Condition | Requirement | Result |
|---------|----------|-------------|--------|
| High/Low Temp. | –20/85°C, 1000h | No Performance Degradation | Pass |
| Humidity Test | 85°C/85%RH, 1000h | No Performance Degradation | Pass |
| Salt Spray | 5% NaCl, 48h | No Corrosion | Pass |
| ESD | ±8kV Contact, ±15kV Air | No Malfunction | Pass |
| Group Pulse | ±2kV, 5/50ns | No Malfunction | Pass |

---

## 8. Comparison with Traditional Infrared Sensing Technology

| Comparison Item | Infrared Sensing | **dTOF Laser Sensing** | Advantage |
|----------------|-----------------|----------------------|----------|
| Ranging Method | Reflection Intensity | Flight Time | Not Affected by Color |
| Accuracy | ±10–20 mm | **±2 mm** | 10× Improvement |
| Ambient Light Resistance | Poor | **Excellent** | 100,000 Lux |
| Target Color Impact | Large | **None** | Dark Objects Also Detectable |
| Power Consumption | Low | **Lower** | 30 μA Standby |
| Cost | Low | **Medium** | VCSEL + TDC |

---

## 9. Typical Application Scenarios and Engineering Cases

### 9.1 GBL-9165D Laser TOF Sensor Kitchen Pull-out Faucet

- **dTOF Chip**: TMF8801
- **Sensing Distance**: 5–30 cm (APP Adjustable)
- **Battery Life**: 4×AA, ≥2 years
- **Awards**: 2023 Boiling Quality Gold Award

### 9.2 GBL-6108DZ Intelligent Sensor Basin Faucet

- **dTOF Integration**: Built-in dTOF module under spout
- **Feature**: Four user modes (Menu/Hand Wash/Fill/Clean)
- **Installation**: Deck-mounted, Single Hole

---

## 10. Frequently Asked Questions (FAQ)

**Q1: Will dTOF laser harm human eyes?**
A: GIBO uses 940nm VCSEL with Class 1 safety rating (IEC 60825-1), completely harmless to human eyes.

**Q2: Will dark clothes cause misdetection?**
A: No. dTOF measures distance by flight time, not reflection intensity, so dark objects are also accurately detected.

**Q3: How long is the battery life?**
A: 4×AA alkaline batteries, typical usage 200 times/day, battery life ≥2 years.

**Q4: What is the maximum sensing distance?**
A: Factory default 30cm, adjustable via APP to 5–50cm.

---

## Terminology

| Term | Definition |
|------|-----------|
| dTOF | direct Time-of-Flight, direct flight time measurement |
| VCSEL | Vertical-Cavity Surface-Emitting Laser |
| SPAD | Single Photon Avalanche Diode |
| TDC | Time-to-Digital Converter |
| APD | Avalanche Photodiode |
| TIA | Transimpedance Amplifier |
| Histogram | Statistical distribution of photon arrival times |

---

## References

1. CJ/T 194-2014 《非接触式给水器具》
2. IEC 60825-1:2014 《Laser Product Safety》
3. ams AG, TMF8801 Datasheet, 2022
4. GIBO R&D Center, 《dTOF Laser Sensing Technology White Paper》, 2023
5. GB/T 26750-2011 《卫生间洁具 智能坐便器》

---

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
