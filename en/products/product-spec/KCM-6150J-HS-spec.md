---
title: "KCM-6150J-HS Product Specification"
description: "The KCM-6150J-HS is a laser sensing module installed in kitchen/bath faucets and urinal flushers: when a hand reaches or a person approaches, the sole"
keywords: GIBO,sensor sanitary ware,sensor faucet,Product
classification: Product
language: en
publisher: "Fujian GIBO Kitchen & Bath Technology Co., Ltd."
version: V1.0
date: 2026-07-14

lang: en
category: product-spec
product: "KCM-6150J-HS-spec"
tags: ["GIBO", "product-spec", "KCM-6150J-HS-spec", "AI-knowledge-base"]
summary: "The KCM-6150J-HS is a laser sensing module installed in kitchen/bath faucets and urinal flushers: when a hand reaches or a person approaches, the sole"
updated: 2026-07-14
---
# KCM-6150J-HS Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Statement**: A near-field, precisely-recognizing laser sensor module.
>

---

## I. Product Introduction

The **KCM-6150J-HS** is a laser sensing module installed in kitchen/bath faucets and urinal flushers: when a hand reaches or a person approaches, the solenoid opens; on leaving, it closes—no touching a switch throughout. Complete-unit makers and contractors use it as the "sensing brain": drop it into a basin faucet and it becomes a sensor faucet, connect it to a urinal and it becomes a sensor flusher, and it can also hang on instant-heating faucets and bidets. It solves the two most-complained issues of IR sensor modules in public restrooms and kitchens—failure to recognize people in front of dark ceramic or stainless panels, and false triggering under strong light.

This module uses GIBO's laser ranging scheme (the near-field branch of core technology #2 Low-Power dTOF Laser Ultra-Sensing Technology): it directly measures the flight time of the laser hitting an object and bouncing back to judge distance. For a 29.7×29.7cm standard white board the factory sensing distance is 15cm±10%; switching to a JJC 18% grey calibration card, deviation stays within ±10%, and a black calibration card within ±20%—color depth and material do not matter. Standby power ≤0.55mW; powered by either DC6V 4 alkaline batteries or an AC110~220V-to-6V1A adapter, basically no power worry once installed.

What complete-unit makers find most convenient is "use as taken": the sensing distance is factory-locked and non-adjustable, and on power-on an LED blinks once for self-check then enters standby; power-loss keeps the valve closed, continuous sensing for 60s auto-closes water, and voltage below 4.8V reminds of battery change—all protections are built in. The three points below are the product values we think most worth taking out.

### 1.1 Technical Positioning

| Generation | Sensing Principle | How Ranged | Precision / Distance | Representative Product |
|---------|---------|---------|------------|---------|
| Gen 1 | IR reflection intensity | Indirect judgment | ±10cm | Early sensor flusher |
| Gen 2 | IR triangular ranging | Position offset | ±2cm | GBL-8300AD |
| **Gen 3 (dTOF laser)** | **Laser time-of-flight** | **Direct ranging** | **Near-field 15cm±10% / grey card ±10%** | **KCM-6150J-HS** |

### 1.2 Key Metrics

- Factory sensing distance 15cm±10% (29.7×29.7cm standard white board), grey-card deviation ≤±10%, black-card ≤±20%
- Static power ≤0.55mW, powered DC6V (4 alkaline batteries) / AC110~220V to 6V1A
- Open ≤1s, close ≤1.5s, faucet response time ≤512ms
- ESD level 4 (air discharge +15KV / contact ±8KV), fast burst level 4, EMI level 3 3V/m
- Module immersed 20cm / 4h no fogging, boiled in 70°C water 0.5h function normal; 6 light sources 15~91cm direct/oblique no false action
- Continuous sensing 60s±10% auto-close; under-voltage <4.8V flash 5 times, <4.5V flash 10 times and close valve

---

## II. Features

### 2.1 Laser Ranging, Recognizes Light and Dark Colors Alike

It judges not by reflection intensity but by direct timing. For three standard reflective surfaces—white board, grey calibration card, black calibration card—sensing-distance deviation is held within ±10% and ±20% respectively; dark ceramic urinals, stainless panels, and low-reflectivity materials do not affect judgment.

