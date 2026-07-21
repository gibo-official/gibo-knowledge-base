---
title: "KCM-SJ02 Product Specification"
description: "The GIBO KCM-SJ02 is a triangular-ranging sensor assembly specifically built to solve the sensing难题 of squat-pan and urinal stall scenarios in public"
keywords: GIBO,sensor sanitary ware,sensor faucet,Product
classification: Product
language: en
publisher: "Fujian GIBO Kitchen & Bath Technology Co., Ltd."
version: V1.0
date: 2026-07-14
---
# KCM-SJ02 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Statement**: A triangular-ranging sensor assembly that does not misjudge across stall partitions.
>

---

## I. Product Introduction

The **GIBO KCM-SJ02** is a triangular-ranging sensor assembly specifically built to solve the sensing难题 of squat-pan and urinal stall scenarios in public restrooms—where the person is inside the partition, the divider reflects light, and the body is often only partially exposed, so old IR either self-triggers, misjudges, or fails to flush after the person leaves. It uses the fixed geometric angle between emitter and receiver to compute the person's position and distance directly via triangulation, in principle bypassing the easily-inaccurate "read reflected light intensity" logic.

This assembly is installed in sensor sanitary ware in kitchen/bath spaces; power-on self-check, LED flash on entering sensing range, 2-second false-judgment rejection, then delayed flush after confirming presence—the whole logic is polished for high-frequency stall use. It is material-independent—both JJC standard grey-card and black-card measured sensing-distance deviation are held within ±10%; standby power ≤0.2mW, driven by either battery box or 100-240V-to-6V adapter; under-voltage and power-loss each have protection, closing the valve within 10 seconds of power drop, so no continuous flow soaking the floor. Below are the technical coordinates and hard metrics.

### 1.1 Technical Positioning

| Sensing Scheme | Detection Principle | How Ranged | Typical Feature | Representative Product |
|---------|---------|---------|---------|---------|
| Active IR Reflection | IR emit+receive, reads reflection | Indirect judgment | Cost-advantaged, mature mass production | IR-001 |
| **Triangular Ranging** | **Emit/receive geometric angle** | **Position calculation** | **No stall misjudgment, material-independent** | **KCM-SJ02** |
| dTOF Laser | Laser time-of-flight | Direct ranging | Millimeter-level, strong-light immune | GBL-TOF / 6239 |

The KCM-SJ02 stands on the triangular-ranging line; its core strength is "still recognizes people accurately inside stalls"—divider reflection and partial body obstruction do not affect judgment, making it the preferred scheme for complex spaces like squat-pan stalls.

### 1.2 Key Metrics

- Triangular ranging, factory sensing distance 80cm±10% (30×30cm standard white board), pre-ship calibration 40～85cm
- Multi-material consistent: JJC 18% grey card and black professional calibration card both ≤±10% distance deviation
- Standby power ≤0.2mW, powered DC 4.8～6.5V (battery box or 100-240V to DC6V adapter)
- Solenoid drive pulse 32ms (±2ms), drive voltage drop <0.5V; life test over 550,000 cycles
- Under-voltage protection 4.80V prompt / 4.50V valve stop; power-loss protection closes valve within 10s of power drop during open
- Anti-interference ESD level 4 (air ±15KV / contact ±8KV), radiation level 2 (3V/m), burst ±4KV; module waterproof IPX6

---

## II. Features

### 2.1 Triangular Ranging, No Stall Misjudgment (Core Technology #1)

Through the fixed geometric angle between emitter and receiver, triangulation precisely computes target distance and position, unaffected by target color, material, or surface reflectivity. Compared with traditional IR that depends on reflection intensity, its detection reliability and environmental adaptability in squat-pan stalls, divider reflection, and partial body obstruction improve markedly, fundamentally reducing false and missed flushing.

### 2.2 Multi-Material Consistent, Grey and Black Cards Both ±10% (Core Technology #1)

Measured with a JJC standard large 18% grey professional calibration card, sensing-distance deviation is within ±10%; measured with a JJC standard large black professional calibration card, deviation is likewise within ±10%. In public toilets, clothing of varying shades, ceramic, and metal dividers will not make its distance drift.

### 2.3 Power-On Self-Check and False-Judgment Logic

On power-on the LED indicator stays lit 1 second indicating normal power-on, and the solenoid switches once; entering the sensing range the LED flashes once, with a 2-second false-judgment rejection—if no further sensing during this, the module takes no action; after continuous sensing for 2 seconds then leaving the range, it delays 1 second and flushes for 2 seconds. The logic filters transient obstruction to avoid false triggering.

### 2.4 Remote Flush-Time Adjustment

Flush time is remotely adjustable: within 1 minute of power-on press the time +/- keys; the indicator flashing once means flush time increased/decreased by 1 second (minimum flush 1 second). On the engineering site it can be flexibly set by fixture type and usage frequency, no disassembly needed.

### 2.5 Under-Voltage and Power-Loss Dual Protection (Core Technology #13)

