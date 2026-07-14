# KCM-组合面板-WDW Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Statement**: A primary-secondary coordinated dual-sensor squat-pan combined panel.
>

---

## I. Product Introduction

The **KCM-1312-WDW / KCM-8307-WDW Combined Panel** is a primary-secondary dual-sensor control panel that GIBO builds for squat pans, based on the 4-in-1 sensor module platform—the primary sensor module KCM-1312-WDW runs squat-pan mode, responsible for long-distance presence judgment and triggering flush; the secondary sensor module KCM-8307-WDW runs a "hand-sensing + manual button" mode, mounted at a handy position, where a wave or a press feeds the signal to the primary module to execute the flush. One module far, one near; one automatic, one manual—the squat pan flushes accurately when it should, and the user has an entry to trigger actively when wanted.

It solves two common awkwardnesses of public stalls: first, relying only on long-distance sensing, with tricky angles inside partitions and the body out of the sensing cone after squatting, leads to "should flush but doesn't"; second, pure automatic has no manual fallback for special scenarios. This combined panel merges automatic sensing and manual trigger—the primary module ships with a 75cm sensing distance covering stall entry/exit flow, and the secondary module at 15cm near-distance hand-sensing plus a physical button provides redundancy.

Technically it is the active-IR reflection plus ultra-low-power MCU approach, standby power ≤0.2mW, with power-loss keeps valve closed, under-voltage auto-close, and timeout auto-close all present. ESD level 4, EMI level 3, fast burst, seven light-source interference, immersion plus boiling-water tests all pass. For complete-unit makers and contractors, this panel is a turnkey squat-pan sensing solution that "flushes automatically and manually, and is rugged."

### 1.1 Technical Positioning

| Module Form | Sensing Method | Trigger Logic | Fitting Fixture | Representative Model |
|---------|---------|---------|---------|---------|
| Single-sensor squat panel | Single long-distance sensing | Automatic | Squat pan | Conventional squat sensor board |
| **Primary-Secondary Dual-Sensor Combined Panel** | **Far auto + near hand-sense/button** | **Auto + manual redundancy** | **Squat pan** | **This product (KCM-1312/8307-WDW)** |
| 4-in-1 universal module | Single-window four modes | Automatic | Faucet/urinal/squat/shower | 4-in-1 universal |

### 1.2 Key Metrics

- Primary module factory sensing distance 75cm±10%, adjustable 35~100cm; secondary module factory 15cm±10%, adjustable 5~40cm
- Primary module normal flush 5S±1S, water-saving mode flushes only 4S within 2 minutes; default normal mode
- Static power ≤0.2mW, response time ≤512mS, output pulse 30mS
- Power-loss keeps closed; voltage <4.8V flash 5 times reminder, <4.5V flash 10 times and auto-close valve
- Anti-interference: ESD level 4 (±15KV/±8KV), EMI level 3 (3V/m), fast burst level 4
- Waterproof: immersed 20cm/4H + 70°C boiling water 0.5h function normal

---

## II. Features

### 2.1 Primary-Secondary Dual Sensor, Both Auto and Manual Work

The primary module KCM-1312-WDW runs squat-pan mode, long-distance judging entry/exit and flushing; the secondary module KCM-8307-WDW runs hand-sensing + manual-button mode, with its output signal connected to the primary module's button port—each sense or press of the secondary module equals the primary module being pressed once. When automatic can't reach, a wave or a press supplements; the two logics are mutually redundant.

### 2.2 Primary Module Long-Distance Squat Sensing, 75cm at Factory

The primary module ships with sensing distance set to 75cm±10%, covering normal stall entry/exit flow, adjustable 35~100cm. False-judgment time 2S; after continuous sensing 2S then leaving, delay 2S flush 5S±1S; if leaving before the first flush segment ends, the second segment is not flushed—no wasted water.

### 2.3 Secondary Module Near-Distance Hand-Sensing Plus Physical Button

