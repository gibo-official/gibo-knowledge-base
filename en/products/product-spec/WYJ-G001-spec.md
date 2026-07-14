# WYJ-G001 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Statement**: A dual-sensor basin faucet with digital temperature readout.
>

---

## I. Product Introduction

The most awkward thing about a public basin is reaching for water and getting scalded, or adjusting the temperature halfway without knowing the current degrees. The **WYJ-G001** basin faucet mounts two IR sensor heads plus an LED numeric temperature screen: water flows the moment a hand approaches and stops when it leaves; a side sensor adds long-flow sensing and a mechanical temperature knob, while the screen shows the real-time water temperature as it flows—38°C is shown as 38°C, no need to test with the back of your hand.

In essence, it is the finished product of GIBO's "dual-sensor + numeric display" philosophy—a front sensor head handles instant output (come for water, leave to stop), a side sensor head handles long-flow output (sense once to open, sense again to close); both sensor heads use IR, paired with the Liteon Smart Sensing algorithm to filter out water-splash and noise false triggers. The mechanical knob switches among cold water, mixed water, hot water, and off, and can still deliver water manually even when powered down. While flowing, the white-light LED 2.5-digit display on the faucet lights up with the current water temperature and goes dark when done, so users always know "how hot it is" and scald risk drops accordingly.

Power is flexible: 4 AA alkaline batteries last over half a year, or it can connect to an AC110~220V-to-DC6V adapter for permanent power—both battery and adapter work. The complete-unit standby current is held at the 45μA level; with the multi-stable low-power architecture, one battery lasts a long time. It also withstands 23 light-source interferences, ESD level 4, and burst ±4KV, staying stable in strong-light and strong-EM environments such as malls, hospitals, and airports. For contractors, this is a public-restroom basin faucet that "outputs accurately when it should, displays truthfully, and saves power for a long time."

### 1.1 Technical Positioning

| Type | Sensing Method | Output Interaction | Temperature Feedback | Representative Product |
|------|---------|---------|---------|---------|
| Traditional mechanical basin faucet | None | Hand-turn handle | None, by hand test | Ordinary faucet |
| Single-sensor IR faucet | Single IR | Hand-reach output | None | Early sensor faucet |
| **GIBO Dual-Sensor Display Faucet (G001)** | **Front+Side dual IR** | **Instant+Long dual mode** | **LED numeric real-time readout** | **WYJ-G001** |

### 1.2 Key Metrics

- Output response ≤0.6s (sense to water), close ≤1.0s (instant) / ≤1.5s (long)
- LED 2.5-digit white-light numeric display, e.g. 38°C; on while flowing, off when done
- Front sensing distance power-on auto-adaptive 20±2cm / 8±3cm, side fixed 7~10cm
- Complete-unit standby current ≤45μA, 4 AA batteries about 6~9 months
- Flow ≤6L/min, static burst pressure 2.5MPa/60s no leakage
- ESD level 4 (air ±15KV), burst ±4KV, EMI 3V/m normal operation

---

## II. Features

### 2.1 Front Sensor Instant Output—Water at Hand's Reach

When a hand or object enters the front sensing range, the faucet outputs water automatically, response ≤0.6s, with a red LED flash as prompt; the moment the hand leaves, water stops, close ≤1s. Continuous flow beyond 60±10s auto-closes to prevent someone leaving the water running.

### 2.2 Side Sensor Long-Flow—Wave to Switch

The side sensor head uses "sense once to open, sense again to close" long-flow logic, response also ≤0.6s, suited to filling containers, washing hair, or rinsing small items that need continuous flow; continuous flow beyond 180±10s auto-closes. The side sensor takes priority over the front; when both heads have signals, the side wins.

### 2.3 LED Numeric Readout—Temperature Visible

While flowing, the white-light 2.5-digit LED on the faucet lights up, directly showing the current outlet temperature (e.g. 38°C)—no need to test by hand. With adapter power, it displays on flow and goes dark when done; if a single use is under 30s, the screen stays on another 30s for easy reading; with battery power, it lights for 30s after flow then goes dark.

