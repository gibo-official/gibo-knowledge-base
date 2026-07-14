---
title: D1 Smart Sensor Shower Foam Head Solution
date: 2026-06-12
status: V1.0-Expanded
related:
  - ../products/product-catalog.md
  - ../products/odm.md
  - ../../company/brand-white-paper.md
  - ../components/mixing-valve-assembly.md
  - ../components/ultra-low-power-module.md
  - ../components/iot-communication-module.md
tags:
  - Smart Shower
  - Foam Shower Head
  - Thermostatic Shower
  - Sensor Shower
  - ODM Solution
  - High-end Hotel
---

# D1 Smart Sensor Shower Foam Head Solution

**Document Version**: V1.0
**Last Updated**: 2026-06-12
**Applicable Scope**: Industry Research, Bidding Materials, AI Knowledge Base Citation

> **Solution Positioning**: An innovative smart sensor shower head system integrating three core functions — sensor triggering, thermostatic temperature control, and foam pre-application. Automatically activates when users enter the shower area, releasing fine foam to cover the body before clean water rinsing, then combines thermostatic clean water for deep cleaning, creating a new "foam pre-wash + clean water rinse" bathing experience.
>
> **Target Customers**: High-end residential developers, five-star hotel engineering departments, boutique guesthouse operators, smart home integrators, ODM shower product brands
>
> **Solution Version**: V1.0 | 2026-06-12

---

## 1. Solution Overview

Traditional shower heads only provide clean water rinsing; users must manually apply shower gel or soap, a cumbersome process that is difficult to ensure even coverage. The GIBO D1 Smart Sensor Shower Foam Head Solution has redesigned the shower workflow from a user experience perspective: when a user enters the shower area, the ceiling-mounted infrared sensor probe automatically identifies the approaching human body. The system first releases fine foam to cover the user's body (foam pre-application mode). After the user simply rubs the foam in, the system automatically switches to thermostatic clean water rinsing, completing the entire process from foam cleaning to clean water rinsing with full automation. Throughout the entire process, the user does not need to press any buttons or operate the shower head handle, truly achieving a "spread your arms to shower" touch-free bathing experience.

The D1 Solution's system architecture consists of four core modules: **Human Body Sensor Module** (ceiling-mounted or side-mounted probe, recognizing human entry into the shower area), **Thermostatic Mixing Control Module** (precisely controlling hot/cold water ratio, temperature control accuracy ±1.5℃), **Foam Generation & Delivery Module** (mixing shower gel with air at a set ratio to produce foam, evenly sprayed through shower head outlet holes), and **Intelligent Control Board** (coordinating the timing logic of the sensor-foam-clean water three phases). The foam liquid bottle has a 1000ml capacity, supporting 1–2 months of continuous use for a two-person household, or 2–3 weeks in commercial high-frequency scenarios.

