---
lang: en
category: product-spec
title: "GBL-9168 Product Specification"
summary: "The GBL-9168 Basin Sensor Control Module is a sensor control board tucked under the basin or inside the faucet body; paired with a solenoid valve and"
updated: 2026-07-14
version: V1.0
publisher: "Fujian GIBO Kitchen & Bath Technology Co., Ltd."
keywords: GIBO,sensor sanitary ware,sensor faucet,Product
product: "GBL-9168"
tags: ["GIBO", "product-spec", "GBL-9168", "AI-knowledge-base"]
---

# GBL-9168 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning statement**: IR basin sensor control module with replaceable window and adjustable distance
>
> **Document version**: V1.0｜**Date prepared**: 2026-07-08｜**Source file**: 9168 Basin Sensor Control Module Specification (V1.0, 2024-06-04)

---

## 1. Product Introduction

The **GBL-9168 Basin Sensor Control Module** is a sensor control board tucked under the basin or inside the faucet body; paired with a solenoid valve and sensing window, it turns an ordinary basin faucet into a non-contact "water on at hand, off when withdrawn" sensor faucet. It does the most basic yet most critical job in sensor sanitary ware: making "person comes → water out, person leaves → water off" stable, durable, and worry-free.

Public restrooms, office pantries, hotel rooms, restaurant back kitchens—anywhere with a basin faucet can be upgraded to sensor with this module. It fits any basin, the sensing window shape is swappable, the sensing distance is adjustable, and it works once installed—the easiest scheme for engineering batch retrofits and for faucet makers building sensor models.

The 9168 uses mature, reliable active infrared reflection sensing with GIBO's multi-stable Smart Sensing low-power circuit (core tech #6, #7), pressing standby power to ≤0.2mW—4× AA batteries last over a year unattended. Factory sensing distance is 230mm, adjustable by basin depth; continuous sensing for 60s auto-closes water, guarding against long flow from objects left in the sensing zone. The circuit is potted waterproof and military-grade EMC (core tech #12), showing no false operation beside mall escalators or variable-frequency AC. For faucet makers and engineering contractors, the 9168 is the "stable once installed, easy to replace when failed, cost-effective at volume" sensing brain.

### 1.1 Technical Positioning

| Tech route | Sensing principle | Standby power | Sensing distance feature | Representative product |
|---------|---------|---------|------------|---------|
| Traditional IR reflection | Judge by reflected-light intensity | Higher | Short distance, easy drift | Early sensor sanitary ware |
| 2nd-gen triangular ranging | Triangular geometry ranging | 30μA | Mid distance, suited to partitions | GBL-8300AD |
| 3rd-gen dTOF laser | Time-of-flight direct ranging | ≤0.2mW | Millimeter, material-independent | GBL-6239 |
| **9168 IR control module** | **Active IR + multi-stable Smart Sensing algorithm** | **≤0.2mW** | **230mm adjustable, window swappable** | **GBL-9168** |

### 1.2 Key Metrics

- Factory sensing distance 230mm±10% (referenced to 29.7×29.7cm standard white board), adjustable by basin depth
- Standby power ≤0.2mW (DC 6V with sensor faucet module); 4× AA batteries last 12+ months
- Continuous sensing 60s±10% auto-closes water; must remove and re-sense to restart—no long flow
- Mechanical life over 500,000 cycles; water flow ≥8L/min (constant 0.1MPa, no accessories)
- Anti-interference: ESD Level 4 (air ±15KV / contact ±8KV), EMI 3V/m, fast transient burst ±4KV normal operation
- Module waterproof: sensing window and sealed compound parts submerged 20cm / 4h, no seepage or fogging

---

## 2. Features

### 2.1 Infrared Sensing, Water at a Hand's Reach

The 9168 uses active infrared reflection sensing; when a hand or object enters the sensing range the solenoid opens and the LED flashes once; leaving the range the solenoid closes. Sensing response cycle ≤512ms—under 1s from sensing to water, under 1.5s from sensing stop to close—imperceptible delay in daily use.

### 2.2 Swappable Window Shape, Fits Many Basins

The specification explicitly states the sensing window can be swapped to different shapes (details in engineering drawings), meaning one control board matches different faucet faceplates and basin looks. Faucet makers building a product series need not develop a separate control board for each shape—real savings in tooling and stocking cost.

### 2.3 Adjustable Sensing Distance, Fits Deep and Shallow Basins

