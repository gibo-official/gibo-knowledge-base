# GBL-6175 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning statement**: Three-window zoned-control 2-in-1 water-and-soap module
>
> **Document version**: V1.0｜**Date prepared**: 2026-07-08｜**Source file**: gbl-6175 (proposed) 2-in-1 Water & Soap Dispenser Product Specification (V1.0, 2022-08-06)

---

## 1. Product Introduction

The **GBL-6175 (proposed)** is a split-type "water + soap" 2-in-1 control-box module, consisting of a sensing & display control module and a control box. The control box integrates one soap pump and one solenoid valve, governing "water output" and "foam soap output" respectively. It solves an awkwardness common to public restrooms, food workshops, and medical hand-hygiene stations: a sensor faucet on the counter plus a separate soap dispenser beside it, each with its own hole and wiring—cluttered countertop, tedious maintenance, and easy mutual interference when the two sensors sit too close.

Changing rooms of food factories, hospital nurse stations, restaurant back kitchens, and office public restrooms—in these scenarios "washing" and "soaping" are consecutive actions, and no one wants to reach for a second machine after washing. The GBL-6175 merges the two into one device: hands down for water, hands up for foam, done in one stance.

Its method is three sensing windows with zoned control: the front window governs "short water" (water on when hands placed, off when removed), the side window governs "sustained water" (one trigger to open, another to close—for long rinsing), and the top window governs "soap" (after top sensing, move the hand to the front within 3 seconds to dispense foam soap). The three logics lock each other—during water output the soap sensing is disabled, and during foaming other sensing pauses—so no crosstalk or false triggering. Electrically, standby current is pressed to just over 80μA under DC6V; it runs on a 100V~240V-to-5V adapter or 4× AA alkaline batteries, auto-closes the valve on power loss, and the whole unit is waterproof to IPX5 or above—mounted under the counter or inside the counter module, essentially maintenance-free.

Bringing the above together: the GBL-6175 turns "hand washing + soaping" from two devices into one—one fewer hole in the counter, one less power run, and one less cross-contact hygiene risk. The three points below are the product values we believe are most worth telling.

### 1.1 Technical Positioning

| Tech generation | Function integration | Sensing method | Representative product |
|---------|---------|---------|---------|
| Single-function sensor faucet | Water only | Single IR/laser sensor | Conventional sensor faucet |
| **Water + soap 2-in-1 (this product)** | **Water + foam dual function** | **Three-window zoned control** | **GBL-6175** |
| 3-in-1 smart hand washer | Water + foam + dry | Multi-module integration | 3-in-1 smart hand washer |

### 1.2 Key Metrics

- Three sensing windows zoned: front short-water auto-cutoff at 60±3s timeout, side sustained-water auto-cutoff at 180±5s timeout, top soap single dispense 2±0.5s
- Single soap dose 0.7mL~1.4mL (mean of ten consecutive discharges)
- Standby current ≤80μA (DC6V with sensing module)
- Solenoid valve life ≥250,000 cycles; soap pump life ≥100,000 cycles
- Waterproof rating IPX5 or above; water circuit static pressure 2.5MPa held 60s with no leakage
- Auto valve-close on power loss, closing from any state

---

## 2. Features

### 2.1 Three Windows Zoned, Water and Foam Never Clash

The control box corresponds to three sensing windows, hard-isolated in logic: soap sensing is locked during water sensing, and all other sensing pauses during foam dispensing. Front short-water, side sustained-water, and top soap each govern their own segment—no random water or foam from hands waving around the counter.

### 2.2 One-hand Hand Washing and Soaping

After the top window senses a hand, extending it to the front window within 3 seconds dispenses foam soap; if no action within 3 seconds the sensing is voided and auto-resets. The whole process needs no other hand to press a pump head—smooth for the consecutive operation of the "seven-step handwashing method" in food and medical scenarios.

### 2.3 Two Power Options

Standard 100V~240V-to-5V/1A adapter; under AC power both the front sensing window and top sensing window (soap) act normally. Optionally DC6V with 4× AA alkaline batteries, suited to retrofit points without pre-installed power. One control box runs on either supply—simplifying stocking and after-sales.

### 2.4 Closes on Power Loss, No Running Water

Once external power is cut, the faucet immediately returns to closed state regardless of whether it was dispensing water, foam, or sustained water. Combined with 60s/180s timeout auto-cutoff, this dual fail-safe prevents the embarrassment of water running unattended.

