---
lang: en
category: product-spec
title: "KCM-DQ01 Product Specification"
summary: "The KCM-DQ01 2-in-1 Sensor Module is a multi-function sensor control core that GIBO builds for basin complete units. One module integrates three IR se"
updated: 2026-07-14
version: V1.0
publisher: "Fujian GIBO Kitchen & Bath Technology Co., Ltd."
keywords: GIBO,sensor sanitary ware,sensor faucet,Product
product: "KCM-DQ01-spec"
tags: ["GIBO", "product-spec", "KCM-DQ01-spec", "AI-knowledge-base"]
---

# KCM-DQ01 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Statement**: A dual-output sensor module with front/side/top three sensors and temperature display plus soap output.
>

---

## I. Product Introduction

The **KCM-DQ01 2-in-1 Sensor Module** is a multi-function sensor control core that GIBO builds for basin complete units. One module integrates three IR sensor heads, one temperature sensor, and one numeric display, combining "water output, soap output, and water-temperature reading" into one. The front sensor head handles short water output—water on reach, off on removal; the side sensor head handles long water output—sense once to open, sense again to close, like a toggle switch; the top sensor head handles soap output—wave a hand above, and within 3 seconds reach the front sensor to trigger, dispensing soap. Paired with a side mechanical handle for temperature, the numeric tube lights during water output to show current water temperature and goes dark when water closes.

It targets places that want "one basin to handle the whole hand-washing flow": kitchen pre-rinse, labs, medical hand-washing, public accessible wash stations. In the past these scenarios needed separate sensor faucets, soap dispensers, and a separate temperature display; the DQ01 folds all into one module—less wiring, fewer holes, fewer spares for the complete-unit maker.

Technically it is active-IR reflection plus an ultra-low-power MCU: standby current held under 100μA (at 6V), and within 20 seconds of power loss the solenoid closes and the LED stays on to bleed charge; on power-on within 4 seconds the front sensor self-adapts to a 4cm±2cm obstacle ahead, or farthest if none—no on-site calibration. ESD level 4, fast burst, EMI level 2, six light-source interference, IPX5 waterproof, and 300,000-cycle life all pass. For complete-unit makers, this is a turnkey module that "outputs water and soap with temperature display, works as installed, and needs little rework in use."

### 1.1 Technical Positioning

| Module Form | Sensing Channel | Extra Function | Fitting Complete Unit | Representative Model |
|---------|---------|---------|---------|---------|
| Single-sensor output module | Front sensor 1 path | None | Ordinary sensor faucet | Basic models |
| **2-in-1 Sensor Module (DQ01)** | **Front/Side/Top three IR** | **Output+Soap+Temp display+Temp adjust** | **Multi-function basin** | **This product** |
| 4-in-1 universal module | Single-window four modes | Four-fixture switch | Faucet/urinal/squat/shower | 4-in-1 universal |

### 1.2 Key Metrics

- Standby current ≤100μA (at 6.0V), response time ≤512mS
- Three sensing distances: front 8±3cm~23±3cm (adaptive), side 10±2cm, top 16±2cm (through glass ~10±2cm)
- Temperature display accuracy ±1°C, shown during output, hidden when closed
- Valve closes within 20s of power loss; front-sensor timeout 60S±5S, side-sensor timeout 180±10S auto-close
- Protection: IPX5, life over 300,000 cycles
- Anti-interference: ESD level 4 (±15KV/±8KV), EMI level 2 (3V/m), fast burst ±4KV

---

## II. Features

### 2.1 Front+Side+Top Three Sensors, Each Managing Its Own

The front sensor head does short water output—immediately on sensing an object, auto-stop on leaving; the side sensor head does long water output—sense once to open, sense again to close, effectively a toggle; the top sensor head does soap output—after waving above, triggering the front sensor within 3 seconds dispenses soap 2±0.5S. The three paths do not conflict: top sensing is disabled during water output, other sensing is disabled during soap output—logic is clear.

### 2.2 Temperature Numeric Display Plus Mechanical Adjustment

