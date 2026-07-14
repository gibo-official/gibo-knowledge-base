# GBL-6239 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning statement**: Laser sensor urinal flush valve unfazed by strong light
>
> **Document version**: V2.0｜**Date prepared**: 2026-07-08｜**Source file**: 6239 Laser Sensor Urinal Flush Valve Specification (S1.0, 2026-05-06)

---

## 1. Product Introduction

The GBL-6239 mounts on public male restroom urinals: it auto-flushes when a person approaches and gives a delayed supplementary flush after they leave—no hand contact with any switch throughout. It solves the three most common headaches of sensor sanitary ware in public restrooms: failure under strong window-side light, sluggishness in dim environments, and equipment that constantly needs attention.

Malls, office buildings, airports and stations, star hotels, hospitals, schools—these places see constant foot traffic, demand high hygiene and reliability, and most dread equipment that "won't flush when it should, flushes randomly when it shouldn't." The 6239 is built for exactly such high-frequency, open, maintenance-sensitive environments.

It uses GIBO's 3rd-generation dTOF laser ranging technology, fundamentally different from old infrared sensing: infrared judges presence by "how strong the reflected light is," easily erring with dark clothing, stainless steel walls, or direct sunlight; the 6239 directly measures the time-of-flight of the laser bouncing off the body, to millimeter precision—indifferent to material and unafraid of strong light. The circuit uses ultra-low-power management; 4× AA batteries last over 12 months, mounted under the basin or in a pre-embedded box, essentially maintenance-free.

Bringing the above together: the 6239 makes the public sensor urinal "flush accurately when it should, not waste when it shouldn't, and need no attention for a year after install." The three points below are the product values we believe are most worth telling.

### 1.1 Technical Positioning

| Tech generation | Sensing principle | How it ranges | Precision | Representative product |
|---------|---------|---------|------|---------|
| 1st gen | IR reflection intensity | Indirect judgment | ±10cm | Early sensor flusher |
| 2nd gen | IR triangular ranging | Position offset | ±2cm | GBL-8300AD |
| **3rd gen (dTOF laser)** | **Laser time-of-flight** | **Direct ranging** | **±2mm** | **GBL-6239** |

### 1.2 Key Metrics

- Ranging precision ±2mm; factory sensing distance 60cm (vs. standard white board)
- Standby power ≤0.2mW; 4 batteries last 12+ months
- Two-stage flushing; water-saving mode saves 40%~60% vs. conventional flushing
- ESD protection ±15KV air discharge; fast transient burst Level 4
- Sensing window submerged 20cm for 4 hours, no water ingress, no fogging

---

## 2. Features

### 2.1 Laser Ranging, Millimeter-precise Person Detection

The 6239 uses 940nm laser pulses with a single-photon detector (SPAD) and time-to-digital converter (TDC) to directly measure photon round-trip time. Dark ceramic urinals, stainless panels, and low-reflectivity materials do not affect precision; it works normally under 100K Lux direct sunlight, bath-heater strong light, and strobe lights. From -5℃ to 50℃, sensing-distance deviation is under 5%, consistent across all seasons.

### 2.2 Two-stage Flushing, Water-saving on Demand

Flushing has two stages: on arrival a 2s pre-rinse wets the inner wall, then after departure a delayed 6s main flush clears it. If the person leaves before the first stage ends, the second stage is not triggered—no wasted water.

In continuously high-frequency venues like malls and stations, switch to water-saving mode: if a user is sensed again within a minute, skip the pre-rinse and flush only the main stage, saving 40%~60% versus conventional mode. Factory default is conventional mode; the remote switches it in one click.

### 2.3 Remote Parameter Setting, No Panel Removal

Sensing distance, second-stage flush duration (1~24s), and water-saving mode switching are all set in front of the urinal with the standard wireless remote—no panel removal, no pre-embedded box opening. At limit values the LED flashes 3 times as a prompt, clear to any veteran technician.

### 2.4 Multiple Protections, No Running Water

Power loss auto-closes the valve; below 4.8V the LED flashes 5 times to prompt battery replacement, below 4.5V it flashes 10 times and auto-closes the valve to stop working; sustained obstruction beyond 3 minutes also auto-cuts off. Clear low-battery prompts let property staff replace batteries in time, with no sudden stop mid-use.

### 2.5 No False Trigger Under Seven Light Sources

Incandescent, fluorescent, halogen, electronic-ballast daylight, bath heater, and a hair dryer on the same outlet—these light sources alone or combined do not cause false operation of the 6239.

