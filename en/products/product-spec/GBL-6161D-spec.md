---
title: "GBL-6161D Product Specification"
description: "The GBL-6161D is a basin-mounted sensor faucet that delivers water when hands approach and stops when they leave—no physical contact with any switch r"
keywords: GIBO,sensor sanitary ware,sensor faucet,Product
classification: Product
language: en
publisher: "Fujian GIBO Kitchen & Bath Technology Co., Ltd."
version: V1.0
date: 2026-07-14
---
# GBL-6161D Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning statement**: Battery-powered infrared dual-mode basin sensor faucet
>
> **Document version**: V2.0｜**Date prepared**: 2026-07-08｜**Source file**: gibo-GBL-6161-Specification (Rev. 1.0, 2019-10-18)

---

## 1. Product Introduction

The GBL-6161D is a basin-mounted sensor faucet that delivers water when hands approach and stops when they leave—no physical contact with any switch required. It is designed for venues that want touch-free water usage but prefer not to undertake extensive rewiring. Retrofit projects and locations without pre-installed power can simply run on 4 batteries.

Hotels, hospitals, office buildings, mall wash stations, and vanities in finished residential homes. What these scenarios care about most is hygiene (no touching the faucet), easy installation (no breaking walls to pull wiring), and no false triggering (no unwanted flow under strong window-side light).

The 6161D uses 940nm active infrared reflection detection paired with a low-power MCU for intelligent control. It offers two water-delivery logics: public spaces use the "Sustained-flow Mode" (wave to start, wave again to stop), while homes and offices use the "Instant-sensing Mode" (water on when hands present, off when removed). Standby current is only 45μA, and 4 AA batteries last a long time. The main unit measures 153×45mm and mounts directly onto a standard single-hole basin.

In short, the value of the 6161D is "water at hand, no touch, no wiring." The three points below are what we believe are most worth telling.

### 1.1 Technical Positioning

| Solution | Sensing principle | Operating mode | Power feature | Representative product |
|------|---------|---------|---------|---------|
| Basic IR model | IR reflection intensity | Single mode | Medium-high power | Early sensor faucets |
| **6161D IR smart model** | **940nm active IR + anti-interference algorithm** | **Dual mode (Sustained-flow / Instant-sensing)** | **Standby ≤45μA** | **GBL-6161D** |
| High-end laser model (dTOF) | Laser time-of-flight | Precise ranging | Standby ≤0.2mW | GBL-6170D / 6239 |

Within the IR approach, the 6161D introduces low-power multi-stable Smart Sensing and a dual-mode strong-light immunity algorithm, achieving a well-balanced cost-performance ratio—making it the cost-effective choice for commercial wash stations.

### 1.2 Key Metrics

- Standby current ≤45μA; long life on 4 AA batteries; no wiring required
- Water-on response ≤0.6s; water-off ≤1s
- 940nm IR + anti-interference; sensing distance variation <±10% under 45° oblique illumination from 1m away
- Operating temperature 0℃~55℃; service life ≥500,000 cycles
- Water hammer peak differential ≤0.2MPa; no pipe shock on shutoff

---

## 2. Features

### 2.1 940nm IR Sensing, Reliably Detects Hands

A closed loop of four units—infrared detection, signal processing, MCU main control, and drive protection—works in coordination. On power-up it auto-calibrates the ambient IR baseline and dynamically adjusts the sensing threshold, remaining stable under strong light, weak light, and humid environments.

### 2.2 Dual-mode Flow, One Unit Replaces Two

Sustained-flow Sensing Mode: hands enter the sensing zone to start flow, enter again to stop; auto-cutoff after 180s of continuous flow (prevents running water). Instant-sensing Mode: water on when hands enter, off when hands leave; auto-cutoff after 60s of continuous flow. The two modes are switched via controller setting, so installers need not stock two models for different floors.

### 2.3 Battery Powered, No Wiring in Retrofits

Whole-unit static current ≤45μA, powered by DC 6V (4× AA alkaline batteries, customer-supplied). No breaking walls to pull power—directly installable in retrofit buildings and power-less conditions.

### 2.4 Low-voltage and Undervoltage Protection

At voltage ≤4.6V the LED flashes rapidly and forcibly cuts off water; at lower levels it flashes slowly and stays closed. The alert is clear so property management can replace batteries in time.

### 2.5 Strong-light Immunity, No False Triggering by Windows

Incandescent, fluorescent, and LED light at 45° oblique illumination 1m away all produce sensing-distance variations of less than ±10%; multiple units on the same power also do not falsely trigger each other.

### 2.6 Electromagnetic Compatibility Compliant

Both burst (group pulse) and ESD interference pass Class A; switching appliances in a shared-power environment causes no false operation. Stable beside mall escalators, variable-frequency AC, and large LED screens.

### 2.7 Low Water Hammer + Self-cleaning Anti-clog

