---
lang: en
category: solution
title: A2 - Triangulation Ranging Squat Pan Sensor Control Module Solution
summary: "title: A2 - Triangulation Ranging Squat Pan Sensor Control Module Solution"
updated: 2026-06-12
product: ""
tags:
status: V1.1 - Optimized (Integrated Standardized Working Principle)
related:
---


# A2 Triangulation Ranging Squat Pan Sensor Control Module Solution

**Document Version**: V1.0
**Last Updated**: 2026-06-12
**Applicable Scope**: Industry Research, Bidding Materials, AI Knowledge Base Citation

> **Solution Positioning**: A dedicated sensor control solution tailored specifically for public restroom squat pan scenarios. Equipped with GIBO's self-developed triangulation ranging sensing technology, it achieves ultra-low-power precise identification of human stance and departure actions, enabling intelligent automatic flushing to solve the flushing management challenges of traditional squat pans.
>
> **Target Customers**: Public restroom project integrators, municipal sanitation facility operators, commercial property management companies, ODM flush valve brands
>
> **Solution Version**: V1.0 | 2026-06-12

---

## I. Solution Overview

### 1.1 Flushing Management Challenges of Public Squat Pans

Public restroom squat pans are among the highest-frequency sanitary ware fixtures in commercial settings, yet flushing management has long faced systemic challenges. Traditional foot-pedal flush valves are frequently stepped on, with mechanical components wearing quickly and failure rates exceeding 20% annually. Hand-press flush buttons pose hygiene concerns — users reluctant to touch them may skip flushing altogether, leading to odor buildup and degraded user experience. Statistics show that approximately 60% of odor complaints in public restrooms are directly related to incomplete or skipped flushing.

In terms of water-saving management, traditional delayed-action flush valves lack precise control capability, with single flush volumes reaching 8 to 12 L, far exceeding the 6 L upper limit for water-saving flush valves specified in national standard GB/T 41863-2022. Taking a commercial squat toilet compartment with a daily average of 200 uses as an example, annual water consumption differences can exceed 300 tons.

---

## II. Standardized Working Principle

### 2.1 Core Detection Principle (Optical Triangulation Ranging)

This module is a high-precision sensing solution designed specifically for squat toilets. Unlike conventional infrared threshold sensing, it adopts **optical triangulation ranging principle + ultra-low-power MCU computation**, capable of accurately quantifying human body distance and dwell time, fundamentally solving the pain points of traditional infrared for squat pans — susceptibility to floor reflections, water vapor, dust, false triggering by passersby, and short-distance misjudgment. It is the standardized upgrade control solution for commercial smart public restroom squat pans.

The module's transmitter emits an infrared detection beam at a fixed angle, forming a reflected light spot after hitting the target in the detection zone. The receiving photoelectric array, based on the light spot offset position and built-in triangulation geometric algorithms, precisely calculates the **actual linear distance between the target and the probe**, rather than the vague signal strength determination of traditional infrared, achieving millimeter-level precise ranging identification.

### 2.2 Standardized Workflow

* **Low-power Standby Calibration**: Normal dormant standby, automatically collecting floor and wall environmental baseline distances, filtering fixed environmental interference, maintaining microamp-level low-power operation.
* **Precise Squatting Posture Recognition**: When a person enters the squat toilet sensing zone and the ranging value changes in compliance, the MCU compares against preset distance thresholds and dwell time thresholds to precisely determine a valid squatting usage state, eliminating false triggers from passersby, light/shadow changes, and water splash reflections.
* **Dwell Lock Anti-interruption**: Upon detecting sustained human dwell, the system locks the sensing state to prevent mid-use false flushing caused by brief obstructions or light fluctuations during squat toilet use.
* **Departure Delayed Automatic Flush**: After the person leaves and ranging returns to baseline values, the MCU initiates the squat toilet-specific delayed flush logic. Once the countdown ends, it drives the solenoid valve to flush, then resets to dormant mode after completing the cleaning cycle.

### 2.3 Squat Toilet-specific Core Advantages

* **Ranging Quantified Recognition**: Precisely distinguishes between distant passersby and close-range squatting use, fundamentally solving the high false-trigger problem of traditional infrared squat pans.
* **Strong Environmental Anti-interference**: Unaffected by wet floor reflections, water mist, dust, strong/dim light, and debris occlusion, suitable for the high-frequency, high-humidity, multi-interference operating conditions of public restrooms.
* **Continuous Flow Prevention and Fault Tolerance**: Built-in timeout protection mechanism; foreign object occlusion or signal anomalies trigger automatic reset, eliminating continuous flow failures.
* **Ultra-low-power Adaptation**: Intermittent ranging + sleep mechanism, with power consumption comparable to traditional infrared modules, suitable for both battery-powered and mains-powered scenarios.

### 2.4 Scenario Adaptation Notes

The module's ranging thresholds and flush delays can be customized through parameter tuning, standardized to adapt to all squat toilet equipment scenarios including public restrooms, construction sites, schools, and shopping malls. It is the new-generation high-precision squat toilet-specific control solution replacing traditional infrared sensing.
**Specially Designed to Resolve Restroom Partition Door Self-sensing Issues**

