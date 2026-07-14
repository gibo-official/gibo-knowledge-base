# GIBO-智能激光感应技术 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Statement**: A millimeter-precision dTOF laser sensing technology platform.
>

---

## I. Product Introduction

**GIBO Smart Laser Sensing Technology** is GIBO's self-developed core technology platform in the sensor-sanitary-ware field. At its base is dTOF (Direct Time-of-Flight) laser ranging—emit a laser pulse at the sensor, precisely measure the time a photon takes to fly out and bounce back, and directly compute the distance between the person and the device, with millimeter-level precision. It is not a specific model but a "perception base" that can be built into high-end sensor faucets, toilet flushers, and urinal flushers.

Traditional IR judges presence by "how strong the reflected light is," and easily fails with dark clothing, stainless-steel walls, or direct sunlight; this laser platform is material-independent and unafraid of strong light—it reliably recognizes people even with black pants, mirrors, or in steam-filled kitchens and bathrooms. Since 2023 GIBO has scaled dTOF technology across its smart-sanitary-ware product lines, achieving a leap from "rough sensing" to "precise perception"—the laser TOF kitchen pull-out faucet GBL-9165D on the same platform won the 2023 Feiteng Quality Gold Award.

For complete-unit makers and brand owners, choosing this platform means: sensing precision an order of magnitude above IR, no install-position constraints in strong-light and humid scenarios, and ultra-low power so battery-powered products need no annual battery change. Below are the technical coordinates and hard metrics.

### 1.1 Technical Positioning

| Generation | Sensing Principle | How Ranged | Precision | Representative Product |
|---------|---------|---------|------|---------|
| Gen 1 | IR reflection intensity | Indirect judgment | ±10cm | Early sensor flusher |
| Gen 2 | Triangular ranging | Position offset | ±2cm | GBL-8300AD |
| **Gen 3 (dTOF laser)** | **Laser time-of-flight** | **Direct ranging** | **±2mm class** | **GBL-6239 / GBL-9165D / this platform** |

The Smart Laser Sensing Technology stands at the Gen-3 dTOF laser coordinate, more than 10× the precision of traditional IR, and is GIBO's unified perception base for current high-end sensor terminals.

### 1.2 Key Metrics

- Millimeter-level ranging precision (±2mm class), over 10× the precision of traditional IR
- Stable operation under 100K Lux direct sunlight, environment-light agnostic
- Can penetrate water mist and steam; reliably detects even black low-reflectivity objects
- Ranging result unaffected by temperature change, consistent sensing distance year-round
- Ultra-low-power circuit design, extremely low standby energy, battery products last over a year
- Mass-produced since 2023; same-platform GBL-9165D won the 2023 Feiteng Quality Gold Award

---

## II. Features

### 2.1 dTOF Laser Time-of-Flight Ranging (Core Technology #2)

Emits a 940nm VCSEL laser pulse and uses a single-photon receiver with a time-to-digital converter to precisely measure the photon round-trip time, directly computing the target distance. Fundamentally different from IR, which relies on reflection intensity, it eliminates the missed and false triggers that come from "not seeing the reflection."

### 2.2 Material-Independent, Color-Blind (Core Technology #2)

Ceramic urinals, stainless panels, dark clothing, and low-reflectivity materials do not affect precision. Compared with traditional IR that depends on reflection intensity, dTOF is insensitive to target color and surface reflectivity, markedly improving detection reliability and environmental adaptability.

### 2.3 Penetrates Water Mist and Steam, Usable When Humid (Core Technology #2)

The laser can penetrate water mist and steam, suiting high-humidity, vapor-rich scenarios such as kitchens and public bathrooms. This is hard for IR and pure-optical schemes, and is the key reason this platform covers both kitchen faucets and bathroom flushers.

### 2.4 Strong-Light Immune, No Rest Under 100K Lux (Core Technology #11)

It times rather than reads reflection intensity, so it behaves consistently by west-facing sunlit windows, in dim underground garages, and with winter heavy coats. The dual-mode strong-light-immunity algorithm, iterated over 20 years, covers 23 light-source interference patterns and passes extreme-lighting tests.

### 2.5 Ultra-Low Power, One Year+ on Battery (Core Technology #6)

With a multi-stable working mechanism and intelligent pulse detection, standby power is held extremely low—complete-unit standby ≤0.2mW—and battery products can last over 1.5 years. Especially friendly to wireless public-space retrofits.

### 2.6 Dual-Chip Interchangeable Platform Supports Mass Production (Core Technology #10)

