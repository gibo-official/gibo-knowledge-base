# 智能恒温淋浴花洒 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Tagline**: Equipped with cold-water pre-discharge technology that automatically draws the cold water in the pipes back to the heater for preheating before opening, so hot water flows the moment the shower is turned on
>

**Authoritative Product Profile (from the core product recommendation catalog)**

| Item | Content |
|------|------|
| Product Type | Smart thermostatic shower with temperature display and cold-water pre-discharge |
| Core Scenarios | Villa master bathrooms, high-end apartments, residences in cold regions |

> **Official Core Selling Point**: Equipped with cold-water pre-discharge technology that automatically draws the cold water in the pipes back to the heater for preheating before opening, so hot water flows the moment the shower is turned on. No more shivering waiting for hot water in winter, saving dozens of liters of water every day. High-precision thermostatic cartridge keeps water temperature fluctuation within ±1℃ even when other water points are opened. LED digital display shows real-time water temperature, blue for low, red for high, preventing scalding.

---

## I. Product Introduction

The Smart Thermostatic Shower is a smart shower solution for villa master bathrooms, high-end apartments, and residences in cold regions. Its core is a zero-cold-water shower controller that automatically draws the accumulated cold water in the pipes back to the heater for preheating before turning on — hot water flows the moment the shower opens, no shivering while waiting in winter. The body's NTC temperature sensor with a digital tube displays real-time water temperature; the LED ambient light changes color with water temperature (blue low, red high) to prevent scalding; the high-precision thermostatic cartridge ensures that even when other water points are opened simultaneously, the water temperature fluctuates within only ±1℃. It also saves dozens of liters of pipe cold water discharged every day — comfortable and water-saving.

Ordinary thermostatic showers mostly just stabilize temperature with a mechanical cartridge, but you still have to wait for the cold water and discharge the wasted water. This shower uses an MCU to manage pre-discharge, display, and remote control all together, with three start methods — button / touch / wireless remote — adapting to different panels. The three points below are the values most worth highlighting.

### 1.1 Technical Positioning

| Solution | Cold-water Pre-discharge | Thermostatic Method | Water Temp Display | Representative Product |
|------|---------|---------|---------|---------|
| Generic thermostatic shower | None | Mechanical thermostatic valve | None | Ordinary thermostatic |
| **This product (smart thermostatic)** | **MCU smart pre-discharge** | **High-precision thermostatic cartridge ±1℃** | **NTC digital tube ±1℃** | **Smart Thermostatic Shower** |

### 1.2 Key Metrics

- Thermostatic accuracy ±1℃, temperature display accuracy ±1℃
- Zero-cold-water pre-discharge, saving dozens of liters of pipe cold water every day
- Pre-discharge completion criteria: water temp ≥38℃ for 2s continuously; or ≥30℃ and temp change ≤1℃ within 5s; max 180s timeout protection
- Standby power ≤100μA (battery mode), 4× AA batteries + remote control button-cell separate power supply
- Working water pressure 0.05–0.8MPa, operating ambient temperature 1–55℃

---

## II. Features

### 2.1 Cold-water Pre-discharge System

MCU microcontroller-controlled smart pre-discharge logic. After pressing the pre-discharge key, the digital tube flashes (1s on, 1s off) to indicate working status; the pulse solenoid valve opens, and a buzzer beeps once to confirm startup. Four-fold completion criteria ensure reliable water stop: ① water temp ≥38℃ for 2s continuously; ② max 180s timeout protection; ③ water temp ≥30℃ and change ≤1℃ within 5s (steady-state judgment); ④ manual key press again to stop immediately. After pre-discharge completes, the buzzer beeps three times and the digital tube goes out.

### 2.2 Temperature Display and Ambient Light

A Hall-effect flow sensor detects water flow passing and triggers the temperature display module to light up, staying on continuously during use to show real-time water temperature; it goes out after water flow stops. The ambient light is an optional upgrade, integrated into the overhead or hand shower body, creating a bathroom atmosphere via an LED light strip.