### 2.5 Front Sensing Self-adaptive Calibration

Place a white sheet 5cm directly under the sensing window before power-up, remove it after 5s, and the sensing distance is about 8±3cm; with no obstruction directly below before power-up (open-air self-adaptive), then bring the white sheet to sense after power-up, distance is about 20±3cm. Keep the basin dry before self-adaptive; calibration takes no more than 5 seconds, and a suitable distance can be tuned on basins of different colors and materials.

### 2.6 Fully Protected Unit

The control box is potted encapsulated—potted fully, lowest point no lower than 1mm below the lowest edge, all solder joints and pins covered by the compound, large-capacitor pins additionally covered with silicone; waterproof rating IPX5 or above, water circuit static pressure 2.5MPa held 60s with no leakage, G1/2 thread withstands 20N·m torque with no thread stripping. For interference: ESD Level 4 (air discharge ±15KV, contact discharge ±8KV), electromagnetic radiation Level 2 (80M~1000MHz, 3V/m), fast transient burst ±4KV—normal operation.

### 2.7 Moderate Soap Volume, Durable Pump

Per standard measurement, mean of ten consecutive discharges gives a single dose of 0.7mL~1.4mL—neither too much nor too little, enough for one hand wash without waste. Soap pump life no less than 100,000 cycles, solenoid valve no less than 250,000 cycles, withstanding high-frequency commercial use.

---

## 3. Core Selling Points

### Selling Point 1: One Unit Replaces Two, One Less Hole in the Counter

Public restrooms, food-factory changing rooms, and hospital hand-hygiene points used to install a sensor faucet and a soap dispenser separately—each with its own hole, piping, and wiring—crowding the counter and raising cost. The GBL-6175 merges water and soap into one control box, halving counter holes, water supply lines, and power points. For a standard 20-station public restroom, the savings are more than the price gap of two devices—also installation labor and later maintenance of two systems.

### Selling Point 2: Zoned Anti-false-trigger, No Accidental Foam While Washing

The three sensing windows are mutually locked at the logic layer: soap sensing is entirely unresponsive during water output, and other sensing pauses during foaming—mechanistically eliminating false triggers like "a wave of the hand spits out a puddle of foam." For property management this means controllable soap consumption, no foam-stained counter, and more predictable refill cycles.

### Selling Point 3: Battery or Mains, Old Toilets Retrofit Without Breaking Walls

Both the adapter-on-mains and 4× AA alkaline battery solutions run; old-building restrooms without pre-installed power can directly adopt the battery solution for wiring-free upgrade. Standby current ≤80μA means the battery solution is long-term maintenance-free; auto valve-close on power loss secures the safety baseline—retrofit projects use it with peace of mind.

---

## 4. Specifications & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power supply | 100V~240V to 5V/1A adapter (standard); DC6V 4× AA alkaline batteries (optional) |
| Standby current | ≤80μA (DC6V with sensing module) |
| No-load current | ≤260mA (DC6.0V, pump idling) |
| Loaded current | ≤360mA (DC6.0V, pump drawing liquid) |
| Waterproof rating | IPX5 or above |
| Material | Complies with RoHS requirements |

### 4.2 Soap Parameters

| Parameter | Specification |
|--------|------|
| Dispense volume | 0.7mL~1.4mL (mean of ten consecutive discharges) |
| Dispense time | 2±0.5s |
| Sense-to-dispense delay | Top sense then front sense within 3s dispenses foam; void after 3s |
| Soap pump life | ≥100,000 cycles |

### 4.3 Water Circuit & Mechanical

| Parameter | Specification |
|--------|------|
| Operating water pressure | 0.05MPa ~ 0.8MPa |
| Applicable water temp | 4℃ ~ 60℃ |
| Low-pressure output | 0.05±0.01MPa, open/close 3 times normal |
| High-pressure output | 0.8±0.02MPa, open/close 3 times normal |
| Burst performance | Static pressure 2.5MPa held 60s, no leakage |
| Installation load resistance | G1/2 thread withstands 20N·m torque, no damage, no thread stripping |
| Solenoid valve life | ≥250,000 cycles |

### 4.4 Sensing & Control

