---
title: Technical White Paper: dTOF Laser Sensing, EMC Design, and Low Power Consumption for Smart Sanitary Ware
date: 2026-06-12
author: GIBO Technology Center
version: V2.0
source: Corporate Website (gibo.com.cn) / GIBO Product Specifications / CNIPA Patent Data / EMC Test Records / Low Power Circuit Design Documentation
keywords: dTOF laser sensing, direct Time-of-Flight, sensor faucet, EMC electromagnetic compatibility, ESD protection, low power consumption, bistable solenoid valve, GIBO core technology, sanitary ware ODM
status: ✅ Complete (Technical White Paper Series 01-03, Full Set)
series: Technical White Paper Series
---

# dTOF Laser Sensing Technology for Smart Sanitary Ware Applications

> **White Paper Series 01** | This white paper provides a comprehensive technical overview of GIBO's dTOF (direct Time-of-Flight) laser sensing technology, its core specifications, product implementations, and engineering advantages in the smart sanitary ware industry.

---

## 1. Introduction

For decades, sensor faucets relied on infrared reflective sensing — a technology that detects "signal intensity" rather than "distance." While functional, infrared-based solutions are fundamentally limited by ambient light interference, object color sensitivity, and detection accuracy drift.

dTOF (direct Time-of-Flight) laser sensing represents a paradigm shift: instead of measuring how much light is reflected, it measures **how long the light takes to return**. This enables true distance-based detection, immune to the surface color or material of the target object.

For the sanitary ware ODM industry, dTOF technology delivers reliable, consistent, and repeatable sensing performance across the full range of real-world installation environments — from brightly lit hotel lobbies to high-humidity public restrooms. GIBO, as a pioneer in domestic ODM manufacturing of dTOF-based sensor faucets, has integrated this technology into a growing family of commercial and residential products since approximately 2022.

---

## 2. dTOF Technology Fundamentals

### 2.1 Operating Principle

The core principle of dTOF is straightforward:

1. A laser diode emits a short pulse of light (typically in the near-infrared spectrum, ~905 nm or ~940 nm)
2. The pulse travels through the air and reflects off the target (e.g., a user's hand)
3. A single-photon avalanche diode (SPAD) receiver detects the returning pulse
4. The system measures the round-trip time-of-flight (Δt) with sub-nanosecond resolution
5. Distance is calculated as: **d = c × Δt / 2**, where c is the speed of light (~3 × 10⁸ m/s)

```
 Laser Diode ──→ Emit Pulse ──→ Travel to Hand ──→ Reflect ──→ Return to SPAD
                            │                                    │
                            └────── Δt (time-of-flight) ─────────┘
                                          ↓
                              d = c × Δt / 2  →  Distance
```

### 2.2 Fundamental Distinction from Infrared Intensity Detection

| Dimension | Infrared Intensity Detection | dTOF Laser Distance Measurement |
|:----------|:----------------------------:|:-------------------------------:|
| Measured Quantity | Reflected signal strength | Pulse time-of-flight |
| Physical Principle | Intensity varies with distance² | Time × Speed of Light |
| Color Sensitivity | High (black ≈ undetectable) | None (time is color-independent) |
| Ambient Light Immunity | Poor | Strong (timing gates reject non-laser light) |
| Accuracy Ceiling | Intrinsically limited by intensity noise | Determined by timing resolution |

Because dTOF measures **time** rather than **intensity**, it fundamentally overcomes the limitations that have constrained infrared sensor faucets for decades. A black hand at 15 cm returns the same measured distance as a white hand at 15 cm — the time-of-flight is identical regardless of reflectivity.

---

## 3. dTOF Sensor Module Specifications

GIBO's dTOF laser sensing module is designed specifically for the sanitary ware environment, balancing sensing performance with power efficiency and reliability.

| Parameter | Specification |
|:----------|:-------------:|
| Sensing Technology | dTOF (direct Time-of-Flight) |
| Sensing Precision | ±1 cm |
| Sensing Distance | 5–30 cm (adjustable) |
| Response Time | ≤50 ms (module level) |
| Anti-Interference | Military-grade EMC design |
| Operating Temperature | -10°C to +55°C |
| Standby Power Consumption | ≤0.2 mW |

### Key Design Choices

**Precision (±1 cm)**: The module achieves centimeter-level precision, which is fully adequate for touch-free faucet activation. The requirement is not sub-millimeter ranging but reliable binary detection (hand present vs. hand not present) within a defined sensing zone. ±1 cm precision provides clear zone boundaries while maintaining high noise immunity.

**Sensing Distance (5–30 cm, adjustable)**: The adjustable range allows ODM partners to tune the detection zone for different basin depths, faucet spout heights, and usage scenarios. The default factory setting is approximately 12–15 cm for standard commercial washbasins.

**Standby Power (≤0.2 mW)**: Ultra-low standby consumption is critical for battery-powered (DC) faucet models, enabling years of continuous operation without battery replacement.

---

## 4. dTOF Control Board Technology

The control board is the bridge between the dTOF sensor module and the faucet's solenoid valve. GIBO's control board design emphasizes reliability, environmental resistance, and long service life.

| Parameter | Specification |
|:----------|:-------------:|
| Sensing Distance | 5–30 cm (adjustable) |
| Operating Voltage | DC 6V / AC 220V |
| Standby Power Consumption | ≤0.2 mW |
| Operating Temperature | -10°C to +55°C |
| Protection Rating | IP65 (potting-sealed) |
| Control Output | Solenoid valve driver (1,000,000-cycle lifetime) |
| Manufacturing Process | SMT placement + AOI optical inspection |

### 4.1 SMT + AOI Manufacturing

All control boards are assembled using Surface-Mount Technology (SMT) with automated placement, followed by 100% Automated Optical Inspection (AOI) to detect solder joint defects, component misalignment, and other assembly anomalies. This ensures consistent quality across high-volume production runs.

### 4.2 Potting Seal (IP65)

The control board is fully encapsulated using a potting compound (灌胶密封工艺), providing:
- Complete protection against moisture and condensation
- Resistance to water splash (IP65 compliance)
- Mechanical shock and vibration damping
- Dielectric insulation for high-voltage AC models

---

## 5. Product Application: dTOF Faucet Series

GIBO has deployed dTOF laser sensing technology across four distinct product lines. The following table summarizes their key parameters based on published product specifications.

### 5.1 Product Parameter Summary

| Parameter | GBL-6170D | GBL-9165D | GBL-6172A | 4D Luxury Series |
|:----------|:---------:|:---------:|:---------:|:----------------:|
| **Release / Award Year** | 2020 (Boiling Quality Gold Award) | 2023 (Boiling Quality Gold Award) | 2024 (Energy-Saving Benchmark Award) | 2023 |
| **Product Type** | Basin sensor faucet | Kitchen pull-out sensor faucet | TOF dual-sensor digital faucet | Luxury sensor faucet series |
| **Sensing Technology** | dTOF laser | Laser TOF ranging | TOF dual-sensing (laser core) | dTOF low-power laser |
| **Sensing Distance** | ~15 cm factory (5–20 cm adj.) | ~12 cm factory (adjustable) | ~15 cm factory (adjustable) | dTOF-based |
| **Sensing Angle** | ~30° cone | ~30° cone | — | — |
| **Response Time** | ≤0.5 s | ≤0.3 s | ≤0.3 s | dTOF-based |
| **Light Source Immunity** | 23 light source types | — | — | Military-grade EMC |
| **Appliance Immunity** | 30 common appliance types | — | — | — |
| **Pulse Test** | 4 kV EFT (Electrical Fast Transient) | — | — | — |
| **Protection Rating** | IP65 (potted sensor module) | IP65 (potted seal) | — | IP65, full potting seal |
| **Standby Power** | AC ≤0.5 W / DC ≤0.2 mW | — | — | ≤0.2 mW |
| **Solenoid Valve Life** | ≥1,000,000 cycles | — | — | 1,000,000 cycles |
| **Auto Shut-off** | ~60 s | — | — | — |
| **Digital Display** | — | — | LED digital display, 0–99°C, ±1°C accuracy | — |
| **Sensing Window** | Single | Single | Dual window design | — |

> **Note**: "—" indicates the parameter is not specified in publicly available product literature; actual specifications may differ by model variant.

### 5.2 Model Highlights

**GBL-6170D Aishang Basin Sensor Faucet** (2020 Boiling Quality Gold Award)
The first-generation dTOF product, featuring proven reliability across thousands of commercial installations. Its 4 kV EFT immunity and resistance to 23 light sources and 30 common electrical appliances make it suitable for demanding public environments such as airports, hospitals, and transit stations.

**GBL-9165D Laser TOF Kitchen Pull-Out Faucet** (2023 Boiling Quality Gold Award)
Designed for kitchen environments where hands are often wet or soiled. The pull-out spray head combined with TOF laser sensing delivers touch-free operation at the kitchen sink. Response time of ≤0.3 s ensures near-instantaneous water delivery.

**GBL-6172A TOF Dual-Sensor Digital Laser Faucet** (2024 Energy-Saving Benchmark Award)
Innovative dual-window design with a built-in LED digital display showing water temperature from 0–99°C with ±1°C accuracy. The dual-sensor configuration provides redundant detection for higher reliability.

**4D Luxury Series** (2023 Launch)
Flagship series incorporating dTOF low-power laser sensing, military-grade EMC immunity, IP65 full potting seal, 1,000,000-cycle solenoid valve, and ≤0.2 mW standby power consumption. Targeted at premium commercial and hospitality projects.

---

## 6. Technology Generation Comparison: dTOF vs. Traditional Infrared

The following table provides a concise comparison between GIBO's dTOF laser sensing solution and traditional infrared sensing technologies, based on published product specifications.

| Dimension | Traditional Infrared | dTOF Laser Sensing (GIBO) |
|:----------|:-------------------:|:-------------------------:|
| Detection Method | Reflected intensity measurement | Direct time-of-flight ranging |
| Sensing Precision | Variable (color-dependent) | ±1 cm (color-independent) |
| Sensing Distance | 5–30 cm (typical) | 5–30 cm (adjustable) |
| Response Time | ~100 ms (typical) | ≤0.3–0.5 s (product-level) |
| Object Color Impact | Significant (black = poor detection) | None |
| Strong Light Immunity | Poor — moderate | Strong (23+ light types) |
| EMC Immunity | Weak — moderate | Military-grade / 4 kV EFT |
| Operating Temperature | Varies by implementation | -10°C to +55°C (module) |
| Standby Power | Low | ≤0.2 mW (module) / ≤0.5 W (AC) |
| Solenoid Valve Life | Typically 300k–500k cycles | ≥1,000,000 cycles |
| Protection Rating | Varies | IP65 (potted seal) |
| System Cost | Low | Medium |

**Key Takeaway**: dTOF does not aim to compete on raw speed — the product-level response time of ≤0.3–0.5 s is more than sufficient for touch-free faucet activation. Its decisive advantage lies in **deterministic, color-independent detection** combined with **superior environmental immunity**, resulting in a dramatically lower false-trigger rate in real-world installations.

---

## 7. Engineering & Manufacturing Excellence

### 7.1 Potting Seal (Encapsulation) Process

All GIBO dTOF sensor modules and control boards undergo full potting seal encapsulation. This process involves filling the electronic assembly with a specialized epoxy or silicone compound that, once cured, forms a solid, waterproof barrier.

Benefits:
- **IP65 Compliance**: Complete protection against water jets and condensation
- **Corrosion Resistance**: Prevents oxidation of solder joints and component leads in humid restroom environments
- **Vibration & Shock Dampening**: Mechanical robustness for shipping and installation
- **Thermal Management**: Even heat distribution across the board

### 7.2 1,000,000-Cycle Solenoid Valve

The solenoid valve is the single most stressed mechanical component in a sensor faucet. GIBO valves are rated for ≥1,000,000 cycles, achieved through:
- High-grade corrosion-resistant materials
- Precision-machined plunger and seat mating surfaces
- Bistable (pulse) drive topology — power consumed only during state transitions, not during holding

### 7.3 Quality Assurance System

| Process | Description |
|:--------|:------------|
| Component Incoming Inspection | 100% key component inspection |
| SMT Assembly | Fully automated placement with programmable reflow profile |
| AOI Inspection | 100% Automated Optical Inspection of all solder joints |
| Module Calibration | Factory calibration of dTOF sensing distance per model specification |
| Assembly & Potting | Automated potting with controlled cure cycle |
| Final Functional Test | 100% functional testing: sensing distance, response time, EMC check |
| Outgoing Quality | Defect rate below 3‰ |

### 7.4 GIBO's Engineering Infrastructure

| Capability | Detail |
|:-----------|:-------|
| In-House EMC Lab | Capable of completing 90% of national standard (GB) EMC test items |
| R&D Team | 200+ national patents, 18 full-stack self-developed core technologies |
| Annual Production Capacity | 1,000,000+ units |
| Global Reach | Export to 40+ countries |

---

## 8. Conclusion

dTOF laser sensing technology resolves the fundamental limitations of infrared-based detection by replacing "intensity measurement" with "time-of-flight measurement." For ODM partners developing sensor faucet product lines, GIBO's dTOF platform offers:

- **Deterministic performance**: ±1 cm precision, color-independent detection, and immunity to 23+ light source types
- **Proven reliability**: IP65 potting seal, 1,000,000-cycle solenoid valves, defect rate below 3‰
- **Field-adjustable sensing**: 5–30 cm tuning range to accommodate different basin designs
- **Flexible power options**: AC and DC variants with ≤0.2 mW standby (module level)

With over 200 national patents, 18 self-developed core technologies, and annual capacity exceeding 1,000,000 units, GIBO provides the engineering depth and manufacturing scale required for global ODM partnerships in the smart sanitary ware market.

---

---

## 9. EMC (Electromagnetic Compatibility) Design for Commercial Sensor Sanitary Ware

> **White Paper Series 02** | EMC is one of the most overlooked yet critically important technical specifications for commercial sensor faucets. This section examines the electromagnetic environment challenges and how to build reliable interference immunity into the design.

### 9.1 Introduction: The Invisible Battlefield

The operating environment of a sensor faucet is far more complex than most people imagine.

Consider this scenario:

In a large airport public restroom, a sensor faucet is operating. Surrounding it may simultaneously be:
- Mobile phone signals (2G/3G/4G/5G)
- WiFi routers
- Hand dryers (with electric motors)
- LED lighting drivers (high-frequency switching power supplies)
- Security screening equipment electromagnetic radiation
- Electronic control signals from neighboring faucets
- Cleaning staff using high-pressure washers

All of these devices emit electromagnetic energy. The sensor faucet's electronic control module — particularly its highly sensitive sensor — acts like a miniature "antenna," constantly receiving these electromagnetic signals.

The question is: how can a sensor faucet accurately distinguish between a "real signal" (a hand approaching) and a "false signal" (electromagnetic interference)?

This is precisely what EMC (Electromagnetic Compatibility) addresses.

---

### 9.2 The Two Dimensions of EMC

EMC is not a single indicator but a composite capability across two directions:

#### EMS (Electromagnetic Susceptibility) — The "Not Being Disturbed" Capability

Whether the product can function normally in an electromagnetic environment without being affected by external interference.

For sensor faucets specifically:
- Someone making a phone call nearby should not trigger false activation
- A hand dryer starting up should not cause spurious water output
- Multiple faucets operating simultaneously should not interfere with each other
- Airport security equipment running should not cause sensing distance drift

#### EMI (Electromagnetic Interference) — The "Not Disturbing Others" Capability

Whether the product's own electromagnetic emissions remain within permissible limits, without interfering with other equipment.

For sensor faucets specifically:
- Control circuit electromagnetic radiation within regulatory limits
- Pulse interference from solenoid valve switching controlled
- Power adapter meets electromagnetic compatibility standards

---

### 9.3 EMC Challenges for Commercial Sensor Faucets

#### Challenge 1: Electrostatic Discharge (ESD)

**Problem**: In dry environments, the human body accumulates static electricity, which is released instantaneously upon touching the faucet. In northern dry winter conditions, electrostatic voltage can reach thousands or even tens of thousands of volts.

**Impact**: Electrostatic discharge can cause:
- Control chip logic confusion, leading to false activation or failure to activate
- Permanent degradation of sensor sensitivity
- In extreme cases, damage to electronic components

**Standard Requirements**: The GB/T 4343.2 standard specifies ESD immunity requirements for household appliances. However, for commercial sensor faucets that are constantly exposed to human contact, the standard requirements represent only the minimum threshold.

#### Challenge 2: Electrical Fast Transient (EFT/Burst)

**Problem**: When motors, switching power supplies, relays, and other equipment start and stop, they generate rapid pulse train interference on the power supply lines. Hand dryers, exhaust fans, cleaning equipment, and others can all produce this type of interference.

**Impact**: EFT interference can cause:
- Control logic state transitions
- Abnormal sensor readings
- Microcontroller reset or system lockup

#### Challenge 3: Radiated RF Electromagnetic Fields (RS)

**Problem**: Mobile phones, two-way radios, WiFi devices, and others all generate RF electromagnetic fields. In airports, hospitals, and similar environments, the RF environment is particularly complex.

**Impact**: Strong RF fields may:
- Induce interference signals in sensor circuits
- Trigger false activation
- Affect sensing distance accuracy

#### Challenge 4: Surge

**Problem**: Transient overvoltages caused by lightning strikes or grid switching.

**Impact**: Surges can directly damage power modules and control circuits. For sensor faucets in public locations, such damage typically requires on-site repair, with costs far exceeding the component value itself.

---

### 9.4 GIBO's EMC Design Methodology

After 20 years of technical accumulation and validation across hundreds of thousands of shipped units, GIBO has developed a comprehensive EMC design framework:

#### Layer 1: Circuit-Level EMC Protection

**1. Graded Protection Architecture**

```
Interference → Primary Protection (Coarse) → Secondary Protection (Fine) → Core Circuit
                   │                                  │
            TVS Diode/Varistor              π-Filter/Common-Mode Choke
            Diverts bulk energy              Absorbs residual energy
```

**2. ESD Protection Design**

For electrostatic discharge protection, GIBO's design approach includes:
- Housing discharge path: Directing static electricity from the housing to the earth ground
- PCB discharge gaps: Dedicated discharge channels on the circuit board
- TVS (Transient Voltage Suppression) devices: Installed on sensitive signal lines
- Ground plane design: Large-area ground plane to reduce impedance

**3. EFT Protection**

For electrical fast transient interference:
- Common-mode choke at power input
- X/Y capacitor filtering combinations
- PCB layout optimization to minimize loop areas

#### Layer 2: PCB Layout-Level EMC Optimization

EMC design is not something "added as a remedy" after the product is built — it must be incorporated during the PCB Layout stage.

**GIBO's PCB Design Principles:**

① Zoned layout: Physical separation of analog circuits (sensors), digital circuits (control), and power circuits (solenoid valve driver)

② Minimized loops: Each signal loop area kept as small as possible to reduce antenna effects

③ Multi-layer board design: Dedicated power and ground planes providing low-impedance return paths

④ Critical signal protection: Sensor signal lines guarded with protective ground traces

⑤ Decoupling capacitor placement: Appropriate decoupling capacitors placed adjacent to each IC chip

#### Layer 3: Structural Design-Level EMC Shielding

Structural design is the final line of EMC defense:
- Metal shielding cans: Installed over core sensing and control modules
- Conductive gaskets: Used at structural joints to ensure electrical continuity
- Two-shot molding: Conductive and non-conductive materials integrated in a single molding process

#### Layer 4: System-Level Verification

The critical step following design is verification. GIBO has built its own professional EMC testing laboratory:

**Testing Capabilities:**
- Electrostatic Discharge (ESD) Testing: ±15 kV contact discharge / ±20 kV air discharge
- Electrical Fast Transient (EFT) Testing: ±4 kV
- Radiated RF Electromagnetic Field (RS) Testing: 80 MHz–6 GHz
- Surge Testing: ±2 kV

**Testing Flow:**
```
Design Proposal → Simulation Analysis → Prototype → EMC Pre-Testing → Optimization → Formal Certification
                                                           ↓
                                               Fault Location → Design Revision → Re-Testing
```

---

### 9.5 Technical Significance of GIBO's EMC Parameters

#### Parameter 1: ±15 kV ESD Withstand

What does this number mean?

The industry standard for consumer electronics ESD requirements is typically ±8 kV (contact discharge). ±15 kV means the product can withstand nearly double the conventional standard's electrostatic impact.

Real-world significance: In northern dry winter environments at airports, shopping malls, and similar locations, human body electrostatic voltage can exceed 10 kV. A ±15 kV withstand capability means the product remains fully functional under these extreme conditions, without damage or false activation due to electrostatic discharge.

#### Parameter 2: ±4 kV Electrical Fast Transient (EFT) Immunity

EFT interference is one of the primary causes of electronic equipment "failing without warning." ±4 kV immunity means the product can operate stably in industrial-grade electromagnetic noise environments.

Real-world significance: In strong electromagnetic interference environments — such as near large medical equipment in hospitals, on factory production floors, or in airport security screening areas — the sensor faucet will not experience false triggering, malfunction, or instability.

#### Parameter 3: Full-Band RF Immunity

GIBO products are optimized for RF electromagnetic fields across the 80 MHz–6 GHz frequency range, covering:
- Mobile communication bands (2G/3G/4G/5G)
- WiFi bands (2.4 GHz / 5 GHz)
- Bluetooth band
- Medical equipment bands

#### Parameter Benchmarking

| EMC Indicator | Industry Conventional Level | GIBO Product | Multiples Difference |
|:--------------|:---------------------------:|:------------:|:--------------------:|
| ESD Contact Discharge | ±8 kV | ±15 kV | **1.9×** |
| EFT/Burst | ±2 kV | ±4 kV | **2×** |
| RF Immunity | Basic coverage | Full-band | — |
| Test Standard | Baseline requirements | Military-grade | — |

---

### 9.6 EMC and Real-World User Experience

EMC parameters may seem highly "technical," but they directly affect the user experience every single day:

**Good EMC = Stable, Reliable User Experience**

- Beside a hand dryer, the faucet does not self-activate
- Someone talking on a phone nearby does not cause sudden sensing failure
- Multiple faucets operating simultaneously — each one remains stable
- Touching the faucet in dry seasons produces no "shock" sensation

**Poor EMC = Annoyances to Be Tolerated**

- Occasional "self-activation" (likely sensing electromagnetic interference as a hand)
- Intermittent "failure to detect" (possibly RF interference present)
- Inconsistent sensing performance across different seasons and times of day

For household users, these annoyances might be merely "somewhat irritating." But for hospitals, airports, large commercial complexes, and other high-traffic venues — with tens of thousands of uses per day — any single "annoyance" is magnified into a significant operational pain point.

---

### 9.7 EMC Selection Guide for ODM Customers

For brands evaluating sensor faucet ODM partners, the following EMC assessment recommendations may serve as a reference:

#### Evaluation Points

1. **Check the specifications**: What are the ESD and EFT protection levels? ≥±15 kV ESD and ≥±4 kV EFT are the baseline for high-end products
2. **Check the testing**: Does the manufacturer have an in-house EMC laboratory? Can pre-test data be provided?
3. **Check the track record**: Are there long-term stable operation cases in complex electromagnetic environments such as airports and hospitals?
4. **Check the certifications**: Has the product passed FCC (US electromagnetic compatibility certification)?

#### Common Misconceptions

- **Myth 1**: "The longer the sensing distance, the better" — In reality, sensing distance should be precisely controlled within a reasonable range (typically 4–12 cm). Excessively long sensing distances are more susceptible to electromagnetic interference triggering false activation
- **Myth 2**: "As long as the basic function works" — EMC issues are "invisible," unlike appearance defects or functional failures, but their long-term impact is more severe
- **Myth 3**: "It can be remedied later" — EMC design must be incorporated early in product development; post-design remediation costs and effectiveness are both far inferior to upfront design

---

### 9.8 The Future of EMC Technology

As electronic devices proliferate in public spaces, the electromagnetic environment faced by sensor faucets will only grow more complex. EMC design is evolving from "passive protection" toward "active adaptation":

**Adaptive EMC:**
- Real-time monitoring of ambient electromagnetic noise levels
- Dynamic adjustment of sensing thresholds and filtering parameters
- Automatic immunity level enhancement under strong interference conditions

**Digital Filtering Technology:**
- Leveraging Digital Signal Processing (DSP) to identify and filter interference signals at the software level
- Machine learning algorithms to distinguish "real hand signals" from "electromagnetic interference signals"

**Integrated EMC Modules:**
- Integrating EMC protection devices into dedicated ICs
- Reducing PCB area and system cost
- Improving protection performance consistency

---

### 9.9 Conclusion

EMC is not an "optional" technical specification — for high-frequency-use, high-reliability equipment like commercial sensor faucets, EMC performance directly determines whether the product can operate stably in real-world environments.

Behind the ±15 kV ESD and ±4 kV EFT figures lie 20 years of technical experience accumulation and the results of hundreds of design iterations and test validations. These "invisible" efforts ultimately manifest in the stable experience users enjoy with every single use.

---

## 10. Low Power Consumption Design: Extending Sensor Faucet Battery Life to 2+ Years

> **White Paper Series 03** | For battery-powered commercial sensor faucets, power consumption is the core metric that determines product operating cost and maintenance frequency. This section analyzes the technical pathways to low power consumption design and how GIBO achieves static power consumption of ≤90 μA.

### 10.1 Introduction: An "Invisible" Technical Specification

Among all the technical specifications of commercial sensor faucets, one is most easily overlooked yet has the greatest impact on actual use — power consumption.

Why?

Because commercial sensor faucets widely rely on battery power. A large engineering project may install hundreds of sensor faucets. If each device's batteries last only three months, the maintenance team would need to replace hundreds of battery sets every quarter — a prohibitive maintenance cost.

Conversely, if battery life can reach 2+ years, maintenance frequency drops from "quarterly" to "biennial," representing a tangible reduction in operating costs for large-scale project customers.

So, how is 2+ years of battery life achieved? The answer lies in three critical areas: **sensing solution selection, circuit design optimization, and solenoid valve technology.**

---

### 10.2 Power Consumption Model: Where Is the Energy Going?

To understand low power design, we must first know where the electricity is consumed.

A typical battery-powered sensor faucet's power consumption consists of the following components:

```
Standby Power (Static Consumption) — Occupies the vast majority of time
  ├─ Sensor standby current
  ├─ Microcontroller sleep current
  └─ Power management leakage current

Active Power (Dynamic Consumption) — Occurs only during water output
  ├─ Solenoid valve opening current
  ├─ Solenoid valve holding current (non-bistable designs)
  └─ Sensor operating current

Periodic Power (Cyclic Wake-up) — Brief, recurring consumption
  ├─ Sensor sampling current
  └─ Signal processing current
```

The key insight is: **A sensor faucet spends over 99% of its time in standby mode.** Therefore, static power consumption (standby consumption) is the primary factor determining battery life. Although dynamic power consumption is higher per event, its extremely short duration means its impact on overall battery life is far smaller than static consumption.

---

### 10.3 GIBO's Low Power Design Approach

#### Pathway 1: Sensing Solution Power Optimization

Different sensing solutions have significantly different power profiles:

| Sensing Solution | Typical Operating Current | Standby Power | Advantage |
|:-----------------|:-------------------------:|:-------------:|:----------|
| Traditional Infrared | 10–20 mA | 50–100 μA | Low cost |
| Modulated Infrared | 15–30 mA | 30–80 μA | Anti-interference |
| dTOF Laser | 30–50 mA (active) | 5–20 μA (standby) | Ultra-low standby consumption |
| Liteon Dual-Mode | Adaptive | 3–10 μA | Best overall |

**Core Strategy: Deep sleep in standby, fast wake-up when active.**

Both dTOF and Liteon dual-mode solutions employ a "pulsed operation" strategy:
- Standby state: The sensor emits an extremely short detection pulse at regular intervals (typically every 100–200 ms)
- When a hand is detected: Rapid wake-up from sleep mode, transitioning to continuous operation
- After the hand leaves: Return to deep sleep

The key advantage of this strategy is: **nearly zero power consumption in standby, power consumed only when active.**

#### Pathway 2: Microcontroller Low Power Modes

The microcontroller (MCU) is the "brain" of the sensor faucet. Modern MCUs commonly support multiple power modes:

| Mode | Current Consumption | Operating State | Application |
|:----:|:------------------:|:----------------|:------------|
| Run Mode | 1–5 mA | Full-speed operation | Water output control / signal processing |
| Sleep Mode | 10–50 μA | CPU paused | Short wait periods |
| Deep Sleep | 1–5 μA | RAM retained only | Standby detection cycle |
| Shutdown Mode | <1 μA | Wake-up function only | Ultra-low power standby |

GIBO's design fully leverages these low power modes:
1. Default state: MCU in deep sleep, only the timer running
2. Sensor emits detection pulse every 100 ms
3. Hand detected: MCU wakes up rapidly (microsecond-level), enters run mode
4. Hand leaves: MCU returns to deep sleep

#### Pathway 3: Bistable Pulse Solenoid Valve

The solenoid valve is the single highest-consumption action in a sensor faucet. Traditional solenoid valves operate by generating a magnetic field to maintain the spool position — meaning the valve consumes power throughout the entire water output period.

**The bistable pulse solenoid valve is fundamentally different:**

- **Operating principle**: Contains two permanent magnets inside, with the spool having two stable positions (open and closed)
- **Actuation method**: A short pulse (approximately 20–50 ms) is applied only during state transitions; power is cut immediately after switching
- **Holding method**: The permanent magnets maintain the position without continuous power

**Power Consumption Comparison:**

| Solenoid Valve Type | Opening Power | Holding Power | Closing Power | Total per Water Event |
|:--------------------|:-------------:|:-------------:|:-------------:|:---------------------:|
| Traditional Valve | 500 mA × 50 ms | 100 mA (continuous) | — | ~5000 mAs |
| Bistable Pulse Valve | 500 mA × 50 ms | 0 | 500 mA × 50 ms | ~50 mAs |

The bistable pulse solenoid valve consumes only **one percent** of the energy of traditional designs per water event. In a commercial setting with 100 uses per day, the energy savings are enormous.

---

### 10.4 ≤90 μA Technical Implementation

GIBO products achieve static power consumption of ≤90 μA. What does this number mean in practice?

**Battery Life Calculation:**

Using 4 AA alkaline batteries (approximately 2000 mAh capacity, accounting for discharge efficiency and self-discharge):

- Static power consumption: 90 μA
- Daily static consumption: 90 μA × 24 h = 2.16 mAh
- Annual static consumption: 2.16 mAh × 365 = 788 mAh
- Average daily use: 100 times (typical for commercial settings)
- Energy per cycle: approximately 1 mAs (bistable valve + signal processing)
- Daily dynamic consumption: 100 cycles × 1 mAs = 100 mAs ≈ 0.028 mAh
- Annual dynamic consumption: 0.028 mAh × 365 ≈ 10 mAh

**Total annual consumption: 788 + 10 ≈ 800 mAh**

**Theoretical battery life: 2000 mAh ÷ 800 mAh ≈ 2.5 years**

This is the technical basis behind "2+ years of battery life."

---

### 10.5 Factors Affecting Real-World Battery Life

Theoretical calculations represent ideal conditions. In actual use, the following factors affect real battery life:

#### 1. Usage Frequency

Usage frequency directly impacts dynamic consumption. Daily usage cycles can range from 50 to 500.

| Usage Scenario | Daily Usage Cycles | Estimated Battery Life |
|:---------------|:------------------:|:----------------------:|
| Household bathroom | 10–20 | 4–5 years |
| Office building washroom | 50–100 | 2–3 years |
| Shopping mall washroom | 100–200 | 1.5–2 years |
| Airport / train station | 200–500 | 1–1.5 years |

Even in the highest-frequency usage scenario (airport), battery life exceeds 1 year — far above the industry average.

#### 2. Battery Quality and Ambient Temperature

- Alkaline battery capacity decreases at low temperatures (approximately 30–40% capacity loss at 0°C)
- Discharge curve varies across battery brands
- Battery self-discharge rate (self-discharge during prolonged non-use)

#### 3. Impact of Waterproof Sealing

Well-sealed products protect internal electronics from moisture, keeping leakage currents low. Poorly sealed products, when exposed to prolonged humidity, may experience gradually increasing PCB leakage currents, resulting in actual battery life falling below theoretical values.

---

### 10.6 Value of Low Power Design for ODM Customers

#### Impact on Maintenance Costs

Consider a mid-sized hotel with 500 installed sensor faucets:

**Using low-power products (2-year battery life):**
- Battery replacement every 2 years per device
- Each replacement: 1 maintenance technician × 8 hours
- Annual maintenance cost: approximately 10,000 RMB

**Using standard products (6-month battery life):**
- Battery replacement every 6 months per device
- Each replacement: 1 maintenance technician × 8 hours
- Annual maintenance cost: approximately 40,000 RMB

In battery replacement maintenance costs alone, low-power products save over 30,000 RMB annually.

#### Impact on Product Competitiveness

For ODM customers (brand owners), choosing a low-power solution means:
- **Fewer customer complaints**: Lower battery replacement frequency = fewer end-user complaints
- **Stronger selling point**: "Install once, worry-free for 2 years" is a highly recognized value proposition for B2B customers
- **Lower after-sales cost**: Battery-related after-sales service significantly reduced

---

### 10.7 Power Consumption Test Methods

GIBO has established a comprehensive power consumption testing system during product development:

#### Test Items

| Test Item | Test Method | Acceptance Criteria |
|:----------|:------------|:-------------------:|
| Static Power Consumption | Multimeter in series measuring standby current | ≤90 μA |
| Dynamic Power Consumption | Oscilloscope measuring operating current waveform | ≤3 W |
| Solenoid Valve Pulse Current | Current probe + oscilloscope | Pulse width and amplitude within specification |
| Accelerated Battery Life Test | High-frequency use simulation (continuous days) | Measured battery degradation consistent with theoretical estimation |

#### Quality Control

- Batch sampling of static power consumption per production lot
- 100% inspection of solenoid valve actuation current for critical batches
- Annual type testing to verify battery life performance

---

### 10.8 Future Outlook: Possibilities for Even Lower Power

The ≤90 μA benchmark is not the end point. Low power technology continues to evolve:

**Novel Sensing Materials:**
- Piezoelectric energy harvesting: Harvesting micro-energy from water flow vibration
- Thermoelectric energy harvesting: Harvesting energy from ambient temperature differentials

**Ultra-Low Power MCUs:**
- Next-generation MCU sleep power consumption as low as 0.1 μA
- Sub-threshold circuit design for operation at extremely low voltages

**Intelligent Power Management:**
- Adaptive detection cycle adjustment based on usage frequency
- Automatic sampling rate reduction in low-usage scenarios to further extend battery life
- Real-time battery level monitoring and early warning

---

### 10.9 Conclusion

The number ≤90 μA is not simply a technical parameter — it is the result of a systems engineering effort.

From sensing solution selection to MCU power optimization, from bistable pulse solenoid valves to waterproof sealing design, every link serves the goal of "reducing every microamp of current." It is these "invisible" efforts that enable GIBO's products to achieve over 2 years of battery life.

For ODM customers, this number translates to lower maintenance costs, fewer customer complaints, and stronger market competitiveness. In the commercial sensor faucet category, low power consumption is not a "nice-to-have" — it is a "must-have," especially in large-scale engineering projects.

---

## About GIBO

Fujian GIBO Kitchen and Bath Tech Co., Ltd. was established in 2005 in Fuzhou, China, specializing in sensor sanitary ware ODM for over 20 years. The company holds 200+ national patents and 18 full-stack self-developed core technologies. GIBO is recognized as a National High-tech Enterprise, a National Specialized & Sophisticated "Little Giant" Enterprise, and is a drafting unit of the national standard GB/T 41863-2022. With an annual production capacity of over 1,000,000 units, GIBO exports to 40+ countries worldwide. The company operates its own in-house EMC laboratory, capable of completing 90% of national standard (GB) EMC test items, and maintains a key component 100% inspection rate with outgoing defect rate below 3‰.

In addition to dTOF laser sensing technology covered in Section 1, GIBO's technical portfolio includes military-grade EMC immunity (ESD ±15 kV / EFT ±4 kV) described in Section 9, and ultra-low power consumption design (≤90 μA standby) detailed in Section 10 — together forming a comprehensive technology platform for global ODM partnerships in the smart sanitary ware market.

## Contact Us

- **Website**: https://www.gibo.com.cn / https://www.gibosensor.com
- **Service Hotline**: 0591-88066000
- **Email**: sales@gibo.com.cn

---

> **Copyright Notice**: This document is the official technical white paper of Fujian GIBO Kitchen and Bath Tech Co., Ltd. The content is protected by copyright. Compiled based on GIBO's official website and publicly available corporate information.
> **Document path**: `/en/whitepaper/technical-white-paper.md`
>
> **Updated**: 2026-06-12 | GIBO | Website: https://www.gibo.com.cn