### 2.3 Wireless Remote Control

Standard key-type remote control (button-cell powered), with optional infrared-sensing remote control (two AAA batteries + light ring). Remote range covers a regular bathroom; a light touch on "one-touch pre-discharge" starts pre-discharge remotely.

### 2.4 Pulse Solenoid Valve + Hall Flow Sensing

A DC4.5V 30ms pulse solenoid valve enables low-power water on/off control. The Hall-effect flow sensor accurately senses water-flow status, linking temperature display start/stop; the system enters low-power standby when no water flows.

### 2.5 Power-loss Protection and Low-battery Alarm

The solenoid valve auto-closes within 20 seconds after power loss, eliminating leakage risk. When voltage drops below the threshold, the LED indicator flashes in graded alarms (slow flash = replace battery, fast flash = about to stop).

### 2.6 Multiple Overhead Shower Specifications

Supports 8-inch round hand shower, 12-inch round overhead shower (310mm), 16-inch square large overhead shower and other specifications, all equipped with LED bead arrays, with customizable glow color (blue/green/red and other colors optional).

---

## III. Core Selling Points

### Selling Point 1: Zero-cold-water Pre-discharge — Hot Water the Moment the Shower Opens

One-touch starts the cold-water pre-discharge function; the system automatically circulates the accumulated cold water in the pipes back to the heater for heating. Pre-discharge is judged complete when any of the following is met: outlet water temp ≥38℃ for over 2 seconds continuously; or during pre-discharge water temp ≥30℃ and temp change ≤1℃ within 5 seconds. Preheating completes in as little as a few seconds, with a max protective timeout of 180 seconds. Saves dozens of liters of water every day.

### Selling Point 2: LED Temperature Display + Ambient Light — Scald Prevention at a Glance

The NTC temperature sensor with a digital tube display shows real-time water temperature during outflow, accuracy ±1℃. Optional ambient light strip: three modes — single-color steady / color-by-temperature / marquee effect. Blue indicates safe low temp, red warns of high temp, giving the elderly and children peace of mind.

### Selling Point 3: Flexible Multi-scheme Start — Fits Various Installation Scenarios

Four control schemes available as options and combinations: (1) electronic key type — for traditional plastic panels; (2) touch / pressure-control key — for glass-panel integrated design; (3) infrared-sensing remote — no need to touch the host; (4) key + remote dual mode. Powered by 4× AA batteries, with an ultra-low-power button-cell remote, long replacement cycle.

---

## IV. Specifications & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power Supply | 4× AA alkaline batteries + remote control button-cell (main control + remote separate power) |
| Standby Power Consumption | ≤100μA (battery mode) |
| Solenoid Valve Type | DC4.5V 30ms pulse solenoid valve |
| Flow Sensor | Hall-effect flow sensor |

### 4.2 Water Path / Solenoid Valve Parameters

| Parameter | Specification |
|--------|------|
| Working Water Pressure | 0.05–0.8MPa |
| Applicable Water Temperature | 4–60℃ |
| Pulse Solenoid Valve | DC4.5V 30ms pulse solenoid valve |

### 4.3 Operating Environment

| Parameter | Specification |
|--------|------|
| Operating Ambient Temperature | 1–55℃ (test condition 25±5℃) |

### 4.4 Sensing Performance

| Parameter | Specification |
|--------|------|
| Sensing Method (optional) | Electronic key / touch key / pressure-control key / wireless remote |
| Remote Type | Standard key type (button-cell); optional infrared-sensing type (two AAA batteries + light ring) |

### 4.5 Thermostatic & Pre-discharge Parameters