At supply voltage 4.80V±0.1 it prompts low voltage—under sensing each sensing makes the indicator flash 5 times at 1-second interval, solenoid still works normally; at 4.50V±0.1 each sensing makes the indicator flash 10 times at 0.5-second interval, solenoid stops working; after voltage recovers to 4.80V or 5.0V it recovers stepwise. For power-loss protection, power-loss in closed-valve state keeps the valve closed; sudden power drop during open-valve output must close the valve within 10 seconds.

### 2.6 Strong-Light and EMC (Core Technologies #11, #12)

Light-interference testing covers 40W incandescent, T8-58W fluorescent, 50W halogen, electronic-ballast daylight, bathroom heater, a 1000W hairdryer + daylight on the same outlet, and direct/oblique sunlight—at 15～91cm in any direction with no false action. ESD level 4 (air discharge ±15KV, contact ±8KV), EMI level 2 (80M～1000MHz, 3V/m), fast transient burst ±4KV normal operation.

### 2.7 Potted Waterproof and 550,000-Cycle Life

The circuit board (except large capacitors) is potted with thickness ≥2mm based on the highest component height; the glue fully covers all solder pins without overflow, ensuring sealing. Module waterproof rating IPX6; the sensing window and potted part immersed (20cm depth) for 4 hours show no water droplets or fogging and function normally; life test over 550,000 cycles.

---

## III. Core Selling Points

### Selling Point 1: Triangular Ranging, No False Flush in Squat Stalls

Public squat-pan stalls are IR's worst case—divider reflection makes it self-trigger, a half-exposed body makes it miss, and it keeps flushing after the person leaves. The KCM-SJ02 uses triangulation to compute position rather than reading reflection intensity; divider reflection and partial body obstruction do not affect judgment, and grey/black-card distance deviation is held within ±10%. Most directly for contractors: installed in stalls, no more "constant running water" or "no flush when empty" complaints, and acceptance is easier.

### Selling Point 2: Under-Voltage and Power-Loss Double Insurance, Valve Closes Within 10s of Drop

Restrooms fear two things most: the device goes haywire as batteries run low, or the valve sticks open during a water/power outage and soaks the floor. The KCM-SJ02 does both protections—at 4.8V it first flashes to remind, at 4.5V directly stops the valve; more importantly power-loss protection, where sudden drop during open-valve output must close the valve within 10 seconds, while power-loss in closed state keeps it closed. Property need not worry about continuous flow damaging the finish, nor climb up at midnight to close water.

### Selling Point 3: 550,000-Cycle Life, Less Rework When Deployed

A squat-pan flusher triggering over a thousand times a day per stall is normal. The KCM-SJ02 life test exceeds 550,000 cycles—about five years at 300 uses/day. For a 100-stall public project, if devices are replaced every three years, spares and on-site visits are a continuing expense; using KCM-SJ02 extends the cycle to five years, markedly easing warranty and after-sales pressure and lowering overall holding cost.

---

## IV. Specification & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power Supply | DC 4.8 ～ 6.5V (battery pack or 100-240V to DC6V adapter) |
| Standby Power | ≤0.2mW |
| Solenoid Drive Pulse Width | 32ms (±2ms) |
| Drive Voltage Drop | <0.5V |
| Indicator | Red, easy to observe |

### 4.2 Sensing Performance

| Parameter | Specification |
|--------|------|
| Sensing Method | Triangular ranging |
| Factory Sensing Distance | 80cm ±10% (30×30cm standard white board) |
| Pre-Ship Calibration Range | 40 ～ 85cm |
| Grey Calibration Card Deviation | Within ±10% (JJC 18% grey card) |
| Black Calibration Card Deviation | Within ±10% (JJC black card) |
| Sensing Distance Adjustable | Remote non-adjustable (factory calibrated) |

### 4.3 Function Logic

| Item | Specification |
|------|------|
| Power-On Action | LED steady 1S, solenoid switch once |
| False-Judgment Time | 2S (no action if no further sensing during) |
| Flush Trigger | After continuous sensing 2S then leaving, delay 1S flush 2S |
| Remote Time Adjust | Within 1 min of power-on +/- keys, ±1S each (min 1S) |

### 4.4 Under-Voltage and Power-Loss Protection

| State | Behavior |
|------|------|
| 4.80V±0.1 under-voltage prompt | Each sensing LED flashes 5 times at 1S, solenoid works normally |
| 4.50V±0.1 under-voltage | Each sensing LED flashes 10 times at 0.5S, solenoid stops working |
| Recover to 4.80V±0.2 | LED red still indicates under-voltage, flashes 5 times each sensing, solenoid normal |
| Recover to 5.0V±0.2 | Module returns to normal |
| Power-Loss Protection (closed state) | Keep valve closed |
| Power-Loss Protection (open state) | Sudden drop closes valve within 10S |

### 4.5 Anti-Interference & Protection

| Item | Specification |
|------|------|
| ESD | Level 4, air discharge ±15KV, contact ±8KV |
| EMI | Level 2, frequency 80M～1000MHz, field strength 3V/m |
| Fast Transient Burst (EFT) | ±4KV normal operation |
| Light Interference | Incandescent/fluorescent/halogen/daylight/bathroom heater/hairdryer+daylight same outlet/direct sunlight, 15～91cm any direction no false action |
| Module Waterproof | IPX6; sensing window immersed (20cm) 4H no droplets/fogging, normal function |
| Operating Temperature | 5°C ～ 50°C |
| Operating Humidity | 10%RH ～ 95%RH |
| Working Water Pressure | 0.05MPa ～ 0.8MPa |