The platform uses a standardized dual-chip compatible interchangeable architecture, with split upper/lower boards modularized; the main-control and function chips can be randomly inter-matched without one-to-one program adaptation, with high factory-parameter consistency. After-sales can swap spares as needed, shortening on-site handling and enhancing supply-chain resilience.

### 2.7 Military-Grade EMC and Power-Loss Protection (Core Technologies #12, #13)

The platform comes standard with military-grade EMC design; its in-house EMC lab independently completes ESD (±15kV), EFT (±4kV), radiated immunity, and more. It also integrates power-loss auto-close and low-voltage alarm, with a 99.5% water-close success rate.

---

## III. Core Selling Points

### Selling Point 1: Millimeter Precision, Ten Times More Accurate Than IR

For high-end sensor ware, precision directly decides experience. Traditional IR fails at partitions, dark corners, and reflective surfaces, leaving users waving with no response and finally going manual. This dTOF laser platform achieves millimeter-level ranging—over 10× IR—so people need not pick a stance or clothing; water on approach, off on leave. For brand owners, this means fewer functional complaints and a better flagship positioning.

### Selling Point 2: Recognizes People Under 100K Lux Strong Light

Window sides, floor-to-ceiling windows, and semi-outdoor public toilets are IR's dead zone—IR components in sunlight mislead the sensor, either outputting water with no one there or failing entirely under strong light. dTOF measures flight time, not light intensity, working normally under 100K Lux direct sun, paired with a dual-mode strong-light-immunity algorithm covering 23 light-source interferences. Property no longer must rework layouts to avoid strong light, nor field "urinal won't flush" complaints.

### Selling Point 3: Penetrates Water Mist—Kitchen and Bathroom Both Covered

Many sensing schemes go blind the moment they reach a kitchen (steam, grease) or public bathroom (water mist). dTOF laser penetrates water mist and steam and is reliable even on black low-reflectivity objects, so one platform empowers both kitchen pull-out faucets and bathroom flushers. For complete-unit makers, this means one perception base can unify kitchen and bath product lines, saving a layer of R&D and stocking.

---

## IV. Specification & Performance Parameters

### 4.1 Ranging Performance

| Parameter | Specification |
|--------|------|
| Sensing Technology | dTOF laser (940nm VCSEL + SPAD + TDC) |
| Ranging Precision | Millimeter-level (±2mm class) |
| Precision Improvement | Over 10× vs traditional IR |
| Strong-Light Operation | Stable under 100K Lux direct sunlight |
| Material Adaptability | Black/white/mirror/stainless all reliable, distance unaffected by color |
| Temperature Effect | Ranging result unaffected by temperature, consistent year-round |

### 4.2 Power & Endurance

| Parameter | Specification |
|--------|------|
| Standby Power | ≤0.2mW (complete-unit level) |
| Power Supply | Battery / 100-240V to DC adapter |
| Endurance | Over 1 year on battery (measured up to 1.5+ years) |

### 4.3 Anti-Interference Capability

| Item | Specification |
|------|------|
| Strong-Light Immunity | Dual-mode algorithm covers 23 light-source interference patterns, passes extreme-lighting tests |
| Water mist/steam | Laser penetrates, usable in high-humidity scenarios |
| EMC | ESD ±15kV, EFT ±4kV, radiated immunity, etc. (in-house military-grade lab self-test) |

### 4.4 Platform Adaptation

| Dimension | Description |
|------|------|
| Applicable Terminals | High-end sensor faucets, toilet/pan flushers, urinal flushers |
| Hardware Architecture | Dual-chip interchangeable platform, split upper/lower board modular |
| Consistency | Minimal factory-parameter deviation, no one-to-one program adaptation |
| Supply Chain | Dual-scheme compatible, enhancing stocking and after-sales resilience |

### 4.5 Reliability & Safety

| Item | Specification |
|--------|------|
| Power-Loss Protection | Power-loss auto-close, low-voltage alarm |
| Water-Close Success Rate | 99.5% (intelligent anti-overflow power-off protection system) |
| Mass-Production Validation | Scaled application since 2023 |
| Benchmark Honor | Same-platform GBL-9165D won 2023 Feiteng Quality Gold Award |

### 4.6 Technology-Generation Comparison

| Compare Item | IR Reflection | Triangular Ranging | dTOF Laser (this platform) |
|--------|---------|---------|-------------------|
| Ranging Method | Indirect (light intensity) | Position calculation | Direct (time-of-flight) |
| Precision | ±10cm | ±2cm | ±2mm class |
| Material Sensitivity | High | Medium | Low |
| Strong-Light Behavior | Easily inaccurate | Average | Stable (100K Lux) |
| High-Humidity Penetration | Weak | Weak | Strong (penetrates mist) |