### 2.6 Stable in Electromagnetic Environments

Passes ESD Level 4 (±15KV), electromagnetic radiation 3V/m, and fast transient burst Level 4. Works normally beside mall escalators, variable-frequency AC, and large LED screens.

### 2.7 Triple-potted Waterproof

The sensing window and circuit module use a three-layer potting process, with connectors rated IP65 or above. Usable even in high-humidity, steam-filled bathroom environments.

---

## 3. Core Selling Points

### Selling Point 1: Laser Ranging, Accurately Detects People Even Under Strong Light

Conventional infrared essentially "strikes" on summer afternoons with direct window sunlight—users wave hands with no response, ending up manually flushing or not flushing at all. The 6239's dTOF laser does not judge by reflected-light intensity but by timing, so west-facing windows, dim underground garages, and winter heavy coats all look the same to it.

The most direct benefit for property management: no more "urinal won't flush" complaints, and no need to alter decor layout to avoid strong light.

### Selling Point 2: 4 Batteries for a Year, Two Fewer Trips for Property Staff

The 6239 standby power is just over 0.2mW. Do the math: a 50-urinal mall where devices need monthly battery swaps would spend over 20 man-hours a year just climbing ladders to swap batteries; the 6239 swaps once a year, basically zeroing that labor. For property managers of dozens of restrooms, small savings add up to real money.

### Selling Point 3: Two-stage Flushing Saves Water by Itself

Public spaces fear two wastes most: random flushing when empty, and incomplete flushing when occupied. The 6239's pre-rinse + main-flush design ensures cleanliness, while water-saving mode auto-skips the pre-rinse during high-frequency periods. At 6L per flush, one device in water-saving mode saves over 200 tons of water a year; a 50-unit commercial complex tops 13,000 tons a year. Beyond water bills, fewer maintenance trips also save money.

---

## 4. Specifications & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power supply | DC 6V (4× AA alkaline batteries) / AC 100V~240V to DC 6V adapter |
| Operating voltage range | 4.5V - 6.5V |
| Static power | ≤ 0.2mW |
| Output pulse width | 30ms (control) / 20ms (solenoid drive) |
| Response time | ≤ 2s |
| Sensing technology | dTOF laser (940nm VCSEL + SPAD + TDC) |

### 4.2 Solenoid Valve Parameters

| Parameter | Specification |
|--------|------|
| Rated voltage | DC 6V |
| Voltage range | 4.5V - 6.5V |
| Coil resistance (20℃) | 15Ω ± 5% |
| Pulse width | 20ms |
| Inlet / outlet | G1/2" internal thread / G1/2" external thread |

### 4.3 Operating Environment

| Parameter | Specification |
|--------|------|
| Operating temperature | 5℃ ~ 50℃ |
| Relative humidity | 10% RH ~ 95% RH |
| Operating water pressure | 0.05MPa ~ 0.7MPa |
| Storage temperature | -10℃ ~ 55℃ |

### 4.4 Sensing Performance

| Parameter | Specification |
|--------|------|
| Factory sensing distance | 60cm ± 10% (vs. 29.7×29.7cm standard white board) |
| Gray color card deviation | Within ± 10% |
| Black color card deviation | Within ± 20% |
| Sensing distance adjustment | Remote step up/down |
| Judgment time | 2s |

### 4.5 Flush Specifications

| Parameter | Specification |
|--------|------|
| Flush mode | Two-stage flushing (pre-rinse + main flush) |
| First-stage flush time | 2s ± 1s |
| Second-stage flush time (factory) | 6s ± 1s |
| Second-stage flush time (adjustable) | 1s - 24s |
| Water-saving mode | Auto-skip first stage during continuous high-frequency use |

### 4.6 EMC & Protection

| Test item | Test standard/condition | Result |
|---------|-------------|------|
| ESD | Level 4, air discharge ±15KV | Normal operation |
| EMI | 80MHz - 1000MHz, 3V/m | Not disturbed |
| Fast transient burst (EFT) | Level 4 | Normal operation |
| Light interference | Multiple light sources 15-91cm direct/oblique | No false trigger |
| Waterproof | Sensing window submerged 20cm for 4h | No seepage, no fogging |
| Burst pressure | 2.5MPa held 60s | No deformation, no leakage |

### 4.7 Compliance Standards

| Standard No. | Standard Name |
|---------|---------|
| CJ/T 194-2014 | Non-contact Water Supply Fittings |
| GB/T 4798.1 | Environmental Conditions for Electrical and Electronic Products — Part 1: Storage |
| GB/T 4798.2 | Environmental Conditions for Electrical and Electronic Products — Part 2: Transport |

