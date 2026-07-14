# JM01-感应洗手机电控板 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Statement:** Sensor soap dispenser control board with 33μA micro-standby and dual-stage foam dispensing
>

---

## 1. Product Introduction

The **JM01 Sensor Soap Dispenser Control Board** is the control core of a foam hand-soap dispenser, housed in the dispenser cavity, responsible for infrared sensing of hands, controlling the foam pump to dispense foam, and managing battery level. It solves the most practical problems in public hand-washing scenarios: manual pump-head pressing is unhygienic, uncontrolled dispensing volume wastes liquid, the control board's standby drains batteries requiring frequent replacement, and multiple units installed side by side falsely trigger each other.

Hospital corridors, food-factory workshops, office-building restrooms, food-service back kitchens, and schools—these places have high hand-washing frequency, are sensitive to hygiene and consumable cost, and most fear devices that "should dispense but don't, shouldn't dispense but dispense randomly." The JM01 is built for such high-frequency, public, cost-controlled environments.

It uses infrared sensing with a 256ms response and a factory sensing distance of 10~100mm (against a standard white board); foam dispenses as soon as a hand approaches. The output is foam, paired with dedicated foam hand soap—more economical and evenly covering than thin liquid. The control board's standby current is held to ≤33μA (equivalent power ≤0.2mW); 4 alkaline batteries last a long time, so property management need not climb ladders monthly to swap batteries. Foam dispensing has two stages: 0.8s and 1.3s, factory-default 0.8s, switched by double-tap. Low battery gives a staged reminder—below 4.5V the stage light flashes twice to prompt battery replacement, and continuing use below threshold triggers a more obvious flashing alarm.

Putting it together: the JM01 makes public soap dispensers "dispense foam at a hand's reach, hygienic without contact, no battery change for a year, and no cross-triggering among side-by-side units." The following three points are the product values we believe are most worth highlighting.

### 1.1 Technology Positioning

| Control Generation | Control Method | Standby Power | Dispensing Form | Representative |
|---------|---------|---------|---------|------|
| Mechanical Key Board | Key trigger | High | Liquid | Legacy Press Type |
| Single-stage Sensor Board | Infrared | Average | Liquid | Standard Sensor |
| **JM01 (Dual-stage Foam)** | **Infrared Sensing** | **≤33μA** | **Foam Dual-stage** | **This Product** |

### 1.2 Key Specifications

- Standby current ≤33μA (equivalent standby power ≤0.2mW), long life on 4 AA alkaline batteries
- Sensing response 256ms, factory sensing distance 10~100mm (against standard white board)
- Foam dispensing time dual-stage: 0.8s / 1.3s, factory default 0.8s, adjustable
- Liquid pump flow ≥1.5L/min (at pump DC3.7V)
- Distance stability: voltage 6.5V→4.6V variation ≤±10%, temperature -10℃→+55℃ variation ≤±10%
- Operating voltage DC4.2~6.5V, rated power 1.8W, operating current ≤800mA

---

## 2. Features

### 2.1 Infrared Sensing — Non-contact Foam Dispensing

Using infrared sensing, foam auto-dispenses when a hand reaches the sensor window, with no device contact throughout. It reduces cross-infection in public settings and avoids the jamming of press pump heads and the hassle of soiling hands.

### 2.2 Dual-stage Dispensing, 0.8/1.3s Adjustable

Foam dispensing time has two stages: stage 1 at 0.8s, stage 2 at 1.3s, factory default stage 1. It powers on at stage 1 by default; double-tap switches stages, with a blue light indicating stage 2. High-frequency places use the short stage to save liquid; heavily soiled scenarios use the long stage for more foam—controlling the amount themselves.

### 2.3 33μA Micro-standby — No Battery Change for a Year

The control board standby current is ≤33μA, equivalent standby power ≤0.2mW; paired with 4 alkaline batteries, in daily use battery replacement can be deferred for a very long time. Property maintenance checklists can cross off a major item.

