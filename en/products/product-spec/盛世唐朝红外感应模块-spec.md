---
title: "盛世唐朝红外感应模块 Product Specification"
description: "The Shengshi Tangchao Infrared (IR) Sensor Module (KCM-SSTC-01) is a 'water outlet + soap dispensing + temperature display' three-in-one sensor contro"
keywords: GIBO,sensor sanitary ware,sensor faucet,Product
classification: Product
language: en
publisher: "Fujian GIBO Kitchen & Bath Technology Co., Ltd."
version: V1.0
date: 2026-07-14
---
# 盛世唐朝红外感应模块 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Statement:** Infrared sensor module integrating water outlet and soap dispensing with a digital water-temperature display
>

---

## 1. Product Introduction

The **Shengshi Tangchao Infrared (IR) Sensor Module (KCM-SSTC-01)** is a "water outlet + soap dispensing + temperature display" three-in-one sensor control board that GIBO supplies for smart bathroom finished products. It packs two infrared sensor heads in one module: one for water outlet and one for soap dispensing, plus a digital temperature display and an LED light strip. Finished-product manufacturers mount it on a basin or faucet so users get water by extending one hand, soap by the other, and can see the water temperature directly—without a separate temperature display screen.

This module is mainly used in finished products such as bathroom basins, sensor hand washers, and soap-dispensing integrated faucets. The two sensing channels never conflict: soap dispensing locks out water outlet, and water outlet locks out soap dispensing, so a single hand won't spray both water and foam at once. During water outlet, the light strip changes color by water temperature—green below 41℃ and red above 42℃ in Celsius mode, with a corresponding scheme in Fahrenheit mode—so elderly and child users can tell at a glance whether the water is cold or hot, and hold back before scalding. A Hall sensor is hidden in the handle (an extension of Core Technology #4); lifting the handle shuts off all sensing and water outlet instantly, cutting the water cleanly.

Under the hood is GIBO's proven active infrared reflection architecture (Core Technologies #6/#7), with standby current held below 80μA. It works with both a battery box and an AC-to-6V adapter, and uses a waterproof mating connector at the power port, sparing finished-product makers wiring headaches. Dual-mode strong-light immunity (Core Technology #11) and military-grade EMC anti-interference (Core Technology #12) are both built in, withstanding six light sources, ESD level 4, and fast transient burst ±4KV. The module body is IPX5 waterproof, ready for humid bathroom environments.

### 1.1 Technology Positioning

| Module Type | Sensing Channel | Additional Functions | Temp. Display Method | Representative Product |
|---------|---------|---------|---------|---------|
| Single-function IR Water-outlet Module | Single water-outlet channel | None | None | Early IR Water-outlet Module |
| Water-outlet + Soap-dispensing Dual-head Module | Water-outlet + soap-dispensing dual channel | Interlock | None | General Soap-dispensing Sensor Module |
| **Shengshi Tangchao Infrared (IR) Sensor Module (This Product)** | **Water-outlet + soap-dispensing dual channel** | **Interlock + Hall handle + temperature display** | **Digital display + color-changing light strip** | **KCM-SSTC-01** |

### 1.2 Key Specifications

- Standby current ≤80μA, power-on to sensing action ≤2S
- Default sensing distance of both sensor heads 10±2cm, adjustable via remote control
- Soap dispensing time 0.5–3S adjustable (±0.5S per step), water outlet auto-closes after 1-minute timeout
- Operating temperature 1℃~55℃, water temperature 4℃~60℃, humidity 10%–95% RH
- ESD protection level 4 (air ±15KV / contact ±8KV), fast transient burst ±4KV
- Module waterproofing IPX5, life over 250,000 cycles

---

## 2. Features

### 2.1 Dual Heads for Water and Soap — No Conflict

The two infrared sensor probes on the module each handle their own job: one for water outlet, one for soap dispensing. Logically they are interlocked—during the soap-dispensing cycle all signals received by the two sensor heads are judged invalid, and soap won't dispense during water outlet. One hand catches water, the other catches foam, with no simultaneous spraying, giving a clean and crisp finished-product experience.

### 2.2 Digital Temperature Display with Color-coded Light Strip

Temperature display starts with the water outlet: in Celsius mode the light strip is green at ≤41℃ and red at ≥42℃, with the digital display showing "XX℃"; in Fahrenheit mode the strip is green at 97℉–107℉ and blue otherwise, showing "XX℉". Both programs are selectable at the factory for different markets. Users need not test the temperature by hand—the light strip color tells them whether the water is scalding.

### 2.3 Hall-effect Handle — Lift to Stop Everything