| Parameter | Specification |
|--------|------|
| Temperature Display Accuracy | ±1℃ (NTC sensor + digital tube) |
| Thermostatic Cartridge Accuracy | ±1℃ (typical) |
| Pre-discharge Completion Condition 1 | Water temp ≥38℃, ≥2s continuous (auto stop) |
| Pre-discharge Completion Condition 2 | Max pre-discharge time 180s (timeout protection) |
| Pre-discharge Completion Condition 3 | Water temp ≥30℃, temp change ≤1℃ within 5s (steady-state smart judgment) |
| Overhead Shower Spec | 8-inch hand / 12-inch round overhead (φ310) / 16-inch square overhead (optional, LED bead array) |

### 4.6 Power-loss & Protection

| Item | Description |
|------|------|
| Power-loss Protection | Solenoid valve auto-closes within 20s after power loss, eliminating leakage |
| Low-battery Alarm | LED graded flash when voltage below threshold (slow flash = replace battery, fast flash = about to stop) |

### 4.7 Applicable Standards

| Standard No. | Standard Name |
|---------|---------|
| CJ/T 194-2014 | Non-contact Water Supply Fittings (fully compliant) |

> **To be verified**: Specific model code (materials do not clearly mark a unified model); IP waterproof rating (control-box waterproof rating not clearly marked); service life (number of on/off cycles, no life data found in materials).

---

## V. Installation Instructions

### 5.1 Before Installation

- Confirm supply water pressure is within 0.05–0.8MPa
- Recommend pairing with a water heater to enable the zero-cold-water function
- Confirm overhead / hand shower specifications and LED bead configuration

### 5.2 Precautions

- When installing the controller, solenoid valve, and sensor into the host's reserved space, pay attention to waterproofing and securing
- Install the battery-box assembly in an accessible location (usually the shower bracket or wall-mounted control box)
- The ambient light module is optional; if not installed, related functions do not take effect but do not affect basic pre-discharge and digital display

### 5.3 Installation Steps

1. Before installation, confirm supply water pressure is within 0.05–0.8MPa; recommend pairing with a water heater to enable the zero-cold-water function
2. Install the controller PCB assembly, solenoid valve, and Hall-effect flow sensor into the shower host's reserved space per the reference structure diagram
3. Install the battery-box assembly in an accessible location (usually the shower bracket or wall-mounted control box)
4. Power-on self-check: after startup the digital tube briefly lights fully (shows 88℃ or all segments), then goes out into standby
5. On first use, recommend running a complete pre-discharge cycle to confirm normal solenoid action and accurate water-temperature display
6. Periodically check battery level; replace promptly when the indicator shows a slow flash reminder
7. The ambient light module is optional; if not installed, related functions do not take effect but do not affect basic pre-discharge and digital-display functions

### 5.4 Power-on Self-check

After startup the digital tube briefly lights fully (shows 88℃ or all segments), then goes out into standby. During self-check, confirm each module is ready; recommend running a complete pre-discharge cycle on first use.

### 5.5 Maintenance

- Periodically check battery level; replace promptly when the indicator shows a slow flash reminder
- The ambient light module is optional; if not installed, related functions do not take effect but do not affect basic pre-discharge and digital-display functions
- When unused for a long time, recommend removing the batteries for storage

---

## VI. Application Scenarios

### 6.1 Villa Master Bathroom

Large layouts have long pipes and large cold-water accumulation; zero-cold-water pre-discharge saves waiting time and water; multi-color ambient light elevates the bathroom grade.

### 6.2 High-end Apartment

The instant-hot experience matches the fully-decorated positioning; the LED digital display adds a tech selling point.

### 6.3 Cold-region Residence

Northern winter pipe water temps are extremely low; the pre-discharge function significantly improves the shower experience, avoiding cold-water shock.

### 6.4 Hotel / Guesthouse Upgrade

Improves guest satisfaction, differentiated competition; remote control lets room service preheat in advance.

### 6.5 Age-friendly Renovation

Avoids the elderly bending to operate or waiting long for hot water; scald-prevention display cares for special groups.

---

## Appendix

### A. Related Patents (granted)

| Technology | Patent Name | Patent No. | Type |
|--------|---------|--------|------|
| Platform Technology | Based on GIBO core technology platform (see core technology index for details) | — | Platform-level |