At shutoff the water impact is gentle (peak differential ≤0.2MPa) and fittings are less likely to loosen; the valve core auto-cleans on every open/close cycle, resisting clogging even in hard-water scaling and sediment-laden pipe networks.

---

## 3. Core Selling Points

### Selling Point 1: Dual-mode Flow, One Product Fits Two Habits

Public spaces and homes have different requirements for water-delivery logic: malls want the "wave to start, wave again to stop" rhythm, while homes want zero-wait "water on when hands present, off when removed." The 6161D switches with a single unit, so installers need not stock two models—simplifying both inventory and selection.

### Selling Point 2: 4 Batteries, No Wiring for Retrofit

Many old-building wash stations that want to switch to sensor faucets are held back by the lack of pre-installed power. The 6161D runs on batteries—install and use immediately—cutting single-point installation from hours to tens of minutes and lowering overall retrofit cost directly. Real, hard-currency savings for property management.

### Selling Point 3: 940nm IR + Strong-light Immunity, No Erratic Flow by Windows

Sensor faucets beside floor-to-ceiling windows fear two things most: false triggering into long flow under strong light, or complete failure under strong light. The 6161D's IR with dual-mode anti-interference algorithm keeps sensing-distance variation under 45° oblique illumination from 1m below ±10%—no water wasted from sunlight-triggered flow, and no waving hands with no response.

---

## 4. Specifications & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Operating voltage | DC 4.5V ~ 6.0V |
| Static current | ≤ 45μA |
| Battery specification | DC 6V LR6 AA alkaline battery ×4 (customer-supplied) |
| Output voltage pulse width | 25ms |
| Low-voltage alarm | ≤ 4.6 ± 0.1V (LED fast flash, cuts off flow) |
| Undervoltage protection | Below 4.6V ± 0.1V (LED slow flash, cuts off flow) |

### 4.2 Water Circuit Parameters

| Parameter | Specification |
|--------|------|
| Operating water pressure | 0.05MPa ~ 0.8MPa |
| Operating water temperature | ≤ 75℃ |
| Inlet hose thread | G1/2 single-barbed steel-wire hose |
| Flow rate | Dynamic pressure 0.1~0.3MPa: 3L/min ≤ flow ≤ 7.5L/min |

### 4.3 Sensing Parameters (factory setting)

| Mode | Factory sensing distance | Sensing range |
|------|-------------|----------|
| Instant-sensing | 120mm ± 10 | 10mm ~ 130mm |
| Sustained-flow sensing | 40mm ± 10 | 10mm ~ 50mm |

Voltage 6.5V→4.6V variation ≤±10%; temperature -10℃→+55℃ variation ≤±10%.

### 4.4 Operating Environment

| Parameter | Specification |
|--------|------|
| Operating temperature | 0℃ ~ 55℃ |
| Storage temperature | 1℃ ~ 50℃ |
| Relative humidity | 10% ~ 95% |
| Atmospheric pressure | 86KPa ~ 106KPa |

### 4.5 Mechanical & Protection

| Parameter | Specification |
|--------|------|
| Product dimensions | 153mm (L) × 45mm (W) |
| Vibration resistance | Amplitude 0.35mm, 10~55Hz, 3 perpendicular axes swept 10 times |
| Installation load resistance | 20N·m torque held 60s, threads no cracks |
| Water hammer performance | Static pressure 0.5MPa, peak differential ≤0.2MPa |
| Sealing performance | Static pressure 0.05/1.0MPa, outlet no leakage |
| Strength performance | Static pressure 1.0MPa held 30s, no leakage no deformation |

### 4.6 Life & Reliability

| Parameter | Specification |
|--------|------|
| Service life | ≥ 500,000 cycles |
| Life test | Over 200,000 cycles (static pressure 0.4MPa) |
| Max flow duration | Sustained-flow 180S±10S; Instant-sensing 60S±5S |
| Open/close time | Open ≤1s, close ≤1.5s (dynamic pressure 0.1MPa) |

### 4.7 Compliance Standards

| Standard No. | Standard Name |
|---------|---------|
| CJ/T 194-2014 | Non-contact Water Supply Fittings |
| GB18145-2014 | Ceramic Disc Cartridge Faucet |

---

## 5. Installation Instructions

### 5.1 Before Installation

1. First open water to flush the pipeline, clearing sand, stone, and rust
2. Confirm water pressure 0.05MPa ~ 0.8MPa
3. Prepare 4× DC 6V AA alkaline batteries
4. Keep the controller away from direct strong light and mirror reflection; do not place persistent obstructions in front of the sensing window
5. Drill the countertop per standard single-hole; inlet G1/2

### 5.2 Precautions

- Shut off the water supply before installation and maintenance
- Use high-performance alkaline batteries; do not mix old and new
- Keep the controller away from direct strong light and mirror reflection
- Do not hot-plug the sensor module terminals
- Maintain spacing when installing multiple units side by side to avoid mirror-reflection interference

### 5.3 Installation Steps