The secondary module ships with sensing distance 15cm±10%, adjustable 5~40cm, false-judgment 1S; after continuous sensing 1S it outputs a signal to the primary module to execute flush; there is also a physical button—each press likewise triggers the primary module flush, and holding it flushes only once without extra power. Gives cleaners and special-needs users a clear active-trigger entry.

### 2.4 Triple Power-Loss, Under-Voltage, and Timeout Protection

On power interruption the valve stays closed; below 4.8V each sensing flashes 5 times to remind of battery change, below 4.5V flashes 10 times and directly closes the valve to stop work; long continuous sensing is auto-closed by timeout logic to prevent false-trigger long flow.

### 2.5 Seven Light Sources No False Trigger

A 40W incandescent, T8-58W fluorescent, 50W halogen, ordinary/high-frequency electronic-ballast daylight, bathroom heater, and a 1000W hairdryer + daylight on the same outlet—at 15cm~91cm direct or oblique—produce no false action. EMI level 3, ESD level 4, burst level 4, stable even beside escalators and variable-frequency equipment.

### 2.6 Potted Waterproof, Also Boiling-Water Resistant

The sensing window and circuit module are triple-potted, connectors above IP65. Module alone tested: immersed 20cm for 4 hours with no droplets or fogging; also 70°C boiling water for 0.5h, normal after cooling—withstands the high humidity, steam, and cleaner hot-water rinsing of public toilets.

### 2.7 One-Click Remote Calibration, No Panel Opening

Primary and secondary module sensing distance, flush time, and water-saving switch are all done in front of the panel with the standard wireless remote—no panel opening, no control-box opening. At the limit the LED flashes 3 times as prompt; a veteran understands at a glance.

---

## III. Core Selling Points

### Selling Point 1: Primary-Secondary Dual Sensor—Stalls No Longer "Should Flush But Don't"

Single long-distance sensing in partitioned stalls often misses due to angles; this panel adds a secondary module hand-sensing plus button for redundancy—when automatic can't reach, a wave or press supplements. Most directly for property: fewer "stall not flushed clean" complaints, less awkwardness of people unwilling to touch for dirt, and smoother cleaner flow.

### Selling Point 2: 75cm Factory Long-Distance Sensing, Ready to Use Once Installed

The primary module ships preset at 75cm, covering stall entry/exit flow, no repeated on-site tuning. A public-toilet retrofit with dozens of stalls can be set once and run, commissioning man-hours minimized; the secondary module's 15cm near-distance hand-sensing is also generously provided—no compromise on experience.

### Selling Point 3: Interference-Immune, Waterproof, Reliable—Rugged in Public-Toilet Environment

ESD level 4, EMI level 3, fast burst, seven light-source interference all pass; sensing window immersed 4 hours plus boiled half an hour function normal. In the high-humidity, strong-light, cleaner-rinsing, dense-power-use environment of public toilets, this panel is less prone to failure or water ingress after install, lowering rework and warranty cost.

---

## IV. Specification & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power Supply | DC 6V (4 alkaline dry batteries) / AC 100V~240V to DC 6V 1A adapter |
| Operating Voltage Range | 4.5V - 6.5V (under-voltage action point see 4.5) |
| Static Power | ≤ 0.2mW |
| Output Pulse Width | 30mS |
| Response Time | ≤ 512mS |
| Sensing Technology | Active IR reflection (940nm) |

### 4.2 Primary Sensor Module (Squat-Pan Mode) Performance

| Parameter | Specification |
|--------|------|
| Factory Sensing Distance | 75cm ±10% (for 29.7×29.7cm standard white board) |
| Sensing Distance Adjustable | 35~100cm |
| Normal Flush | Continuous sensing 2S then leave, delay 2S flush 5S±1S |
| Water-Saving Mode | Within 2 min of sensing flushes only 4S; beyond 2 min same as normal (default normal mode) |
| False-Judgment Time | 2S |

### 4.3 Secondary Sensor Module (Hand-Sensing + Manual Button) Performance

