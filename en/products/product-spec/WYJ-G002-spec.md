# WYJ-G002 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Statement**: A dual-sensor basin faucet that shows water temperature by color ring.
>

---

## I. Product Introduction

For a public basin faucet, users fear two things most: no water when reaching, or suddenly very hot water. The **WYJ-G002** uses "front + side" two IR sensor heads to handle output, and a ring of LED light to solve "can you see the water temperature"—while flowing, the ring changes color by temperature zone: below 35°C is blue (cold), 35~49°C is orange (warm), above 49°C is red (hot, over-temperature); standing in front of the faucet and glancing at the color tells you whether the water is cool or hot, no need to test by hand.

Unlike the numeric-display model, the G002 does not pile on numbers but speaks with color. It also has front-sensor instant output (come for water, leave to stop) and side-sensor long-flow output (sense once to open, sense again to close), with a side mechanical knob for cold/mixed/hot/off four-position temperature control, still manually deliverable when powered down. The color distinction is crisp: blue is blue, orange is orange, with clear boundaries between zones—no vague flickering that confuses. The ring lights while flowing and goes dark when done; if a single use is under 30s it stays lit 30s for clarity.

For power, the G002 recommends an AC110~220V-to-DC6V adapter for permanent power, and can also take 4 AA batteries for half a year. Complete-unit standby current is held at the 45μA level; ESD level 4, burst ±4KV, EMI 3V/m all normal; 6 light-source types within 15~91cm direct/oblique cause no false trigger. For contractors, this is a public-restroom basin faucet where "color reports the temperature for you, outputs accurately when it should, and stays stable anywhere," suited to malls, offices, and hospitals where both safety and experience matter.

### 1.1 Technical Positioning

| Type | Sensing Method | Output Interaction | Temperature Feedback | Representative Product |
|------|---------|---------|---------|---------|
| Traditional mechanical basin faucet | None | Hand-turn handle | None | Ordinary faucet |
| Single-sensor IR faucet | Single IR | Hand-reach output | None | Early sensor faucet |
| Numeric dual-sensor faucet | Front+Side dual IR | Instant+Long | Numeric readout | WYJ-G001 |
| **GIBO LED-Ring Dual-Sensor Faucet (G002)** | **Front+Side dual IR** | **Instant+Long dual mode** | **LED color-ring zone prompt** | **WYJ-G002** |

### 1.2 Key Metrics

- Output response ≤0.6s (sense to water), close ≤1.0s (instant) / ≤1.5s (long)
- LED dual-color ring: blue (<35°C) / orange (35~49°C) / red (>49°C over-temp)
- Front sensing distance power-on auto-adaptive 20±3cm / 8±3cm, side fixed 7~10cm
- Complete-unit standby current ≤45μA, 4 AA batteries about 6 months
- Flow ≤6L/min, static burst pressure 2.5MPa/60s no leakage
- ESD level 4 (air ±15KV), burst ±4KV, EMI 3V/m normal operation

---

## II. Features

### 2.1 Front Sensor Instant Output—Water at Hand's Reach

When a hand or object enters the front sensing range, water outputs automatically, response ≤0.6s, red LED flashes once as prompt; hand leaves, auto-close, close ≤1s. Continuous flow beyond 60±10s auto-closes to prevent waste from long flow.

### 2.2 Side Sensor Long-Flow—Wave to Switch

The side sensor head uses "sense once to open, sense again to close" long-flow logic, response ≤0.6s, suited to filling containers and washing hair that need continuous flow; beyond 180±5s auto-closes. Side sensor priority higher than front; on conflicting signals, side wins.

### 2.3 Dual-Color Ring—Temperature Reported by Color

While flowing, the LED ring on the faucet lights, in three colors by temperature: below 35°C shows blue (cold), 35~49°C shows orange (warm), above 49°C shows red (hot over-temperature warning). Zone boundaries are clear—no vague blue-orange transition. When done the ring goes dark; if a single use is under 30s it stays lit 30s for clarity.

### 2.4 Mechanical Knob Temperature Control—Usable Even When Powered Down

The side mechanical knob, front to back, is "cold water—mixed water—hot water—off," controlling both on/off and temperature. With dead batteries or power loss, the knob still delivers cold/mixed water manually—never becomes a dead weight.

### 2.5 Power-On Auto-Adaptation—Ready Once Installed

On first power-on the LEDs light together and turn off after 1 second to complete auto-calibration; afterward re-powering requires an interval of more than 3 minutes from the previous power-on to ensure calibration validity. Keep the basin dry before adaptation—essentially no tuning.

### 2.6 Low-Voltage Reminder—Advance Warning to Change Batteries

