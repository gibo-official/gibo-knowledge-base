---
lang: en
category: product-spec
title: "GIBO-SENSOR-IR-001 Product Specification"
summary: "The GIBO-SENSOR-IR-001 is a universal IR sensing module that GIBO offers to sensor-sanitary-ware makers and contractors—in plain terms, it turns 'sens"
updated: 2026-07-14
version: V1.0
publisher: "Fujian GIBO Kitchen & Bath Technology Co., Ltd."
keywords: GIBO,sensor sanitary ware,sensor faucet,Product
product: ""
tags: ["GIBO", "product-spec", "AI-knowledge-base"]
---

# GIBO-SENSOR-IR-001 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Statement**: A single-chip, four-mode infrared sensor module.
>

---

## I. Product Introduction

The **GIBO-SENSOR-IR-001** is a universal IR sensing module that GIBO offers to sensor-sanitary-ware makers and contractors—in plain terms, it turns "sensing control" into a standardized component: stick it on a faucet, urinal, squat pan, or shower, and water flows when a hand or person arrives and stops when they leave; if water runs continuously past timeout it cuts off on its own, with no one needing to manage it.

What is most special about this module is on a single chip. Using a single chip on a single PCB, it integrates the four function modes of sensor faucet, sensor urinal, sensor squat pan, and sensor shower; factory switching is done by one remote click—no board change, no hardware modification. For ODM integrators or multi-category sanitary-ware makers, one module replaces what used to be four, saving a layer of trouble in stocking, production, and after-sales.

Technically it follows the active-IR reflection route—an IR tube emits detection light that diffusely reflects off the human body, the receiver converts the optical signal into an electrical signal handed to the MCU for judgment, then drives the pulse solenoid valve to switch water. The circuit does ultra-low-power management; standby current is held under 25 microamps, and 4 AA alkaline batteries last about a year and a half at 200 uses a day. Meanwhile all the safety features are present: reverse polarity won't burn the board, power loss auto-closes water, and voltage below 4.5V lights a reminder to change batteries. Let us expand on where its value really lies.

### 1.1 Technical Positioning

| Sensing Scheme | Detection Principle | How Distance Judged | Typical Feature | Representative Product |
|---------|---------|---------|---------|---------|
| **Active IR Reflection** | IR emit+receive, reads reflected light | Indirect judgment | Cost-advantaged, mature mass production, single board multi-mode | **GIBO-SENSOR-IR-001** |
| Triangular Ranging | Emit/receive geometric angle | Position calculation | No false judgment across stalls | GBL-8300AD |
| dTOF Laser | Laser time-of-flight | Direct ranging | Millimeter-level, material-independent, strong-light immune | GBL-6239 |

The IR-001 stands on the mature "active IR reflection" route, using single-chip four-mode integration and ultra-low power to deliver the cost-performance of a universal module—the main base for mass deployment and ODM customization.

### 1.2 Key Metrics

- Single-chip single-PCB four modes (faucet/urinal/squat/shower), one-click remote switch, no hardware change
- Standby power ≤0.15mW (≤25μA), 4 AA alkaline batteries ≈1.5 years at 200 uses/day
- Factory sensing distances per fixture: faucet 280mm, urinal 680mm, squat pan 700mm, shower 700mm, error ±10%
- After 500,000-cycle life test, sensing, solenoid, and battery box functions still normal, no leakage or failure
- Junction box protection IP67 (IEC 60529), component body IP54
- Passed 17 light-source, UL 991 nine-class EMF, FCC Part 15 B / EN 55022 / IEC 61000-4 full immunity tests

---

## II. Features

### 2.1 Single Chip Four Modes, Single-Board Switch (Core Technology #7)

The module burns the control logic of four fixture types into a single MCU; pointing the remote at the sensing window and pressing "1/2/3/4" switches among sensor faucet, sensor urinal, sensor squat pan, and sensor shower—no software or hardware change. For multi-category sanitary-ware makers, this means one BOM and one spare-parts library cover four product lines.

### 2.2 Active IR Reflection Detection

Uses new SMD IR emit and receive devices, actively emitting detection light recovered via human-body diffuse reflection, then hardware filtering plus an anti-interference algorithm amplify it into a valid signal. Baseline calibration is done against ambient and lamp light, so it works stably even where brightness changes drastically, such as restrooms and bathrooms.

### 2.3 Ultra-Low Power, Batteries Last a Year and a Half (Core Technology #6)