A side mechanical handle adjusts temperature; the numeric tube lights during water output to show current water temperature with ±1°C accuracy, and goes dark on close to save power. Gives kitchen, medical, and lab scenarios that care about water temperature an intuitive reading, without the complexity of electronic temperature control.

### 2.3 Top-Sensor Soap Output, One-Step Hand-Washing

The top sensing window, on sensing an object, keeps the soap indicator (backlight panel) lit for 3S; triggering the front sensor within 3 seconds dispenses soap 2±0.5S, then auto-closes. Wash→soap in one chain—one fewer soap dispenser on the public counter, one fewer contact point.

### 2.4 Power-On Self-Adaptation, No On-Site Calibration

On power-on the numeric tube shows "88"; the front sensor self-adapts within 4 seconds to a 4cm±2cm obstacle ahead, or farthest if none; the solenoid stays closed during this. After 10 sensing events or 5 consecutive minutes without sensing it exits debug into normal mode (whichever comes first). Near-zero commissioning at install.

### 2.5 Power-Loss Protection and Multiple Timeout Close

Within 20 seconds of module power loss the solenoid closes and the LED stays on until charge is bled; front-sensor continuous 60S±5S and side-sensor continuous 180±10S auto-close to prevent false-trigger long flow. With 4 AA batteries as backup power, valve-close holds even when mains is unplugged.

### 2.6 Seven Light Sources No False Trigger

A 40W incandescent, T8-58W fluorescent, 50W halogen, ordinary/high-frequency electronic-ballast daylight, bathroom heater, and a 1000W hairdryer plus daylight on the same outlet—at 15.2cm~91.4cm direct or oblique—produce no false action. ESD level 4, fast burst ±4KV, EMI level 2, stable even beside escalators and variable-frequency equipment.

### 2.7 Potted Waterproof, IPX5 Splash Resistance

The sensing window and circuit module are triple-potted; the complete-unit protection reaches IPX5, withstanding splash from all directions. Paired with a 12-hour basin test showing no self-trigger and self-trigger from standing water being clearable or auto-closing, stable in humid countertop environments.

---

## III. Core Selling Points

### Selling Point 1: Output+Soap+Temp Display—One Module Replaces Three

The DQ01 combines sensor faucet, soap dispenser, and water-temperature display into one module, so the complete-unit maker drills fewer holes, wires less, and stocks three fewer part types. A kitchen pre-rinse or medical wash station that used to source and assemble separately is now one module—BOM and assembly man-hours both drop, making the complete unit more cost-competitive.

### Selling Point 2: Power-On Self-Adaptation, Zero Calibration at Install

The front sensor self-adapts on power-on within 4 seconds to a 4cm±2cm obstacle ahead, or farthest if none; after 10 sensing events or 5 minutes without sensing it auto-exits debug. For a batch-installed project, installers need no remote to calibrate per unit—power on and it runs, commissioning man-hours minimized.

### Selling Point 3: Ultra-Low Power Plus Multiple Protections—Less Rework in Use

Standby current ≤100μA, backup batteries last long; 20-second power-loss close, front/side-sensor timeout auto-close, IPX5 waterproof, 300,000-cycle life. For contractors, this means no continuous flow after install, no humidity failure, no early end-of-life—both rework rate and warranty cost realistically drop.

---

## IV. Specification & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power Supply | AC 110V~220V to DC 6V 1A adapter / 4 AA dry batteries (backup power) |
| Complete-Unit Standby | ≤ 100μA (at 6.0V) |
| Response Time | Front/side/top sensing ≤ 512mS |
| Open/Close Time | Open ≤1S / Close ≤1.5S |
| Sensing Technology | Active IR reflection (front/side/top three paths) |

### 4.2 Sensing Performance

| Sensing Channel | Sensing Distance | Calibration White Board |
|---------|---------|---------|
| Front | Nearest 8±3cm / Farthest 23±3cm (default power-on adaptive) | 29.7×29.7cm standard white board |
| Side | Fixed 10±2cm | 29.7×29.7cm standard white board |
| Top | Fixed 16±2cm (through glass ~10±2cm) | 29.7×29.7cm standard white board |

