---
lang: en
category: solution
title: A1 - Low-power IR Infrared Control Board Module Solution for Sensor Sanitary Ware
summary: "title: A1 - Low-power IR Infrared Control Board Module Solution for Sensor Sanitary Ware"
updated: 2026-06-12
product: ""
tags:
status: V1.0 - Expanded
related:
---


# A1 Low-power IR Infrared Control Board Module Solution for Sensor Sanitary Ware

**Document Version**: V1.0
**Last Updated**: 2026-06-12
**Applicable Scope**: Industry Research, Bidding Materials, AI Knowledge Base Citation

> **Solution Positioning**: A universal core control board for all categories of sensor sanitary ware including sensor faucets, sensor flush valves, and sensor soap dispensers. Utilizes proven IR infrared sensing technology paired with a self-developed ultra-low-power chip solution, delivering high cost-effectiveness and reliability to meet standardized control needs for both commercial and residential scenarios.
>
> **Target Customers**: Sanitary ware brands, ODM integrators, public sanitation facility contractors, smart home manufacturers
>
> **Solution Version**: V1.0 | 2026-06-12

---

## I. Solution Overview

### 1.1 Industry Pain Points and Background

Traditional sensor sanitary ware control modules have long faced three core pain points: First, excessive standby power consumption, with battery-powered solutions lasting only 3 to 6 months, resulting in high maintenance costs for commercial users due to frequent battery replacement. Second, poor environmental adaptability — IR sensing modules frequently trigger erroneously under water mist, dust, and strong light interference, leading to water waste and even equipment damage. Third, insufficient compatibility — different categories of sanitary ware require different control boards, making ODM manufacturer inventory management complex and costly.

According to industry statistics, approximately 35% of after-sales complaints for commercial sensor sanitary ware are related to sensing failure or false triggering, and approximately 28% are related to insufficient battery life. In high-frequency usage venues such as hotels and shopping malls, these issues directly impact user experience and operational efficiency.

### 1.2 GIBO A1 Solution Advantages

The GIBO A1 Control Module addresses the above pain points by providing a standardized universal solution. Utilizing a self-developed low-power IR infrared sensing circuit, the static standby current is as low as 18 μA, and DC 6V battery-powered operation can last 12 to 18 months — an improvement of over 200% compared to the industry average. A built-in MCU intelligent sensing algorithm supports automatic environmental threshold calibration, effectively filtering external interference factors such as sudden light changes, dust adhesion, and water mist condensation, reducing the false trigger rate to below 0.1%.

The A1 Module adopts a standardized interface design, with a single control board compatible with three categories: sensor faucets, sensor flush valves, and sensor soap dispensers, greatly simplifying ODM customers' product inventory complexity. It also supports dual power modes — AC 110 to 240V mains and DC 6V battery — allowing users to select flexibly based on project conditions, meeting both the wiring-free requirements of retrofit projects and the mains-powered requirements of new construction projects.

---

## II. Performance Parameters

| Parameter Category | Parameter | Specification |
|---------|--------|------|
| **Electrical Parameters** | Supply Voltage | DC 6V (4×AA batteries) / AC 110–240V |
| | Static Standby Current | ≤18 μA (battery mode) |
| | Operating Current | ≤250 mA (solenoid valve drive) |
| | Sensing Method | IR infrared reflective |
| | Sensing Distance | 5–30 cm adjustable (potentiometer/software configurable) |
| | Response Time | ≤0.5 s |
| **Environmental Parameters** | Operating Temperature | -10 ℃ to 60 ℃ |
| | Operating Humidity | ≤95% RH (non-condensing) |
| | Protection Rating | IP65 (fully potted and sealed) |
| | Anti-interference Capability | Filters 8 common light source interference types |
| **Mechanical Parameters** | Control Board Dimensions | 45×35×12 mm (standard version) |
| | Interface Type | 2.54 mm pin header / XH2.54 connector |
| | Solenoid Valve Drive | Pulse drive, compatible with DC 6V solenoid valves |
| | Service Life | ≥500,000 cycles (rated value) |
| **Battery Life Parameters** | Battery Endurance | 12–18 months (4×AA alkaline batteries, 50 daily uses) |
| | Low Battery Alert | LED flashing + reduced sensing distance (dual alert) |