When any sensor head senses a hand, if battery voltage is 4.5~4.7V it first opens the valve and makes the LED flash quickly 5 times to remind of battery change; below 4.5V the solenoid stays closed and the LED flashes 10 times, avoiding running flat in front of a customer.

### 2.7 Power-Loss Protection and Anti-Interference—Stable Anywhere

If external power is suddenly cut, the solenoid closes immediately regardless of state—no continuous flow. The module immersed in 25°C water 24h and boiled in water 0.5h functions normally with sensing-distance change under 10%; 6 light-source types (incandescent, fluorescent, halogen, bathroom heater, hairdryer, etc.) within 15~91cm direct/oblique cause no false trigger.

---

## III. Core Selling Points

### Selling Point 1: Temperature Reported by Color—Over-Temp Turns Red at a Glance

A numeric screen needs you to lean in to read digits; the ring is more direct—blue/orange/red correspond to cold, warm, hot, readable from two meters away to know if the water is safe to take. For hotel, hospital, and school logistics, the red over-temperature warning puts the "scalding hot water hurts someone" risk on the counter ahead of time, especially useful in children's activity areas and elderly-care spaces; compared to testing by hand, color is a zero-cost safety prompt.

### Selling Point 2: Dual Sensors, Two Logics—Full Scenario Coverage

Single-sensor faucets can only output on reach or only wave to switch, awkward when filling half a basin or hands are full. The G002 front sensor handles instant washing, side sensor handles long filling—two logics in one unit, side prioritized. Per the specification, 4 Nanfu batteries at 30 short + 20 long sensing per day last about 6 months—more carefree than frequently changed counterparts; a 50-unit public restroom saves more than half the annual ladder-climbing battery-change labor.

### Selling Point 3: Accurate Even in Strong Light and Strong EMI—No Fussy Install Location

At mall atriums and hospital corridors, lighting is mixed and equipment abundant, so ordinary IR is easily dazzled into false action. The G002 uses the Liteon Smart Sensing algorithm; 6 light-source types within 15~91cm direct/oblique cause no false trigger, ESD level 4 (air ±15KV), burst ±4KV normal operation. Engineering need not re-route to avoid strong lights, and the maintenance list handed to property managers is short; the recommended adapter-power option also eliminates battery changes entirely.

---

## IV. Specification & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power Supply | DC 6V (4 AA dry batteries) / AC110V~220V to DC6V/1A adapter (adapter power recommended) |
| Complete-Unit Consumption (standby current) | ≤45μA (at DC 6.0V) |
| Solenoid Parameters | DC 4.5V |
| Usable Water Temperature Range | 4°C~60°C |
| Power-On Auto-Adaptation Interval | Re-power requires interval >3 min from first power-on |

### 4.2 Sensing Parameters

| Parameter | Specification |
|--------|------|
| Front Sensing Distance | Power-on auto-adaptive, for white paper 20±3cm / 8±3cm |
| Side Sensing Distance | Fixed, for white paper 7~10cm |
| Front Response | Output ≤0.6s, close ≤1.0s |
| Side Response | Switch ≤0.6s |
| Dead Zone (white paper) | 5cm > dead zone > 2cm |

### 4.3 Output & Timing

| Parameter | Specification |
|--------|------|
| Front Instant Output Timeout Protection | 60s ± 3s auto-close |
| Side Long-Flow Timeout Protection | 180s ± 5s auto-close |
| Power-Loss Protection | External power loss, solenoid closes immediately |
| Side Priority | Side sensor priority higher than front |

### 4.4 LED Ring & Prompts

| Parameter | Specification |
|--------|------|
| Display Method | Dual-color LED ring, zone color display |
| Zone Colors | <35°C blue / 35~49°C orange / >49°C red (over-temp) |
| On/Off Logic | On while flowing; off when done; if single use <30s, stays on 30s |
| Low-Voltage Prompt | 4.5~4.7V flash 5 times; <4.5V flash 10 times and close valve |

### 4.5 Water Path & Flow

| Parameter | Specification |
|--------|------|
| Working Water Pressure | 0.05MPa ~ 1.0MPa |
| Flow (complete unit) | ≤6L/min |
| Burst Performance | Static pressure 2.5MPa held 60s no leakage |

### 4.6 Environment & Protection

| Parameter | Specification |
|--------|------|
| Operating Ambient Temperature | 1°C~55°C |
| Relative Humidity | 10%~95% RH |
| Storage Temperature | -20°C~65°C, humidity ≤80% RH |
| Module Waterproof | Immersed in 25°C water 24h no seepage; boiled 0.5h function normal, distance change ≤10% |
| ESD | Level 4, air discharge ±15KV, contact discharge ±8KV |
| EMI | Level 2, 80M~1000MHz, field strength 3V/m |
| Fast Transient Burst | ±4KV normal operation |