### 2.4 Mechanical Knob Temperature Control—Usable Even When Powered Down

The side mechanical knob, from front to back, is "cold water—mixed water—hot water—off," controlling both on/off and temperature. Even with dead batteries or power loss, the knob still delivers cold/mixed water manually—it never becomes a "dead weight when battery dies" ornament.

### 2.5 Power-On Auto-Adaptation—Ready Once Installed

On first power-on the LEDs light together and turn off after 1 second, completing auto-calibration to the basin environment; afterward re-powering requires an interval of more than 2 minutes from the previous power-on to ensure calibration validity. Keep the basin dry before adaptation—essentially no tuning needed.

### 2.6 Low-Voltage Reminder—Advance Warning to Change Batteries

When any sensor head senses a hand, if the battery voltage is measured at 4.5~4.7V, it first opens the solenoid and makes the LED flash quickly 5 times to remind of battery change; below 4.5V the solenoid stays closed and the LED flashes 10 times, avoiding running flat in front of a customer.

### 2.7 Power-Loss Protection and Anti-Interference—Stable Anywhere

If external power is suddenly cut, the solenoid closes immediately regardless of state—no continuous flow. The module passed waterproof tests of 24h water immersion and 0.5h boiling water with normal function, sensing-distance change under 10%; within 15~91cm, direct and oblique illumination from 6 light-source types (incandescent, fluorescent, halogen, bathroom heater, hairdryer, etc.) causes no false trigger.

---

## III. Core Selling Points

### Selling Point 1: Numeric Temperature Visible—Fewer Scalds and Misunderstandings

The most common complaint in public restrooms is "water too hot"—users can't see the temperature, get scalded reaching in, and either complain or misoperate. The G001 puts outlet temperature as an LED numeric display right on the faucet—38°C is 38°C—and the temperature knob with the readout can precisely stop at a comfortable range. For hotel, hospital, and school logistics, this small screen blocks scald complaints and "water suddenly hot/cold" disputes, with the most intuitive value in children's activity areas and elderly-care spaces.

### Selling Point 2: Dual Sensors, Two Logics—Full Scenario Coverage

Many single-sensor faucets can only output on reach or only wave to switch, awkward when "filling half a basin" or "hands full and can't free them." The G001 front sensor handles instant washing, the side sensor handles long filling—two logics in one faucet, with the side prioritized, no conflict. Per the specification, 4 Nanfu batteries at 30 short + 20 long sensing per day last 6~9 months—more carefree than frequently changed counterparts; a 50-unit public restroom saves more than half the annual ladder-climbing battery-change labor.

### Selling Point 3: Accurate Even in Strong Light and Strong EMI—No Fussy Install Location

At mall atriums, hospital corridors, and airport arrivals, lighting is mixed and equipment abundant, so ordinary IR sensing is easily dazzled into false action or failure. The G001 uses the Liteon Smart Sensing algorithm; the specification lists 6 light-source types within 15~91cm direct/oblique with no false trigger, ESD level 4 (air ±15KV), burst ±4KV normal operation. Engineering need not re-route wiring or reposition points to avoid strong lights, and the maintenance list handed to property managers is short.

---

## IV. Specification & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power Supply | DC 6V (4 AA dry batteries) / AC110V~220V to DC6V/1A adapter |
| Complete-Unit Consumption (standby current) | ≤45μA (at DC 6.0V) |
| Solenoid Parameters | DC 4.5V, pulse width 20ms |
| Usable Water Temperature Range | 4°C~60°C |
| Power-On Auto-Adaptation Interval | Re-power requires interval >2 min from first power-on |

### 4.2 Sensing Parameters

| Parameter | Specification |
|--------|------|
| Front Sensing Distance | Power-on auto-adaptive, for white paper 20±2cm / 8±3cm |
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

### 4.4 LED Display & Prompts