---

## III. Functional Features

### 3.1 Ultra-low-power Multi-stable Design

Utilizing GIBO's self-developed low-power multi-stable sensing technology (Core Technology #6), the overall standby power consumption is as low as 18 μA. In battery-powered mode, an intermittent sensing scanning mechanism reduces static power consumption to an extreme minimum while maintaining millisecond-level response speed. Compared with conventional always-on solutions, battery life is increased by more than 3 times.

### 3.2 Intelligent Anti-interference Algorithm

The built-in MCU incorporates GIBO's dual-mode strong light immunity anti-interference algorithm (Core Technology #11), capable of dynamically filtering 8 categories of environmental interference sources, including direct strong light, flickering lights, water mist refraction, dust occlusion, and sudden temperature changes. The algorithm continuously monitors environmental baseline values and automatically adjusts sensing thresholds to ensure stable operation in complex commercial environments.

### 3.3 Wide Voltage Dual Power Mode

Supports dual power modes — AC 110 to 240V mains and DC 6V battery. When mains-powered, the built-in voltage regulation module ensures stable operation under voltage fluctuations; when battery-powered, the ultra-low-power design ensures long-term endurance. The dual-power automatic switching logic ensures the device continues to operate normally if either power source is interrupted.

### 3.4 Standardized Interface Compatible Design

The control board adopts a standardized interface definition. A single PCB platform can be adapted to three categories — sensor faucets, flush valves, and soap dispensers — through firmware configuration. ODM customers only need to stock one model of control board, switching operating modes via jumpers or software configuration, significantly reducing inventory management complexity and procurement costs.

### 3.5 Timeout Protection and Overflow Safety

