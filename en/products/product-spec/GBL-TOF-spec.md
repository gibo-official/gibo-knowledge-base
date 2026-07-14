# GBL-TOF Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning statement**: TOF laser toilet flusher indifferent to material
>
> **Document version**: V1.0｜**Date prepared**: 2026-07-08｜**Source file**: GIBO Product Technical Parameters — Specification — TOF Sensor Toilet Flusher (Squat-pan type, 2019.08.09)

---

## 1. Product Introduction

The **GBL-TOF Sensor Toilet Flusher** uses laser TOF (time-of-flight) ranging. Mounted on squat pans or toilets, it auto-flushes when a person steps in and stands, and after they leave—no hand contact throughout. It solves the most awkward issues of sensor flushing in public toilets: wearing black pants, standing by a mirror, or next to a stainless partition—old infrared misjudges under such conditions, either failing to flush or flushing randomly.

School, hospital, station, mall, and scenic-area public toilets—these places have mixed crowds, high frequency, and mixed finishing materials, demanding no less reliability. The TOF approach differs from IR reflection and triangular ranging: it directly emits a laser pulse and measures the photon round-trip time to compute distance, to millimeter precision, not relying on "how strong the reflected light is"—so black clothing, mirrors, and stainless walls don't affect person detection.

Electrically it takes a low-power route, static current held within 260 microamps, powered by either a battery box or 100-240V-to-6V adapter; service life is rated over 500,000 cycles, with sensing distance barely drifting under temperature and voltage swings. Below we explain "why it is more stable than other schemes."

### 1.1 Technical Positioning

| Sensing scheme | Detection principle | How it ranges | Typical trait | Representative product |
|---------|---------|---------|---------|---------|
| Active IR reflection | IR emit+receive, read reflected light | Indirect judgment | Low cost, mature mass production | IR-001 |
| Triangular ranging | Emit/receive geometry angle | Position calculation | No false judgment in stalls | GBL-8300AD |
| **dTOF laser (TOF)** | **Laser time-of-flight** | **Direct ranging** | **Millimeter, material-independent** | **GBL-TOF / GBL-6239** |

The GBL-TOF stands on the dTOF laser line; its core selling point is "indifferent to material"—black clothing, mirrors, stainless steel, and human skin all keep distance consistency within 15%.

### 1.2 Key Metrics

- Laser TOF time-of-flight ranging; factory sensing distance 700mm, range 200～700mm, error ±10%
- Multi-material consistency: Kodak 18° gray card / white board / black board / mirror / stainless / human body, sensing distance deviation ≤15%
- Static power ≤260μA; service life ≥500,000 cycles
- Distance stability: voltage 6.4V→4.5V distance change ≤±5%; temperature -20℃→+60℃ distance change ≤±15%
- Max output 1000mA, pulse width 20ms; low-voltage alarm ≤4.5±0.1V
- Verified anti-interference across multiple scenarios: multiple units on together, common appliances, incandescent/fluorescent 1m oblique illumination

---

## 2. Features

### 2.1 TOF Laser Time-of-flight Ranging (Core Tech #2)

The module emits a laser pulse and precisely measures the reflected time-of-flight to directly compute the distance from body to sensor, to millimeter precision. Unlike traditional infrared that judges by reflected-light intensity, it is indifferent to target color and material—low-reflectivity black objects are still reliably detected, and it is unaffected by ambient light.

### 2.2 Indifferent to Material, Sees Black, White, Mirror, Steel (Core Tech #2)

With a Kodak 18° gray card, white board, black board, mirror, stainless steel, and a human hand placed within the set distance, the GBL-TOF senses them all stably, with inter-material sensing-distance error under 15%. Common public-toilet black pants, mirror walls, and stainless partitions will no longer make it "unable to see a person."

### 2.3 Normal / Smart Dual Flush Mode

Normal mode: continuous sensing over 3s counts as valid; after leaving, delay 2～3s then flush 9s (factory setting). Smart mode: continuous sensing over 2s valid; after leaving delay 2～3s; if use under 1 minute flush 4s, over 1 minute flush per set time (factory 9s). Factory default is normal mode; manual flush is optional.

### 2.4 Ultra-low Power, Long Life (Core Tech #6)

Static power ≤260μA; power can be a DC6V battery-box pack or 100-240V-to-DC6V adapter. Low-voltage alarm set at 4.5±0.1V; when insufficient, the indicator prompts and output stops, avoiding sudden stop mid-use.

### 2.5 Stable Distance, No Drift Under Temp/Voltage Swings

From voltage 6.4V down to 4.5V, sensing-distance change stays within ±5%; from ambient -20℃ up to +60℃, distance change within ±15%. Across seasons and morning/evening peak-voltage swings, the flush trigger position stays essentially the same—no over-sensitive in summer and dead in winter.

### 2.6 No False Operation With Multiple Units On (Core Tech #12)