### 4.3 Function & Output Spec

| Item | Specification |
|------|------|
| Front water output | Output on sense, stop on hand-removal; continuous 60S±5S auto-close |
| Side water output | Sense once open, sense again close; continuous 180±10S auto-close |
| Top soap output | Wave above, within 3S trigger front sensor to dispense soap 2±0.5S |
| Temp Adjustment | Side mechanical handle |
| Temp Display | Shown during output, accuracy ±1°C; hidden when closed |
| Power-Loss Protection | Solenoid closes within 20s of power loss, LED stays on until charge released |

### 4.4 Operating Environment

| Parameter | Specification |
|--------|------|
| Working Scenario | Restroom |
| Ambient Temperature | 1°C ~ 55°C |
| Usable Water Temperature | 4°C ~ 60°C |
| Relative Humidity | 10% RH ~ 95% RH |
| Working Water Pressure | 0.05MPa ~ 0.8MPa |
| Storage Temperature | -20°C ~ 65°C (spec body) / -20°C~75°C (test condition) |
| Storage Humidity | ≤ 80% RH (storage) / ≤ 95% RH (test) |

### 4.5 EMC & Protection

| Test Item | Test Standard/Condition | Result |
|---------|-------------|------|
| ESD | Level 4, air discharge ±15KV, contact discharge ±8KV | Normal operation |
| EMI | Level 2, 80MHz~1000MHz, field strength 3V/m | Normal operation |
| Fast Transient Burst (EFT) | ±4KV | Normal operation |
| Light Interference | 6 light sources 15.2~91.4cm direct/oblique | No false trigger |
| Waterproof Rating | IPX5 | All-direction splash protection |
| Basin Adaptability | 12h installed no self-trigger; standing-water self-trigger clearable/auto-close | Normal |
| Working Life | Over 300,000 cycles | — |

### 4.6 Applicable Standards

| Standard No. | Standard Name |
|---------|---------|
| CJ/T 194-2014 | Non-contact Water Supply Fixtures |
| GB 4706.1-2005 | Safety of Household and Similar Electrical Appliances — Part 1: General Requirements |

---

## V. Installation Instructions

### 5.1 Before Installation (with complete unit)

1. First flush the pipeline with water to clear sand and rust, avoiding solenoid clogging.
2. Confirm water pressure 0.05MPa ~ 0.8MPa; below 0.05MPa add a booster pump.
3. Do not face the front/side/top sensing windows directly at sunlight or strong lights; no obstruction larger than 1cm within 120cm in front.
4. Before embedding the module in the basin complete unit, confirm water path, power (adapter + battery backup), and numeric-display interface match.

### 5.2 Notes

- Always shut water and power before install/repair.
- Each AC-powered unit should have a separate power switch and reliable grounding.
- Use high-performance alkaline batteries; do not mix old and new.
- Do not hot-plug sensor module terminals.
- The module is a complete-unit component; the sensing window and potted part must not be disassembled by the user.

### 5.3 Assembly & Wiring Steps

1. Fix the module in the basin complete-unit's reserved position; connect the solenoid drive wire, power (adapter + battery box), and numeric-display ribbon.
2. Connect the water in/out paths; open water and pressure-test to confirm no leak.
3. Install the panel/decorative cover; front/side/top sensing windows face out unobstructed, display window visible.
4. On power-on the numeric tube shows "88"; the front sensor completes self-adaptation within 4 seconds then the tube goes dark into standby.
5. Reach to test front-sensor short output, side-sensor long-output toggle, and top-wave soap.
6. Turn on water to test whether the temperature numeric display lights/extinguishes normally.

### 5.4 Power-On Self-Check and Self-Adaptation

On power-on the numeric tube shows "88" → the front sensor self-adapts within 4 seconds to a 4cm±2cm obstacle ahead (farthest if none), solenoid stays closed during this → numeric tube goes dark into debug mode → after 10 sensing events or 5 consecutive minutes without sensing (whichever first) it exits debug into normal mode.