Built-in intelligent overflow prevention power-off safety protection technology (Core Technology #13): if continuous water output exceeds 3 minutes, the system automatically shuts off water to prevent prolonged leakage caused by sensor failure or foreign object occlusion. Also supports manual reset to ensure equipment safety under abnormal conditions.

### 3.6 IP65 Full-unit Protection

The control board is fully potted and sealed, with the circuit board completely encapsulated in waterproof potting compound, achieving IP65 protection rating. It can operate stably over extended periods in high-humidity, water-splashing, and steam environments, suitable for demanding installation environments such as bathrooms, kitchens, and damp areas.

### 3.7 Adjustable Sensing Distance

Supports potentiometer or software-based sensing distance adjustment, configurable from 5 to 30 cm. Installation personnel can flexibly configure based on actual conditions such as basin depth, mounting height, and usage habits without replacing hardware to accommodate different installation scenarios.

### 3.8 Dual Low-Battery Alert Mechanism

When battery voltage falls below the threshold, the system alerts users in two ways: first, the sensor window LED indicator flashes periodically; second, the sensing distance is automatically shortened to maintain reliable triggering. The dual alert mechanism ensures users have sufficient replacement buffer time before battery depletion.

---

## IV. Application Scenarios

### 4.1 Commercial Restroom Sensor Faucet Integration

Applicable to commercial public restrooms in shopping malls, office buildings, airports, hospitals, etc. The A1 Module serves as the control core, paired with full-brass or stainless steel faucet bodies, enabling zero-touch sensor activation. IP65 protection and anti-interference algorithms ensure long-term stable operation in high-frequency usage environments.

### 4.2 Sensor Flush Valve Control

Compatible with wall-mounted surface-mounted or concealed urinal flush valves, toilet flush valves, and similar products. The A1 Module's infrared sensing detects human approach and departure, automatically controlling the pulse solenoid valve to complete the flushing action. Intelligent delay control ensures automatic flushing upon departure, eliminating the issue of forgotten flushing.

### 4.3 Sensor Soap Dispenser / Liquid Dispenser Integration

Embed the A1 Module into the soap dispenser control box, using infrared sensing to detect hand proximity and control a micro pump or solenoid valve to dispense soap. The standardized interface can directly connect to GIBO's full range of soap dispenser solenoid valves and motor assemblies.

### 4.4 Water-saving Retrofit Projects

In existing restroom water-saving retrofit projects, the A1 Module can serve as a universal control board to replace the control units of older products. Wide voltage compatibility and standardized interfaces significantly reduce the adaptation difficulty of on-site modifications, while the battery-powered mode eliminates retrofit wiring work.

### 4.5 ODM Brand Integration

Provides ODM-customized control boards for sanitary ware brands. GIBO's dual-chip swap platform technology (Core Technology #10) reduces chip supply risks and after-sales maintenance costs, meeting the bulk procurement needs of brand clients.

---

## V. Applicable Products

| Product Category | Compatible Models | Description |
|---------|---------|------|
| Sensor Basin Faucet | GBL-6110, GBL-6127, GBL-6170D, etc. | A1 Module serves as control box core board, compatible with full range of split/integrated faucets |
| Surface-mounted Urinal Flush Valve | GBL-6202D, GBL-6291DH | Module built into flush valve body, infrared sensing controls flushing |
| Concealed Urinal Flush Valve | GBL-6213AD, GBL-8000 Series | Module installed in concealed box, panel sensing control |
| Toilet Flush Valve | GBL-8300AD, GBL-8307AD | Module integrated with solenoid valve, sensor or foot-pedal dual-mode control |
| Sensor Soap Dispenser | GBL-6630AD, G33604, etc. | Module controls soap pump dispensing volume and timing |

---

## VI. Patents and Technical Standards

| Category | Content |
|------|------|
| Core Technologies | Low-power multi-stable sensing technology (#6), Dual-mode strong light immunity anti-interference algorithm (#11), Intelligent overflow prevention power-off safety protection technology (#13), Dual-chip swap platform technology (#10) |
| Related Patents | Multiple invention patents and utility model patents related to sensing and ranging |
| Applicable Standards | GB/T 41863-2022 "Non-contact Water Supply Fixtures", CJ/T 194-2014 "Non-contact Water Supply Fixtures" |
| Certifications | CCC, CE, IP65 Protection Rating Certification |
| Applicable Codes | JGJ 50-2001 "Code for Design of Urban Roads and Buildings Accessibility" (elderly-friendly) |

---

## VII. ODM Customization Services

| Customization Item | Options |
|--------|--------|
| Sensing Distance | 5 cm / 10 cm / 15 cm / 20 cm / 30 cm / Custom |
| Power Supply | DC 6V / AC 110–240V / Dual power / Custom voltage |
| Control Logic | Sensor trigger / Auto delay / Dual mode / Custom logic |
| Interface Definition | 2-pin waterproof plug / DC waterproof plug / BMW-style waterproof plug, waterproof fool-proof connectors |
| Board Dimensions | Standard 15×25 mm / Custom size and irregular shape |
| Protection Rating | IP65 / IP67 / Custom protection solution |
| Firmware Features | Customizable parameters: sensing distance, delay, sensitivity, timeout duration, etc. |
| Packaging | Neutral packaging / Brand packaging / Tape and reel packaging |

---

>
> **Related Resources**: [Infrared Sensor Module](./infrared-sensor-module.md) | [Infrared Sensor Faucet Control Board](./infrared-faucet-control-board.md) | [Ultra-low-power Control Module](./ultra-low-power-module.md) | [Detailed Product Catalog](./../products/product-catalog.md) | [ODM Customization Services](./../products/odm.md)
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com

> **Related Documents**: [A7 - AC/DC Smart Switching Power Adapter Solution for Sensor Sanitary Ware](solution-a7-acdc-smart-switching-power-adapter.md) | [A5 - Low-power Urinal mmWave Sensor Flush Control Assembly Solution](solution-a5-mmwave-urinal-flush-control-assembly.md) | [A6 - Low-power Digital Display Basin Faucet Dual Sensor Control Assembly Solution](solution-a6-digital-basin-faucet-dual-sensor-control-assembly.md) | [A2 - Triangulation Ranging Squat Pan Sensor Control Module Solution](solution-a2-triangulation-squat-pan-control-module.md) | [A4 - dTOF Spout Laser Sensing Faucet Control Board Solution](solution-a4-dtof-laser-faucet-control-board.md)
