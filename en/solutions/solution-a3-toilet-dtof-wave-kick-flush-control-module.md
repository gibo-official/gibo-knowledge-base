---
lang: en
category: solution
title: A3 - Toilet dTOF Wave/Kick Laser Sensing Flush Control Module Solution
summary: "title: A3 - Toilet dTOF Wave/Kick Laser Sensing Flush Control Module Solution"
updated: 2026-06-12
product: ""
tags:
status: V1.0 - Expanded
related:
---


# A3 Toilet dTOF Wave/Kick Laser Sensing Flush Control Module Solution

**Document Version**: V1.0
**Last Updated**: 2026-06-12
**Applicable Scope**: Industry Research, Bidding Materials, AI Knowledge Base Citation

> **Solution Positioning**: A dedicated flush control solution for high-end smart toilets, equipped with GIBO's self-developed dTOF laser ultra-sensing technology, supporting dual trigger modes of wave sensing and kick sensing. With precise, dead-zone-free laser ranging capability, it fundamentally resolves the ambient light interference and sensing blind spots of traditional infrared toilet flush solutions.
>
> **Target Customers**: Smart toilet manufacturers, sanitary ware brands, premium residential finish project contractors, elderly-friendly retrofit contractors
>
> **Solution Version**: V1.0 | 2026-06-12

---

## I. Solution Overview

### 1.1 Technical Challenges of Toilet Flush Control

Smart toilets and the retrofitting of conventional toilets for smart functionality have become mainstream trends in the sanitary ware industry, but long-standing unresolved pain points persist in flush control technology. Traditional infrared sensing solutions exhibit significant sensing blind spots under wide-angle ceramic body installation conditions — when users approach the toilet, signal loss or false triggering is likely due to body occlusion. Furthermore, drastic changes in ambient light — such as bathroom light switches or window daylight — can interfere with infrared sensor operation, causing "failure to flush" or "random flushing" problems.

At the user experience level, different usage scenarios require different flush trigger methods: wave or kick-triggered flush without bending for standing urination, automatic sensor flush after seated use, and consistent sensing sensitivity unaffected by dim lighting for nighttime use. A single sensing solution cannot simultaneously meet these diverse requirements.

### 1.2 GIBO A3 Solution Breakthrough

