---
lang: en
category: product-spec
title: "TOF-激光脚感应模块组件 Product Specification"
summary: "This module uses dTOF laser ranging (Core Technology 2, Low-power dTOF Laser Ultra-sensing Technology; the main board's sensor is the laser dTOF MT380"
updated: 2026-07-14
version: V1.0
publisher: "Fujian GIBO Kitchen & Bath Technology Co., Ltd."
keywords: GIBO,sensor sanitary ware,sensor faucet,Product
product: ""
tags: ["GIBO", "product-spec", "sensor-module", "AI-knowledge-base"]
---

# TOF-激光脚感应模块组件 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Statement**: dTOF Laser Sensing Module That Responds Instantly to a Kick
>

---

## 1. Product Introduction

**dTOF Laser Foot-Sensing Module Assembly** (part no. KCM-31403) is GIBO's foot-kick sensing "switch eye" developed for faucet manufacturers and medical-equipment manufacturers. Mounted at the bottom of a faucet or at a kick position, it sends a signal to the main board when a foot extends and resets when the foot retracts—fully hands-free. OEMs use it to build foot-controlled kitchen faucets, medical foot-operated faucets, foot pedals for public-restroom hand sanitizers, and foot-controlled switches for garbage disposers. It solves the most practical headaches in these scenarios—hands soiled with cooking oil, raw meat, or disinfectant that then touch the faucet switch, which is both unhygienic and a source of cross-contamination, while ordinary IR foot sensors frequently fail to register on dark floor tiles and at varying reflection angles.