### 4.6 Reference Standards & Life

| Item | Specification |
|------|------|
| Reference Standards | GB/T 4798.1, GB/T 4798.2, CJ/T 194-2014 Non-contact Water Supply Fixtures |
| Life Test | Over 550,000 cycles |
| Storage Environment | Temperature -20°C～65°C, relative humidity ≤80%RH |
| Potting Requirement | Thickness ≥2mm, fully cover solder pins, no overflow |

---

## V. Installation Instructions

### 5.1 Before Installation

1. Confirm power DC 4.8～6.5V (battery box or 100-240V to 6V adapter).
2. Check water pressure 0.05～0.8MPa, ambient temperature 5～50°C, humidity 10～95%RH.
3. Confirm no continuous strong direct light or mirror direct reflection in front of the sensing window.
4. Clarify fixture type; pre-ship calibrate sensing distance by need (40～85cm range).

### 5.2 Notes

⚠️ Always disconnect power before install/repair.
⚠️ The sensing window must never face mirror material or continuous strong direct light.
⚠️ Sensing distance is factory-calibrated and remote-non-adjustable; batch must be set uniformly within the calibration range.
⚠️ The potted surface and terminals must be intact to avoid water ingress causing failure.

### 5.3 Installation Steps (with complete unit)

1. Place the assembly into the complete-unit pre-embedded box/control cavity, fix and connect the water in/out pipes.
2. Connect the DC power input and the solenoid drive load end.
3. Open water and pressure-test to confirm no leak.
4. Power-on self-check: LED steady 1S, valve switch once, enter standby.
5. Simulate use with a body in the sensing range; verify 2S false-judgment rejection and delayed flush logic.
6. Within 1 minute of power-on use the remote to set flush time (minimum 1S).

### 5.4 Power-On Self-Check

After power-on the LED stays lit 1 second indicating normal power-on, and the solenoid switches once; entering the sensing range the LED flashes once. At low voltage it flashes graded per 4.80V/4.50V. After installation, do in/out simulation in the sensing range to confirm delayed flush and mode meet site needs.

### 5.5 Maintenance

From below 4.80V it flashes to prompt; below 4.50V the solenoid stops working, requiring battery replacement or adapter check. Replacement: disconnect power → open cover → replace same-spec power/battery → re-power self-check. Life over 550,000 cycles, daily maintenance-free; storage note -20～65°C, humidity ≤80%RH.

---

## VI. Applicable Complete Units & Integration Solutions

### 6.1 Companion Complete Units

The KCM-SJ02 is a triangular-ranging dedicated sensor assembly, directly fitting:

- **Squat-Pan Flusher (stall type)**: triangular ranging specifically cures divider reflection and partial body obstruction, fewest false/missed flushes.
- **Urinal Flusher**: fits high-frequency public toilets, multi-material consistent, strong-light immune.
- **Other kitchen/bath sensor ware**: terminals needing stable sensing in complex light and partitioned spaces.

### 6.2 ODM Integration Value

For complete-unit makers and contractors, the KCM-SJ02 turns the hardest task—"stable stall sensing"—into a standardized component: triangular-ranging algorithm, under-voltage/power-loss dual protection, potted waterproofing, and EMC immunity are all built in, so complete-unit makers can ship a finished product by just mounting the body. For contractors doing public restrooms, transport hubs, and school projects, uniformly adopting KCM-SJ02 means stall points no longer constrain install environment and pass acceptance first time, also unifying spares and repair training, lowering long-term holding cost.

---

## Appendix

### A. Core Technology Index

| No. | Technology Name | Application in This Product |
|------|---------|-----------|
| #1 | Triangular-Ranging Sensing Technology | Geometric-angle ranging, no stall misjudgment, material-independent |
| #6 | Low-Power Multi-Stable Agile Sensing Technology | ≤0.2mW standby, long endurance |
| #11 | Dual-Mode Strong-Light-Immunity Anti-Interference Algorithm | 7 light sources + direct sunlight no false action |
| #12 | Military-Grade EMC Technology | ESD level 4, radiation level 2, burst ±4KV |
| #13 | Intelligent Anti-Overflow Power-Off Safety Protection Technology | Graded under-voltage prompt, valve close within 10S of power loss |

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
| Chinese Website | [www.gibo.com.cn](https://www.gibo.com.cn) |
| English Website | [www.gibosensor.com](https://www.gibosensor.com) |
| Service Hotline | 0591-88066000 |
| Company Email | sales@gibol.com.cn |
| Company Address | Building 3, Liangyuan Science Park, High-Tech Zone, Fuzhou City, Fujian Province |

---

> This document is compiled based on the GIBO KCM-SJ02 Triangular-Ranging Sensor Assembly Specification V1.0 (2025.01.16). Parameters are subject to the actual unit. GIBO reserves the final right of interpretation and modification of the technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