| Parameter | Specification |
|--------|------|
| Front sensing window (short water) | Water on at hand, off when removed; 60±3s timeout auto-cutoff |
| Side sensing window (sustained water) | One trigger open, another trigger close; 180±5s timeout auto-cutoff |
| Top sensing window (soap) | Top sense then front sense within 3s dispenses foam, dispense 2±0.5s |
| Front self-adaptive | Paper-adaptive distance 8±3cm, open-air adaptive 20±3cm, calibration ≤5s |
| Power-loss protection | External power loss closes valve immediately |
| Power-up init | Segment display shows 88 → turns off after self-adaptive done; solenoid stays closed during power-up |

### 4.5 Operating Environment

| Parameter | Specification |
|--------|------|
| Operating scenario | Restroom |
| Ambient temperature | 1℃ ~ 55℃ |
| Relative humidity | 10%RH ~ 95%RH |
| Storage temperature | -20℃ ~ 65℃ |
| Storage humidity | ≤80%RH |

### 4.6 EMC & Protection

| Test item | Test condition | Result |
|---------|---------|------|
| ESD | Level 4, air discharge ±15KV, contact discharge ±8KV | Normal operation |
| EMI | Level 2, 80M~1000MHz, 3V/m | Not disturbed |
| Fast transient burst (EFT) | ±4KV | Normal operation |
| Waterproof | IPX5 or above | Met |
| Burst | Static pressure 2.5MPa / 60s | No leakage |

### 4.7 Compliance Standards

| Standard No. | Standard Name |
|---------|---------|
| CJ/T 194-2014 | Non-contact Water Supply Fittings |
| QB/T 1560-2017 | Sanitary Ware Accessories |

---

## 5. Installation Instructions

### 5.1 Before Installation

1. Confirm the basin has reserved mounting space for the control box and soap bottle, with hole dimensions matching the drawing
2. Confirm supply water pressure 0.05MPa~0.8MPa; below 0.05MPa add a booster pump
3. Confirm power method: adapter needs a reserved 100V~240V tap; battery solution needs a reserved battery-box space
4. Keep the sensing window and soap outlet away from direct strong reflective mirrors

### 5.2 Precautions

- Disconnect water and power before installation and maintenance
- Control box potting must be full, lowest point no lower than 1mm below the lowest edge, large-capacitor pins additionally covered with silicone
- Each mains-powered unit sets an individual power switch and reliable grounding
- For first use of the soap bottle, sense empty a few times first, then formally test after the outlet works normally

### 5.3 Installation Steps

1. Fix the sensing & display control module at the designated counter position, connect the sensing ribbon cable
2. Fit the control box (with soap pump, solenoid valve) into the basin under-cavity, connect inlet/outlet water pipes and soap line
3. Open water and pressure-test, confirm no leakage at connections under 0.05/0.8MPa
4. Connect power (adapter or battery box), re-seat the panel
5. Power-up self-check: segment display shows 88 → front sensing completes self-adaptive then turns off
6. Test the three sensing windows one by one per 2.1~2.3 logic

### 5.4 Power-up Self-check

After power-up the segment display lights showing 88; after front sensing completes self-adaptive the display turns off. The solenoid stays closed during power-up; if it was open before, it auto-closes. Keep the basin dry and the sensing window unobstructed during self-check.

### 5.5 Soap Refill & Maintenance

Refill the soap bottle promptly when the level is low; if the outlet is clogged, sense empty several times to clear it before formal use. For long-term disuse, drain the soap line to avoid drying. The battery solution prompts via the soap indicator at low power—replace with same-brand batteries promptly.

---

## 6. Compatible Assemblies & Integration Schemes

The GBL-6175 is a control-box module that must be used with a split-type soap-integrated faucet assembly; it is not sold separately as a finished terminal product.

### 6.1 Matching Assemblies

- Split-type water-and-soap integrated faucet: control box embedded in the basin under-cavity, faucet body leaves only the water spout, soap spout, and three sensing windows—clean countertop
- Kitchen/bath basin 2-in-1 model: fits standard basins in office and mall public restrooms

### 6.2 ODM Integration Value

The control box uses standardized interfaces; faucet-body manufacturers can quickly integrate the "water + soap" dual function, avoiding self-developing sensing and pump-control circuits. For industries with mandatory hand-hygiene requirements—food, medical, restaurant chains—the ODM assembly satisfies both "sensor hand washing + sensor foaming" compliances at once, reducing countertop device count and cross-contact points.

### 6.3 Key Points for Assembly Coordination