| Parameter | Specification |
|--------|------|
| Display Method | White SMD LED, 2.5-digit numeric, e.g. 38°C |
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
| Module Waterproof | Immersed in 25°C water 24h no seepage; boiled in water 0.5h function normal, distance change ≤10% |
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
4. Confirm power method (battery box or adapter); adapter needs a power point reserved.

### 5.2 Notes

- Always shut water and cut power before install/repair (remove battery box or unplug adapter).
- Use same-brand high-performance alkaline batteries; do not mix old and new.
- Do not hot-plug sensor module terminals.
- The side mechanical knob's range includes an "off" position; turn to off when unused to prevent accidental opening.

### 5.3 Installation Steps

1. Fix per faucet-body hole, connect cold/hot inlet pipes.
2. Connect the control module, lock the union (standard basin faucet fit).
3. Open water and pressure-test; confirm no leak.
4. Install battery box or connect DC6V adapter.
5. Power on: LEDs light together, turn off after ~1s, entering adaptation.
6. Wave in front of the sensor window to test front instant output and side long-flow.
7. Turn the mechanical knob to confirm cold/mixed/hot/off four positions, check LED numeric readout.

### 5.4 Power-On Self-Check

After power-on the LEDs light together and go dark after ~1s to complete adaptation; the first sense afterward flashes the red LED once to indicate trigger. To re-power for calibration, interval must exceed 2 minutes from previous power-on, and the basin must stay dry.

### 5.5 Battery Replacement

When voltage drops to 4.5~4.7V, each sense flashes the red LED 5 times to remind battery change; below 4.5V flashes 10 times and closes valve to stop work. Replacement: shut water → remove battery box → replace 4 same-brand new alkaline batteries → reinstall and re-power for adaptation.

---

## VI. Application Scenarios

### 6.1 Hotels / Clubs

Guest basins in rooms and public areas see high turnover; numeric temperature directly cuts "water too hot" complaints; dual sensors cover both hand-washing and filling; mechanical knob works even when powered down—stable experience.

### 6.2 Hospitals / Elderly-Care Institutions

The young, old, sick, and weak are sensitive to water temperature; the LED numeric readout lets attendants and patients see clearly before drawing water; low-voltage advance warning avoids failing in front of customers when flat.

### 6.3 Malls / Office Buildings

Atrium strong light and strong EMI near escalators—the G001's 6 light-source anti-interference and EMC metrics ensure stability; batteries changed every 6~9 months keeps property maintenance light.

### 6.4 Schools / Venues

Students running around and splashing—Liteon algorithm filters transient interference to reduce false triggers; timeout auto-close prevents continuous flow, saving water and worry.

### 6.5 Airports / Transport Hubs

24-hour operation, short maintenance windows—adapter permanent-power option avoids battery changes; wide pressure 0.05~1.0MPa adapts to old networks.

---

## Appendix

### A. Core Technology Index

| No. | Technology Name | Application in This Product |
|------|---------|---------------|
| #7 | Liteon Smart Sensing Technology | Dual IR sensor heads filter and debounce, filtering water-splash/noise false triggers |
| #6 | Low-Power Multi-Stable Agile Sensing Technology | Complete-unit standby ≤45μA, battery life 6~9 months |
| #4 | Capacitive Touch Technology | LED 2.5-digit numeric temperature display module |
| #11 | Dual-Mode Strong-Light-Immunity Anti-Interference Algorithm | 6 light-source types 15~91cm direct/oblique no false trigger |

### A.1 Related Patents (Granted)

| Technology Point | Patent Name | Patent No. | Type |
|--------|---------|--------|------|
| Dual-sensor output | A smart faucet with dual-sensor output | ZL 2018 2 0847903.7 | Utility Model |
| Display faucet | A sensor numeric-display faucet | ZL 2023 2 3354865.1 | Utility Model |

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

> This document is compiled based on the "WYJ-G001 LED Numeric Temperature-Display Basin Faucet Specification" (V1.0, 2020-11-21). Parameters are subject to the actual unit. GIBO reserves the final right of interpretation and modification of the technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