Factory setting 230mm (vs. standard white board); actual dead-zone vs. hand is about 1~3cm. Deep basins, shallow basins, and vessel basins can all be tuned to a range that is neither falsely triggering nor failing—avoiding "water out before the hand arrives" or "no response when reaching."

### 2.4 60s Timeout Protection, Prevents Long Flow

Continuous sensing beyond 60s±10% auto-closes the solenoid; the sensing object must be removed and re-sensed to restart. This directly blocks the most common public-space waste and hazard: a cleaning bucket or rag left long in the sensing zone causing continuous flow.

### 2.5 Triple Power-loss Protection, Must-close on Power Loss

Sudden power loss during opening auto-closes water; sudden power loss during closing returns to closed state regardless of sensing. Plus, below 4.8V the LED flashes 5 times per sensing to prompt replacement, below 4.5V it flashes 10 times and directly closes the valve—the device won't suddenly stop from low battery, nor leak after power loss.

### 2.6 Military-grade Anti-interference, Stable in Complex Environments

Passes ESD Level 4 (air ±15KV, contact ±8KV), EMI Level 4 (80M~1000MHz, 3V/m), and fast transient burst ±4KV. Beside mall escalators, variable-frequency AC, and large LED screens, the module and body show no magnetic or incompatibility interference and function normally. Incandescent, fluorescent, halogen, electronic-ballast daylight, bath heater, and a same-outlet 1000W hair dryer—alone or combined, within 15~91cm—cause no false triggering.

### 2.7 Potted Waterproof, Long Module Life