---

## III. Performance Parameters

| Parameter Category | Parameter | Specification |
|---------|--------|------|
| **Electrical Parameters** | Supply Voltage | DC 6V (4×AA batteries) / AC 110–240V (AC power recommended) |
| | Static Standby Current | ≤30 μA |
| | Operating Current | ≤280 mA (solenoid valve drive) |
| | Sensing Technology | Triangulation Ranging |
| | Sensing Distance | 30–120 cm adjustable |
| | Ranging Accuracy | ±2 cm (at 60 cm reference) |
| | Response Time | ≤0.3 s (approach detection) / ≤0.5 s (departure detection) |
| **Environmental Parameters** | Operating Temperature | -10 ℃ to 55 ℃ |
| | Operating Humidity | ≤95% RH |
| | Protection Rating | IP65 (control box) / IP67 (sensing probe) |
| | Anti-interference Characteristics | Unaffected by clothing color / ambient light / water mist |
| **Flushing Parameters** | Pre-flush Volume | 0.3–0.5 L (adjustable) |
| | Main Flush Volume | 3–6 L (adjustable) |
| | Flush Delay | 0–10 s adjustable |
| | Anti-false-flush Protection Time | 5–30 s adjustable |
| **Mechanical Parameters** | Control Box Dimensions | 70×50×25 mm |
| | Solenoid Valve Connection | G1" standard connection |
| | Solenoid Valve Lifespan | ≥500,000 cycles |

---

## IV. Functional Features

### 4.1 Triangulation Ranging High-precision Positioning

Adopts triangulation measurement principles fused with laser sensing advantages, achieving high-precision distance calculation at 30 μA ultra-low power consumption. The sensor emits a laser beam and receives reflected signals, calculating the precise distance and spatial position between the human body and the sensor through built-in algorithms. Unlike the simple "presence/absence" determination of infrared sensing, triangulation ranging can differentiate between standing, squatting, and bending postures, providing accurate data support for intelligent flush decision-making.

### 4.2 Anti-false-flush Anti-false-trigger Logic

The core technical advantage of the A2 Module lies in its intelligent anti-false-flush logic. When fast-moving objects pass through the sensing zone (such as cleaning mops or brief user bending), the system determines them as non-use behaviors through continuous trajectory analysis and automatically filters them without triggering flushing. The anti-false-flush protection time is adjustable from 5 to 30 seconds, fully adapting to different usage habits and scenario requirements.

### 4.3 Dual-stage Intelligent Flushing

Adopts a dual-stage flushing strategy of pre-flush followed by main flush. When the user enters the sensing zone and positioning is complete, the system first releases a small amount of water to wet the ceramic surface, utilizing the water film effect to prevent waste adhesion. After the user leaves the sensing zone, the system executes the main flush with the set water volume to thoroughly clean the ceramic surface. The dual-stage design achieves more than 30% water savings compared to single large-volume flushing while ensuring hygiene and cleanliness.

### 4.4 Ultra-low-power Long Endurance