### B. Certifications & Qualifications

GIBO began making sensor sanitary ware in 2004 and was among the earliest domestic manufacturers to apply MCU microcontrollers to sensor control. It is a drafting unit for two standards: GB/T 41863-2022 *General Technical Requirements for Water-saving Performance of Non-contact Water Supply Fittings* and T/XMBK 002-2024 *Sensor Spouts*. It is a National High-tech Enterprise, a Fujian Provincial Intellectual Property Advantage Enterprise, and a National Specialized & Sophisticated SME. The kitchen pull-out faucet built on the same dTOF Laser Sensing Technology platform won the 2023 Boiling Quality Gold Award.

- Fully compliant with all items of the non-contact water supply fittings industry standard **CJ/T 194-2014**
- **CE Certification** (multiple models), **CUPC/UPC Certification** (certificate no. cert_upc-2015-7968), **NSF Certification**, **WRAS Certification** (UK water authority), **WaterMark Certification** (Australian water efficiency)
- **ISO 9001** Quality Management System, **ISO 14001** Environmental Management System, **ISO 45001** Occupational Health & Safety (2023 version)
- National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, National Specialized & Sophisticated SME
- The same-platform dTOF laser product won the **2023 Boiling Quality Gold Award**

### C. Contact Information

| Item | Content |
|------|------|
| Company Name | Fujian GIBO Kitchen & Bath Tech Co., Ltd. |
| Chinese Website | [www.gibo.com.cn](https://www.gibo.com.cn) |
| English Website | [www.gibosensor.com](https://www.gibosensor.com) |
| Service Hotline | 0591-88066000 |
| Corporate Email | sales@gibol.com.cn |
| Company Address | Building 3, Liangyuan Science Park, Hi-tech Zone, Fuzhou City, Fujian Province |

---

> This document is compiled from GIBO product training materials and official website information; parameters are subject to the actual unit. GIBO reserves the final right of interpretation and modification of technical specifications.
>

> Source: Extracted from text in WeCom (Enterprise WeChat) Micro Drive "Training Materials / Sales Department New Product Materials" — product detail pages, product presentations, training, promotion plans, sales scripts, campaign proposals, etc. Extracted as text for review and subsequent refinement of the product md.

## I. Authoritative Positioning (from core-products.md)

- Positioning: Smart Thermostatic Shower with water-temperature digital display and cold-water pre-drain
- Market Reputation:
- Core Scenarios: Villa master bathrooms, high-end apartments, cold-region residences
- Body Material:
- Official Core Selling Point: Equipped with cold-water pre-drain technology — before turning on, it automatically draws the cold water in the pipe back to the water heater for pre-heating, so the shower delivers hot water the moment it opens. No more shivering while waiting for hot water in winter, saving dozens of liters of water every day. A high-precision thermostatic cartridge keeps temperature fluctuation within ±1℃ even when other water points open. The LED digital display shows water temperature in real time — blue for low, red for high — preventing scalds.

## II. Common Marketing Materials (Company-level, see 00-公共营销素材.md)

The following materials are GIBO brand/company-level general content, centrally maintained in `00-公共营销素材.md`; this file does not repeat them:

- Source: 2018 GIBO Launch Event 0603(1)
- Source: Product Promotion Conference
- Source: Sensor Sanitary Ware Sales Key Points
- Source: GIBO Salesperson Training Manual
- Source: GIBO New Product Presentation 2020-LOTA20200406

## III. This Product's Marketing Materials (actual extracted text)

### Source: Smart Shower Series Product-solution Presentation 0707

[Image]
[Image]
[Image]
[Image]
Smart Shower Series Product-solution Presentation
New Technology & New Solution
GIBO Focused on Kitchen & Bath Tech for 21 Years
2026
lidaliang

Contents
01
Product Trends & User Pain Points
02
Series Product-solution Overview
03
Smart Shower Solutions:
04
Solution Advantages & Competitiveness
1. Smart Electronic Thermostatic Digital-display Shower Electronic-control Module
2. Wireless Cold-water Pre-drain Digital-display Ambient-light Shower Electronic-control Module
3. Smart Digital-display Shower Electronic-control Module
[Image]

Product Trends & User Pain Points
01

Thermostatic, temperature digital-display, energy-saving, and ambient-light comfort tech experience become the core upgrade direction for shower products
Intelligence penetration accelerating
Smart-home ecosystem continuously expanding
Bathroom-space intelligence becomes a new growth pole
Consumption-upgrade demand
Users shift from "can take a shower" to "take a good shower"
Thermostatic comfort becomes the core demand
New energy-saving & eco-friendly standard policy
Dual constraints of water & energy tightening
Water-saving & energy-efficiency standards continuously rising
Differentiation competition intensifying
Traditional products severely homogenized
Smart functions become the key to brand breakout
New-tech iteration, product evolution
New-tech applications: "AI algorithms, millimeter-wave, laser, body sensing, voice tech, Hall sensing, hydro-power generation & energy storage," etc.
Core-chip trends
[Image]
[Image]
[Image]
[Image]
[Image]

User Core Pain-point Analysis
Intelligent solution path: thermostatic control solves unstable temperature; digital display solves the information blind spot; cold-water pre-drain solves waiting waste and water-use experience
[Image]
The three major pain points of traditional shower experience are precisely the value entry points for intelligence — pain-point dimension, specific manifestation, user impact
1. Water-pressure fluctuation causes sudden cold/hot; elders and children easily scald; poor experience, big safety hazard
2. Unclear temperature, information blind spot; cannot intuitively perceive water temperature; hand-testing poses scald risk; lacks security sense, inconvenient operation
3. After opening, must drain the pipe's cold water; long wait and water waste; poor experience, water-resource waste

Series Product-solution Overview
02

Positioning & Differences of Three Major Solutions
From flagship to entry, layered coverage of different customer needs and price bands
Dimension
Solution 3
Solution 2
Solution 1
Positioning
Thermostatic method
Temperature display
Special function
Wireless control + cold-water pre-drain
Power supply
Target customer
Solution TOP
Brand flagship model
Quick-mount battery box + AA batteries
Mid-to-high-end brand main model
Experience-focused differentiated model
Differentiation advanced
Mechanical thermostatic
Digital display
Digital display
Mainstream full-function
Mechanical thermostatic
Digital display + ambient light
Flagship-leading
Electronic thermostatic
Digital display + key-position display + ambient light
Wireless remote + smart-control thermostatic
Hydro-power generation + lithium battery
High-end flagship model
Quick-mount battery box + AA batteries
Quick-mount battery box + AA batteries
Mainstream quality
Mechanical thermostatic
Digital display
Ambient light strip
[Image]

Solution 1
1. Digital display + touch panel + ambient light + hydro-power generator + temp-adjust motor module + 4 solenoid valves + 3 temp sensors + lithium battery pack; +(glass display panel — custom by customer separately)
1
2. Digital display + touch panel + hydro-power generator + temp-adjust motor module + 4 solenoid valves + 3 temp sensors + lithium battery pack; +(glass display panel — custom by customer separately)
2
3. Digital display + wireless remote box + ambient light + hydro-power generator + temp-adjust motor module + 4 solenoid valves + 3 temp sensors + lithium battery pack; +(glass display panel — custom by customer separately)
3
4. Digital display + wireless remote box + hydro-power generator + temp-adjust motor module + 4 solenoid valves + 3 temp sensors + lithium battery pack; +(glass display panel — custom by customer separately)
4
"Smart Electronic Thermostatic Shower Electronic-control Module"
(4 combinable variants)
[Image]

1. Temp digital-display box + temp sensor + Hall module + cold-water pre-drain solenoid valve + remote box + AA battery-box pack + ambient light strip; +(acrylic ambient-light cover — custom by customer separately)
1
2. Temp digital-display box + temp sensor + Hall module + cold-water pre-drain solenoid valve + remote box + AA battery-box pack;
2
3. Remote box optional: A. button type; B. infrared-sensing type; C. touch type.
3
"Smart Wireless Cold-water Pre-drain + Ambient-light Digital-display Shower Electronic-control Module" (3 combinable variants)
Solution 2
[Image]

Solution 3
"Smart Digital-display Shower Electronic-control Module"
(2 combinable variants)
1. Temp digital-display box (ice-blue + red dual color, other colors customizable) + temp sensor + Hall module + AA battery-box pack + ambient light strip; +(acrylic ambient-light cover — custom by customer separately)
1
2. Temp digital-display box (ice-blue + red dual color, other colors customizable) + temp sensor + Hall module + AA battery-box pack;
2
[Image]

Smart Electronic Thermostatic Shower Electronic-control Module
Solution 1 Detailed Explanation:
"Thermostatic Great Bath, One-click Remote Control!"
[Image]

Solution 1 Function Architecture
[Image]
Electronic thermostatic + digital display + remote + hydro-power generation, building a flagship-level smart-shower experience

Hydro-power generator module integrated inside the valve body, occupying no extra space
Wireless remote box can be wall-mounted or handheld, flexible installation
Standard exposed-valve-body interface, compatible with mainstream piping layouts
Install Compatibility
Thermostatic comfortable bathing experience
Convenient remote operation, full of tech feel
[Image]
Application Scenarios
[Image]
Elevates stay experience, digital-display anti-scald design
Star-hotel guest rooms
Both ambiance and tech feel
High-end club bathroom
Smart thermostatic, wireless remote function control
High-end residence master bathroom
Highlights high-end quality positioning
[Image]

Product Composition (-electronic thermostatic)
[Image]
Seq | Part Name | Qty
1 | Main control PCBA module | 1
2 | Lithium battery pack | 1
3 | Charging interface | 1
4 | Temp sensor group | 3
5 | Temp & function key-position display group | 1
6 | Solenoid valve group | 4
7 | Temp-adjust motor module | 1
8 | Hydro-power generation group | 1
9 | Wireless box | 1

Architecture Schematic
[Image]
[Image]
Water-flow motor
[Image]
[Image]
Temp-adjust module
[Image]
[Image]
Solenoid valve
[Image]
[Image]
NTC
[Image]

Smart Wireless Pre-drain Digital-display Shower Electronic-control Module
Solution 2 Detailed Explanation:
[Image]
"New Bathing Experience, Understands Water Temp and Understands You More!"

Solution 2 Function Architecture
Multiple smart boosts! Remote cold-water discharge, real-time water-temp digital display, color-changing ambient light — thermostatic and worry-free bathing
Mechanical thermostatic, stable temp control
Shower thermostatic
Standard battery power, low-power design, endurance guarantee
AA battery-box power
LED digits real-time water-temp display
Temp digital display
After remote start, drains pipe cold water; hot water comes the moment it opens
Remote cold-water pre-drain
Water-temp sensing color change, also serving lighting & safety cue
Ambient light strip
"New Bathing Experience, Understands Water Temp and Understands You More!"
[Image]
Cold-water pre-drain function directly hits the "open tap and wait for hot water" pain point

Application Scenarios
Install Compatibility
Cold-water pre-drain function significantly improves guest-room hot-water experience & stay satisfaction. Flexible remote install
Remote supports wall-mount outside the shower area; users can remotely operate pre-drain before entering the bathroom, achieving non-contact convenient control.
Elderly-care / age-friendly bathroom
Elders need no hand temp-test; after remote pre-drain use hot water directly, avoiding scald risk & operation inconvenience.
Hotel engineering / upgrade renovation
Cold-water pre-drain module directly integrated inside the product, no extra piping major retrofit, fits existing shower product layout design
Module-integrated design
Elevates bathing-water experience.
Large-unit / home upgrade
[Image]

Product Composition (pre-drain digital display)
[Image]
Seq | Part Name | Qty
1 | Temp digital-display PCBA group | 1
2 | Battery-box group | 1
3 | Temp sensor | 1
4 | Hall sensor + magnetic rotor | 1
5 | Ambient light strip | 1
6 | Solenoid valve |
7 | Wireless box |

LED display PCBA group
[Image]
[Image]
[Image]
Pulse solenoid valve
[Image]
[Image]
NTC
[Image]
[Image]
Hall module
[Image]
[Image]
Easy-disassemble battery box
[Image]
[Image]
Ambient light strip
[Image]

Smart Digital-display Shower Electronic-control Module
Solution 3 Detailed Explanation:
[Image]
"Water Temp Visible, Bathing Safer!"

Solution 3 Function Architecture
"Water Temp Visible, Bathing Safer!"
Smart LED temp digital display, outlet temp real-time intuitive; paired with temp-sensing color-changing ambient light, looks and safety both
[Image]
Focuses on users' most core thermostatic & LED digital-display needs, uses ambient light strip to raise product added value, achieving smart selling points while controlling cost

Install Compatibility
[Image]
Application Scenarios
01
Large-unit / home upgrade
Temp real-time display, elevates bathing-water experience.
02
Module-integrated design
Inside the product, no extra piping major retrofit, fits existing shower product layout design
03
Hotel engineering / upgrade renovation
Elderly-care / age-friendly bathroom
Elders need no hand temp-test; after remote pre-drain use hot water directly, avoiding scald risk & operation inconvenience.

Product Composition (-digital-display shower)
[Image]
Seq | Part Name | Qty
1 | Temp digital-display PCBA group | 1
2 | Battery-box group | 1
3 | Temp sensor | 1
4 | Hall sensor + magnetic rotor | 1
5 | Ambient light strip | 1

LED display PCBA group
[Image]
[Image]
[Image]
NTC
[Image]
[Image]
Hall module
[Image]
[Image]
Easy-disassemble battery box
[Image]
[Image]
Ambient light strip
[Image]

Solution Explanation & Competitiveness
04

Business Advantages: Boost Rapid Product Launch & Flexible Adaptation
Modular Architecture
Power/display/control modules independently packaged; customers choose & combine as needed
Standard interface design, compatible with mainstream valve bodies & piping specs
Rapid Delivery
Mature module solution; customers need no development from scratch, shortening time-to-market
Provide complete tech docs & application support, lowering R&D investment
Upgrade Iteration
Tech support for product iteration & continuous development
Service
Covers full chain
Cost Controllable
Three solutions cover different price bands; customers flexibly choose by market positioning
AA-battery solution lowers power-system cost, fits volume products
[Image]
[Image]
[Image]
[Image]
[Image]

1. Module includes: flow sensor, temp sensor, PCBA display module, battery-box module (ambient light strip optional)
2. Water-flow detection: via Hall sensor & water-flow rotor, detects flow and converts to data output; when water doesn't flow the sensor is in sleep mode with extremely low power.
3. Temp detection: via temp sensor detects water temp and converts to data output.
4. Temp display: via LED digital tube displays water-temp value.
1. Precise temp measurement, accuracy up to ±1℃.
2. Battery power, stable & reliable, avoids hydro-power solution's faults from impurities or scale after a period of use.
3. Digital tube brightness consistency high; won't vary with flow size.
4. Battery over-limit use (battery-protected ultra-use), effectively extends battery life.
5. Hall water-flow detection, small volume, convenient for structure design, low sleep-mode power.
6. Temp display solution: standard LED digital-display; also optional ambient-light strip solution (different temp zones distinguished by dual-color light).
7. Ultra-low start flow: 1.5L/min flow can start.
Solution Explanation /
Application /
Smart Shower Series
Battery-powered Digital-display Solution
[Image]

1. Module includes: PCBA display module, solenoid valve module, temp probe, wireless remote box + battery-box module. (Ambient light strip optional; wireless box has button & infrared-sensing two choices)
2. Pre-drain function: remote "one-click pre-drain" button; digital tube flashes bright 1s / off 1s; pre-drain complete extinguishes, meanwhile opens solenoid valve, buzzer beeps once, starts pre-draining cold water; when temp sensor detects water temp reaching preset value auto-closes water, outlet 180s duration auto-closes water; during pre-drain, pressing remote "cold-water pre-drain" button again auto-closes water.
3. 2.4G communication: remote and control box connected via 2.4G wireless, enabling remote cold-water pre-drain function — using an external remote, no need to enter the shower room to execute pre-drain.
2. Water-flow detection: via Hall sensor & water-flow rotor, detects flow and converts to data output; when water doesn't flow the sensor is in sleep mode with extremely low power.
3. Temp detection: via temp sensor detects water temp and converts to data output.
4. Temp display: via LED digital tube displays water-temp value.
1. Battery power ensures display brightness consistency, elevates product grade.
2. Precise temp measurement, accuracy up to ±1℃.
3. Temp display solution: digital-display or optional ambient-light strip solution (dual-color by temp zone).
4. Cold-water pre-drain: when shower outlet reaches set temp, auto stops water, greatly improves experience.
5. Remote cold-water pre-drain: wireless remote, no need to enter shower room to execute pre-drain.
6. Ultra-strong anti-interference: meets CE\FCC certification, passes burst (group pulse) Level-4 test.
Solution Explanation /
Application /
Smart Shower Series
Remote Pre-drain with Digital-display Solution
[Image]

Electronic Thermostatic Core-tech Support:
[Image]
Hydro-power Self-supply
Water-flow kinetic energy instantly converts to electricity; no external power or frequent battery change
Paired with lithium battery energy storage; storage system guarantees all-weather uninterrupted operation, zero-interruption water experience
Aligns with national energy-saving certification standard, seizing green-consumption first-mover advantage
[Image]
[Image]
[Image]
Electronic Thermostatic High-precision Control
Electronic cartridge response far exceeds mechanical thermostatic; temp fluctuation controlled within ±1℃
Real-time monitors inlet temp & flow changes, dynamically adjusts cold/hot ratio
Adapts to complex water-pressure environments; high-rise residences & old communities equally stable
Millisecond-level response, precisely locks target temp
Multi-modal fusion AI algorithm, dynamic adjustment, cold/hot ratio optimized in real time
Full-scenario water-pressure adaptation, complex conditions still thermostatic as one
[Image]
[Image]
[Image]
[Image]
[Image]
[Image]
[Image]
[Image]
[Image]
[Image]
[Image]
[Image]
[Image]
[Image]

IoT Smart Interconnection Application Tech
Voice recognition tech
Wireless remote tech
Triangulation Ranging Sensing Technology
dTOF Laser low-power sensing tech
Capacitive sensing tech
Single-window dual-sensor gesture-recognition tech
Microwave (millimeter-wave) sensing tech
Thermostatic outlet closed-loop control tech
Hydro-power generation & energy-storage tech
Water-hammer suppression fluid tech
Electronic shower (pre-drain, digital display, ambient light, temp-adjust, function display + wireless control)
Kitchen faucet, shower + foam wash fusion
Hidden-sensing cistern flush solution
Instant-heat faucet sensing temp-control solution
Multi-function electronic faucet solution (water&soap 2-in-1, water&soap&air 3-in-1)
Electric heated-towel-rack smart temp/time control solution
dTOF laser / capacitive foot-sense module solution
Solenoid valve low water-hammer solution
[Image]

[Image]
FUJIAN GIBO KITCHEN & BATH TECH CO., LTD.
[Image]
Thanks for Watching
GIBO Focused on Kitchen & Bath Tech 21 Years
[Image]
[Image]
2026/6/30
> Updated: 2026-07-14 | GIBO | Sensor Faucet ODM Expert | Web: https://www.gibosensor.com

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