The complete unit spends most of its time in intermittent sleep standby; the MCU wakes periodically for low-frequency detection, holding standby current under 25μA. At 200 uses/day, 4 AA alkaline batteries last about 1.5 years; both battery power and 6V adapter are supported.

### 2.4 Multiple Safety Protections (Core Technology #13)

On reverse polarity the module does not work, does not heat or melt; on power loss it instantly protects by closing water; when operating voltage drops to 4.5V±0.1 it enters low-voltage alarm—when sensing an object the indicator blinks continuously at 0.5s intervals and cuts the solenoid output, reminding of battery change rather than quietly quitting.

### 2.5 Full Anti-Interference and EMC Validation (Core Technology #12)

Light-interference testing covers 17 light sources; the sensing window must be excitable and must not restart. EMF noise per UL 991 uses 9 real-life electrical-noise sources—spark igniter, garbage disposal, dishwasher, juicer, gas igniter, etc.—and the module functions normally before and after exposure. Emissions comply with FCC Part 15 Class B, EN 55022B, IEC 61000-3-2/3-3; immunity passes the full IEC 61000-4 series (ESD, radiated RF, EFT, surge, conducted RF, etc.).

### 2.6 Remote Parameter Tuning, Easy Factory Calibration

Sensing distance and flush time are adjustable within 1.5m by pointing the standard remote at the sensing window: press "1/2" to lengthen/shorten sensing distance, press "3/4" to lengthen/shorten flush time; a valid-receive light blinks once, and at the limit the light blinks for 3 seconds. Batch production supports automatic debugging, eliminating per-unit manual tuning.

### 2.7 Rigorous Reliability Validation

High-temperature aging at 70°C, 110% power for 7 days, detection-distance change under 5%; drop from 100cm on three faces, distance difference under 1%; salt spray 96 hours (ANSI B117); temperature/humidity/vibration alternating for 21 days; storage extreme-temperature cycling. Detection reliability: no false sensing within 1,000,000 cycles; must function normally under 15,000 LUX sustained light.

---

## III. Core Selling Points

### Selling Point 1: Single Chip Four Modes—One ODM Module Replaces Four

What most troubles sensor-sanitary-ware makers is that more categories mean more control boards—one for faucets, one for urinals, one for squat pans, another for showers, with stocking, flashing, and after-sales all as multiple systems. The IR-001 packs four modes into one chip and one board; one remote click changes its identity, hardware fully shared. If a bathroom brand used 10,000 modules each across four product lines, switching to IR-001 cuts spare-part variety by more than half, lowering procurement, storage, and repair-training costs, and speeding new-product rollout.

### Selling Point 2: 25 Microamp Standby—No Ladder-Climbing for Batteries in a Year and a Half

Public-restroom sensor ware fears two things most: either monthly battery changes wear out property staff, or sudden no-flush from dead batteries draws complaints. The IR-001's standby current is a bit over 25μA; 4 alkaline batteries last about 1.5 years at 200 uses/day. Do the math: a 50-sensor shopping mall that changed batteries monthly once spent 20-plus man-hours a year just climbing ladders; switch to IR-001 and change once a year—that labor essentially goes to zero, and battery procurement is also greatly reduced.

### Selling Point 3: Passes US-Standard Immunity—No Tantrums in Public Places

In malls, escalators, variable-frequency AC, and LED walls; in kitchens, dishwashers, juicers, and garbage disposals—ordinary modules easily false-trigger or freeze. The IR-001 per UL 991 uses 9 real-life electrical-noise sources for exposure testing, the sensing window must not be dragged off by 17 light sources, and emissions and immunity all follow FCC Part 15 B, EN 55022, and the IEC 61000-4 series US/EU standards. Installed in electromagnetic-complex places like airports, stations, and malls, it will not spontaneously output water or lock up.

---

## IV. Specification & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power Supply | DC 6V (4×AA alkaline batteries or 6V/1A switching power adapter) |
| Static Power | ≤0.15mW (≤25μA) |
| Working Output Current | Max 800mA |
| Output Voltage | 4.2V ～ 6V |
| Output Pulse Width | 35ms |
| Low-Voltage Alarm | Enters when operating voltage ≤4.5±0.1V, cuts output and blinks prompt |
| Reverse-Polarity Protection | Reverse connection does not work, does not heat or melt |