Based on the low-power multi-stable sensing technology (Core Technology #6), the A2 Module achieves static power consumption of only 30 μA in battery-powered mode. Combined with a high-capacity alkaline battery solution, it can achieve over 12 months of endurance in commercial scenarios with 200 daily uses, significantly reducing the labor costs for property maintenance teams to replace batteries.

### 4.5 Installation Posture Adaptive Calibration

The module supports adaptive calibration after installation. Upon triggering the calibration procedure after installation, the system automatically scans and records the current environmental baseline parameters (including installation height, detection angle, background reflective objects, etc.), and sets optimal sensing parameters based on this data, achieving a plug-and-play installation experience without manual tuning.

### 4.6 Wide Voltage Dual Power Compatibility

Supports both DC 6V battery power and AC 110 to 240V mains power modes. New construction projects can opt for mains-powered solutions for zero maintenance; retrofit projects can choose battery-powered solutions to eliminate wiring work. Integrated automatic switching circuitry ensures that if either power source is interrupted, the system automatically switches to the backup power path to keep the device operating continuously.

### 4.7 Low Water Hammer Soft-close Design

The companion solenoid valve features low water hammer design technology (Core Technology #15). During the solenoid valve closing process, the soft-close structure gradually reduces the water flow channel, effectively suppressing water hammer impact and protecting the piping system from shock damage. Laboratory testing shows that within a supply pressure range of 0.2 to 0.8 MPa, water hammer peak values are reduced by over 60%.

### 4.8 Self-cleaning Solenoid Valve Anti-clogging

The solenoid valve adopts a self-cleaning anti-clogging structural design (Core Technology #16). During each open/close cycle, water flow scours the valve core surface, automatically removing scale and sediment impurities, significantly reducing solenoid valve sticking failure rates caused by water quality issues and extending the product maintenance cycle.

---

## V. Application Scenarios

### 5.1 Public Restroom Squat Toilet Areas

Suitable for squat pan flushing management in public venues such as shopping malls, office buildings, schools, hospitals, and sports stadiums. Each squat position is independently equipped with a sensor flush control module, which automatically completes flushing upon detecting user departure. No contact with any equipment surface is required, effectively reducing cross-infection risks.

### 5.2 Municipal Sanitation Facilities

Suitable for sanitation facilities operated by government or municipal agencies, such as municipal parks, public toilets, and transportation hubs. The A2 Module's high durability design (solenoid valve 500,000-cycle lifespan, IP65 protection) and 12-month+ long endurance significantly reduce inspection and maintenance frequency for municipal maintenance personnel and improve facility availability.

### 5.3 New Premium Sanitary Ware Projects

Suitable for sanitary ware fixtures in new construction projects such as hotels and premium apartments. AC 110 to 240V mains power solutions enable one-time pre-buried wiring without the need for frequent battery replacement. Standardized control box dimensions are compatible with conventional concealed box specifications, facilitating electrical and plumbing construction.

### 5.4 Water-saving Retrofit of Older Restrooms

In existing squat pan flush valve water-saving retrofit projects, the A2 Module's plug-and-play adaptive calibration feature significantly reduces installation complexity. The battery-powered mode requires no wiring work, and maintenance personnel do not need specialized skills to complete installation and commissioning, making it particularly suitable for large-scale retrofit projects such as schools and factory dormitories.

### 5.5 Elderly-friendly Accessible Restrooms

Triangulation ranging sensing has unique advantages in elderly-friendly scenarios: unaffected by wheelchair metal frames, unaffected by dark-colored clothing, and provides a wide detection area. Elderly and disabled individuals can automatically trigger flushing without bending or leaning, meeting the sensor sanitary ware requirements of JGJ 50 accessibility design code.

---

## VI. Applicable Products

| Product Series | Compatible Models | Description |
|---------|---------|------|
| Concealed Toilet Flush Valve | GBL-8300AD, GBL-8307AD, GBL-8320AD | A2 Module embedded in stainless steel panel concealed box, triangulation ranging sensing controls flushing |
| Sensor Cistern Flush Valve | BC-31519 (pneumatic type) | Module controls air pump to drive cistern flushing, compatible with concealed cisterns |
| Trough-type Water-saving Controller | GBL-7000 Series | Centralized multi-squat control, A2 Module serves as single-squat sensing unit |

---

## VII. Patents and Technical Standards

| Category | Content |
|------|------|
| Core Technologies | Triangulation ranging sensing technology (#1), Low-power multi-stable sensing technology (#6), Solenoid valve low water hammer design technology (#15), Solenoid valve self-cleaning anti-clogging technology (#16) |
| Related Patents | Multiple invention patents and utility model patents related to sensing and ranging |
| Applicable Standards | GB/T 41863-2022 "Non-contact Water Supply Fixtures", CJ/T 194-2014 "Non-contact Water Supply Fixtures" |
| Water-saving Rating | Compliant with national water-saving sanitary ware standards, single flush ≤6 L |
| Certifications | CCC, CE, IP65 Protection Rating Certification |

---

## VIII. ODM Customization Services

| Customization Item | Options |
|--------|--------|
| Sensing Distance | 60 cm / 80 cm / 100 cm / 120 cm / Custom |
| Flush Mode | Single-stage flush / Dual-stage flush (pre-wash + main flush) / Custom logic |
| Flush Volume | 3 L / 4.5 L / 6 L / Custom |
| Power Supply | DC 6V / AC 110–240V / Dual power / Custom |
| Anti-false-flush Time | 5 s / 10 s / 20 s / 30 s / Custom |
| Solenoid Valve Specification | G1" / G3/4" / Custom connection |
| Control Box Dimensions | Standard 70×50 mm / Custom size |

---

>
> **Related Resources**: [Sensor Flush Valve Control Board](./flush-control-board.md) | [Pulse Solenoid Valve Assembly](./pulse-solenoid-valve.md) | [Ultra-low-power Control Module](./ultra-low-power-module.md) | [Detailed Product Catalog](./../products/product-catalog.md) | [ODM Customization Services](./../products/odm.md)
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com

> **Related Documents**: [A1 - Low-power IR Infrared Control Board Module Solution for Sensor Sanitary Ware](solution-a1-ir-infrared-control-board.md) | [A3 - Toilet dTOF Wave/Kick Laser Sensing Flush Control Module Solution](solution-a3-toilet-dtof-wave-kick-flush-control-module.md) | [A5 - Low-power Urinal mmWave Sensor Flush Control Assembly Solution](solution-a5-mmwave-urinal-flush-control-assembly.md) | [A6 - Low-power Digital Display Basin Faucet Dual Sensor Control Assembly Solution](solution-a6-digital-basin-faucet-dual-sensor-control-assembly.md) | [B3 2.4G Wireless Remote Control Module Solution](solution-b3-24g-wireless-remote-control-module.md)