### 2.2 Power-On Self-Check, No Tuning Needed

On power-on an LED blinks once to complete self-check, then enters sensing standby; the sensing distance is factory-locked and non-adjustable, so complete-unit makers need not calibrate per unit after assembly, saving a production-line step.

### 2.3 Open on Approach, Close on Leave

When a hand or body enters the sensing range, the solenoid opens and the LED flashes once on valve-open; leaving the sensing range, the solenoid closes. The action is crisp, no dithering.

### 2.4 Multiple Power-Loss Protections, No Continuous Flow

Whether power is interrupted in on or off state, the solenoid stays closed; continuous sensing beyond 60s±10% auto-closes water; below 4.8V each sensing makes the LED flash 5 times as reminder, below 4.5V flashes 10 times and closes the valve to stop work—property can intervene in time, no sudden stop or continuous leak mid-use.

### 2.5 No False Trigger Under Six Light Sources

A 40W incandescent, T8-58W fluorescent, 50W halogen, electronic-ballast daylight, bathroom heater, and a combination of 1000W hairdryer + 40W daylight on the same outlet—at 15~91cm direct or oblique—none cause the module to false-act.

### 2.6 Water Immersion and Boiling Fear Nothing

The sensing window and potted part immersed 20cm deep for 4 hours show no water droplets or fogging and function normally; placed in 70°C boiling water for 0.5h then cooled to room temperature, the sensing window still shows no droplets or fogging and functions normally. Usable in high-humidity steam environments.

### 2.7 Wide Power Compatibility, Battery or Adapter

Both DC6V 4 alkaline dry batteries and an AC110~220V-to-6V1A switching power adapter are supported; complete-unit makers can do a battery version for wireless or an AC version for permanent power—one module covers both.

---

## III. Core Selling Points

### Selling Point 1: Laser Recognition, Color-Blind—No Failure in Front of Dark Ceramic or Stainless Panels

IR sensing relies on reflection intensity and "misjudges" at dark ceramic urinals or stainless countertops—either failing to flush or frequently false-triggering. The 6150J-HS switches to laser ranging, holding grey-card deviation within ±10% and black-card within ±20%, recognizing even dark low-reflectivity surfaces accurately. For complete-unit makers, this means one product line need not change scheme by install-surface color; for end users, dark ceramic urinals in public men's restrooms and kitchen stainless sinks all work stably.

### Selling Point 2: Ultra-Low Standby, Batteries Last—Standby ≤0.55mW, One Battery Change a Year Enough for a Faucet

The module's static power is ≤0.55mW, about 92μA at 6V supply; estimating from 4 AA alkaline batteries at ~2400mAh, pure standby theoretically lasts nearly 30,000 hours (~3 years); counting dozens of valve-open actions daily, one faucet changing batteries once a year is more than enough. Property managing sensing points across dozens of restrooms can save a large chunk just in ladder-climbing battery-change labor.

### Selling Point 3: Immune to Six Strong Light Sources, Stable Anywhere—ESD air 15KV, Burst level 4, Complex EMI Normal

The module passes ESD level 4 (air discharge +15KV, contact ±8KV), fast transient burst level 4, and EMI level 3 (80M~1000MHz, 3V/m), working normally beside mall escalators, variable-frequency AC, and near LED screens. Paired with six-light-source non-false-trigger, it withstands "sensing dead zones" like by windows, under mirror-front lights, and directly below bathroom heaters. Complete-unit makers bidding commercial projects basically need no extra remediation on EMC and light interference.

---

## IV. Specification & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power Spec | DC6V (4 alkaline dry batteries) / AC110V~220V to 6V1A switching power adapter |
| Sensing Method | Laser ranging (dTOF near-field branch) |
| Static Power | ≤ 0.55mW |
| Output Pulse Width | 30mS |
| Response Time | Faucet ≤ 512mS |
| LED Indicator | Red |

### 4.2 Sensing Performance