A Hall sensor is built into the handle (Core Technology #4). Opening the handle outputs a high level that closes the solenoid valve and liquid pump regardless of their current state, while masking the two infrared heads, the light strip, and the temperature display into standby; if the display runs over 300S it also turns off the light strip to save power. Lifting the handle instantly quiets the entire module, shutting off the water completely with no false outlet.

### 2.4 Automatic Water-outlet Shutoff — No Idle Flow

The IR water-outlet probe logic is restrained: sense to start water, sense again to stop; if no further sense within 1 minute of outlet, it auto-closes; even if continuously sensed for a full minute, it still closes. There is no awkward "water keeps running after the person leaves" or "hand trembles and water stops"—saving water and preventing waste.

### 2.5 Timed, Metered Soap Dispensing — Stops Even If Hand Stays

After the soap probe senses, the light strip lights up, then after about a 1-second delay the soap pump starts and dispenses for 1.5 seconds before stopping and extinguishing the strip. Even if the hand stays in the sensing zone, it only dispenses this one round and stops, never continuous spray. To adjust the soap volume, finished-product makers use the remote's time +/- keys, 0.5S per step, range 0.5–3S.

### 2.6 Strong-light Immunity — No False Triggers Under Six Light Sources

Backed by the dual-mode strong-light immunity algorithm (Core Technology #11), it resists false actuation under direct or oblique light within 15–91cm from incandescent, fluorescent, halogen, electronically ballasted daylight, bathroom heaters, and a 1000W hair dryer + 40W daylight sharing the same socket. It stays stable under mirror-front lights, by windows, and beneath bathroom heat lamps.

### 2.7 Staged Undervoltage Reminder — A Floor for Valve Shutoff

When battery voltage drops to 4.8±0.2V, opening the handle or sensing makes the light strip flash red 3 times before normal display resumes, and the solenoid valve and pump still work; if it falls further to 4.5±0.2V, opening the handle flashes red 3 times then extinguishes, and sensing will not open the valve or pump—just 3 red flashes then off. Full recovery only occurs when voltage rebounds above 5.0V. On power loss it unconditionally stays closed.

---

## 3. Core Selling Points

### Selling Point 1: Water, Soap and Temperature on One Board — Three Fewer Parts for OEMs

The biggest headache in making a soap-dispensing integrated faucet is the split design—one board for water outlet, one for soap, and another for the temperature screen, with wiring, drilling, and alignment all being painful work. This module crams dual-head sensing, interlock, temperature display, and a color-changing light strip onto a single board, so finished-product makers can mount it directly in alignment, saving at least two independent modules and one temperature screen in materials and assembly. For engineering contractors, one module delivers the complete "sensor water outlet + sensor soap dispensing + visible water temperature" experience, making quoting and delivery clean.

### Selling Point 2: Light Strip Shows Water Temperature — Halving Scald Complaints

Public restrooms, nursing homes, and children's hospitals fear scalding most from fluctuating water temperatures. When the module outputs water, the light strip changes color by temperature—green below 41℃, red above 42℃—paired with a direct digital readout, so users know before reaching in whether the water is safe to touch. This is especially valuable for aging-friendly and maternal-child scenarios: instead of waiting to be scalded, the colored strip blocks the risk up front, easing infection control and customer complaints.

### Selling Point 3: 80μA Standby + IPX5 — Saving Batteries and Wiring

With standby current held below 80μA, the module can run long-term on an AC-to-6V adapter or go battery-box for wireless use, and the power port uses a waterproof mating connector. The IPX5 waterproof body with a baseline life of 250,000 cycles needs essentially no dedicated maintenance in humid bathrooms. For retrofits of old buildings and outdoor public restrooms where rewiring is undesired, it works once installed, with low later battery-replacement frequency, tangibly lowering property maintenance costs.

---

## 4. Specifications and Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power Supply | AC 100–240V to DC 6V adapter / DC 6V battery box (waterproof mating connector) |
| Standby Current | ≤ 80μA |
| Power-on to Sensing Response | ≤ 2S |
| Load | DC 4.5V / 350mA solenoid valve + DC 5V / 500mA liquid pump (requires step-up under load) |
| Sensing Technology | Active infrared reflection (dual probe) |

### 4.2 Sensing and Temperature Display Parameters

| Parameter | Specification |
|--------|------|
| Default Sensing Distance of Both Sensor Heads | 10 ± 2cm |
| Sensing Distance Adjustment | Remote distance +/- keys |
| Water-outlet Timeout Shutoff | Auto-closes after 1 min with no further sensing / continuous sensing |
| Soap Dispensing Time | 0.5–3S adjustable (±0.5S per step) |
| Temperature Display | Digital display XX℃ / XX℉, Celsius/Fahrenheit dual program |
| Light Strip Colors (℃) | ≤41℃ green, ≥42℃ red |
| Light Strip Colors (℉) | 97–107℉ green, others blue |

### 4.3 Handle and Protection Parameters

| Parameter | Specification |
|--------|------|
| Hall-effect Handle | Handle open → close valve and pump, mask dual IR heads, light strip & temp display to standby |
| Display Protection | Light strip / temperature display auto-off after 300S |
| Power-loss Protection | Stays closed on power interruption |
| Undervoltage Reminder (≤4.8±0.2V) | Light strip flashes red 3 times then normal display; valve & pump still work |
| Undervoltage Shutoff (≤4.5±0.2V) | Light strip flashes red 3 times then off; valve & pump not opened |

### 4.4 Operating Environment

| Parameter | Specification |
|--------|------|
| Operating Scene | Restroom |
| Ambient Temperature | 1℃ ~ 55℃ |
| Relative Humidity | 10% RH ~ 95% RH |
| Applicable Water Temperature | 4℃ ~ 60℃ |
| Storage Temperature | -20℃ ~ 65℃ |
| Storage Humidity | ≤ 80% RH |

### 4.5 EMC and Protection

| Test Item | Test Standard / Condition | Result |
|---------|-------------|------|
| Electrostatic Discharge (ESD) | Level 4, air discharge ±15KV, contact discharge ±8KV | Normal operation |
| Electromagnetic Radiation (EMI) | Level 2, 80MHz–1000MHz, field strength 3V/m | Unaffected |
| Fast Transient Burst (EFT) | ±4KV | Normal operation |
| Light Interference | 6 types of light sources 15–91cm direct/oblique | No false trigger |
| Module Waterproofing | IPX5 | Meets bathroom spray environment |

### 4.6 Life and Identification

| Parameter | Specification |
|--------|------|
| Service Life | Over 250,000 cycles |
| Manufacturer Info | Laser marking on sensor window or online: manufacturer, production date, model, version |
| Potting Requirement | Fully covers all solder joints and pins, with no glue overflow |

### 4.7 Applicable Standards

| Standard No. | Standard Name |
|---------|---------|
| CJ/T 194-2014 | Non-contact Water Supply Fittings |

---

## 5. Installation Instructions

### 5.1 Before Installation

1. Confirm finished-product power is AC 100–240V to 6V or DC 6V battery box, with a waterproof mating connector at the power port
2. Do not face the sensor window directly at sunlight or strong lights; leave the default ~10cm recognition space in front of the sensor head
3. Verify alignment of the two sensor heads (water/soap) with the finished-product openings; orient the light strip / digital display toward the user side
4. Accurately align the handle Hall element with the finished-product handle mechanism before fixing

### 5.2 Precautions

- Always cut power before installation and repair
- Use high-performance alkaline batteries; do not mix old and new
- Do not hot-plug module terminals; power on only after the waterproof mating connector is firmly inserted
- Install only after the sensor window's static film is intact and the backside potting has no voids

### 5.3 Installation Steps

1. Fix the module inside the finished product, aligning the water/soap dual sensor windows and the temperature display window
2. Connect the power (adapter or battery box) and the solenoid valve and liquid pump drive wires
3. Install the handle and confirm the Hall element travel is in place
4. Power-on self-check: solenoid valve closes once, digital display lights 0.5S, light strip lights green 0.5S, then enters normal mode
5. Extend hand to test water outlet, soap dispensing, and temperature display; fine-tune sensing distance / soap time via remote

### 5.4 Power-on Self-check

After power-on, the solenoid valve closes once → digital display fully lights 0.5S → light strip lights green 0.5S → enters normal mode. Do not keep blocking the sensor head during self-check.

### 5.5 Maintenance Notes

Battery voltage below 4.8V makes the light strip flash red 3 times as a reminder; below 4.5V it flashes red 3 times and stops opening valve and pump. Maintenance: cut power → open the finished-product cover → replace with same-brand new batteries / check adapter → power on and self-check.

---

## 6. Applicable Finished Products and Integration Solutions

### 6.1 Compatible Finished Products

Positioned as a sensor control core component, the Shengshi Tangchao Infrared (IR) Sensor Module (KCM-SSTC-01) works with **sensor hand washers, soap-dispensing integrated faucets, and basin sensor faucets** from GIBO and partner finished-product makers. The module contains no water or soap path; water/soap capability depends on the paired solenoid valve and liquid pump. We do not claim the water-path metrics as our own here—only the module-side capability is described.

### 6.2 Value for Finished-product Integration

- **Three-in-one greatly reduces burden**: water outlet, soap dispensing, and temperature display on one board—saving two modules and one temperature screen in materials and assembly
- **Interlock logic built in at factory**: water/soap interlock and Hall-handle emergency stop—finished-product makers need not write this logic themselves
- **Platform reuse**: inherits GIBO's active infrared + ultra-low power + dual-mode anti-interference platform (Core Technologies #6/#7/#11/#12) for fast alignment with soap-dispensing faucets

### 6.3 ODM / Engineering Customization

The module supports Celsius/Fahrenheit dual programs, adjustable soap time 0.5–3S, and remote fine-tuning of sensing distance, suiting export finished-product makers for regional-market customization, and also fitting aging-friendly, maternal-child, and medical hand-washing scenarios for differentiated finished products.

---

## Appendix

### A. Core Technology Index

| No. | Technology Name | Application in This Product |
|------|---------|-----------|
| #4 | Capacitive Touch Technology | Hall-handle emergency stop, sensor-window interaction concept extension |
| #5 | Wireless Remote Control Technology | Remote adjusts sensing distance and soap time |
| #6 | Low-power Multi-stable Agile Sensing Technology | Standby current ≤80μA, dual battery/adapter supply |
| #7 | Liteon Smart Sensing Technology | Dual-head adaptive threshold, filters transient obstruction |
| #11 | Dual-mode Strong-light Immunity Anti-interference Algorithm | No false trigger under 6 light sources within 15–91cm |
| #12 | Military-grade EMC Anti-interference Technology | ESD level 4, fast transient burst ±4KV |
| #13 | Intelligent Anti-overflow Power-off Safety Protection Technology | Stays closed on power loss, staged undervoltage valve shutoff |

### Related Patents (Granted)

| Technology | Patent Name | Patent No. | Type |
|--------|---------|--------|------|
| Sensing Algorithm | A Sensor Water-outlet Device and Signal Detection Method | ZL201910380558.X | Invention Patent |
| Sensing & Manual Control | A Sensor and Manual-control Faucet | ZL201520753357.7 | Utility Model |
| Dual-mode / Temperature Control | A Dual-mode Faucet | ZL201922113032.3 | Utility Model |
| Soap Dispensing | A Simplified Sensor Liquid Dispenser | ZL202111150757.5 | Invention Patent |
| Soap Dispensing | A Liquid-bottle Structure for a Sensor Liquid Dispenser | ZL2021 2 2383207.X | Utility Model |
| Soap Dispensing | An Electric Liquid-extruding Faucet | ZL2021 2 1443671.7 | Utility Model |
| Waterproof Sensor Module | A Waterproof Sensor Module for a Water-outlet Device | ZL2020 2 2360603.6 | Utility Model |
| Panel Light Scattering | A Kitchen & Bath Wireless Sensor Module with Panel Light Scattering | ZL2022 2 2533102.2 | Utility Model |
| Light-effect Toilet Module | A Toilet Sensor Flush Module with Light-effect Components | ZL2022 2 1337429.6 | Utility Model |
| Wireless Control | A Wireless-control Faucet Device | ZL201520751977.7 | Utility Model |

### B. Certifications and Qualifications

GIBO has been making sensor sanitary ware since 2004 and was one of the earliest domestic manufacturers to apply MCU microcontrollers to sensor control. It is a drafting unit for two standards: GB/T 41863-2022 *General Technical Requirements for Water-saving Performance of Non-contact Water Supply Fittings* and T/XMBK 002-2024 *Sensor Faucets*, and is a National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, and National Specialized & Sophisticated SME. The pull-out kitchen faucet featuring the same dTOF Laser Sensing Technology platform won the 2023 Boiling Quality Gold Award.

- Fully compliant with the industry standard **CJ/T 194-2014** for Non-contact Water Supply Fittings
- **CE Certification** (multiple models), **CUPC/UPC Certification** (certificate No. cert_upc-2015-7968), **NSF Certification**, **WRAS Certification** (UK Water), **WaterMark Certification** (Australian water efficiency)
- **ISO 9001** Quality Management System, **ISO 14001** Environmental Management System, **ISO 45001** Occupational Health & Safety (2023 edition)
- National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, National Specialized & Sophisticated SME
- dTOF Laser products on the same platform won the **2023 Boiling Quality Gold Award**

### C. Contact Information

| Item | Content |
|------|------|
| Company Name | Fujian GIBO Kitchen & Bath Tech Co., Ltd. |
| Chinese Website | [www.gibo.com.cn](https://www.gibo.com.cn) |
| English Website | [www.gibosensor.com](https://www.gibosensor.com) |
| Service Hotline | 0591-88066000 |
| Company Email | sales@gibol.com.cn |
| Company Address | Building 3, Liangyuan Science Park, High-tech Zone, Fuzhou, Fujian Province |

---

> This document is compiled based on the Shengshi Tangchao Infrared (IR) Sensor Module (KCM-SSTC-01) Specification (V1.5, 2026-05-25); parameters are subject to the actual product. GIBO reserves the final right of interpretation and modification of the technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