---

## 5. Installation Instructions

### 5.1 Before Installation

1. First open water to flush the pipeline, washing away sand, stone, and rust to avoid clogging the solenoid
2. Confirm water pressure 0.05MPa ~ 0.7MPa; below 0.05MPa add a booster pump
3. Keep the sensing window away from direct sun and strong lamps; no obstruction larger than 1cm within 120cm in front
4. Install the pre-embedded box before tiling

### 5.2 Precautions

- Always shut off water and power before installation and maintenance
- Each AC-powered unit sets an individual power switch and reliable grounding
- Use high-performance alkaline batteries; do not mix old and new
- Do not hot-plug the sensor module terminals

### 5.3 Installation Steps

1. Cut the groove per pre-embedded box size, place the box, connect inlet/outlet water pipes
2. Level and fix
3. Open water and pressure-test, confirm no leaks
4. After tile dries, remove the protective cover
5. Connect power (battery box or adapter), install the sensing panel
6. On power-up the LED flashes once and the solenoid opens/closes once (self-check) then enters standby
7. Use the remote to tune sensing distance and flush time
8. Wave hand in front of the sensing window to test

### 5.4 Power-up Self-check

On power-up the LED flashes once → the solenoid briefly opens/closes → enters a 1-minute learning mode (LED steady on) → transitions to normal standby. During learning mode, do not keep the sensing window obstructed.

### 5.5 Battery Replacement

Below 4.8V, each sensing triggers the LED to flash 5 times to prompt battery replacement; below 4.5V it flashes 10 times and auto-closes the valve. To replace: shut off water → open panel → take out battery box and replace 4× same-brand new alkaline batteries → re-seat and re-run self-check.

---

## 6. Application Scenarios

### 6.1 Malls / Shopping Centers

Dense weekend/holiday foot traffic; water-saving mode auto-saves water; one battery change a year drops a 50-urinal venue's annual maintenance labor to about 4 hours; laser works normally under atrium skylight direct sun and complex lighting.

### 6.2 Offices / Corporate HQs

Sensitive user experience—the 6239 flushes on approach, no waving and waiting; remote tuning personalizes by floor usage frequency; concealed stainless panel fits high-end decor.

### 6.3 Airports / High-speed Rail Stations

24-hour operation with short maintenance windows. Full-condition adaptation, -10℃~55℃ storage, 5℃~50℃ operation; unaffected by direct sunlight; stable near escalators and security equipment.

### 6.4 Star Hotels / Clubs

Laser sensing has no visible red-light blink—quiet and elegant; low water hammer solenoid means low flush noise; dual-power compatible, guest rooms can use the adapter for permanent power, public areas use batteries wiring-free.

### 6.5 Hospitals / Elderly Care

Fully automatic non-contact meets infection control; indifferent to clothing material, works with patient gowns and heavy coats; power-loss auto valve-close prevents leaks.

### 6.6 Schools / Venues

The 2s judgment window filters brief obstructions from running students; battery solution needs no wiring, ideal for old-campus retrofit; burst pressure 2.5MPa, rugged.

---

## Appendix

### A. Related Patents (granted)

| Tech point | Patent name | Patent No. | Type |
|--------|---------|--------|------|
| dTOF laser sensing | A sensor faucet water-out device | ZL201910383793.2 | Invention Patent |
| Ranging/signal detection | A sensing water-out device and signal detection method | ZL201910380558.X | Invention Patent |
| Anti-false-trigger | A laser-IR dual-sensor faucet against false triggering | ZL 2024 2 1519018.8 | Utility Model Patent |
| Laser sensing module | An infrared-laser dual-beam sensing module | ZL 2025 2 0411615.7 | Utility Model Patent |
| Laser sensing module | A stacked laser sensing module for kitchen/bath equipment | ZL 2025 2 0632762.7 | Utility Model Patent |
| Bistable solenoid valve | A bistable solenoid valve and sensing water-out device | ZL 2019 2 0857586.1 | Utility Model Patent |
| Low water hammer | A kitchen/bath solenoid valve body with improved water-hammer structure | ZL 2023 2 3529883.9 | Utility Model Patent |
| Low water hammer | A low water-hammer solenoid valve assembly | ZL 2019 2 2114857.7 | Utility Model Patent |

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

> This document is prepared based on GBL-6239 Product Specification (S1.0, 2026-05-06). Parameters are subject to the actual product. GIBO reserves the final right of interpretation and modification of technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