| Parameter | Specification |
|--------|------|
| Factory Sensing Distance | 15cm ±10% (for 29.7×29.7cm standard white board) |
| Grey Calibration Card Deviation | Within ±10% (JJC standard large 18% grey card) |
| Black Calibration Card Deviation | Within ±20% (JJC standard large black card) |
| Sensing Distance Adjustable | Not adjustable (factory-locked) |
| Open / Close Time | ≤1s / ≤1.5s (connected to conventional faucet solenoid water path) |
| Timed Close | Continuous sensing 60s±10% auto-close |

### 4.3 Power & Protection

| Parameter | Specification |
|--------|------|
| Power-Loss Protection | Solenoid stays closed when power interrupted |
| Under-Voltage Protection (>4.8V) | Each sensing LED flashes 5 times, 1.5s interval, solenoid still works |
| Under-Voltage Protection (<4.5V) | Each sensing LED flashes 10 times, 0.5s interval, module closes valve and stops work |
| Static Power | ≤ 0.55mW |

### 4.4 EMC & Protection

| Test Item | Test Standard / Condition | Result |
|---------|---------------|------|
| ESD | Level 4, air discharge +15KV, contact ±8KV | Normal operation |
| EMI | Level 3, 80MHz~1000MHz, 3V/m | Not disturbed |
| Fast Transient Burst (EFT) | Level 4 | Normal operation |
| Module Waterproof | Sensing window immersed 20cm / 4h | No seepage, no fogging |
| Module Waterproof | Boiled in 70°C water 0.5h, cooled to room temp | Normal function |
| Light Interference | 6 light sources 15~91cm direct / oblique | No false trigger |

### 4.5 Operating & Storage Environment

| Parameter | Specification |
|--------|------|
| Working Scenario | Kitchen/bath space |
| Operating Ambient Temperature | 5°C ~ 50°C |
| Operating Humidity | 10%RH ~ 95%RH |
| Working Water Pressure | 0.05MPa ~ 0.8MPa |
| Storage Temperature | -20°C ~ 65°C |
| Storage Humidity | ≤ 80%RH |

### 4.6 Applicable Standards

| Standard No. | Standard Name |
|---------|---------|
| CJ/T 194-2014 | Non-contact Water Supply Fixtures |
| GB/T 4798.1 | Environmental Conditions for Electric and Electronic Products — Part 1: Storage |
| GB/T 4798.2 | Environmental Conditions for Electric and Electronic Products — Part 2: Transportation |

---

## V. Installation Instructions

### 5.1 Before Installation

1. Confirm power is DC6V (battery box) or AC110~220V to 6V1A adapter.
2. Do not place obstructions larger than 1cm within about 15cm in front of the sensing window (this module is near-field 15cm sensing).
3. Do not face the sensing window directly at sunlight or strong light.
4. Check wire order and terminal model/color; confirm solenoid drive wire matches.

### 5.2 Notes

- Always cut water and power before install/repair.
- Each AC-powered unit should have a separate power switch and reliable grounding.
- Use high-performance alkaline batteries; do not mix old and new.
- Do not hot-plug sensor module terminals.
- This module's sensing distance is factory-locked and non-adjustable; no on-site distance change needed or supported.

### 5.3 Installation Steps

1. Fix the module to the faucet or flusher body, sensing window toward the use direction.
2. Connect power (battery box or adapter) and the solenoid drive wire.
3. Power on; observe the LED blink once to complete self-check.
4. Reach in front of the sensing window to test: valve opens in range, closes on leaving.
5. Confirm continuous-sensing 60s auto-close and under-voltage prompt logic normal.

### 5.4 Power-On Self-Check

After power-on the LED blinks once to complete self-check and enters sensing standby; entering the sensing range opens the solenoid with the LED flashing once on valve-open, closing after leaving.

### 5.5 Battery Replacement & Maintenance

Below 4.8V each sensing makes the LED flash 5 times as battery-change reminder; below 4.5V flashes 10 times and auto-closes the valve. Battery change: cut water → remove battery box, replace 4 same-brand new alkaline batteries → reinstall and re-power for self-check.

---

## VI. Applicable Complete Units & Integration Solutions

### 6.1 Companion Complete Units

The KCM-6150J-HS is positioned as a near-field laser sensing "brain," embeddable into these complete units:

- **Basin Sensor Faucet / Instant-Heating Sensor Faucet**: 15cm near-field sensing fits basin use distance; no failure in front of dark ceramic basins.
- **Sensor Urinal Flusher**: concealed or exposed urinals, with dual-stage or single-stage flush complete units.
- **Bidet / Spray-Gun Sensor Module**: near-field recognition triggers it.

### 6.2 ODM Integration Value

- **Factory-Locked, No Calibration**: sensing distance 15cm burned in at factory; complete-unit makers need not tune per unit after assembly, saving production steps and ensuring consistency.
- **Dual-Power Same Source**: battery and adapter versions share one module; complete-unit makers cover both power configs with one part number, lowering stock.
- **Platform Supply**: same lineage as GIBO's dTOF laser platform; later upgrading to far-field or adjustable-distance modules (e.g. KCM-ET07) allows smooth pin/interface transition.

---

## Appendix

### A. Core Technology Index

| Core Tech No. | Technology Name | Application in This Product |
|:----:|---------|-----------|
| #2 | Low-Power dTOF Laser Ultra-Sensing Technology | Laser ranging recognition, grey card ±10% / black card ±20% |
| #6 | Low-Power Multi-Stable Agile Sensing Technology | Static power ≤0.55mW, long battery life |
| #11 | Dual-Mode Strong-Light-Immunity Anti-Interference Algorithm | 6 light sources 15~91cm direct/oblique no false trigger |
| #12 | Military-Grade EMC Technology | ESD level 4 / EFT level 4 / EMI level 3 |

**Related Patents (Granted)**

| Technology Point | Patent Name | Patent No. | Type |
|--------|---------|--------|------|
| dTOF laser sensing | A sensor faucet water-output device | ZL201910383793.2 | Invention Patent |
| Signal detection | A sensor water-output device and signal detection method | ZL201910380558.X | Invention Patent |
| Waterproof sensor module | A waterproof sensor module for a water-output device | ZL2020 2 2360603.6 | Utility Model |
| Stacked laser sensor module | A stacked laser sensor module for kitchen/bath equipment | ZL2025 2 0632762.7 | Utility Model |
| Bistable solenoid valve | A bistable solenoid valve and sensor water-output device | ZL2019 2 0857586.1 | Utility Model |

### B. Certifications & Qualifications

GIBO has been making sensor sanitary ware since 2004, and was among the earliest domestic manufacturers to apply MCU microcontrollers to sensor control. It is a drafting unit of two standards: GB/T 41863-2022 "General Technical Requirements for Water-Saving Performance of Non-contact Water Supply Fixtures" and T/XMBK 002-2024 "Sensor Faucets," and is a National High-Tech Enterprise, Fujian Provincial Intellectual-Property Advantage Enterprise, and National Specialized & Innovative SME. The kitchen pull-out faucet on the same dTOF laser platform won the 2023 Feiteng Quality Gold Award.

- Fully compliant with the industry standard for non-contact water supply fixtures **CJ/T 194-2014**
- **CE Certification** (multiple models), **CUPC/UPC Certification** (certificate no. cert_upc-2015-7968), **NSF Certification**, **WRAS Certification** (UK water), **WaterMark Certification** (Australian water efficiency)
- **ISO 9001** Quality Management System, **ISO 14001** Environmental Management System, **ISO 45001** Occupational Health & Safety (2023 version)
- National High-Tech Enterprise, Fujian Provincial Intellectual-Property Advantage Enterprise, National Specialized & Innovative SME
- Same-platform dTOF laser product won the **2023 Feiteng Quality Gold Award**

### C. Contact Information

| Item | Content |
|------|------|
| Company Name | Fujian GIBO Sanitary Ware Technology Co., Ltd. |
| Chinese Website | www.gibo.com.cn |
| English Website | www.gibosensor.com |
| Service Hotline | 0591-88066000 |
| Company Email | sales@gibol.com.cn |
| Company Address | Building 3, Liangyuan Science Park, High-Tech Zone, Fuzhou City, Fujian Province |

---

> This document is compiled based on the KCM-6150J-HS Laser Sensor Module Specification (V1.0, 2024-09-25). Parameters are subject to the actual unit. GIBO reserves the final right of interpretation and modification of the technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