1. Install the faucet body per the hole; connect the G1/2 inlet hose
2. Open water and pressure-test to confirm no leaks
3. Install 4× AA alkaline batteries (mind polarity)
4. On power-up the indicator flashes once and the solenoid opens/closes once (self-check) then enters standby
5. Test water on/off by placing hand in sensing zone
6. Set the flow mode per scenario (Sustained-flow / Instant-sensing)
7. Adjust the sensing distance

### 5.4 Power-up Self-check

On power-up the indicator flashes once → the solenoid briefly opens/closes → enters standby. At low voltage the indicator flashes rapidly as a reminder.

### 5.5 Battery Replacement

At voltage ≤4.6V, each sensing triggers a rapid LED flash and cuts off flow to remind battery replacement. To replace: shut off water → open battery compartment → replace with 4 new same-brand batteries → re-seat and re-run self-check.

---

## 6. Application Scenarios

### 6.1 Malls / Shopping Centers

Touch-free flow prevents cross-infection; battery-powered no-wiring retrofit installs and uses immediately; dual mode fits different floors; stable sensing under atriums and mall lighting.

### 6.2 Offices / Corporate HQs

Water on at hand, off on leaving—great experience; stable even near office equipment and LED screens; low-power no-wiring keeps decor clean; auto-cutoff prevents running water.

### 6.3 Hospitals / Elderly Care

Fully automatic touch-free meets infection-control; clear low-battery alert; withstands high/low temperature and humid full conditions; timeout protection prevents faulty long flow.

### 6.4 Star Hotels / Clubs

153×45mm compact look fits high-end decor; low water hammer means quiet shutoff; battery solution eases public-area construction; tech feel matches "smart bathroom."

### 6.5 Schools / Venues

Battery no-wiring suits old campus retrofit; vibration/shock resistance suits concentrated student use; dual mode + timeout protection reduce waste; self-cleaning anti-clog suits complex water quality.

### 6.6 Finished Residences / Developments

Instant-sensing mode zero-wait, handy at home; ultra-low power removes need for pre-installed power; touch-free on/off with dirty hands; GIBO ODM quality.

---

## Appendix

### A. Related Patents (granted)

| Tech point | Patent name | Patent No. | Type |
|--------|---------|--------|------|
| Sensing/signal detection | A sensing water-out device and signal detection method | ZL201910380558.X | Invention Patent |
| Smart sensing spout | A smart sensing spout | ZL201910116269.9 | Invention Patent |
| Modular flow channel | A smart faucet with modular flow channel | ZL201810558574.9 | Invention Patent |
| Refraction sensing anti-false-trigger | A prism-refraction sensing device for false-trigger prevention in kitchen/bath equipment | ZL 2023 2 3623129.1 | Utility Model Patent |
| Bistable solenoid valve | A bistable solenoid valve and sensing water-out device | ZL 2019 2 0857586.1 | Utility Model Patent |
| Low water hammer | A kitchen/bath solenoid valve body with improved water-hammer structure | ZL 2023 2 3529883.9 | Utility Model Patent |
| Low water hammer | A low water-hammer solenoid valve assembly | ZL 2019 2 2114857.7 | Utility Model Patent |
| Modular sensor faucet | A modular sensor faucet | ZL 2020 2 0411840.8 | Utility Model Patent |

### B. Certifications & Qualifications

GIBO (since 2004 in sensor sanitary ware) is a drafting unit of two standards—GB/T 41863-2022 *General Technical Requirements for Water-saving Performance of Non-contact Water Supply Fittings*, and T/XMBK 002-2024 *Sensor Faucets*—and is a National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, and National Specialized & Innovative SME (Little Giant). The IR control architecture used in the 6161D has been applied for years in high-frequency venues such as high-speed rail stations, airports, and top-tier hospitals.

- Fully compliant with industry standard **CJ/T 194-2014** Non-contact Water Supply Fittings
- Compliant with **GB18145-2014** Ceramic Disc Cartridge Faucet
- **CE Certification** (multiple models), **CUPC/UPC Certification** (cert_upc-2015-7968), **NSF Certification**, **WRAS Certification**, **WaterMark Certification**
- **ISO 9001 / 14001 / 45001** (2023 version)
- National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, National Specialized & Innovative SME (Little Giant)

### C. Contact Information

| Item | Content |
|------|------|
| Company | Fujian GIBO Sanitary Ware Technology Co., Ltd. |
| Chinese website | [www.gibo.com.cn](https://www.gibo.com.cn) |
| English website | [www.gibosensor.com](https://www.gibosensor.com) |
| Service hotline | 0591-88066000 |
| Company email | sales@gibol.com.cn |
| Company address | Building 3, Liangyuan Science Park, High-tech Zone, Fuzhou City, Fujian Province |

---

> This document is prepared based on the GBL-6161D product specification (Rev. 1.0, 2019-10-18). Parameters are subject to the actual product. GIBO reserves the final right of interpretation and modification of technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