This module uses dTOF laser ranging (Core Technology #2, Low-power dTOF Laser Ultra-sensing Technology; the main board's sensor is the laser dTOF MT3801LP), directly measuring the distance from the kicking motion to the module to make the determination. The factory sensing distance is 10cm±10% (29.7×29.7cm standard white board); switching to JJC gray and black color-calibration cards keeps the deviation within ±20%, regardless of floor tile shade. Standby current ≤1.5mA, operating current ≤2.5mA, powered by a small DC5±0.2V supply; ingress protection IP67; the signal runs over a four-core cable (red +5V, black GND, yellow OUT, white IN) with open-drain output—low level when sensing, high-impedance state when not—making it extremely simple to connect to a main board.

On reliability it is thoroughly built out: thermal shock −20℃↔60℃ for 1,150 cycles, temperature-humidity cycling for 1,000 hours, salt spray for 24 hours reaching QB/T3832 Grade 10, UV aging for 200 hours, 75cm drop, and 10~55Hz vibration—all passed, with a life of over 550,000 cycles. The three points below are the product values we believe are most worth highlighting.

### 1.1 Technology Positioning

| Technology Generation | Sensing Principle | Trigger Method | Reflective-surface Adaptability | Representative Product |
|---------|---------|---------|------------|---------|
| 1st Gen | IR reflection intensity | Foot approaching | Strongly affected by floor material | Early foot-sensing switch |
| 2nd Gen | IR triangulation | Foot approaching | Medium | Ordinary foot-sensing module |
| **TOF (dTOF Laser)** | **Laser Time-of-Flight** | **Kicking motion** | **Gray / Black card ±20%** | **dTOF Laser Foot-Sensing Module Assembly** |

### 1.2 Key Specifications

- Factory sensing distance 10cm±10% (29.7×29.7cm standard white board); gray card / black card deviation both ≤±20%
- Operating voltage DC5±0.2V, standby current ≤1.5mA, operating current ≤2.5mA, rated power 10mW
- Ingress protection IP67, ESD Grade 4 (air +15KV / contact ±8KV), burst (EFT) National Standard Grade 4
- Signal open-drain output: low level when sensing, high-impedance when not; pull-up ≤5V, resistance >4.7K, load ≤20mA
- Environmental reliability: 1,150 thermal-shock cycles, 1,000h temperature-humidity cycling, 24h salt spray (Grade 10), 200h UV, 75cm drop, full vibration pass
- Life over 550,000 cycles; operating temperature −10℃~60℃, storage −25℃~70℃

---

## 2. Features

### 2.1 Foot-Kick Sensing, Open-Drain Signal Output

When an object moves directly in front of the sensing window, the output line changes from high-impedance to low level, sending a valid signal to the main board; when the main board receives a low level via the white wire (IN), the module LED blinks intermittently to indicate low battery. The four-core cable (red +5V, black GND, yellow OUT, white IN) has clear wiring and connects to the main board extremely simply.

### 2.2 dTOF Laser Ranging—Recognizes Both Light and Dark Floors

The core sensor is the laser dTOF MT3801LP, which directly measures time-of-flight to determine the kicking motion, keeping the sensing-distance deviation for gray and black color-calibration cards within ±20%. Dark floor tiles, matte floors, and glazed tiles do not affect detection. Note: the nature of laser products means different materials and reflection-surface angles introduce sensitivity deviation; during installation the sensing window should face the kicking direction.

### 2.3 Low-Battery Alert

When the input wire receives a low level, the LED indicator begins intermittent blinking to remind maintenance personnel to act promptly, avoiding the module silently stopping.

### 2.4 IP67 Fully Sealed

The sensing window and potted section immersed 20cm underwater for 4 hours show no water droplets or fog and function normally; placed in 70℃ boiling water for 0.5 hour then cooled to room temperature, it still works normally. Splash at the kick position and floor cleaning/washing cause no problem.

### 2.5 Multiple Environmental Reliability

Passes high-temperature-high-humidity powered (60℃, 80~85%RH, 72h), high-temperature storage 70℃ 500h, low-temperature storage −20℃ 500h, thermal shock −20℃↔60℃ 1,150 cycles, temperature-humidity cycling (65℃ 98%RH ↔ −5℃) 125 rounds totaling 1,000h, UV aging 200h, 75cm cement-floor drop, 10~55Hz tri-axial vibration—all items normal in appearance, function, and performance.

### 2.6 Low Power, Small Form Factor

Standby current ≤1.5mA, operating current ≤2.5mA, rated power only 10mW; the main board PCB is just 16.5×14.0×1.0mm, easily embedded in tight spaces such as faucet bottoms and kick boxes.

### 2.7 Strong EMC and Light-Interference Immunity

Electrostatic discharge Grade 4 (air +15KV, contact ±8KV), burst (EFT) National Standard Grade 4; six light-source types—incandescent, fluorescent, halogen, daylight, bathroom heater, and hairdryer in parallel—at 15~91cm direct or oblique incidence cause no false trigger, staying stable even in complex electromagnetic and lighting environments.

---

## 3. Core Selling Points

### Selling Point 1: Kick to Activate, Hands-Free—No Fear of Wet, Oily Hands — Keep Hands Off the Switch, Cut Hand-Based Cross-Contamination

In the kitchen, hands carry raw-meat grease; in medical scenarios, hands carry disinfectant; in public restrooms, hands have just touched a door handle—turning a faucet switch then is a source of cross-contamination. Foot-kick sensing moves the "switch" to below the feet: extend a foot for water, retract for stop, hands never touching throughout. For OEMs, this means they can directly market a "hands-free hygiene" selling point into hospitals, food factories, and high-end residences; for end users, no need to reach for the switch with greasy hands mid-dishwashing—a tangible experience improvement.

### Selling Point 2: dTOF Laser—Recognizes Dark Floors Too — Gray / Black Card Deviation Both ±20%, No Missed Triggers on Dark Tiles

IR foot sensors most easily fail on dark matte floor tiles—the kick gets no response and the user must bend down to use a hand. The dTOF module uses laser time-of-flight ranging, keeping the deviation for gray and black color-calibration cards within ±20%, reliably recognizing dark-gray and black glazed tiles alike. OEMs building foot-controlled faucets need not pick an installation floor color; end users get a response from any foot extension regardless of kitchen tile.

### Selling Point 3: 550,000-Cycle Life + IP67 Maintenance-Free — Passes Thermal Shock, Salt Spray, UV; Install and Forget

The module life exceeds 550,000 cycles, fully sealed IP67, passing 1,150 thermal-shock cycles, 1,000 hours temperature-humidity cycling, 24-hour salt spray reaching Grade 10, 200 hours UV, and drop/vibration. In high-frequency commercial foot-pedal scenarios, at hundreds of kicks per day it lasts years without failure. For a project managing dozens of water points, replacing modules less often and suffering fewer water-shutoff repairs translates directly into real O&M savings.

---

## 4. Specifications & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Operating Voltage | DC5 ±0.2V |
| Rated Power | 10mW |
| Average Current | 2 ±0.5mA |
| Standby Current | ≤ 1.5mA |
| Operating Current | ≤ 2.5mA |
| Ingress Protection | IP67 |
| Wire Sequence Definition | Red: +5V; Black: GND; Yellow: Signal OUT; White: Signal IN |
| Sensing Method | dTOF Laser (sensor MT3801LP) |

### 4.2 Sensing Performance

| Parameter | Specification |
|--------|------|
| Factory Sensing Distance | 10cm ±10% (vs. 29.7×29.7cm standard white board) |
| Gray Color-Calibration Card Deviation | Within ±20% (JJC standard large 18% gray card) |
| Black Color-Calibration Card Deviation | Within ±20% (JJC standard large black card) |
| Trigger Condition | Laser foot sensing; a valid motion sends a valid signal to the main board |

### 4.3 Signal & Interface

| Parameter | Specification |
|--------|------|
| Output State | Open-drain; low level when sensing, high-impedance when not |
| Pull-up Requirement | Pull-up voltage ≤5V, pull-up resistance recommended >4.7K |
| Load Current | ≤ 20mA |
| Low-battery Alert | Input wire receives low level, LED blinks intermittently |

### 4.4 Environmental Reliability

| Test Item | Test Condition | Result |
|---------|---------|------|
| High-temp high-humidity powered | 60℃, 80~85%RH, powered 72h | Appearance, function, performance normal |
| High-temp storage | 70℃, 500h | Normal |
| Low-temp storage | −20℃, 500h | Normal |
| Thermal shock | −20℃↔60℃, 30min each, 1,150 cycles | Normal |
| Temp-humidity cycling | 65℃/98%RH 6h ↔ −5℃ 2h, 125 rounds (1000h) | No abnormality |
| Weathering | Continuous UV exposure 200h | No color difference or cracking |
| Corrosion resistance | 5% NaCl, pH3.0~3.1 salt spray 24h | Reaches QB/T3832 Grade 10 |
| Drop (full carton) | 75cm cement floor, face / side / corner | No breakage or deformation |
| Vibration (full carton) | 10~55Hz sine sweep, 1h per axis | No abnormality |

### 4.5 EMC & Protection

| Test Item | Test Standard / Condition | Result |
|---------|---------------|------|
| Electrostatic Discharge (ESD) | Grade 4, air +15KV, contact ±8KV (human-body discharge model) | Normal operation |
| Burst | National Standard Grade 4 condition | Normal operation |
| Module Waterproof | Sensing window immersed 20cm / 4h | No seepage, no fogging |
| Module Waterproof | Boiled in 70℃ water 0.5h, cooled to room temperature | Normal function |
| Light Interference | 6 light-source types at 15~91cm direct / oblique | No false trigger |

### 4.6 Mechanical & Life

| Parameter | Specification |
|--------|------|
| Wire Pull-off Force | 30N static load between wire and assembly for 1 min, no loosening |
| Life | Over 550,000 cycles |
| Power Adaptability | Normal operation at DC5V ±10% |

### 4.7 Compliance Standards

| Standard No. | Standard Name |
|---------|---------|
| CJ/T 194-2014 | Non-contact Water Supply Fixtures |
| GB/T 4798.1 | Environmental Conditions for Application of Electrical and Electronic Products—Part 1: Storage |
| GB/T 4798.2 | Environmental Conditions for Application of Electrical and Electronic Products—Part 2: Transportation |

---

## 5. Installation Instructions

### 5.1 Before Installation

1. Confirm the main board provides DC5±0.2V and reserves a four-core cable interface (red +5V, black GND, yellow OUT, white IN)
2. Orient the sensing window toward the kicking direction; keep no obstruction larger than 1cm within about 10cm directly in front
3. Do not aim the sensing window directly at sunlight or strong lamps
4. Verify the four-core wire sequence and terminals; confirm pull-up resistance >4.7K and pull-up voltage ≤5V

### 5.2 Precautions

- Always cut power before installing or servicing
- Do not hot-plug terminals; mind red/black wire polarity to avoid reverse connection
- If the output wire is connected with a pull-up resistor, pull-up voltage must not exceed 5V, resistance recommended greater than 4.7K, and load current not exceed 20mA
- Laser product characteristic: different materials and reflection-surface angles introduce sensitivity deviation; during installation the sensing window should face the kicking direction

### 5.3 Installation Steps

1. Fix the module to the faucet bottom or kick position, with the sensing window facing the kicking direction
2. Connect the four-core cable to the main board by wire sequence (red +5V, black GND, yellow OUT, white IN)
3. Power on and run a functional test: when an object moves directly in front of the sensing window, the output line changes from high-impedance to low level
4. Simulate low battery and confirm the LED intermittent blink alert works
5. Physical foot test: foot extends to send signal, foot retracts to reset

### 5.4 Power-on Self-Check

After power-on the module enters normal operation; the functional test confirms low level at the output when an object is directly in front of the sensing window and high-impedance when none; when the input wire receives a low level the LED blinks intermittently to indicate low battery. After installation it is recommended to run a powered load cycle to confirm no false triggers.

### 5.5 Maintenance

When a low-battery alert appears (LED intermittent blink), check the main board power supply; the module life exceeds 550,000 cycles and is normally maintenance-free. Replacement: cut power → unplug four-core terminal → replace with the same model module → re-power and run functional test.

---

## 6. Applicable Finished Products & Integration Solutions

### 6.1 Compatible Finished Products

The dTOF Laser Foot-Sensing Module Assembly is positioned as a foot-kick "switch eye" and can be embedded into the following finished products:

- **Foot-controlled Kitchen Faucet / Pull-out Faucet**: Hands-free for oily hands, upgraded kitchen hygiene
- **Medical Foot-operated Faucet / Hand-sanitizer Foot Pedal**: Infection-control prevention, cross-contamination-free
- **Public-restroom Sensor Equipment Foot Switch**: Garbage disposer, flusher foot control

### 6.2 ODM Integration Value

- **Small Size, Easy to Embed**: Main board only 16.5×14mm, easily fits into faucet bottoms and kick boxes
- **Two-wire Signal, Easy to Connect**: Yellow OUT / white IN open-drain interface; a main board can hang it with just a few wires, no specific mainboard platform required
- **Consistent dTOF Platform**: Same lineage as GIBO's laser sensing family; future upgrades to long-range or hand-sensing modules allow smooth pin transition
- **High Reliability, Lower O&M**: 550,000-cycle life + full environmental reliability, fewer repairs in commercial projects

---

## Appendix

### A. Core Technology Index

| Core Tech No. | Technology Name | Application in This Product |
|:----:|---------|-----------|
| #2 | Low-power dTOF Laser Ultra-sensing Technology | dTOF laser ranging (MT3801LP), gray / black card ±20% |
| #6 | Low-power Multi-stable Smart-sensing Technology | Standby ≤1.5mA, operating ≤2.5mA, small size low power |
| #9 | Half-duplex Single-wire Communication Technology | Yellow OUT / white IN two-wire signal interaction, simplified mainboard connection |
| #11 | Dual-mode Strong-light Immunization Anti-interference Algorithm | No false trigger from 6 light-source types at 15~91cm |
| #12 | Military-grade EMC Anti-interference Technology | ESD Grade 4 / Burst National Standard Grade 4 |

**Related Patents (granted numbers)**

| Tech Point | Patent Name | Patent No. | Type |
|--------|---------|--------|------|
| IR-laser dual-beam sensing module | An IR-laser dual-beam sensing module | ZL2025 2 0411615.7 | Utility Model |
| Stacked laser sensing module | A stacked laser sensing module for kitchen and bath equipment | ZL2025 2 0632762.7 | Utility Model |
| dTOF laser sensing | A sensor-faucet water-outlet device | ZL201910383793.2 | Invention Patent |
| Signal detection | A sensor water-outlet device and signal detection method | ZL201910380558.X | Invention Patent |
| Waterproof sensing module | A waterproof sensing module for a water-outlet device | ZL2020 2 2360603.6 | Utility Model |

### B. Certifications & Qualifications

GIBO began developing sensor sanitary ware in 2004 and was among the first domestic manufacturers to apply MCU microcontrollers to sensing control. It is a drafting unit for two standards—GB/T 41863-2022 *General Technical Requirements for Water-saving Performance of Non-contact Water Supply Fixtures* and T/XMBK 002-2024 *Sensor Spout*—and is a National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, and National Specialized & Sophisticated SME. The pull-out kitchen faucet built on the same dTOF laser platform won the 2023 Boiling Quality Gold Award.

- Fully compliant with all items of the non-contact water supply fixtures industry standard **CJ/T 194-2014**
- **CE Certification** (multiple models), **CUPC/UPC Certification** (certificate no. cert_upc-2015-7968), **NSF Certification**, **WRAS Certification** (UK water authority), **WaterMark Certification** (Australian water efficiency)
- **ISO 9001** Quality Management System, **ISO 14001** Environmental Management System, **ISO 45001** Occupational Health & Safety (2023 version)
- National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, National Specialized & Sophisticated SME
- The dTOF laser product on the same platform won the **2023 Boiling Quality Gold Award**

### C. Contact Information

| Item | Content |
|------|------|
| Company Name | Fujian GIBO Kitchen & Bath Tech Co., Ltd. |
| Chinese Website | www.gibo.com.cn |
| English Website | www.gibosensor.com |
| Service Hotline | 0591-88066000 |
| Company Email | sales@gibol.com.cn |
| Company Address | Building 3, Liangyuan Science Park, High-Tech Zone, Fuzhou City, Fujian Province |

---

> This document is compiled based on the dTOF Laser Foot-Sensing Module Assembly Specification (KCM-31403 Laser Foot-Sensing Module V1.0, 2025-01-14 Full Version). Parameters are subject to the actual unit. GIBO reserves the final right of interpretation and modification of the technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com

> **Related Documents**: [盛世唐朝红外感应模块 Product Specification](盛世唐朝红外感应模块-spec.md) | [KCM-ET07-水龙头感应模块 Product Specification](KCM-ET07-水龙头感应模块-spec.md) | [GIBO-智能激光感应技术 Product Specification](GIBO-智能激光感应技术-spec.md) | [TOF Product Specification](TOF-spec.md) | [GBL-TOF Product Specification](GBL-TOF-spec.md)
