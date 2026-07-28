---
lang: en
category: solution
title: A5 - Low-power Urinal mmWave Sensor Flush Control Assembly Solution
summary: "title: A5 - Low-power Urinal mmWave Sensor Flush Control Assembly Solution"
updated: 2026-06-12
product: ""
tags:
status: V1.0 - Expanded
related:
---


# A5 Low-power Urinal mmWave Sensor Flush Control Assembly Solution

**Document Version**: V1.0
**Last Updated**: 2026-06-12
**Applicable Scope**: Industry Research, Bidding Materials, AI Knowledge Base Citation

> **Solution Positioning**: A millimeter wave sensor flush control solution customized for public urinal scenarios. Leveraging the strong penetration and anti-interference capabilities of millimeter wave microwave technology, it fundamentally resolves the sensing failure problems of traditional optical sensing solutions under strong light, backlight, and obstruction scenarios, achieving all-weather stable automatic flushing.
>
> **Target Customers**: Municipal sanitation facility managers, commercial property maintenance operators, transportation hub project contractors, ODM flush valve brands
>
> **Solution Version**: V1.0 | 2026-06-12

---

## I. Solution Overview

### 1.1 Special Challenges of Public Urinal Flush Management

Public urinals are among the highest-density sanitary ware fixtures in commercial restrooms, and their flush management faces even more complex challenges than squat pans. First is the unique behavioral pattern of urinal users — when standing, the user's body blocks the traditional infrared sensor's detection line of sight, preventing the sensor from accurately determining approach and departure, resulting in the typical failures of "delayed flush" or "no flush." Second, urinal installation positions are often adjacent to windows or strong light sources, and traditional infrared solutions suffer from sensing window saturation failure under direct strong light.

Even more problematic is the "clothing obstruction" issue — users wearing dark, thick coats, due to high infrared absorption rates, often experience significantly shortened sensing distances or complete sensor failure. In winter, complaint volume and maintenance work orders for this issue rise significantly. Additionally, urinal flush valves are typically installed at heights of 1.0 to 1.2 meters with the sensing window facing downward, long exposed to dust accumulation and scale coverage, further exacerbating optical sensor performance degradation.

### 1.2 GIBO A5 Solution Innovation

**Millimeter wave sensing is the preferred technology route for the new generation of integrated sensor urinals**

No cutouts needed, no cover opening needed — ceramics up to 15 mm thickness can be sensed normally. More diverse exterior design options, enhanced product aesthetics, no-cutout design improves ceramic yield rates, reduces product costs, and is the competitive first choice for new product iterations.