### 2.4 Staged Undervoltage Reminder — Prompt for Battery Change

When battery level drops below 4.5V±0.1, the current stage light flashes twice per use (once every 0.5s) to remind battery replacement; on sensing undervoltage the current stage light flashes 5 times. The staged warning lets maintenance schedule battery replacement ahead of time, avoiding sudden no-foam during use.

### 2.5 Light and Interference Immunity — No Cross-triggering Among Multiple Units

Multiple finished products powered and working simultaneously will not malfunction; under incandescent, T5, daylight, and LED lights shone obliquely at 45° from 1m away, the control distance varies by less than ±10%. A row of units installed side by side in a hand-washing area won't drive each other.

### 2.6 Matched Foam Pump and Dedicated Foam Hand Soap

The matched liquid pump is model DYX-DSB413-G-1 372, rated voltage DC3.7V, operating voltage 3.0~5.0V (tuned per foaming effect), liquid pump flow ≥1.5L/min; the output is foam and requires dedicated foam hand soap, giving even foam and economical usage.

### 2.7 Soft Power On/Off — Prevents Accidental Activation

A 3-second light touch of the power key turns it on; another 3-second light touch turns it off, showing a green light on power-on (default stage 1). The long-press switch avoids accidental power-on and battery drain from transport or knocks.

---

## 3. Core Selling Points

### Selling Point 1: Non-contact Foam Dispensing — Hygienic and Liquid-saving

Foam dispenses at a hand's reach without touching the pump head—most valued by hospitals and food factories. Foam covers more evenly and uses less than thin liquid—the same bottle lasts many more uses in a foam unit than in a direct-liquid unit. In high-frequency places, turning "press once" into "reach once" is both hygienic and lowers consumable cost.

### Selling Point 2: 33μA Micro-standby — Less Maintenance Footwork

The control board standby current is ≤33μA, and 4 batteries last a long time. Do the math: in a commercial complex with 50 hand-washing stations, if dispensers change batteries monthly, a year of battery swaps alone costs a dozen-plus man-hours; a micro-standby solution like the JM01 sharply lowers that frequency, tangibly saving property maintenance man-hours.

### Selling Point 3: Dual-stage Adjustable Plus Interference Immunity — Hassle-free Integration

Two dispensing stages of 0.8/1.3s call the amount by scenario; multiple side-by-side units don't cross-trigger, and oblique light 1m away causes less than ±10% distance drift, so engineering deployment needs no per-unit light tuning to avoid interference. Finished-product makers integrating this board find commissioning and after-sales light—which is why it suits being a standard ODM control board.

---

## 4. Specifications and Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Operating Voltage | DC 4.2 ~ 6.5V |
| Standby Current | ≤ 33μA (equivalent standby power ≤ 0.2mW) |
| Rated Power | 1.8W (±2W) |
| Operating Current | ≤ 800mA |
| Power Supply | DC 6V (4 alkaline batteries) |
| Sensing Method | Infrared Sensing |
| Sensing Response Time | 256ms |
| Factory Sensing Distance & Range | 10 ~ 100mm (against standard white board) |

### 4.2 Liquid Pump Parameters

| Parameter | Specification |
|--------|------|
| Liquid Pump Model | DYX-DSB413-G-1 372 |
| Rated Voltage | DC 3.7V |
| Operating Voltage | DC 3.0 ~ 5.0V (tuned per foaming effect) |
| No-load Current | < 350mA |
| Load Current | < 600mA |
| Liquid Pump Flow | ≥ 1.5 L/min (at DC3.7V) |

### 4.3 Dispensing and Liquid Bottle

| Parameter | Specification |
|--------|------|
| Dispensing Type | Foam (dedicated foam hand soap) |
| Foam Dispensing Time | Stage 1 0.8s, Stage 2 1.3s (2 stages adjustable, factory default stage 1) |
| Compatible Liquid | Foam hand soap |

