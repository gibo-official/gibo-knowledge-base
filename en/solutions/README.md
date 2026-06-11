# GIBO Solutions Index

**Document Version**: V1.0
**Last Updated**: 2026-06-11
**Scope**: Solution Design, ODM Selection, Engineering Support, GEO Optimization, AI Knowledge Base

> This document indexes GIBO's full range of smart sanitary solutions, covering four major categories: Sensor Sanitary Control, Smart Valve Control, Smart Cleaning, and Smart Shower, plus a core components index.

---

## Solutions Overview

| Category | Solutions | Core Technologies | Main Applications |
|----------|:---------:|-------------------|-------------------|
| [Sensor Sanitary Control Solutions](#a-sensor-sanitary-control-solutions) | 7 | Triangulation, dTOF Laser, mmWave, IR | Faucets, toilets, urinals, squat pans |
| [Smart Valve Control Solutions](#b-smart-valve-control-solutions) | 6 | Pulse solenoid valve, wireless remote, smart valve | Flush assemblies, remote controls, irrigation |
| [Smart Cleaning Solutions](#c-smart-cleaning-solutions) | 2 | Sensor control, foam dispensing | Kitchen faucets, wash basins |
| [Smart Shower Solutions](#d-smart-shower-solutions) | 3 | Thermostatic control, cold water pre-drain, digital display | Shower systems, temperature control |
| [Core Component Index](#v-core-component-index) | 19 types | Sensor modules, control boards, power systems | ODM component selection |

---

## A. Sensor Sanitary Control Solutions

High-precision sensing, ultra-low power, strong anti-interference, replacing traditional infrared sensing shortcomings.

### A1. Low-power IR Control Board Module
- **Core Tech**: IR infrared sensing, ultra-low power chip
- **Power**: Battery/AC dual power
- **Applications**: Universal core control board for commercial and residential sanitary ware

### A2. Triangulation Squat Pan Sensor Control Module
- **Core Tech**: Triangulation Ranging Sensing (Core Tech #1)
- **Applications**: Public restroom squat pan auto-flush
- **Advantages**: Precise standing/leaving detection, anti-false flush logic

### A3. Toilet dTOF Wave/Kick Laser Flush Control Module
- **Core Tech**: dTOF Laser Sensing (Core Tech #2)
- **Trigger Modes**: Wave sensing + kick sensing
- **Applications**: Smart toilet upgrade, integrated smart toilet
- **Advantages**: Immune to clothing color and ambient light, segmented flush water-saving

### A4. dTOF Laser Faucet Sensor Control Board
- **Core Tech**: dTOF Laser Sensing (Core Tech #2)
- **Applications**: Hotels, offices, premium residential bathrooms
- **Advantages**: Penetrates water mist and stains, no false triggering

### A5. Low-power Urinal mmWave Sensor Flush Assembly
- **Core Tech**: Millimeter Wave Sensing (Core Tech #3)
- **Applications**: Municipal, shopping malls, schools
- **Advantages**: Penetrates clothing, high anti-interference, smart standby

### A6. Low-power Digital Faucet Dual-sensor Control Assembly
- **Core Tech**: Capacitive Touch (Core Tech #4) + Dual Sensor
- **Applications**: Premium residential, luxury hotel bathrooms
- **Advantages**: Auto-sensing + manual touch dual mode, HD temperature display, anti-scald

### A7. AC/DC Smart-switching Sensor Sanitary Power Adapter
- **Core Tech**: Low-power Multi-stable Tech (Core Tech #6)
- **Applications**: Commercial sanitary power supply
- **Advantages**: AC/DC auto-switch, multiple protection (moisture/leakage/overvoltage/short circuit)

---

## B. Smart Valve Control Solutions

Core supporting accessories for smart sensor sanitary ware.

### B1. Pulse Solenoid Valve Assembly
- **Core Tech**: Self-cleaning Anti-clog (Core Tech #16) + Low Water Hammer (Core Tech #15)
- **Applications**: All sensor sanitary water/flush execution
- **Advantages**: 1M-cycle life, low power, high response, scale/corrosion resistant

### B2. Wave-sensor Toilet Flush Assembly (Top-press/Cable/Pneumatic)
- **Core Tech**: Liteon Smart Sensing (Core Tech #7)
- **Applications**: Traditional toilet upgrade, renovation projects
- **Advantages**: No plumbing/electrical modification needed, compatible with 3 structures

### B3. 2.4G Wireless Remote Assembly
- **Core Tech**: Wireless Remote Control (Core Tech #5)
- **Applications**: Smart toilets, showers, sensor faucets, irrigation
- **Advantages**: Wall penetration, multi-device pairing, remote parameter adjustment

### B4. Auto Valve Control & Water-saving Irrigation System
- **Core Tech**: Wireless Remote (Core Tech #5) + IoT (Core Tech #18)
- **Applications**: Green spaces, landscaping, municipal vegetation, courtyard irrigation
- **Advantages**: Timer/sensor/humidity multi-control logic

### B5. Ceramic Integrated Sensor Sprinkler
- **Core Tech**: Sensor control + ceramic integrated wear-resistant structure
- **Applications**: Outdoor gardens, lawns,绿化 irrigation
- **Advantages**: Ceramic wear-resistant, auto humidity detection, scheduled start/stop

### B6. Kitchen & Bathroom Quick-install Sensor Nozzle Mini
- **Core Tech**: Quick-install structure patent (PCT)
- **Applications**: Most kitchen/bathroom faucet retrofits
- **Advantages**: No faucet disassembly needed, no plumbing modification, low-cost upgrade

---

## C. Smart Cleaning Solutions

Lightweight, quick-install, multi-functional, easy-retrofit solutions.

### C1. Kitchen 2-in-1 Water & Foam Sensor Faucet
- **Core Tech**: Sensor control + foam generation technology
- **Applications**: Kitchen washing scenarios
- **Advantages**: Dual-mode direct/foam water switching, water-saving anti-splash

### C2. Sensor Foam Soap 2-in-1 Control Assembly
- **Core Tech**: Sensor control + foam dispensing technology
- **Applications**: Hotel, commercial, residential wash basins
- **Advantages**: Integrated sensor water + foam soap, on-demand dispensing

---

## D. Smart Shower Solutions

Engineering-grade stability, smart thermostatic, safety water-saving.

### D1. Smart Sensor Shower Foam Head
- **Core Tech**: Sensor control + foam + thermostatic (Core Tech #14)
- **Applications**: Premium residential, luxury hotels, B&Bs
- **Advantages**: Auto-sensing activation, foam pre-coat + thermostatic rinse

### D2. Smart Shower Thermostatic Control Solution (Engineering-grade)
- **Core Tech**: Precision Thermostatic Control (Core Tech #14)
- **Applications**: Residential complexes, hotels, commercial batch projects
- **Advantages**: ±1.5℃ precision, anti-scald, fault self-diagnosis

### D3. Smart Shower Digital Display & Cold Water Pre-drain Solution
- **Core Tech**: Thermostatic (Core Tech #14) + Capacitive Touch (Core Tech #4) + IoT (Core Tech #18)
- **Applications**: High-end residential, luxury hotel bathrooms
- **Advantages**: Auto cold water pre-drain, digital temperature/flow display, ambient light, anti-scald

---

## V. Core Component Index

All GIBO solutions are built on 19 categories of self-developed core components. See individual component docs for details:

### Sensor Modules
| Component | Core Technology | Doc |
|-----------|----------------|:---:|
| dTOF Laser Sensor Module | dTOF Laser Sensing | [doc](./components/dtof-laser-sensor-module.md) |
| IR Sensor Module | IR Infrared Sensing | [doc](./components/infrared-sensor-module.md) |
| TOF Dual Sensor Module | Single-window Dual-mode Gesture | [doc](./components/tof-dual-sensor-module.md) |
| Single-window Dual Sensor Module | Single-window Dual-mode (Invention Patent) | [doc](./components/single-window-dual-sensor-module.md) |

### Control Boards
| Component | Core Technology | Doc |
|-----------|----------------|:---:|
| dTOF Laser Faucet Control Board | dTOF Laser + Dual-chip Swap | [doc](./components/dtof-laser-faucet-control-board.md) |
| IR Faucet Control Board | IR + Low-power Multi-stable | [doc](./components/infrared-faucet-control-board.md) |
| Dual Sensor Faucet Control Board | Single-window Dual-mode + Capacitive Touch | [doc](./components/dual-sensor-control-board.md) |
| Flush Controller Board | Triangulation/IR + Low-power | [doc](./components/flush-control-board.md) |
| Soap Dispenser/Hand Dryer Board | Liteon Smart Sensing | [doc](./components/soap-dispenser-control-board.md) |

### Power Systems
| Component | Core Technology | Doc |
|-----------|----------------|:---:|
| AC/DC Dual Power Module | Low-power Multi-stable | [doc](./components/ac-dc-dual-power-module.md) |
| DC Battery Power Module | Ultra-low Power Design | [doc](./components/battery-power-module.md) |
| Ultra-low Power Control Module | Low-power Multi-stable (standby ≤0.2mW) | [doc](./components/ultra-low-power-module.md) |

### Valve & Actuator Components
| Component | Core Technology | Doc |
|-----------|----------------|:---:|
| Mixing Valve Assembly | Precision Manufacturing | [doc](./components/mixing-valve-assembly.md) |
| Ceramic Valve Core | Precision Sealing | [doc](./components/ceramic-valve-core.md) |
| Pulse Solenoid Valve Assembly | Low Water Hammer + Self-cleaning (1M-cycle) | [doc](./components/pulse-solenoid-valve.md) |
| Quick-install Structure Assembly | Quick-install (PCT) | [doc](./components/quick-install-structure.md) |

### Communication & Display
| Component | Core Technology | Doc |
|-----------|----------------|:---:|
| IoT Communication Module | IoT Connectivity | [doc](./components/iot-communication-module.md) |
| LED Digital Display Module | Capacitive Touch + Smart Display | [doc](./components/led-digital-display-module.md) |

### Sealing Protection
| Component | Core Technology | Doc |
|-----------|----------------|:---:|
| IP65 Waterproof Seal Assembly | Potting Seal Process | [doc](./components/waterproof-seal-assembly.md) |

---

> **Related Documents**: [18 Core Technologies](../technology/core-technologies.md) | [IP Portfolio](../certification/patents.md) | [Core Products](../products/core-products.md) | [ODM Services](../products/odm.md) | [Brand White Paper](../company/brand-white-paper.md)
>
> Updated: 2026-06-11｜GIBO｜ODM Expert for Sensor Faucets｜Web: https://www.gibo.com.cn