| Parameter | Specification |
|--------|------|
| Factory Sensing Distance | 15cm ±10% (for 29.7×29.7cm standard white board) |
| Sensing Distance Adjustable | 5~40cm |
| Hand-Sensing Logic | False-judgment 1S, after continuous sensing 1S output signal to primary module to execute flush |
| Manual Button | Each press triggers primary module flush; holding flushes only once without extra power |
| Signal Access | Secondary module output connects to primary module button port |

### 4.4 Operating Environment

| Parameter | Specification |
|--------|------|
| Working Scenario | Kitchen/bath space |
| Operating Ambient Temperature | 5°C ~ 50°C |
| Relative Humidity | 10% RH ~ 95% RH |
| Working Water Pressure | 0.05MPa ~ 0.8MPa |
| Storage Temperature | -10°C ~ 55°C |
| Storage Humidity | ≤ 95% RH |

### 4.5 EMC & Protection

| Test Item | Test Standard/Condition | Result |
|---------|-------------|------|
| ESD | Level 4, air discharge ±15KV, contact ±8KV | Normal operation |
| EMI | Level 3, 80MHz~1000MHz, field strength 3V/m | Normal operation |
| Fast Transient Burst (EFT) | Level 4 | Normal operation |
| Light Interference | 6 light sources 15~91cm direct/oblique | No false trigger |
| Power-Loss Protection | Power interruption | Keeps closed state |
| Under-Voltage Protection | <4.8V flash 5 times (1.5S interval); <4.5V flash 10 times (0.5S interval) close valve | Solenoid closed, no work |
| Module Waterproof | Immersed 20cm/4H; 70°C boiling water 0.5h | No seepage, no fogging |

### 4.6 Applicable Standards

| Standard No. | Standard Name |
|---------|---------|
| CJ/T 194-2014 | Non-contact Water Supply Fixtures |
| GB/T 4798.1 | Environmental Conditions for Electric and Electronic Products — Part 1: Storage |
| GB/T 4798.2 | Environmental Conditions for Electric and Electronic Products — Part 2: Transportation |

---

## V. Installation Instructions

### 5.1 Before Installation (with complete unit)

1. First flush the pipeline with water to clear sand and rust, avoiding solenoid clogging.
2. Confirm water pressure 0.05MPa ~ 0.8MPa; below 0.05MPa add a booster pump.
3. Do not face the primary sensing window directly at sunlight or strong lights; no obstruction larger than 1cm within 120cm in front.
4. Install the secondary sensor module at a handy height, ensuring both the hand-sensing window and button are easy to operate.
5. Confirm primary/secondary module wiring (secondary output to primary button port) matches the complete unit.

### 5.2 Notes

- Always shut water and power before install/repair.
- Each AC-powered unit should have a separate power switch and reliable grounding.
- Use high-performance alkaline batteries; do not mix old and new.
- Do not hot-plug sensor module terminals.
- The module is a complete-unit component; the sensing window and potted part must not be disassembled by the user.

### 5.3 Assembly & Wiring Steps

1. Fix the primary and secondary modules in the panel's reserved positions; connect the solenoid drive wire, power, and secondary→primary button signal wire.
2. Connect the water in/out paths; open water and pressure-test to confirm no leak.
3. Install the decorative cover; primary sensing window faces out unobstructed, secondary module hand-sensing window and button exposed and handy.
4. On power-on the LED flashes once, the solenoid actuates instantly once (self-check), then enters standby.
5. With remote select squat-pan mode; primary module auto-calibrates 75cm sensing distance, secondary module calibrates near sensing distance.
6. Approach to test primary module auto-flush; wave/press button to test secondary module trigger.

### 5.4 Power-On Self-Check

On power-on the LED flashes once → solenoid instant actuation → enters 1-minute learning mode (LED steady, calibrates by standard white-board distance) → switches to normal standby. Do not keep blocking the sensing window during learning mode.

### 5.5 Battery Replacement & Tuning

Below 4.8V each sensing makes the LED flash 5 times as battery-change reminder; below 4.5V flashes 10 times and auto-closes the valve. Battery change: shut water → open panel → remove battery box, replace 4 same-brand new alkaline batteries → reinstall and re-self-check. Sensing distance, flush time, and water-saving switch are adjusted on-site by remote, no disassembly.