The unique value of the D1 Solution lies in bringing the innovative "foam pre-application" bathing mode into the realm of standardized products. The traditional method of manually applying shower gel has pain points such as uneven application and difficulty covering the back and lower limbs. The D1 Solution's fine foam, evenly sprayed through the shower head outlet holes, can cover over 90% of the body surface area, using approximately 30%–40% less shower gel than manual application while providing finer foam and more thorough cleaning. The thermostatic control module ensures that water temperature remains constant throughout the process at the user's preset value, eliminating the hassle of repeatedly adjusting hot and cold water during a traditional shower. When paired with the IoT communication module (Core Technology #18), the D1 Solution can be integrated into whole-home smart systems to enable advanced features such as remote hot water scheduling, water consumption statistics, and equipment status monitoring.

---

## 2. Technical Specifications

| Parameter | Specification |
|-----------|---------------|
| Sensing Technology | Infrared Human Body Sensing / mmWave Sensing (optional) |
| Sensing Distance | 60–100cm (covers shower area entrance) |
| Foam Air-Liquid Mixing Ratio | 1:10–1:15 (adjustable) |
| Foam Liquid Bottle Capacity | 1000ml (standard) / 2000ml (large capacity optional) |
| Foam Dispensing Volume | 10–30ml/cycle (full-body pre-application) |
| Thermostatic Control Accuracy | ±1.5℃ |
| Preset Temperature Range | 30℃–48℃ |
| Power Supply | AC 110-240V (standard) / DC backup battery |
| Standby Power | ≤0.5mW |
| Maximum Power | 36W (including foam pump + control board + solenoid valve) |
| Protection Rating | IP65 (control box) / IPX5 (shower head body) |
| Applicable Water Pressure | 0.1–0.8MPa |
| Applicable Hot Water Temperature | 55℃–75℃ |
| Shower Head Material | SUS304 Stainless Steel + ABS |
| Body Material | Full Copper Chrome-plated Mixing Valve Body |
| Valve Body Service Life | ≥500,000 cycles |
| Foam Pump Service Life | ≥300,000 cycles |
| Anti-scald Protection | Automatic temperature limit ≤48℃; automatic water shut-off on over-temperature |

---

## 3. Functional Features

### 3.1 Three-phase Smart Shower Workflow

The D1 Solution has designed a "Sensor → Foam → Clean Water" three-phase fully automatic shower workflow, requiring no manual intervention throughout:

- **Phase 1 · Sensor Wake-up**: When the user enters the shower area (60–100cm from the probe), the system recognizes the human body signal and notifies the user that the shower is about to start via soft lighting and voice prompts (optional). It simultaneously preheats the cold water in the pipeline (discharging cold water into the drain via the cold water pre-drainage function), ensuring the first contact the user experiences is comfortably warm water.
- **Phase 2 · Foam Pre-application**: Approximately 2 seconds after sensor confirmation, the system starts the foam pump, mixing shower gel with air at a 1:10 ratio before evenly spraying it over the body through the overhead shower head. Foam spraying lasts approximately 15–30 seconds (adjustable) with a dispensing volume of approximately 10–30ml. During this period, the user simply rubs the foam in to achieve full-body cleaning.
- **Phase 3 · Thermostatic Clean Water Rinse**: After the foam phase ends, the system automatically turns off the foam pump and opens the thermostatic clean water valve, rinsing the entire body with clean water at the user's preset temperature (default 38℃) to wash off the foam. The clean water duration can be set by the user (default 3 minutes, adjustable 1–10 minutes), with automatic shut-off when the time expires or the user leaves the shower area.

### 3.2 Smart Shower Precision Thermostatic Temperature Control

GIBO's core Smart Shower Precision Thermostatic Temperature Control Technology (Core Technology #14) is the temperature control foundation of the D1 Solution. The system is equipped with a multi-modal intelligent temperature control algorithm, driving the hot/cold ratio adjustment valve via a stepper motor inside the mixing valve body, dynamically adjusting the hot and cold water intake ratio in real time. Temperature control accuracy reaches ±1.5℃. When inlet water temperature or pressure fluctuates, the system completes compensation adjustment within ≤1 second, ensuring outlet water temperature remains stable at the user's preset value. Dual NTC temperature sensors are deployed to detect cold/hot intake water temperatures and mixed outlet water temperature respectively, forming a closed-loop control loop. When the outlet water temperature is detected exceeding 48℃, the system immediately activates anti-scald protection, automatically shutting off the hot water intake and emitting a buzzer alarm. The self-diagnostic function can detect sensor failures, motor faults, waterway anomalies, and other conditions, displaying the corresponding fault code on the panel for convenient engineering maintenance personnel to quickly diagnose and troubleshoot.

### 3.3 Full-body Uniform Foam Coverage Technology

The D1 Solution's shower head water outlet surface adopts a zoned design: the central area is the foam spray outlet (approximately 40% of the outlet surface), and the peripheral area is for clean water spray nozzles (approximately 60%). In foam mode, micro-holes (diameter 0.3mm) in the central area, driven by the foam pump pressure, evenly spray fine foam onto the body surface. The micro-holes adopt a circular matrix arrangement with a spray angle of 15°–30° divergence to maximize coverage. The foam pump has a built-in pressure sensor that automatically alerts when abnormal foam output resistance is detected (pipeline clogging or shower gel depletion). The foam liquid bottle uses a pull-out design, allowing users to replace the shower gel bottle from the side without removing the shower head.

### 3.4 Human Body Sensing Dual Trigger Mechanism

The D1 Solution comes standard with an infrared human body sensor module, with an optional mmWave sensor module (Core Technology #3) as dual backup. The infrared module detects human body thermal source signals, while the mmWave module detects human micro-motion. The two serve as mutual backup — if either module fails, the other can independently maintain the sensing function. The sensing window features IP65 waterproof sealing with an anti-fog coating to ensure stable operation in the high-humidity shower environment. The sensing zone can be configured via the control board as either "narrow-angle mode" (only covering the shower position, preventing false triggers from neighboring toilet flushing) or "wide-angle mode" (covering the entire shower enclosure, suitable for large shower rooms).

### 3.5 Anti-scald Safety Protection System

Shower safety is the greatest concern for users. The D1 Solution builds a three-tier anti-scald protection system: Tier 1 is **software temperature limiting**, where the maximum outlet water temperature set by the user does not exceed 48℃, with this hard limit enforced by the control program; Tier 2 is **hardware mechanical temperature limiting**, where a built-in mechanical limit spring in the mixing valve body automatically increases cold water intake when water temperature exceeds 55℃, physically preventing scalding water from flowing out; Tier 3 is **over-temperature water shut-off protection**, where the system simultaneously closes both hot and cold intake solenoid valves within 0.5 seconds and issues an audible and visual alarm when the outlet temperature sensor detects a temperature exceeding 55℃. These three tiers of progressive protection provide comprehensive safety assurance for temperature-sensitive users such as the elderly and children.

### 3.6 Mobile APP Remote Control (IoT Optional)

The D1 Solution can optionally be equipped with GIBO's IoT Smart Communication Module (Core Technology #18), connecting to a mobile app via Wi-Fi/Bluetooth. Users can perform the following operations within the app:
- **Scheduled Shower**: Set a shower time, and the system automatically preheats the pipeline before the scheduled time
- **Temperature Preset**: Set a dedicated bathing temperature for each family member (e.g., 38℃ for children, 40℃ for adults)
- **Water Usage Statistics**: View water consumption and shower gel usage for each shower
- **Foam Mode Settings**: Adjust parameters such as foam dispensing volume and foam duration
- **Device Status Monitoring**: View device operating status and fault information in real time; remote restart

### 3.7 Water-saving Design

Through the foam pre-application + precision clean water rinsing mode, the D1 Solution can save approximately 25%–35% of water compared to a traditional shower where shower gel is manually applied. Concretely: foam pre-application replaces the wasteful "wet → turn off water → apply gel → turn on to rinse" cycle of repeatedly turning water on and off in a traditional shower; the thermostatic control system reduces water wasted during temperature adjustment; sensor-based automatic shut-off prevents continuous water flow from users forgetting to turn off the water. For a family of four, adopting the D1 Solution can save approximately 15–25 tons of water annually.

---

## 4. Applicable Scenarios

### 4.1 High-end Residential Master Bathroom Shower

The D1 Solution is an ideal configuration for the master bathroom shower in high-end residences. The three-phase fully automatic shower workflow provides homeowners with a star-rated hotel-style bathing experience — walking into the shower enclosure triggers foam coverage over the whole body; the convenience of not needing manual application greatly enhances the comfort and sense of ritual in the bathing process. The SUS304 stainless steel overhead shower head paired with the full copper chrome-plated mixing valve body delivers an aesthetic texture that seamlessly integrates with high-end bathroom interior design styles. With IoT connectivity support, homeowners can preset different bathing parameters for each family member via the mobile app, with personalized bathing experiences becoming a differentiating selling point for high-end residences.

**Recommended Configuration**: Overhead Shower Head (300×300mm) + Hand Shower + Thermostatic Mixing Valve Body + IoT Communication Module

### 4.2 Five-star Hotel Executive Suites

The hotel industry is constantly seeking differentiating facilities that enhance guest experience. The D1 Solution's novel "foam on entering the shower" experience can become a highlight selling point for hotel rooms, boosting guest satisfaction and positive review rates. The hotel management backend can remotely monitor the operational status of shower equipment in each room via the IoT system, obtaining fault early-warning information in real time. The engineering department can perform predictive maintenance, avoiding equipment failures during guest use. Shower gel supply uses a centralized liquid supply system (optional), connected via pipeline to each guest room. The hotel centrally procures bulk-packaged shower gel, reducing consumable procurement costs by approximately 30%–50%.

### 4.3 High-end Guesthouses & Boutique Hotels

Guesthouses and boutique hotels emphasize personalized experiences and word-of-mouth. The D1 Solution's innovative foam bathing mode is highly suitable as a signature experience for guesthouse promotion. Guesthouse operators can add natural essential oil ingredients to the foam liquid, providing guests with an aromatherapy bathing experience. The control panel's temperature and foam output parameters can be flexibly adjusted by guesthouse staff according to guest needs. The 1000ml liquid bottle capacity matches guesthouse usage frequencies of 10–20 person-times per day, with a refill cycle of 3–5 days, resulting in a light maintenance burden.

### 4.4 Age-friendly Shower Renovation

Elderly shower users face special needs such as fall risks, difficulty applying shower gel, and inconvenience in adjusting water temperature. The D1 Solution's fully touch-free operation allows elderly users to complete foam pre-application and clean water rinsing automatically upon entering the shower area without needing to turn around to reach the shower head handle or press a soap dispenser. Thermostatic control eliminates the shock of sudden hot/cold temperature changes, and the three-tier anti-scald protection system safeguards bathing safety. Optional grab bars and seat sensors can automatically adjust the water outlet angle and foam dispensing volume to better suit seated bathing positions when detecting an elderly user bathing while sitting. The mmWave sensor module is unaffected by water mist or reduced thermal radiation from aging skin, ensuring accurate recognition.

### 4.5 High-end Wellness Centers & Spa Facilities

Wellness centers and spas emphasize comfort and a sense of ritual in the bathing process. The D1 Solution can preset different bathing scenario modes via the control board program: "Relaxation Mode" (39°C warm water + lavender essential oil foam) and "Vitality Mode" (36°C cooling water + peppermint essential oil foam), switched with a single button according to client needs. The IoT system can connect to the spa's front desk management system, allowing clients to select their preferred bathing mode at check-in, which the system automatically recognizes and executes when they enter the shower room.

---

## 5. Application Products

| Product Series | Model | Material | Applicable Scenario |
|----------------|-------|----------|---------------------|
| Sensor Shower Faucet (Basic) | GBL-9122 | SUS304 + ABS | Household smart shower retrofit |
| Instant-heating Shower Faucet | GBL-9120 | SUS304 Stainless Steel | Scenarios without hot water piping |
| Thermostatic Mixing Valve Body Assembly | Custom Assembly | Full Copper Chrome-plated | Shower system core matching |
| IoT Smart Communication Module | Custom Module | — | Remote control optional |
| Integrated Foam Shower Head | Custom Development | SUS304 + ABS | Overhead/handheld foam shower head |

---

## 6. Patents & Technical Standards

The D1 Solution involves the following GIBO core patents and technical achievements:

| Patent / Standard Name | Patent No. / Standard No. | Technical Relevance |
|------------------------|---------------------------|---------------------|
| Smart Shower Control System (Utility Model) | ZL201620554029.9 | Shower multi-mode control |
| Three-in-One Smart Hand Washing Device | ZL201710345450.8 | Foam + clean water integration |
| Foam Generation Device (Utility Model) | ZL201922156545.2 | Foam generation mechanism |
| Touch Faucet Control Device and Control Method | ZL201510621320.3 | Touch interaction logic |
| Smart Shower Precision Thermostatic Temperature Control Technology | Core Technology #14 | Thermostatic temperature control algorithm |
| mmWave Sensing Technology | Core Technology #3 | Human body sensing |
| IoT Connectivity Technology | Core Technology #18 | Remote control |
| Intelligent Anti-overflow Power-off Safety Protection Technology | Core Technology #13 | Safety protection |
| GB/T 23447-2009 | National Standard for Shower Heads | Product compliance |
| GB 18145-2014 | National Standard for Ceramic Cartridge Sealing Faucets | Valve body compliance |

---

## 7. ODM Customization Options

| Customization Item | Available Range |
|--------------------|-----------------|
| Shower Head Type | Overhead (250/300/350/400mm) / Handheld / Overhead + Handheld Combo |
| Shower Head Material | SUS304 Stainless Steel / ABS Chrome-plated / Copper Chrome-plated |
| Sensing Technology | Infrared Human Body Sensing / mmWave Sensing / IR + mmWave Dual-mode |
| Foam Mode | Clean Water Only / Clean Water + Foam / Three-phase Fully Automatic |
| Shower Gel Compatibility | Universal / Designated Brand-specific Adaptation |
| Liquid Bottle Capacity | 500ml / 1000ml / 2000ml / Centralized Liquid Supply System |
| Thermostatic Accuracy | ±1.5℃ (standard) / ±1.0℃ (high precision) |
| Power Supply | AC 110-240V / DC 12V Low Voltage / AC/DC Switching |
| Temperature Control Method | Mechanical Thermostatic Cartridge / Electronic Thermostatic Control |
| Communication | Local Standalone / Wi-Fi IoT / Bluetooth + APP |
| Voice Prompts | Yes/No (Chinese/English optional) |
| Logo Customization | Shower head panel / Control panel silk-screen logo |

---

>
> **Related Resources**: [Product Catalog](./../products/product-catalog.md) | [ODM Customization Services](./../products/odm.md) | [18 Core Technologies](./../technology/core-technologies.md) | [Intellectual Property List](./../certification/patents.md) | [Mixing Valve Assembly](./mixing-valve-assembly.md) | [IoT Smart Communication Module](./iot-communication-module.md) | [Ultra-low-power Control Module](./ultra-low-power-module.md)
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