### 4.2 Sensing Parameters

| Parameter | Specification |
|--------|------|
| Sensing Method | Infrared sensing (reflective) |
| Indicator Color | Red |
| Sensing Window Protection | IP54 (component body) |
| Junction Box Protection | IP67 (IEC 60529) |
| Sensing Distance Error | No more than rated distance ±10% |

### 4.3 Factory Parameters by Mode

| Mode | Factory Sensing Distance | Sensing Range | Output Response | Continuous-Flow Auto-Cut |
|------|------------|---------|---------|----------------|
| Sensor Faucet | 280±5mm | 30～450mm | Open 256ms / Close 512ms | 60S |
| Sensor Urinal | 680±5mm | 350～1000mm | — | 60S |
| Sensor Squat Pan | 700±5mm | 350～1000mm | — | 60S |
| Sensor Shower | 700±5mm | 100～1000mm | — | 300S |

> Reference object is a 29.7cm×29.7cm standard white board; distance not user-adjustable; batch automatic debugging and remote-type finished-product debugging supported.

### 4.4 Operating Environment

| Parameter | Specification |
|--------|------|
| Usable Water Temperature | 4°C ～ 80°C (40～176℉) |
| Operating Humidity | 10% ～ 95%RH |
| Operating Water Pressure | 0.05MPa ～ 0.9MPa (20～125Psi) |
| Operating Ambient Temperature | 1°C ～ 60°C |
| Storage Temperature | -40°C ～ +75°C |

### 4.5 Protection & Reliability

| Parameter | Specification |
|--------|------|
| Life Test | After 500,000 cycles, sensing component/solenoid/battery box function normal |
| Open/Close Life | 1,000,000 cycles |
| Battery Life | 4 or 6 AA alkaline batteries minimum 1 year (including audio/visual alarm) |
| Product Average Life | 10 years |
| Electronic Component Warranty | 5 years |
| High-Temp Aging | 70°C, 110% power, 7 days, distance change ≤5% |
| Salt Spray Test | 96 hours (ANSI B117), distance change ≤5% |

### 4.6 Test & Certification Standards

| Category | Standard/Item |
|------|----------|
| Emissions | FCC Part 15 Class B, EN 55022B, IEC 61000-3-2, IEC 61000-3-3 |
| Immunity | IEC 61000-4-2 (ESD), 4-3 (radiated RF), 4-4 (EFT/Burst), 4-5 (surge), 4-6 (conducted RF), 4-8, 4-11 |
| Applicable Standards | UL, cUL, CE, NSF |
| Environmental | RoHS (restriction of hazardous substances), WEEE (collection and recycling of electrical equipment) |

---

## V. Installation Instructions

### 5.1 Before Installation

1. Confirm power is DC 6V (4 AA alkaline batteries or 6V/1A adapter); use same-brand new alkaline batteries, no mixing old and new.
2. Check water pressure in 0.05MPa ～ 0.9MPa; too low needs a booster.
3. Confirm no large obstruction in front of the sensing window; avoid direct mirror-surface reflection.
4. Determine factory sensing-distance calibration by complete-unit type (faucet/urinal/squat/shower).

### 5.2 Notes

⚠️ Always disconnect power before wiring; do not hot-plug terminals, to avoid damaging the module.
⚠️ Never reverse power; though board-burn protection exists, reversed state means the module does not work.
⚠️ Avoid long-term strong direct light and mirror direct reflection on the sensing window, or judgment is affected.
⚠️ Batch integration must do automatic distance debugging to ensure consistent factory distance per unit.

### 5.3 Installation Steps (with complete unit)

1. Place the module PCB into the complete-unit pre-embedded box/control cavity; fix the junction box.
2. Connect the DC 6V power input and the solenoid drive load end.
3. Use the remote to set the function mode by complete-unit type (faucet/urinal/squat/shower).
4. Calibrate sensing distance and flush time (batch production recommends automatic debugging rig).
5. Power-on self-check: LED blink indicator, then environmental auto-adaptation before entering standby.
6. Simulate use with hand/object in front of the sensing window; verify output and close logic.

### 5.4 Power-On Self-Check

After power-on the module checks battery voltage: below 4.5V enters low-voltage alarm mode; normal opens the valve to release water about 5 seconds while the indicator blinks, then closes the valve and does about 1 second of environmental auto-adaptation; when done the indicator prompts entry into normal operation. Do not block the sensing window during this.