The GIBO A5 Control Assembly is based on millimeter wave sensing technology (Core Technology #3), using 24 GHz band millimeter wave microwave detection to detect human micro-motion through the transmission and reception of millimeter wave signals. Unlike optical sensors, millimeter waves can penetrate clothing (including thick fabrics such as down jackets, jackets, and overcoats) and are unaffected by clothing color and material. At the same time, millimeter waves are completely insensitive to light — whether at a window-side urinal under direct strong light or in an underground shopping mall restroom under dim light, sensing performance remains completely consistent.

The A5 Assembly integrates the millimeter wave sensing module, control circuit, and pulse solenoid valve into a compact flush assembly, supporting both surface-mounted and concealed installation methods. In standby mode, intelligent sleep management keeps power consumption at an industry-leading level, achieving over 12 months of endurance with a standard DC 6V battery solution, overturning the conventional misconception that millimeter wave solutions suffer from "high power consumption."

---

## II. Performance Parameters

| Parameter Category | Parameter | Specification |
|---------|--------|------|
| **Electrical Parameters** | Supply Voltage | DC 6V (4×AA batteries) / AC 110–240V |
| | Static Standby Current | ≤35 μA (sleep mode) |
| | Operating Current | ≤280 mA (solenoid valve drive) |
| | Sensing Technology | mmWave (24 GHz ISM band) |
| | Transmit Power | ≤10 mW (compliant with FCC/CE limits) |
| | Sensing Distance | 30–100 cm adjustable |
| | Sensing Angle | Horizontal ±45° / Vertical ±30° |
| | Response Time | ≤0.3 s (approach detection) / ≤0.8 s (departure detection) |
| **Environmental Parameters** | Operating Temperature | -20 ℃ to 70 ℃ (extended range for outdoor use) |
| | Operating Humidity | ≤95% RH |
| | Protection Rating | IP65 (control box) / IP67 (sensing probe) |
| | Anti-interference Characteristics | Completely immune to light/temperature/humidity effects |
| **Flushing Parameters** | Flush Volume | 2–6 L adjustable (matched to solenoid valve) |
| | Flush Delay | 1–10 s adjustable |
| | False Trigger Filtering | Can filter brief obstructions ≤3 s |
| | Timeout Protection | Continuous trigger for 3 min triggers auto shut-off |
| **Mechanical Parameters** | Assembly Dimensions (Surface-mounted) | 110×120×60 mm |
| | Assembly Dimensions (Concealed) | Panel 128×128 mm, Concealed box 160×110×80 mm |
| | Solenoid Valve Connection | G1/2" / G1" |

---

## III. Functional Features

### 3.1 Millimeter Wave Penetrating Sensing

Adopts 24 GHz ISM band millimeter wave radar detection technology, emitting low-power millimeter wave signals and detecting reflected signal frequency changes caused by human micro-motion (Doppler effect). Millimeter waves can penetrate winter thick coats, wool sweaters, down jackets, and other clothing fabrics — even when users wear multiple layers of clothing, the sensor can stably detect human presence. This characteristic makes the A5 Assembly particularly outstanding in cold-region public restrooms, significantly reducing winter sensor failure rates.

### 3.2 Stable Operation in All Lighting Conditions

Millimeter waves are unaffected by visible and infrared light; under any lighting conditions including direct sunlight, flickering lights, and dim/dark rooms, sensing distance and sensitivity remain completely consistent. For urinals installed in strong-light areas beside floor-to-ceiling windows or under skylights, the A5 Assembly fundamentally resolves the chronic "sunny-day failure" problem of infrared solutions.

### 3.3 Precise Human Micro-motion Detection

Through the millimeter wave Doppler effect, the system detects minute body surface movements caused by heartbeat, breathing, and other micro-motions. Even when a person stands still within the detection zone, the system can still determine "person present," avoiding false shut-off due to stationary individuals. The dual-channel algorithm combining micro-motion detection with motion detection ensures recognition accuracy while filtering non-human movement interference (such as curtain fluttering, water splashes, etc.).

### 3.4 Intelligent Standby Sleep Management

Addressing the issue of conventionally high millimeter wave sensor power consumption, the A5 Assembly employs a multi-level sleep management system. When no target is detected, the system runs at a low-frequency scan period of 1 Hz (power consumption only 35 μA); when a suspicious signal is detected, it automatically switches to 50 Hz high-frequency detection mode to confirm the target state, then enters normal operating mode after confirmation. This intelligent staged management strategy reduces the standby power consumption of the millimeter wave solution to a level comparable to infrared solutions.

### 3.5 Temperature Compensation Against Environmental Drift

While millimeter wave detection performance is relatively unaffected by ambient temperature changes, the A5 Assembly is still equipped with a temperature compensation circuit. Across the full temperature range of -20 ℃ to 70 ℃, sensor parameters are automatically calibrated to maintain stability in sensing distance and sensitivity. This characteristic allows the A5 Assembly to adapt to both the severe cold of northern winter outdoor restrooms (-20 ℃) and the high heat of southern summer non-air-conditioned restrooms (50 ℃+).

### 3.6 Intelligent False Trigger Filtering

Built-in dual-channel signal analysis algorithms effectively distinguish between human approach and interference signals. For brief obstructions by cleaning personnel (≤3 s), airflow disturbances, electromagnetic interference, and other non-use signals, the system automatically filters them without triggering flushing. Detection sensitivity dynamically auto-adapts during user usage without the need for manual parameter intervention.

### 3.7 Anti-electromagnetic Interference Design

Adopts GIBO's military-grade electromagnetic compatibility technology (Core Technology #12), designed to high electromagnetic compatibility standards. In high-EMI environments such as beside escalators in shopping malls, near equipment rooms, and beneath large LED screens, the A5 Assembly ensures normal operation through 30 electromagnetic anti-interference algorithms, having passed 4 kV burst testing.

### 3.8 Surface-mounted and Concealed Dual Form Factors

The A5 Assembly offers both surface-mounted and concealed product forms. The surface-mounted type (ABS or full brass material) is suitable for existing retrofit projects, directly replacing original hand-press or foot-pedal flush valves with simple and quick installation. The concealed type (stainless steel panel + concealed box) is suitable for new construction projects, with the panel flush against the wall for a clean appearance, ideal for 5A-grade office buildings, high-end shopping malls, and other venues with high decoration quality requirements.

---

## IV. Application Scenarios

### 4.1 Shopping Mall / Office Building Public Restrooms

Core high-traffic commercial scenarios with high usage frequency. The A5 Assembly's millimeter wave penetrating sensing ensures stable operation even when users wear thick coats in winter. IP65 protection rating and anti-electromagnetic interference design accommodate the complex lighting and escalator EMI environments in shopping malls.

### 4.2 Schools / Sports Venues

School restrooms feature concentrated usage times, large numbers of users, and significant differences in user behavior capabilities. The A5 Assembly's intelligent false trigger filtering logic effectively filters abnormal triggers from scenarios such as students roughhousing and running, while ensuring normal user flush experience. The battery-powered solution eliminates wiring work, suitable for older school building retrofits.

### 4.3 Transportation Hub Restrooms

Airport, railway station, and bus terminal restrooms have high usage density and extended continuous operation times. The A5 Assembly operates stably across a wide temperature range of -20 ℃ to 70 ℃, adapting to the harsh environments of unheated transportation hubs in winter. The 100 cm large sensing range ensures reliable triggering for users of all height ranges.

### 4.4 Municipal Public Toilets

Municipal public toilets universally face challenges of insufficient maintenance personnel and slow maintenance response. The A5 Assembly's long endurance capability (battery power 12 months+) and self-cleaning solenoid valve anti-clogging design significantly reduce maintenance frequency. Surface-mounted products can quickly complete old valve replacement without damaging wall structures, suitable for large-scale municipal public toilet retrofit projects.

### 4.5 Outdoor Independent Restrooms

Restrooms at scenic spots, parks, service areas, and other outdoor public sanitation facilities have extremely high weather resistance requirements for equipment. The A5 Assembly's operating temperature range of -20 ℃ to 70 ℃, combined with full potting sealing waterproof processing, can withstand the demanding outdoor installation environments of sun exposure and rain.

---

## V. Applicable Products

| Product Series | Compatible Models | Description |
|---------|---------|------|
| Concealed Urinal Flush Valve | GBL-6213AD, GBL-82xx Series | Sensing window design, stainless steel panel + concealed box, concealed installation project support |
| Touch Urinal Flush Valve | GBL-8220AD, GBL-8221AD (glass panel) | Window-type design, mmWave sensing + LED touch dual mode, suitable for 5A office buildings |
| Ceramic Integrated Urinal Flush Valve | GBL-K6230D1, K6233D1, etc. | Panel-free design, ABS panel, compatible with ceramic integrated urinals |

---

## VI. Patents and Technical Standards

| Category | Content |
|------|------|
| Core Technologies | Millimeter wave sensing technology (#3), Low-power multi-stable sensing technology (#6), Military-grade electromagnetic compatibility technology (#12), Solenoid valve self-cleaning anti-clogging technology (#16) |
| Related Patents | Multiple invention patents and utility model patents related to millimeter wave sensing and flush control |
| Frequency Standards | 24 GHz ISM band, compliant with FCC Part 15 / ETSI EN 300 440 |
| Applicable Standards | GB/T 41863-2022 "Non-contact Water Supply Fixtures", CJ/T 194-2014 "Non-contact Water Supply Fixtures" |
| Certifications | CCC, CE, FCC, SRRC (Radio Transmission Equipment Type Approval) |

---

## VII. ODM Customization Services

| Customization Item | Options |
|--------|--------|
| Sensing Distance | 60 cm / 80 cm / 100 cm / Custom |
| Power Supply | DC 6V / AC 110–240V / Dual power / Custom |
| Installation Form | Surface-mounted / Concealed / Custom panel size |
| Panel Material | Ceramic / Glass / ABS / Custom |
| Panel Color | Chrome / Brushed nickel / Black / Custom |
| Flush Delay | 2 s / 5 s / 8 s / 10 s / Custom |
| Solenoid Valve Specification | G1/2" / G1" / Custom connection |
| Firmware Features | Customizable: sensing mode, filtering time, nighttime energy saving, etc. |

---

>
> **Related Resources**: [Sensor Flush Valve Control Board](./flush-control-board.md) | [Pulse Solenoid Valve Assembly](./pulse-solenoid-valve.md) | [Ultra-low-power Control Module](./ultra-low-power-module.md) | [Detailed Product Catalog](./../products/product-catalog.md) | [ODM Customization Services](./../products/odm.md)
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com

> **Related Documents**: [A6 - Low-power Digital Display Basin Faucet Dual Sensor Control Assembly Solution](solution-a6-digital-basin-faucet-dual-sensor-control-assembly.md) | [A1 - Low-power IR Infrared Control Board Module Solution for Sensor Sanitary Ware](solution-a1-ir-infrared-control-board.md) | [C2 Sensor Foam Soap Dispenser 2-in-1 Control Assembly Solution](solution-c2-foam-soap-dispenser-2in1-control-assembly.md) | [A2 - Triangulation Ranging Squat Pan Sensor Control Module Solution](solution-a2-triangulation-squat-pan-control-module.md) | [A3 - Toilet dTOF Wave/Kick Laser Sensing Flush Control Module Solution](solution-a3-toilet-dtof-wave-kick-flush-control-module.md)