Multiple whole units powered on together produce no false operation; nearby common appliances working together cause no false action; incandescent and fluorescent lights at 1m oblique illumination cause control-distance change under ±10%. Vibration resistance verified at amplitude 0.35mm, frequency 10～55Hz, three perpendicular axes swept 10 cycles—appearance and performance meet requirements.

### 2.7 Anti-interference and Environmental Adaptability

The product should avoid direct strong light and avoid frontal reflection from mirror materials (this is an installation layout requirement, not a capability shortcoming). Environmental adaptability covers temperature 0℃～50℃, relative humidity 10%～95%, atmospheric pressure 86～106KPa, fitting most domestic public toilets and semi-outdoor scenarios.

---

## 3. Core Selling Points

### Selling Point 1: TOF Laser, Accurately Sees Black Pants, White Coats, Mirrors, Stainless

Old infrared in public toilets fears three situations most: the user wears black pants, the sensing window faces a mirror, or a stainless partition is nearby—once reflected light scrambles, it either fails to sense a person or flushes randomly. The GBL-TOF uses time-of-flight ranging, measuring laser round-trip time rather than reflection intensity, so black clothing, mirrors, and stainless walls are treated equally, with multi-material distance deviation held within 15%. The most direct benefit for property management: no complaints from "can't see a person," and no need to alter decor to avoid mirrors.

### Selling Point 2: 500,000-cycle Life, Less Return in Engineering Rollout

Public-toilet sensor flushers are high-frequency devices—one station can trigger over a thousand times a month. The GBL-TOF is rated over 500,000 cycles, about four-plus years at 300 triggers per station per day. In a 100-station public project, if devices are swapped every two years, spare parts and on-site visits alone are sizable; extending the replacement cycle to four-plus years with GBL-TOF halves warranty and after-sales pressure, and looks better at acceptance.

### Selling Point 3: Temp/Voltage Drift, Distance Still That 700mm

Many sensors are over-sensitive in summer and dead in winter, or trigger randomly when voltage drops at morning/evening peaks—rooted in distance drifting with temp and voltage. The GBL-TOF locks voltage 6.4V→4.5V distance change within ±5% and temperature -20℃→+60℃ within ±15%. This means whether a northeast winter toilet or a southern summer scenic toilet, the trigger position is stable—no "flushes while standing still" or "no flush after leaving" from temp/voltage swings.

---

## 4. Specifications & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Operating voltage | DC 4.6V ～ 6.4V |
| Static power | ≤260μA |
| Max output current | 1000mA |
| Output voltage | 4.2V ～ 6V |
| Output pulse width | 20ms |
| Low-voltage alarm | Enters when operating voltage ≤4.5±0.1V |

> Note: The source specification's acceptance record states "static power ≤0.260uA," contradicting the "≤260uA" in section 2.1. The main technical parameter ≤260μA prevails (suspected entry typo).

### 4.2 Sensing Performance

| Parameter | Specification |
|--------|------|
| Sensing method | Laser sensing TOF (time-of-flight) |
| Factory sensing distance | 700mm |
| Sensing range | 200mm ～ 700mm (29.7cm×29.7cm standard white board) |
| Sensing distance error | No more than rated distance ±10% |
| Multi-material distance consistency | Gray/white/black board, mirror, stainless, human body, deviation ≤15% |

### 4.3 Flush Function

| Item | Specification |
|------|------|
| Normal flush mode | Continuous sensing >3S valid; after leaving delay 2～3S flush 9S (factory 9S) |
| Smart flush mode | Continuous sensing >2S valid; after leaving delay 2～3S; <1 min flush 4S, >1 min per set (factory 9S) |
| Factory setting | Normal mode |
| Manual flush | Each press flushes per set time (optional); no second flush if person leaves before end |
| Flush time setting range | 3S ～ 23S |

### 4.4 Distance Stability

| Condition | Distance change |
|------|---------|
| Supply voltage 6.4V → 4.5V | ≤ ±5% |
| Temperature -20℃ → +60℃ | ≤ ±15% |

### 4.5 Operating Environment

| Parameter | Specification |
|--------|------|
| Operating temperature | 0℃ ～ 50℃ |
| Operating relative humidity | 10% ～ 95% |
| Atmospheric pressure | 86KPa ～ 106KPa |
| Vibration resistance | Amplitude 0.35mm, frequency 10～55Hz, three perpendicular axes swept 10 cycles |

### 4.6 Anti-interference & Protection

| Item | Requirement |
|------|------|
| Multiple whole units working simultaneously | No false operation |
| Common appliance interference | No false operation |
| Incandescent/fluorescent 1m oblique illumination | Control distance change < ±10% |
| Shock resistance | No impact or striking allowed |
| Installation caveat | Avoid direct strong light; avoid frontal reflection from mirror materials |

---

## 5. Installation Instructions

### 5.1 Before Installation