### 4.7 Applicable Standards

| Standard No. | Standard Name |
|---------|---------|
| CJ/T 194-2014 | Non-contact Water Supply Fixtures |
| QJMJCP 007002-2017 | Non-contact Water Supply Fixtures (enterprise standard, fully compliant for appearance/assembly/anti-interference etc.) |

---

## V. Installation Instructions

### 5.1 Before Installation

1. First flush the pipeline with water to clear sand and rust, avoiding solenoid clogging.
2. Confirm water pressure 0.05~1.0MPa; below 0.05MPa add a booster pump.
3. Keep the basin dry for power-on auto-calibration.
4. Confirm power method; G002 recommends adapter permanent power, reserve a power point in advance.

### 5.2 Notes

- Always shut water and cut power before install/repair (remove battery box or unplug adapter).
- Use same-brand high-performance alkaline batteries; do not mix old and new.
- Do not hot-plug sensor module terminals.
- The mechanical knob's range includes an "off" position; turn to off when unused to prevent accidental opening.

### 5.3 Installation Steps

1. Fix per faucet-body hole, connect cold/hot inlet pipes.
2. Connect the control module, lock the union (standard basin faucet fit).
3. Open water and pressure-test; confirm no leak.
4. Connect DC6V adapter (recommended) or install battery box.
5. Power on: LED lights, turns off after ~1s, entering adaptation.
6. Test front instant output and side long-flow in front of the sensor window.
7. Turn the mechanical knob to confirm cold/mixed/hot/off, watch ring color change with water temperature.

### 5.4 Power-On Self-Check

After power-on the LEDs light together and go dark after ~1s to complete adaptation; the first sense afterward flashes the red LED once to indicate trigger. To re-power for calibration, interval must exceed 3 minutes from previous power-on, and the basin must stay dry.

### 5.5 Battery Replacement

When voltage drops to 4.5~4.7V, each sense flashes the red LED 5 times to remind battery change; below 4.5V flashes 10 times and closes valve to stop work. Replacement: shut water → remove battery box → replace 4 same-brand new alkaline batteries → reinstall and re-power for adaptation.

---

## VI. Application Scenarios

### 6.1 Hotels / Clubs

High guest turnover at public basins; the color ring puts water-temperature risk right on the counter, fewer bad reviews; dual sensors cover both washing and filling, manual output when powered down—stable experience.

### 6.2 Hospitals / Elderly-Care Institutions

The young, old, sick, and weak are sensitive to water temperature; red/orange/blue is more intuitive than digits, understood at a glance by attendants; low-voltage advance warning avoids failing in front of customers when flat.

### 6.3 Malls / Office Buildings

Atrium strong light and strong EMI near escalators—the G002's 6 light-source anti-interference and EMC metrics ensure stability; adapter-power option eliminates battery changes, light property maintenance.

### 6.4 Schools / Venues

Students running and splashing—Liteon algorithm filters transient interference to reduce false triggers; timeout auto-close prevents long flow, saving water and worry.

### 6.5 Airports / Transport Hubs

24-hour operation, short maintenance windows—adapter permanent power avoids battery changes; wide pressure 0.05~1.0MPa adapts to old networks.

---

## Appendix

### A. Core Technology Index

| No. | Technology Name | Application in This Product |
|------|---------|---------------|
| #7 | Liteon Smart Sensing Technology | Dual IR sensor heads filter and debounce, filtering water-splash/noise false triggers |
| #6 | Low-Power Multi-Stable Agile Sensing Technology | Complete-unit standby ≤45μA, battery life about 6 months |
| #4 | Capacitive Touch Technology | LED dual-color zone ring display module |
| #11 | Dual-Mode Strong-Light-Immunity Anti-Interference Algorithm | 6 light-source types 15~91cm direct/oblique no false trigger |

### A.1 Related Patents (Granted)

| Technology Point | Patent Name | Patent No. | Type |
|--------|---------|--------|------|
| Dual-sensor output | A smart faucet with dual-sensor output | ZL 2018 2 0847903.7 | Utility Model |
| Display/light-display faucet | A sensor numeric-display faucet | ZL 2023 2 3354865.1 | Utility Model |

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

> This document is compiled based on the "WYJ-G002 LED-Ring Temperature-Display Basin Faucet Specification" (V1.0, 2020-11-11). Parameters are subject to the actual unit. GIBO reserves the final right of interpretation and modification of the technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