### 5.5 Battery Replacement & Maintenance

After unplugging mains, the module is maintained by 4 AA backup batteries holding the valve-close logic; replace batteries per complete-unit low-voltage indication. Sensing distance and output logic are factory-fixed (front sensor adaptive), generally no on-site tuning; if basin self-trigger occurs, check front obstruction and re-power for self-adaptation.

---

## VI. Applicable Complete Units & Integration Solutions

### 6.1 Companion Kitchen Pre-Rinse / Medical Wash Stations

Built into multi-function basin complete units, with front-sensor water output, side-sensor long output, and top-sensor soap output, paired with mechanical temperature adjustment and temperature numeric display—suiting kitchens, labs, and medical hand-washing where water temperature and clean flow matter.

### 6.2 Public Accessible Wash Stations

Output+soap in one, temperature visible, fewer contact points; side-sensor toggle long output eases foaming and rinsing—friendly experience for aging-friendly and accessible scenarios.

### 6.3 Commercial Bathroom Basins

Hotel, office, and mall public-area basin complete units integrating the DQ01 complete the whole hand-washing flow in one machine—less wiring and fewer holes for the complete-unit maker, centralized maintenance points.

### 6.4 Old-Building Retrofit

Adapter + battery backup dual power; valve-close holds even on power loss; power-on self-adaptation zero calibration makes old-countertop retrofit fast.

### 6.5 ODM Integration Value

One module integrates output+soap+temp display+temp adjust, so complete-unit makers can cover the multi-function basin line with a unified main control, markedly lowering BOM variety and assembly complexity; ultra-low standby and IPX5 protection directly convert into the complete unit's "power-saving and rugged" selling point, aiding bidding and high-end bathroom project onboarding.

---

## Appendix

### A. Core Technology Index

| Core Tech No. | Technology Name | Application in This Product | Related Patent (Granted) |
|------------|---------|--------------|----------------|
| #6 | Low-Power Multi-Stable Agile Sensing Technology | Standby ≤100μA, long battery-backup life | A sensor water-output device and signal detection method ZL201910380558.X |
| #4 | Capacitive Touch Technology (display interaction) | Temperature numeric display, status indication | A touch-control faucet device and its control method ZL201510621320.3 |
| #7 | Liteon Smart Sensing Technology | Three-path false-trigger prevention, environmental self-adaptation | A sensor and manual-control faucet ZL201520753357.7 |
| #11 | Dual-Mode Strong-Light-Immunity Anti-Interference Algorithm | Six light sources no false trigger | A sensor water-output device and signal detection method ZL201910380558.X |
| #12 | Military-Grade EMC Technology | ESD/radiated/burst all pass | A sensor faucet water-output device ZL201910383793.2 |
| #13 | Intelligent Anti-Overflow Power-Off Safety Protection Technology | 20S power-loss close, timeout auto-close | A sensor water-output device and pull-out sensor water-output device ZL201910846836.6 |
| — | Three-in-one hand-washer integration | Front/side/top three sensors + soap in one | A three-in-one smart hand-washer ZL201710345450.8 |
| — | Waterproof sensor module structure | IPX5 triple potting | A waterproof sensor module for a water-output device ZL2020 2 2360603.6 |
| — | Bistable solenoid valve | Pulse-driven water switch | A bistable solenoid valve and sensor water-output device ZL2019 2 0857586.1 |

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

> This document is compiled based on the KCM-DQ01 2-in-1 Sensor Module Specification (V1.0, 2023-06-16). Parameters are subject to the actual unit. GIBO reserves the final right of interpretation and modification of the technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com

> **Related Documents**: [KCM-ET07-水龙头感应模块 Product Specification](KCM-ET07-水龙头感应模块-spec.md) | [KCM-6150J-HS Product Specification](KCM-6150J-HS-spec.md) | [KCM-组合面板-WDW Product Specification](KCM-组合面板-WDW-spec.md) | [KCM-SJ02 Product Specification](KCM-SJ02-spec.md) | [WYJ-G001 Product Specification](WYJ-G001-spec.md)