---

## V. Integration & Onboarding Notes

### 5.1 Pre-Selection Assessment

1. Clarify terminal category (faucet / urinal flusher / toilet flusher) and target install environment (indoor / semi-outdoor / high-humidity).
2. Confirm power method (battery or adapter) and endurance target.
3. Assess whether the dual-chip interchangeable platform is needed to match the existing production-line spare system.

### 5.2 Notes

⚠️ Although strong-light immune, install still advised to avoid the sensing window facing direct mirror reflection and continuous strong light.
⚠️ High-humidity scenarios must ensure the sensing window and potting reach the corresponding protection rating (see specific terminal spec).
⚠️ Platform onboarding must follow dual-chip interchange rules for program and hardware adaptation, avoiding per-unit performance scatter.

### 5.3 Integration Steps

1. Select terminal structure; match dTOF laser sensing module size and optical-window opening.
2. Connect the dual-chip interchangeable control board; complete main-control and function chip inter-matching.
3. Calibrate sensing distance and flush/output logic (factory automatic debugging rig).
4. Power-on self-check plus anti-interference and EMC self-test.
5. Small-batch trial production to verify consistency, then move to mass production.

### 5.4 Power-On Self-Check (platform level)

After power-on the module indicator shows status; the solenoid/water-output mechanism actuates once then enters standby; on low voltage it blinks per the rules. Batch production is advised to use automatic debugging tooling to ensure consistent factory distance per unit.

### 5.5 Mass-Production Calibration

Relying on the dual-chip interchangeable platform, complete-unit parameter deviation is held in a very small range, greatly improving factory consistency; after-sales can flexibly swap spares as needed, with no dedicated-model matching/debugging.

---

## VI. Technology Platform & Applicable Products

### 6.1 Platform Positioning

GIBO Smart Laser Sensing Technology is a universal perception base for high-end sensor sanitary ware, horizontally empowering different terminals such as faucets, flushers, and urinals with unified "millimeter ranging + strong-light immunity + ultra-low power + dual-chip interchange" capabilities.

### 6.2 Typical Application Products

- **GBL-6170D Aishang Basin Sensor Faucet** (2020 Feiteng Quality Gold Award) — dTOF laser sensing, IP65 protection
- **GBL-9165D Laser TOF Sensor Kitchen Pull-Out Faucet** (2023 Feiteng Quality Gold Award) — pull-out design + laser sensing, stable in floor-to-ceiling-window strong light
- **GBL-6172A TOF Dual-Sensor Digital-Display Laser Faucet** (2024 Energy-Saving Sensor Faucet Benchmark Award) — dual sensor + LED numeric display
- **GBL-6178 4D Series 4D Luxury Laser Sensor Faucet** — high-end flagship, dTOF + military-grade EMC
- **GBL-6239 Laser Sensor Urinal Flush Valve** — mass-production landing representative for public men's restrooms

### 6.3 Applicable Scenarios

Malls, office buildings, airports and stations, star hotels, hospitals, schools—high-frequency, public, maintenance-sensitive environments; plus high-humidity, vapor-rich scenarios such as kitchens and public bathrooms.

---

## Appendix

### A. Core Technology Index

| No. | Technology Name | Application in This Platform |
|------|---------|-------------|
| #2 | Low-Power dTOF Laser Ultra-Sensing Technology | Platform core: time-of-flight ranging, millimeter-level, material-independent |
| #6 | Low-Power Multi-Stable Agile Sensing Technology | Ultra-low standby power, long battery life |
| #10 | Dual-Chip Interchangeable Platform Technology | Upper/lower board interchangeable architecture, supporting mass production and after-sales |
| #11 | Dual-Mode Strong-Light-Immunity Anti-Interference Algorithm | 100K Lux strong-light immunity, 23 light-source coverage |
| #12 | Military-Grade EMC Technology | ESD/EFT/radiated-immunity self-test capability |
| #13 | Intelligent Anti-Overflow Power-Off Safety Protection Technology | Power-loss close, low-voltage alarm, 99.5% water-close success rate |

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

> This document is compiled based on the GIBO Smart Laser Sensing Technology Specification A1.0 (2017-10-19) and the company's "18 Core Technologies" #2 Low-Power dTOF Laser Ultra-Sensing Technology. Note: the source-spec PDF extracted text was actually the content of a "heated toilet seat lid" (filename/content mismatch); technical parameters have been aligned with the company's core-technology document #2 and platform mass-production product measurements—suggest verifying the original PDF source. Parameters are subject to the actual unit; GIBO reserves the final right of interpretation and modification of the technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