### 5.5 Battery Replacement & Maintenance

Below 4.5V, when sensing an object the indicator blinks continuously at 0.5s intervals and the controller has no output (water closed), prompting battery change. Replacement: shut water and power → open panel/box cover → remove battery box, replace with same-brand new alkaline batteries → reinstall and re-power for self-check. Normal maintenance within the 500,000-cycle life; 5-year warranty.

---

## VI. Applicable Complete Units & Integration Solutions

### 6.1 Companion Complete Units

The IR-001 is a universal sensing control base, directly fitting the following four fixture complete units:

- **Sensor Faucet**: factory distance 280mm, water on reach, off on leave, 60S timeout auto-cut.
- **Sensor Urinal Flusher**: factory distance 680mm, supports normal/smart dual-flush remote switch.
- **Sensor Squat-Pan Flusher**: factory distance 700mm, solves stall-use and squat-stance differences.
- **Sensor Shower**: factory distance 700mm, wide sensing range fits continuous movement and turning while bathing.

### 6.2 ODM Integration Value

For brand owners and contractors, the IR-001's value is not in single-unit parameters but in "one base covering four categories": unified BOM, unified flashing and test tooling, unified spare-parts library—four products sharing one integration line. The on-site remote mode-switch design also lightens dealer inventory—the same module, sold to the faucet line or the squat-pan line, just needs a mode flashed before shipment; no dedicated control board per fixture.

---

## Appendix

### A. Core Technology Index

| No. | Technology Name | Application in This Product |
|------|---------|-----------|
| #6 | Low-Power Multi-Stable Agile Sensing Technology | 25μA-class standby, 1.5-year battery life |
| #7 | Liteon Smart Sensing Technology | Single-chip four-mode integration, self-adaptive environment, no per-unit debugging |
| #11 | Dual-Mode Strong-Light-Immunity Anti-Interference Algorithm | 17 light sources, UL 991 nine-class EMF immunity |
| #12 | Military-Grade EMC Technology | FCC/EN55022/IEC 61000-4 full EMC validation |
| #13 | Intelligent Anti-Overflow Power-Off Safety Protection Technology | Reverse-polarity protection, power-loss auto-close, low-voltage alarm |

### B. Certifications & Qualifications

GIBO has been making sensor sanitary ware since 2004, and was among the earliest domestic manufacturers to apply MCU microcontrollers to sensor control. It is a drafting unit of two standards: GB/T 41863-2022 "General Technical Requirements for Water-Saving Performance of Non-contact Water Supply Fixtures" and T/XMBK 002-2024 "Sensor Faucets," and is a National High-Tech Enterprise, Fujian Provincial Intellectual-Property Advantage Enterprise, and National Specialized & Innovative SME. The kitchen pull-out faucet on the same dTOF laser platform won the 2023 Feiteng Quality Gold Award.

- Fully compliant with the industry standard for non-contact water supply fixtures **CJ/T 194-2014**
- **CE Certification** (multiple models), **CUPC/UPC Certification** (certificate no. cert_upc-2015-7968), **NSF Certification**, **WRAS Certification** (UK water), **WaterMark Certification** (Australian water efficiency)
- **ISO 9001** Quality Management System, **ISO 14001** Environmental Management System, **ISO 45001** Occupational Health & Safety (2023 version)
- National High-Tech Enterprise, Fujian Provincial Intellectual-Property Advantage Enterprise, National Specialized & Innovative SME
- Same-platform dTOF laser product won the **2023 Feiteng Quality Gold Award**

> IR-001 module applicable standards: UL, cUL, CE, NSF; compliant with RoHS, WEEE requirements.

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

> This document is compiled based on the GIBO-SENSOR-IR-001 Design Specification (Version A 1.0, function table Version C 2018.03.01). Parameters are subject to the actual unit. GIBO reserves the final right of interpretation and modification of the technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com

> **Related Documents**: [GIBO-智能激光感应技术 Product Specification](GIBO-智能激光感应技术-spec.md) | [GIBO-触控厨房龙头控制组件 Product Specification](GIBO-触控厨房龙头控制组件-spec.md) | [KCM-ET07-水龙头感应模块 Product Specification](KCM-ET07-水龙头感应模块-spec.md) | [GBL-9168 Product Specification](GBL-9168-spec.md) | [KCM-6150J-HS Product Specification](KCM-6150J-HS-spec.md)