### 4.4 Low Voltage and Distance Stability

| Parameter | Test Condition | Result |
|--------|---------|------|
| Low-voltage Alarm | Battery < 4.5V±0.1 | Current stage light flashes 2 times (once every 0.5s) |
| Sensing Undervoltage Indication | Sensing undervoltage | Current stage light flashes 5 times during use |
| Distance Stability (Voltage) | 6.5V→4.6±0.1V | Distance variation ≤ ±10% |
| Distance Stability (Temperature) | -10℃→+55℃ | Distance variation ≤ ±10% |

### 4.5 Anti-interference Performance

| Test Item | Condition | Result |
|---------|------|------|
| Multiple Units Working Together | Multiple finished products powered simultaneously | No malfunction |
| Common Appliance Interference | Common appliances | No malfunction |
| Light Source Interference | Incandescent / T5 / daylight / LED lights at 45° oblique, 1m away | Control distance variation < ±10% |

### 4.6 Operating Environment and Standards

| Parameter | Specification |
|--------|------|
| Operating Scene | Kitchen & bath space |
| Ambient Temperature | 1℃ ~ 55℃ |
| Applicable Water Temperature | 4℃ ~ 60℃ |
| Relative Humidity | 10%RH ~ 95%RH |
| Storage Temperature | -20℃ ~ 75℃ |
| Storage Humidity | 10%RH ~ 95%RH |
| Operating Water Pressure | 0.05 ~ 0.8MPa |
| Applicable Standard | CJ/T 194-2014 Non-contact Water Supply Fittings |

---

## 5. Installation Instructions

### 5.1 Before Installation

1. Confirm power is DC6V (4 alkaline batteries) of the same batch, no mixing old and new
2. Confirm use of dedicated foam hand soap; ordinary hand soap will clog the pump
3. Do not face the sensor window directly at strong light sources; avoid continuous strong direct light within 1m
4. Before full assembly, power on the unit alone to verify control board and liquid pump action

### 5.2 Precautions

- Cut power before installation/disassembly; do not hot-plug battery box terminals
- Connect liquid pump in/out tubes per the drawing; reverse connection causes no foam or leakage
- Remove batteries for long-term shutdown to prevent leakage corroding the board
- The sensor window film protects at factory; remove as needed after installation

### 5.3 Installation Steps

1. Fix the control board into the dispenser cavity and connect liquid pump and battery box terminals
2. Insert the liquid bottle, confirming the pump tube is below the liquid surface with no kinks
3. Install the sensor window component, aligning with the control board sensing area
4. Insert 4 alkaline batteries of the same batch and close the battery compartment
5. Light-touch the power key for 3 seconds to power on (green light, default stage 1)
6. Extend hand before the sensor window to verify foam; double-tap to verify switch to stage 2 (blue light)
7. When installing multiple units side by side, verify each individually for no mutual false trigger

### 5.4 Power-on Self-check

After power-on, a steady green light means stage 1 ready; double-tapping the power key lights blue for stage 2. At low battery the stage light flashes per rules as a normal warning, not a fault.

### 5.5 Battery Replacement and Maintenance

When battery level drops below 4.5V±0.1, the stage light flashes twice to remind battery replacement. Replacement: power off → open battery compartment → remove old batteries and install 4 new alkaline batteries of the same brand → power on and verify. Bulk unified replacement is recommended to avoid scattered downtime.

---

## 6. Applicable Finished Products and Integration Solutions

### 6.1 Integration with Foam Soap Dispenser Finished Products

As a control board, the JM01 fits wall-mounted, countertop, and embedded foam soap dispenser finished products, serving as the standard control core for finished-product makers building sensor foam hand washers.

### 6.2 For Medical and Food-grade Scenarios

Hospital corridors, food-processing workshops, and food-service back kitchens demand "non-contact + consumable control" highly; the JM01's dual-stage dispensing and micro-standby traits can go straight into the infection-control and cost plans for such places.