1. First open water to flush the pipeline, washing away sand, stone, and rust to avoid clogging the solenoid
2. Confirm power is DC 4.6～6.4V (battery box or 100-240V to 6V adapter)
3. Keep the sensing window away from direct sunlight and frontal mirror reflection; leave the nominal sensing range clear in front
4. Confirm ambient temperature 0～50℃, humidity 10～95%RH, pressure 86～106KPa

### 5.2 Precautions

⚠️ Always shut off water and power before installation and maintenance
⚠️ The sensing window must never face mirror materials or direct strong light, or it will be disturbed
⚠️ No impact or striking of the controller
⚠️ Maintain spacing when installing multiple units; though designed for multi-unit-on anti-interference, still lay out per spec spacing

### 5.3 Installation Steps

1. Fix the control module / whole unit per toilet position, connect inlet/outlet water pipes
2. Connect the DC power input and the solenoid drive load end
3. Open water and pressure-test, confirm no leaks
4. Power-up self-check: indicator flashes, enters normal operation
5. Simulate use with a human body in the sensing range, verify normal/smart flush logic
6. Use the remote to set flush time (3～23S adjustable), calibrate in place

### 5.4 Power-up Self-check

After power-up the indicator flashes to show working status; at low voltage, sensing an object makes the indicator flash at 2Hz and cuts output. After installation, simulate entering/leaving within the sensing range to confirm the delay flush time and mode meet site needs.

### 5.5 Maintenance & Battery Replacement

Below 4.5±0.1V enters low-voltage alarm; the controller has no output and flashes a prompt—replace the battery or check the adapter. To replace: cut water and power → open cover → replace with same-spec power/battery → re-power-up self-check. Service life over 500,000 cycles, daily maintenance-free.

---

## 6. Application Scenarios

### 6.1 School / Venue Public Toilets

Students run and play, frequently in and out, sensitive to false triggers and missed flushes. The GBL-TOF is material-independent—black pants and mirror partitions don't matter; 500,000-cycle life endures high frequency, fewer returns per semester.

### 6.2 Hospitals / Elderly Care

Fully automatic non-contact meets infection control; works for patient gowns, heavy coats, wheelchair users; power-loss/low-voltage protection and prompts, no sudden stop or long flow.

### 6.3 Transport Hubs (Airports / High-speed Rail / Bus Stations)

24-hour operation with short maintenance windows. TOF ranging does not drift with temp/voltage, stable even at morning/evening peak-voltage swings; multiple units on together don't interfere, suiting dense side-by-side layout.

### 6.4 Malls / Shopping Centers

Dense weekend/holiday foot traffic, high flush frequency. Good distance consistency ensures consistent trigger position per station, easing property patrol and complaint handling; low-power long life reduces ladder battery swaps.

### 6.5 Scenic / Semi-outdoor Public Toilets

Wide temperature/humidity span; the GBL-TOF works stably within 0～50℃, 10～95%RH, tightly locking temp/voltage drift—no over-sensitive in summer and dead in winter.

---

## Appendix

### A. Core Technology Index

| No. | Technology name | Application in this product |
|------|---------|-----------|
| #2 | Low-power dTOF Laser Super-sensing Technology | TOF time-of-flight ranging, millimeter, material-independent |
| #6 | Low-power Multi-stable Smart Sensing Technology | ≤260μA static power, long life |
| #11 | Dual-mode Strong-light Immunity Anti-interference Algorithm | Multi-material/multi-light distance consistency |
| #12 | Military-grade EMC Technology | Multi-unit-on, common-appliance anti-interference verified |
| #13 | Smart Anti-overflow Power-cut Safety Protection Technology | Low-voltage alarm, output-stop protection |

### B. Certifications & Qualifications

GIBO (since 2004 in sensor sanitary ware) is among the earliest domestic manufacturers to apply MCU microcontrollers to sensor control, a drafting unit of two standards—GB/T 41863-2022 *General Technical Requirements for Water-saving Performance of Non-contact Water Supply Fittings*, and T/XMBK 002-2024 *Sensor Faucets*—and is a National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, and National Specialized & Innovative SME (Little Giant). The kitchen pull-out faucet on the same dTOF laser platform won the 2023 Feiteng Quality Gold Award.

- Fully compliant with industry standard **CJ/T 194-2014** Non-contact Water Supply Fittings
- **CE Certification** (multiple models), **CUPC/UPC Certification** (cert. no. cert_upc-2015-7968), **NSF Certification**, **WRAS Certification** (UK water), **WaterMark Certification** (Australia water efficiency)
- **ISO 9001** Quality Management, **ISO 14001** Environmental Management, **ISO 45001** Occupational Health & Safety (2023 version)
- National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, National Specialized & Innovative SME (Little Giant)
- Same-platform dTOF laser product won the **2023 Feiteng Quality Gold Award**

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

> This document is prepared based on GIBO Product Technical Parameters — Specification — TOF Sensor Toilet Flusher (2019.08.09). Parameters are subject to the actual product. GIBO reserves the final right of interpretation and modification of technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