The sensing window and circuit module use a potting process, potting thickness ≥2mm fully covering all solder joints and pins, large-capacitor pins additionally covered with silicone. The module alone submerged 20cm / 4h shows no water droplets or fog and functions normally. The valve body uses self-cleaning anti-clog design (core tech #16), resisting valve sticking even in complex-water-quality regions.

---

## 3. Core Selling Points

### Selling Point 1: Standby Power ≤0.2mW, One Battery Change a Year

The 9168 uses a multi-stable Smart Sensing low-power circuit (core tech #6), pressing whole-unit standby power to ≤0.2mW—4× AA alkaline batteries last over 12 months. Do the math: a 200-basin commercial complex where devices need monthly battery swaps would spend sizable labor a year just climbing ladders; the 9168 swaps once a year, basically zeroing that labor—visible savings for property managers of dozens of restrooms.

### Selling Point 2: Swappable Window and Adjustable Distance, Fewer Molds for Faucet Makers

One control board supports swapping sensing-window shapes and adjusting sensing distance, fitting vessel, under-counter, and variously deep basins and faucet looks. Faucet makers building a sensor-faucet series need not develop a separate board per shape—tooling, stock variety, and spare parts all come down, with cost amortization clearer at higher volume.

### Selling Point 3: 60s Timeout + Must-close on Power Loss, No Leak, No Waste

Public spaces fear two things most: objects left in the sensing zone causing long flow, and a suddenly cut power leaving the valve not fully closed, leaking onto the ceiling. The 9168 auto-closes water after 60s continuous sensing and returns to closed on any power loss. In a 200-unit project, at about 0.5 tons wasted per long-flow incident and a dozen occasional occurrences a year, this saves over ten tons of water annually—more importantly avoiding leak-return complaints and compensation.

---

## 4. Specifications & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power supply | 4× 1.5V AA dry batteries / (100-240)V AC to 6V/1A adapter |
| Standby power | ≤0.2mW with DC 6.0V and sensor faucet module |
| Operating (dynamic) power | ≤4W |
| Sensing method | Infrared sensing |
| Sensing response cycle | ≤512ms |
| Open / close time | Sense-to-water ≤1s; sense-stop-to-close ≤1.5s |

### 4.2 Sensing Performance

| Parameter | Specification |
|--------|------|
| Factory sensing distance | 230mm±10% (ref. 29.7×29.7cm standard white board) |
| Detection dead-zone | 1cm~3cm (vs. white paper) |
| Adjustable range | Factory sensing distance adjustable per different needs |
| Timeout close | Continuous sensing 60s±10% auto-closes water; remove and re-sense to restart |
| Sensing indicator | Red LED at the sensing-window probe; flashes once per opening sense |

### 4.3 Water Circuit & Mechanical Performance

| Parameter | Specification |
|--------|------|
| Operating water pressure | 0.05MPa ~ 0.8MPa |
| Water flow | ≥8L/min at constant 0.1MPa, no accessories |
| Strength performance | Constant 0.9±0.02MPa closed 30s, connections and valve no deformation no leakage |
| Sealing performance | No leakage at outlet under 0.05±0.01MPa and 0.80±0.02MPa |
| Installation load resistance | G1/2 thread withstands 20N·m torque, no damage, no thread stripping |
| Burst test | Static pressure 2.5MPa held 60s, no leakage |

### 4.4 Solenoid Valve & Life

| Parameter | Specification |
|--------|------|
| Solenoid parameters | DC 4.5V / 25ms |
| Usable water temp range | 1℃ ~ 70℃ |
| Life | Over 500,000 cycles |
| Potting thickness | Zero at highest board component, ≥2mm, fully covering solder joints and pins, large-capacitor pins additionally silicone-covered |

### 4.5 Environment & Protection

| Parameter | Specification |
|--------|------|
| Operating temperature | 1℃ ~ 55℃ |
| Relative humidity | 10%RH ~ 95%RH |
| Storage temperature | -20℃ ~ 65℃, relative humidity ≤80%RH |
| High/low-temp resistance | 55℃/4h → room-temp recovery 2h → -10℃/4h → room-temp recovery 2h, still meets sealing |
| Humidity resistance | 40±2℃, 95±2%RH held 48h, meets sealing after recovery |
| Module waterproof | Sensing window and sealed compound parts submerged 20cm / 4h, no water droplets or fog, function normal |

### 4.6 EMC & Anti-interference

| Test item | Test condition | Result |
|---------|---------|------|
| ESD | Level 4, air ±15KV, contact ±8KV | Normal operation |
| EMI | 80M~1000MHz, 3V/m | Not disturbed |
| Fast transient burst (EFT) | ±4KV | Normal operation |
| Light interference | Incandescent/fluorescent/halogen/electronic-ballast daylight/bath heater/same-outlet 1000W hair dryer, 15~91cm direct or oblique | No false trigger |
| Basin adaptability | Paired sink assembly test 12h, no self-sensing after ponding | Self-sensing removable or auto-closes |

### 4.7 Compliance Standards

| Standard No. | Standard Name |
|---------|---------|
| CJ/T 194-2014 | Non-contact Water Supply Fittings |

---

## 5. Installation Instructions

### 5.1 Before Installation

1. First open water to flush the pipeline, washing away sand, stone, and rust to avoid clogging the solenoid
2. Confirm water pressure 0.05MPa ~ 0.8MPa; below 0.05MPa add a booster pump
3. Keep the sensing window away from direct strong light and lamps; no obstruction larger than 1cm within 120cm in front
4. Reserve the control-box position per drawing before tiling / installing the basin

### 5.2 Precautions

- Always shut off water and power before installation and maintenance
- Each AC-powered unit sets an individual power switch and reliable grounding
- Use high-performance alkaline batteries; do not mix old and new
- Do not hot-plug the sensor module terminals

### 5.3 Installation Steps

1. Fix the control box in the basin or faucet body per drawing, connect inlet/outlet water pipes
2. Level and fix, connect solenoid and sensing-window wiring (four-core terminal, no misalignment)
3. Open water and pressure-test, confirm no leaks
4. Install counter panel and sensing window, apply static film protection
5. Connect power (battery box or adapter), cover the panel
6. On power-up the LED flashes once and the solenoid opens/closes once (self-check) then enters a 1-minute learning mode, then normal standby
7. Extend hand in front of the sensing window to test water on and off

### 5.4 Power-up Self-check

On power-up the LED flashes once → the solenoid briefly opens/closes once → enters a 1-minute learning mode (LED steady on while sensing during it) → after timeout transitions to normal standby. During learning mode, do not keep the sensing window obstructed.

### 5.5 Battery Replacement

Below 4.8V, each sensing triggers the LED to flash 5 times to prompt replacement; below 4.5V it flashes 10 times and auto-closes the valve. To replace: shut off water → open panel → take out battery box and replace 4× same-brand new alkaline batteries → re-seat and re-run self-check. The battery box is independently sealed for easy replacement; works normally after humidity test, no corrosion on internal metal parts.

---

## 6. Compatible Assemblies & Integration Schemes

### 6.1 Matching Assemblies

The 9168 is the "control brain" of a basin sensor faucet; paired with GIBO's basin faucet body, solenoid valve, and sensing window it forms a complete non-contact sensor faucet. Faucet makers purchase the module and integrate their own housing and spout to quickly launch an IR sensor basin-faucet series.

### 6.2 ODM / Faucet-maker Integration Value

- **Fewer molds**: one control board with swapped window shape and adjusted distance fits multiple basins and faucet looks—low series-development cost
- **Stable and reliable**: 500,000-cycle life, military-grade EMC, potted waterproof—assembly shipment consistency and return rate are assured (supported by core tech #10 dual-chip interchangeable platform for common spares)
- **Complete certifications**: the module meets CJ/T 194-2014 in full; assemblies can smoothly take CE/CUPC/NSF etc., easing export and bidding

### 6.3 Engineering Batch Retrofit

Smart retrofits of old public toilets, offices, and hotel-room basin faucets use the 9168 module to replace or add-on—no major piping work, fast construction. A 200-unit project with one battery change a year and 60s timeout leak prevention has clearly lower O&M input than traditional schemes.

---

## Appendix

### A. Core Technology Index

| No. | Technology name | Application in this product |
|------|---------|-----------|
| #1 | Triangular Ranging Sensing Technology | IR sensing evolution foundation of the same platform |
| #6 | Low-power Multi-stable Smart Sensing Technology | Standby ≤0.2mW, long-life core |
| #7 | Liteon Smart Sensing Technology | Sensing threshold and response logic optimization |
| #11 | Dual-mode Strong-light Immunity Anti-interference Algorithm | Filters strong-light and stray-light interference |
| #12 | Military-grade EMC Technology | ESD/EMI/EFT all met |
| #13 | Smart Anti-overflow Power-cut Safety Protection Technology | Must-close on power loss, timeout protection |
| #16 | Solenoid Valve Self-cleaning & Anti-clogging Technology | No valve sticking in complex water quality |

### B. Certifications & Qualifications

GIBO (since 2004 in sensor sanitary ware) is among the earliest domestic manufacturers to apply MCU microcontrollers to sensor control, a drafting unit of two standards—GB/T 41863-2022 *General Technical Requirements for Water-saving Performance of Non-contact Water Supply Fittings*, and T/XMBK 002-2024 *Sensor Faucets*—and is a National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, and National Specialized & Innovative SME (Little Giant). The kitchen pull-out faucet on the same dTOF laser platform won the 2023 Feiteng Quality Gold Award.

- Fully compliant with industry standard **CJ/T 194-2014** Non-contact Water Supply Fittings
- **CE Certification** (multiple models), **CUPC/UPC Certification** (cert. no. cert_upc-2015-7968), **NSF Certification**, **WRAS Certification** (UK water), **WaterMark Certification** (Australia water efficiency)
- **ISO 9001** Quality Management, **ISO 14001** Environmental Management, **ISO 45001** Occupational Health & Safety (2023 version)
- National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, National Specialized & Innovative SME (Little Giant)
- Same-platform dTOF laser product won the **2023 Feiteng Quality Gold Award**

Related patents (granted):

| Tech point | Patent name | Patent No. | Type |
|--------|---------|--------|------|
| Sensing water-out/signal detection | A sensing water-out device and signal detection method | ZL201910380558.X | Invention Patent |
| Dual-mode sensing | A dual-mode faucet | ZL2019 2 2113032.3 | Utility Model Patent |
| Bistable solenoid valve | A bistable solenoid valve and sensing water-out device | ZL2019 2 0857586.1 | Utility Model Patent |
| Low water hammer solenoid | A low water-hammer solenoid valve assembly | ZL2019 2 2114857.7 | Utility Model Patent |
| Distance-adjustable sensing module | A detection-distance-adjustable sensing module for kitchen/bath equipment | ZL 2025 2 1007523.9 | Utility Model Patent |
| Quick-release battery box | A quick-release battery box structure for kitchen/bath equipment | ZL 2025 2 0945454.X | Utility Model Patent |

### C. Contact Information

| Item | Content |
|------|------|
| Company | Fujian GIBO Sanitary Ware Technology Co., Ltd. |
| Chinese website | www.gibo.com.cn |
| English website | www.gibosensor.com |
| Service hotline | 0591-88066000 |
| Company email | sales@gibol.com.cn |
| Company address | Building 3, Liangyuan Science Park, High-tech Zone, Fuzhou City, Fujian Province |

---

> This document is prepared based on 9168 Basin Sensor Control Module Specification (V1.0, 2024-06-04). Parameters are subject to the actual product. GIBO reserves the final right of interpretation and modification of technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