---

## VI. Applicable Complete Units & Integration Solutions

### 6.1 Companion Squat-Pan Complete Units

Built into exposed/concealed squat-pan flushers; primary module long-distance auto-flush, secondary module hand-sensing + button redundancy—fitting partitioned restrooms and public squat stalls. The 75cm factory sensing distance covers entry/exit flow.

### 6.2 Public-Toilet Retrofit and New Build

For old public-toilet retrofits with tricky partition angles, the primary-secondary dual sensor fills the missed-dead-zone of single sensing; for new public toilets batch-installed, one remote calibration runs through, low commissioning man-hours.

### 6.3 High-Frequency Public Places

Stalls in malls, stations, schools, and scenic areas see high foot traffic; the water-saving mode (flushes only 4S within 2 minutes) cuts water use, and the auto+manual dual entry lowers complaints.

### 6.4 Accessible and Aging-Friendly Scenarios

The secondary module's physical button gives mobility-limited users a clear active-flush entry, not dependent on automatic sensing angle—friendlier experience.

### 6.5 ODM Integration Value

Based on the 4-in-1 sensor module platform, the primary-secondary dual-sensor panel can share main-control hardware, flashing, and after-sales systems—simple stocking for complete-unit makers; factory long-distance preset + manual redundancy directly convert into the complete unit's "reliable flush" selling point, aiding bidding and public-building project onboarding.

---

## Appendix

### A. Core Technology Index

| Core Tech No. | Technology Name | Application in This Product | Related Patent (Granted) |
|------------|---------|--------------|----------------|
| #6 | Low-Power Multi-Stable Agile Sensing Technology | Standby ≤0.2mW, long battery life | A sensor water-output device and signal detection method ZL201910380558.X |
| #7 | Liteon Smart Sensing Technology | False-trigger prevention, environmental self-adaptation | A sensor and manual-control faucet ZL201520753357.7 |
| #11 | Dual-Mode Strong-Light-Immunity Anti-Interference Algorithm | Seven light sources no false trigger | A sensor water-output device and signal detection method ZL201910380558.X |
| #12 | Military-Grade EMC Technology | ESD/radiated/burst all pass | A sensor faucet water-output device ZL201910383793.2 |
| #13 | Intelligent Anti-Overflow Power-Off Safety Protection Technology | Power-loss keeps valve closed, timeout auto-close | A sensor water-output device and pull-out sensor water-output device ZL201910846836.6 |
| #10 | Dual-Chip Interchangeable Platform Technology | Primary/secondary modules unified main-control platform | An adjustable-detection-distance sensor module for kitchen/bath equipment ZL2025 2 1007523.9 |
| — | Toilet sensor flush module | Squat-pan primary sensor flush | A toilet sensor flush module with a lighting-effect component ZL2022 2 1337429.6 |
| — | Waterproof sensor module structure | Triple potting, immersion and boiling resistant | A waterproof sensor module for a water-output device ZL2020 2 2360603.6 |
| — | Bistable solenoid valve | Pulse-driven water switch | A bistable solenoid valve and sensor water-output device ZL2019 2 0857586.1 |

### B. Certifications & Qualifications

GIBO (GIBO) has been making sensor sanitary ware since 2004, and was among the earliest domestic manufacturers to apply MCU microcontrollers to sensor control. It is a drafting unit of two standards: GB/T 41863-2022 "General Technical Requirements for Water-Saving Performance of Non-contact Water Supply Fixtures" and T/XMBK 002-2024 "Sensor Faucets," and is a National High-Tech Enterprise, Fujian Provincial Intellectual-Property Advantage Enterprise, and National Specialized & Innovative SME. The kitchen pull-out faucet on the same dTOF laser platform won the 2023 Feiteng Quality Gold Award.

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

> This document is compiled based on the KCM-1312-WDW, KCM-8307-WDW Beijing Wang Dawei Combined Panel Specification (V1.0, 2024-05-28). Parameters are subject to the actual unit. GIBO reserves the final right of interpretation and modification of the technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