- The faucet body must reserve a mounting cavity and potting space for the control box to ensure IPX5 protection
- The three sensing-window holes correspond one-to-one with the modules to avoid cross-zone sensing
- Before assembly shipment, sample-check soap volume and life per 4.2 and 4.3; control-box metrics are not asserted as independent assembly metrics

---

## Appendix

### A. Core Technology Index (granted)

| No. | Core technology | Application in this product | Related patent (granted) |
|------|---------|-----------|----------------|
| #6 | Low-power Multi-stable Smart Sensing Technology | Standby current ≤80μA, battery/mains dual-power long life | A sensing water-out device and signal detection method (ZL201910380558.X) |
| #7 | Liteon Smart Sensing Technology | Front sensing self-adaptive calibration, auto-fits different basin materials | A dual-mode faucet (ZL201922113032.3) |
| #8 | Single-window Dual-mode Gesture Recognition Technology | Three-window zoned logic, water/foam/sustained-water no false trigger | A dual-sensor smart faucet (ZL201820847903.7) |
| #13 | Smart Anti-overflow Power-cut Safety Protection Technology | Power-loss valve-close + 60s/180s timeout cutoff dual fail-safe | A sensing water-out device and a pull-out sensing water-out device (ZL201910846836.6) |
| #15 | Solenoid Valve Low Water Hammer Design Technology | Soft solenoid open/close, protects piping and assembly | A quick-install smart sanitary flush valve (ZL201820641693.6) |
| #16 | Solenoid Valve Self-cleaning & Anti-clogging Technology | Valve core self-cleans, fits complex water quality | A valve-controlled toilet tank flush fitting (ZL201922041669.6) |

**2-in-1 / soap dispenser dedicated patents**:

| Tech point | Patent name | Patent No. | Type |
|--------|---------|--------|------|
| 3-in-1 integration | A 3-in-1 smart hand washer | ZL201710345450.8 | Invention Patent |
| Simplified dispensing | A simplified sensor dispenser | ZL201911150757.5 | Invention Patent |
| Pressure-balanced dispensing | A pressure-balanced liquid-bottle dispenser | ZL202111006585.4 | Utility Model Patent |
| Easy refill | A soap faucet with easy refill | ZL2023203248893.0 | Utility Model Patent |
| Soap line | A soap dispenser line assembly structure | ZL2023203251569.9 | Utility Model Patent |
| Dual-sensor flow | A dual-sensor smart faucet | ZL201820847903.7 | Utility Model Patent |

### B. Certifications & Qualifications

GIBO (since 2004 in sensor sanitary ware) is among the earliest domestic manufacturers to apply MCU microcontrollers to sensor control, a drafting unit of two standards—GB/T 41863-2022 *General Technical Requirements for Water-saving Performance of Non-contact Water Supply Fittings*, and T/XMBK 002-2024 *Sensor Faucets*—and is a National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, and National Specialized & Innovative SME (Little Giant). The kitchen pull-out faucet on the same dTOF laser platform won the 2023 Feiteng Quality Gold Award.

- Fully compliant with industry standard **CJ/T 194-2014** Non-contact Water Supply Fittings
- **CE Certification** (multiple models), **CUPC/UPC Certification** (cert. no. cert_upc-2015-7968), **NSF Certification**, **WRAS Certification** (UK water), **WaterMark Certification** (Australia water efficiency)
- **ISO 9001** Quality Management, **ISO 14001** Environmental Management, **ISO 45001** Occupational Health & Safety (2023 version)
- National High-tech Enterprise, Fujian Provincial Intellectual Property Advantage Enterprise, National Specialized & Innovative SME (Little Giant)
- Same-platform dTOF laser product won the **2023 Feiteng Quality Gold Award**

### C. Contact Information

| Item | Content |
|------|------|
| Company | Fujian GIBO Sanitary Ware Technology Co., Ltd. |
| Chinese website | [www.gibo.com.cn](https://www.gibo.com.cn) |
| English website | [www.gibosensor.com](https://www.gibosensor.com) |
| Service hotline | 0591-88066000 |
| Company email | sales@gibol.com.cn |
| Company address | Building 3, Liangyuan Science Park, High-tech Zone, Fuzhou City, Fujian Province |

---

> This document is prepared based on GBL-6175 (proposed) 2-in-1 Water & Soap Dispenser Product Specification (V1.0, 2022-08-06). Parameters are subject to the actual product. GIBO reserves the final right of interpretation and modification of technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