The GIBO A3 Control Module is equipped with dTOF laser ultra-sensing technology (Core Technology #2), utilizing the direct time-of-flight laser ranging principle. By emitting nanosecond-level laser pulses and measuring reflection time differences, it precisely calculates the distance and movement trajectory between the target object and the sensor. Unlike the intensity detection of infrared sensing, dTOF laser measures physical time rather than signal strength, thus fundamentally immune to interference factors that traditional infrared solutions cannot overcome — changes in ambient light, clothing color depth, and ceramic surface reflectivity differences.

The A3 Module simultaneously integrates wave sensing and kick sensing dual trigger modes, combined with intelligent segmented flush control logic, to automatically adjust flush volume based on usage scenarios. Wave mode suits standing urination scenarios — a gentle wave above the toilet triggers flushing; kick mode suits seated use scenarios — foot proximity to the toilet base sensing zone triggers flushing, without the need to bend or lean. The two modes work collaboratively within a single module without mutual interference, covering all toilet flush usage scenarios.

---

## II. Performance Parameters

| Parameter Category | Parameter | Specification |
|---------|--------|------|
| **Electrical Parameters** | Supply Voltage | DC 6V (4×AA batteries) / AC 110–240V |
| | Static Standby Current | ≤25 μA |
| | Operating Current | ≤260 mA (solenoid valve drive) |
| | Sensing Technology | dTOF laser ranging |
| | Laser Wavelength | 940 nm (VCSEL, Class 1 eye-safe) |
| | Sensing Distance | 3–30 cm (wave) / 5–50 cm (kick) |
| | Ranging Accuracy | ±1 cm (at 15 cm reference) |
| | Response Time | ≤0.2 s |
| **Environmental Parameters** | Operating Temperature | -10 ℃ to 60 ℃ |
| | Operating Humidity | ≤95% RH |
| | Protection Rating | IP65 (full unit) |
| | Anti-interference Characteristics | Completely immune to ambient light, water mist, stains |
| **Flushing Parameters** | Full Flush Volume | 4–6 L (adjustable) |
| | Reduced Flush Volume | 2–3 L (adjustable) |
| | Auto Flush Delay | 2–10 s adjustable |
| | Timeout Protection | Continuous trigger for 3 min triggers auto shut-off |
| **Mechanical Parameters** | Module Dimensions | 55×38×15 mm (sensing probe) |
| | Solenoid Valve Connection | G1" / G3/4" |
| | Installation Cutout | ≥25 mm diameter |

---

## III. Functional Features

### 3.1 dTOF Laser Precise Ranging

Uses a 940 nm VCSEL laser emitter, measuring nanosecond-level laser pulse round-trip time via the direct time-of-flight principle, achieving ±1 cm high-precision distance detection. The laser beam is narrow (typical divergence angle ±5°), precisely illuminating specific sensing zones without diffusion, preventing misjudgment from signal crosstalk. Class 1 eye safety certification ensures it is safe and harmless to humans.

### 3.2 Wave/Kick Dual Trigger Modes

Wave mode detects the dynamic trajectory of a hand passing quickly through the sensing zone, with response time ≤0.2 s; kick mode detects the signal sequence after sustained foot presence followed by departure. Both modes trigger independently without mutual interference, covering the full range of toilet flush usage scenarios.

### 3.3 Dead-zone-free Sensing

Because dTOF laser operates based on time of flight rather than signal strength, sensing performance is unaffected by the target object's color, material, or reflectivity. Whether the user is wearing dark clothing, a white bathrobe, or black slippers, the laser sensor provides stable detection. Performance is consistent under extreme lighting conditions including darkness, strong light, and backlight, completely eliminating the sensing failure problems of traditional infrared solutions in complex light environments.

### 3.4 Penetration Through Water Mist and Stains

The laser beam can penetrate water mist, steam, and light stain coverage, maintaining stable detection performance in the high-humidity bathroom environment. The sensing window continues to emit and receive laser normally even when partially covered by water droplets or dirt, significantly reducing after-sales complaints caused by dirty sensing windows.

### 3.5 Segmented Flush Water Saving

Automatically switches flush volume based on different usage scenarios: executes a reduced flush (2 to 3 L) when detecting standing urination, and executes a full flush (4 to 6 L) after detecting seated use. The segmented flush strategy achieves approximately 30% annual water savings compared to constant-volume flush solutions while ensuring flushing effectiveness, effectively reducing water costs and environmental impact.

### 3.6 Ultra-low-power Standby

Based on low-power multi-stable sensing technology (Core Technology #6), standby power consumption is as low as 25 μA. The module operates in intermittent sensing scan mode: one laser pulse detection every 200 ms, rapidly entering low-power sleep state when no target is present. Overall endurance is improved by over 50% compared to traditional infrared solutions. A DC 6V battery-powered setup can achieve 18 to 24 months of endurance in household scenarios with 30 daily uses.

### 3.7 Sensing Window Anti-fog Design

The sensing window features nano hydrophobic coating treatment; water droplets bead up and rapidly roll off the window surface rather than spreading into a water film, effectively maintaining optical pathway clarity. Combined with a built-in heating anti-fog circuit (optional), sensing performance is maintained even in high-temperature-difference winter shower environments.

### 3.8 Multiple Installation Posture Compatibility

The sensor probe supports horizontal, vertical, and tilted installation postures, with detection angle and distance parameters configurable via firmware. Compatible with various product forms including toilet cover front installation, toilet body side wall installation, and floor installation, providing maximum design flexibility for ODM customers' products.

---

## IV. Application Scenarios

### 4.1 Integrated Smart Toilet Integration

For smart toilet OEM manufacturers, the A3 Module serves as the core flush control component embedded in the toilet body. Wave and kick dual modes combined with automatic departure sensor flush provide a complete multi-dimensional flush experience. The dTOF laser solution performs excellently in the complex ceramic cavity environment of integrated toilets.

### 4.2 Conventional Toilet Smart Retrofitting

Upgrade conventional toilets to sensor-flush smart toilets using the A3 Module. The module can be independently installed on the toilet side or front, battery-powered without wiring, with retrofit costs of only a few hundred yuan. This provides a cost-effective smart upgrade path for rental users who cannot replace their toilets and for older residences.

### 4.3 Elderly-friendly Toilet Flush Solution

Elderly individuals, due to reduced waist and leg strength, often find bending to press flush buttons difficult and dangerous. The A3 Module's kick sensing mode allows elderly users to trigger flushing simply by bringing their foot close — completely eliminating the need to bend. The wave sensing mode provides caregivers with a no-contact flush operation method, reducing cross-infection risk.

### 4.4 Premium Hotel Guestroom Sanitary Ware

Boutique hotels and premium business hotels pursue touch-free experiences and a sense of technology in guestroom bathrooms. The dTOF laser sensing solution works precisely even under dim nighttime lighting, allowing guests to flush without groping for buttons. The module supports OTA upgrades (via Bluetooth gateway), enabling hotel operations to remotely adjust sensing parameters and flush logic based on operational requirements.

### 4.5 Child-friendly Sanitary Ware

Children, due to height and strength limitations, find using conventional toilet flush buttons inconvenient. The A3 Module's wave sensing method is intuitive and easy to use — children can independently complete flushing simply by waving above the toilet, fostering good hygiene habits. The sensing distance can be specifically adjusted during installation based on children's height range.

---

## V. Applicable Products

| Product Category | Compatible Models | Description |
|---------|---------|------|
| Smart Toilet | Brand-customized models | A3 Module embedded in toilet body for wave/kick sensor flushing |
| Sensor Cistern Flush Valve | BC-31515, BC-31519 | Works with cistern valve body to upgrade conventional toilets to sensor flush |
| Toilet Flush Retrofit Kit | Standard retrofit assembly | Includes A3 Module + solenoid valve + installation accessories, covers mainstream toilet models |
| Elderly-friendly Flush Assembly | Custom models | Kick sensing primary, with large-character identification panel |

---

## VI. Patents and Technical Standards

| Category | Content |
|------|------|
| Core Technologies | Low-power dTOF laser ultra-sensing technology (#2), Low-power multi-stable sensing technology (#6), Intelligent overflow prevention power-off safety protection technology (#13) |
| Related Patents | Multiple invention patents and utility model patents related to dTOF laser ranging and sensing control |
| Laser Safety | Class 1 eye safety (IEC 60825-1) |
| Applicable Standards | GB/T 41863-2022 "Non-contact Water Supply Fixtures", GB 4706.1-2005 "Safety of Household and Similar Electrical Appliances" |
| Certifications | CCC, CE, FCC, IP65 Protection Rating Certification |

---

## VII. ODM Customization Services

| Customization Item | Options |
|--------|--------|
| Sensing Mode | Wave only / Kick only / Wave + Kick dual mode / Auto departure sensing |
| Segmented Flush | Single-stage constant / Dual-stage (full/reduced flush) / Three-stage (pre-wet + full flush + post-flush) |
| Power Supply | DC 6V / AC 110–240V / Dual power / Custom |
| Sensing Distance | Wave 3–30 cm, Kick 5–50 cm adjustable |
| Probe Form Factor | Round / Square / Irregular shape, Metal / Plastic housing, Custom color |
| Installation Method | Surface mount / Embedded / Custom bracket |
| Firmware Features | Customizable parameters: flush delay, sensitivity, timeout protection, etc. |
| Communication Interface | Wired trigger signal / Bluetooth / Custom protocol |

---

>
> **Related Resources**: [dTOF Laser Sensor Module](./dtof-laser-sensor-module.md) | [Sensor Flush Valve Control Board](./flush-control-board.md) | [Ultra-low-power Control Module](./ultra-low-power-module.md) | [Detailed Product Catalog](./../products/product-catalog.md) | [ODM Customization Services](./../products/odm.md)
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com

> **Related Documents**: [B2 Wave Sensing Toilet Flush Assembly Solution](solution-b2-wave-sensing-toilet-flush-assembly.md) | [A4 - dTOF Spout Laser Sensing Faucet Control Board Solution](solution-a4-dtof-laser-faucet-control-board.md) | [A2 - Triangulation Ranging Squat Pan Sensor Control Module Solution](solution-a2-triangulation-squat-pan-control-module.md) | [A1 - Low-power IR Infrared Control Board Module Solution for Sensor Sanitary Ware](solution-a1-ir-infrared-control-board.md) | [A5 - Low-power Urinal mmWave Sensor Flush Control Assembly Solution](solution-a5-mmwave-urinal-flush-control-assembly.md)