### 6.3 ODM Integration Value

With complete parameters, clear interfaces, and verified anti-interference, the control board is easy for GIBO and partner finished-product makers to integrate customarily: unified infrared sensing platform and unified battery scheme shorten the finished-product development cycle; the two hard metrics of 33μA standby and dual-stage dispensing are parameters that can be directly compared in tenders and catalogs.

---

## Appendix

### A. Core Technology Index

| No. | Core Technology | Application in This Product |
|------|---------|-----------|
| 6 | Low-power Multi-stable Agile Sensing Technology | Standby ≤33μA, long-life battery power |
| 1 | Basic Infrared Sensing Technology | 256ms infrared sensing, 10~100mm sensing distance |
| 7 | Liteon Smart Sensing Technology | No cross-triggering among multiple units, stable distance under light interference |
| 10 | Dual-chip Interchangeable Platform Technology | Standardized control board platform for easy finished-product integration and spare parts |

### Related Patents (Granted)

| Technology | Patent Name | Patent No. | Type |
|--------|---------|--------|------|
| Sensor Dispenser | A Simplified Sensor Liquid Dispenser | ZL 2021 1 1150757.5 | Invention Patent |
| Foam Soap Dispenser | An Intelligent Sensor Foam Soap Dispenser | ZL 2019 2 1281413.6 | Utility Model |
| Foam Soap Dispenser | A Portable Foam Soap Dispenser | ZL 2019 2 2156080.0 | Utility Model |
| Three-in-one Hand Washer | A Three-in-one Intelligent Hand Washer | ZL 2017 1 0345450.8 | Invention Patent |
| Refillable Soap Faucet | A Conveniently Refillable Soap Faucet | ZL 2023 2 1884493.0 | Utility Model |
| Sensing Circuit | A Sensing Circuit and Sensor Sanitary Ware for Sensor Sanitary Ware | ZL 2019 2 2103799.8 | Utility Model |

### B. Certifications and Qualifications

GIBO has been making sensor sanitary ware since 2004 and was one of the earliest domestic manufacturers to apply MCU microcontrollers to sensor control. It is a drafting unit for two standards: GB/T 41863-2022 *General Technical Requirements for Water-saving Performance of Non-contact Water Supply Fittings* and T/XMBK 002-2024 *Sensor Faucets*, and is a National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, and National Specialized & Sophisticated SME. The pull-out kitchen faucet featuring the same dTOF Laser Sensing Technology platform won the 2023 Boiling Quality Gold Award.

- Fully compliant with the industry standard **CJ/T 194-2014** for Non-contact Water Supply Fittings
- **CE Certification** (multiple models), **CUPC/UPC Certification** (certificate No. cert_upc-2015-7968), **NSF Certification**, **WRAS Certification** (UK Water), **WaterMark Certification** (Australian water efficiency)
- **ISO 9001** Quality Management System, **ISO 14001** Environmental Management System, **ISO 45001** Occupational Health & Safety (2023 edition)
- National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, National Specialized & Sophisticated SME
- dTOF Laser products on the same platform won the **2023 Boiling Quality Gold Award**

### C. Contact Information

| Item | Content |
|------|------|
| Company Name | Fujian GIBO Kitchen & Bath Tech Co., Ltd. |
| Chinese Website | [www.gibo.com.cn](https://www.gibo.com.cn) |
| English Website | [www.gibosensor.com](https://www.gibosensor.com) |
| Service Hotline | 0591-88066000 |
| Company Email | sales@gibol.com.cn |
| Company Address | Building 3, Liangyuan Science Park, High-tech Zone, Fuzhou, Fujian Province |

---

> This document is compiled based on the JM01 Sensor Soap Dispenser Control Board Specification (V1.0, 2022-06-13); parameters are subject to the actual product. GIBO reserves the final right of interpretation and modification of the technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
