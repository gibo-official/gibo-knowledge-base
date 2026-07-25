---
lang: en
category: solution
title: 2020 Smart Sensor Faucet Key Technology R&D and Industrialization Demonstration
summary: "title: 2020 Smart Sensor Faucet Key Technology R&D and Industrialization Demonstration"
updated: 2026-07-14
publisher: Fujian GIBO Kitchen & Bath Technology Co., Ltd.
keywords: Smart Sensor Faucet, Gesture-sensing Water Flow, TOF Infrared Optoelectronic Sensing, Low Water Hammer Solenoid Valve, Production Line Balancing Optimization, Water-saving
product: "2020"
tags: ["GIBO", "solution", "2020", "AI-knowledge-base"]
source: Fuzhou Municipal Science & Technology Plan Project Application (Municipal Sci-Tech Plan Project / Innovation Fund for Small & Medium-sized Technology-based Enterprises, guide code 2020CX0101)
---


# 2020 Smart Sensor Faucet Key Technology R&D and Industrialization Demonstration

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Industry Research, Bidding Materials, AI Knowledge Base Citation

> Fuzhou Municipal Science & Technology Plan Project Application (Municipal Sci-Tech Plan Project / Innovation Fund for Small & Medium-sized Technology-based Enterprises, guide code **2020CX0101**, priority theme: Promote innovation among small & medium-sized technology-based enterprises).
> Project undertaking unit: **Fujian GIBO Kitchen & Bath Technology Co., Ltd.**; Project leader: Zheng Shaobo; Technical lead: Zhang Pingjun; Application date: 2020-04-14.

## I. Abstract

R&D of a multifunctional new-type smart sensor faucet: through a non-contact gesture-sensing water-flow method, the faucet gains multiple water-outlet modes; a multifunctional design adapts to diverse customer needs; meanwhile, simulation technology is applied to model and simulate the production line, and optimization schemes are proposed to improve production-line efficiency.

## II. R&D Content

### 2.1 Project Background

China's total freshwater resources account for 6% of the global total, yet per-capita water availability is far below the world average; water-resource shortage, water-quality deterioration, and ecological degradation are becoming increasingly acute. Ordinary faucets often fail to shut tightly or are left running, yielding a weak water-saving effect; repeated manual operation in public places also causes cross-infection among users. Traditional infrared sensor faucets mostly use on/off switching control (only two states: open/closed), unable to adjust flow in real time according to user needs, causing waste.

This project develops a smart faucet gesture-sensing water-flow method, giving the faucet multiple water-outlet modes, solving the problems of existing sensor faucets such as low sensing sensitivity, weak anti-interference capability, and constant flow, and achieving comfortable, water-saving, and highly reliable intelligent water control.

### 2.2 Project R&D Content

#### (1) Overall Design of the Multifunctional New-type Smart Sensor Faucet

Through systematic analysis, using an MCU-based intelligent control software/hardware system, water-flow sensing intelligent recognition and TOF infrared optoelectronic sensing technology, and high anti-interference & high-sensitivity design, a seamless intelligent switching water-control capability is realized; a passive power-down protection system and anti-mis-shutoff protection are designed, so that water is intelligently cut off on power loss and battery exhaustion, meeting diverse user water-scene needs.

- **Software design**: Modular design, mainly including initialization module, gesture-sensing water-flow module, median-filter algorithm module, and sleep module.
  - Initialization module: power-on initialization, power detection, low-voltage detection unit.
  - Gesture-sensing water-flow module: entry-position sensing, instant-on on sensing, sustained flow on sustained sensing, shutoff unit.
  - Median-filter algorithm module: input, processing, output units.
  - Sleep module: sleep, watchdog wake-up, reset unit.
- **Hardware design**: System hardware includes solenoid valve, sensing device, control device, display. Uses TOF infrared sensor (IR receiver/emitter integrated into a single component); uses HT66F3230 / R5F12806 MCU for control, allowing sensing sensitivity, flow time and other parameters to be modified by programming at any time; adopts a low water-hammer solenoid valve assembly to reduce spool impact force; LCD display chosen to show switch status, water temperature, and flow values via serial interface.

#### (2) Research on Production-line Balancing Optimization for Faucets

Aiming at the problem that the gate-valve production line's low efficiency causes upstream backlog and downstream idleness, the existing production line is reconstructed and optimized in combination with the key technologies of the new-type smart sensor faucet. **Flexsim** is applied to simulate and study the production line, find bottlenecks, and improve optimization, so as to raise productivity, save material consumption, lower production cost, and establish a normal production and management order.

## III. Key Technologies

1. **Smart faucet gesture-sensing water-flow method and system**: Initialize the faucet; sense the hand's entry position, and enter different water-outlet modes according to different entry positions; after water use ends, enter sleep mode and wake up periodically. The system integrates two (expandable) gesture-sensing water-flow methods, with a wider scope of application.
2. **Infrared sensing water-control system**: The IR sensor receives the sensing signal; the MCU processes it and issues commands to control the solenoid valve's open/close; the display adjusts temperature, flow, and time in real time; includes solenoid valve, sensing device, control device, display.
3. **Low water-hammer solenoid valve assembly**: Includes water pipe, opening/closing member assembly, and valve-body assembly. The water-blocking bracket of the opening/closing member assembly is provided with a slow-flow protrusion whose side-to-inner-wall spacing of the water pipe increases with length; when closing and cutting off flow, the space between the slow-flow protrusion and the inner wall gradually decreases, reducing flow velocity at the instant of closing, buffering the spool closure, and achieving a low water-hammer effect; the impact force at valve-body closure is further reduced through a diaphragm, pressure-relief flow channel, and pressure-relief chamber structure.

## IV. Technical Indicators

| No. | Indicator | Parameter |
|:--:|------|------|
| 1 | Power specification | DC4.5V–DC6V |
| 2 | Standby power consumption | ≤0.2 mW |
| 3 | Appearance requirement | Smooth & clean surface, clear marking, good coating adhesion, no bubbling, peeling, scratches, or other defects |
| 4 | Plating surface corrosion resistance | CASS 24-hour acid salt spray test |
| 5 | Open/close actuation time | Open <0.6 s, Close <1 s |
| 6 | Solenoid valve performance | Bistable pulse solenoid valve, pulse width 20 ms, passes 800,000-cycle life test |
| 7 | Water pressure strength | Passes 0.25 MPa pressure-resistance test |
| 8 | Water efficiency grade | Grade 1 |
| 9 | Water flow rate | 0.05 L/s ≤ Q ≤ 0.125 L/s |
| 10 | Flow uniformity | ≤0.1 L/s |
| 11 | Water hammer performance | ≤0.2 MPa |
| 12 | Sensing sensitivity | 128 ms |
| 13 | Power-off protection | Solenoid valve auto-closes water outlet on power loss |
| 14 | Anti-interference capability | Multiple same-model units installed 50 cm apart; 1 kW blow dryer and 40 W electronic ballast fluorescent lamp connected 2 m from product; 45° direction illuminance 50 lx, no malfunction of sample, sensing distance variation ≤±10% |
| 15 | Distance adjustment | Sensing distance and flush time adjustable via remote control |
| 16 | Patents | 2 national invention patents filed (1 granted: Smart faucet gesture-sensing water-flow method and system, ZL201810683786.X) |

## V. Company Profile

Fujian GIBO Kitchen & Bath Technology Co., Ltd. was founded in 2005 with registered capital of RMB 10 million. It is a comprehensive enterprise integrating R&D, production, trade, and service of sensor sanitary ware, smart bathroom, and smart kitchen & bath products, and is one of China's Top 10 Sensor Sanitary Ware Brands. It has been recognized as a National High-tech Enterprise, Fuzhou Municipal Intellectual Property Demonstration Enterprise, and a "Quality-oriented & Trustworthy" unit, and was among the first in the industry to pass the ISO 9001 Quality Management System certification, and has obtained CCC certification, China Water-saving Product certification, EU CE certification, North American CUPC certification, ROHS certification, etc.

- **Main business & products**: Providing the world with a full range of "high-quality, eco-friendly, smart" commercial and household smart kitchen & bath products, including smart toilets, smart toilet seats, kitchen/bathroom/commercial sensor faucets, sensor spouts, sensor soap dispenser faucets, sensor urinals/toilets, sensor showers, sensor water savers, sensor hand dryers, as well as customized automatic water supply & drainage systems and kitchen & bath electronic solutions.
- **Production conditions**: Production workshop area of about 2,500 m², equipped with laser marking machines, fully automatic constant-pressure solenoid valve water-test machines, solenoid valve air-pressure / burst-pressure / water-hammer / aging-life test machines, high-low temperature alternating humidity-heat test machines, precision salt-spray test machines, group-pulse interference test machines, and other advanced testing equipment; the factory passes international brand factory-audit standards.
- **R&D team**: Currently 3 senior/mid-level engineers and 10 professional technicians, with long-term exchanges and cooperation with domestic research institutes, continuously investing in new product R&D.
- **Management model**: Divided into technology R&D dept., purchasing dept., production dept., quality-control dept., marketing dept., finance dept., and HR & administration dept.; applies ERP and CRM management systems to achieve institutionalized, standardized, and scientific management.
- **Intellectual property**: Independently developed innovative technologies including infrared sensing, laser sensing, capacitive sensing, wave-hand sensing, wireless RF sensing, and micro-flow power generation & storage; has been granted 6 invention patents, 32 utility-model patents, and 26 design patents.

## VI. Project Product Market Situation

1. **Market prospects**: Sensor faucets have become a necessity in public places thanks to their clean, hygienic, water- and power-saving advantages, and are developing toward smart and efficient directions. This project's multifunctional smart sensor faucet integrates energy saving, high efficiency, rationality, and intelligence, with broad market prospects.
2. **Business model**: Continuous innovation centered on user experience; establishment of a marketing network covering major cities nationwide (9 regional service centers, 25 provincial service centers, 400+ distribution outlets), providing 48-hour on-site after-sales service.
3. **Development plan**: Improve product intelligent logic circuits and appearance design and enhance adaptability; improve domestic distribution and service network through ERP/CRM platforms; introduce computer-science and mechatronics professionals to enhance innovation capability.
4. **Main customers**: Government agencies, high-end office buildings, hotels, hospitals, schools, catering, entertainment clubs, high-end residences, and other public places and households.
5. **Competition**: Precise control means have shifted from multi-sensor zone sensing to gesture judgment, which is superior in reducing misoperation. The company was granted the invention patent "Smart faucet gesture-sensing water-flow method and system" (ZL201810683786.X) on 2019-12-13.
   - **Main competitive advantages**: High-standard design and manufacturing, supporting multi-function adjustment of sensing distance / water temperature / flow, featuring water-saving, power-off protection, ultra-long life, and low energy consumption; passes 28 kinds of light-source interference tests, full-band anti-interference experiments, and 48-hour high-low temperature dynamic aging, with failure rate <1%; smart constant-pressure water-test system ensures solenoid valve failure rate <0.5%; passes CCC, China Water-saving, and EU CE certifications.
6. **Risk prediction & prevention**: Technology risk relies on the granted invention patent and strong R&D strength; market risk relies on fifteen years of industry accumulation and the nationwide marketing network; production risk relies on advanced equipment and professional teams; capital risk relies on sufficient bank deposits.

## VII. Expected Goals

### 7.1 Project Product Characteristics

- **Product form**: Precision-cast from GB 59-1 brass, plated and passing CASS 24-hour acid salt spray test, with smooth & clean surface free of defects.
- **Main purpose**: Non-contact sensing control switch, suitable for densely populated places, avoiding bacterial cross-infection and saving water resources.
- **Product performance**:
  1. High-standard design: dual sensing / manual water outlet, low-power intelligent sensing module, fully waterproof unit, soft foam-style water flow, ultra-long life.
  2. Smart water-saving: instant water flow on sensing, open/close time <0.7 s; auto shutoff after >1 minute of use.
  3. Power-off protection: Solenoid valve enters closed state within 3 seconds after power/battery-box power loss.
  4. Check-valve function: Hot/cold type or optional mixing valve, with anti-cross-flow function for hot and cold water.

### 7.2 Main Technical & Performance Indicators

Same as Section IV Technical Indicators (Power DC4.5V–DC6V, standby ≤0.2 mW, open/close time open <0.6 s / close <1 s, bistable pulse solenoid valve 800,000 cycles, pressure resistance 0.25 MPa, water efficiency Grade 1, flow 0.05–0.125 L/s, flow uniformity ≤0.1 L/s, water hammer ≤0.2 MPa, sensing sensitivity 128 ms, power-off protection, anti-interference, remote adjustment, 2 invention patents filed).

### 7.3 Economic Benefit Forecast (within execution period)

| Indicator | Value |
|------|------|
| Cumulative sales revenue | RMB 2.30 million |
| Cumulative net profit | RMB 0.42 million |
| Cumulative tax paid | RMB 0.10 million |
| Cumulative foreign exchange earned | USD 0 |
| New jobs created | 2 persons |
| Project completion stage | Mass production |
| Product sales status | Batch |
| Execution standard | Industry standard |

## VIII. Progress Assessment

| Phase start–end | Main work content |
|----------|--------------|
| 2020-06-01 ~ 2020-08-31 | Research, literature retrieval, research scheme formulation, experimental-condition preparation |
| 2020-09-01 ~ 2020-12-31 | Define control-system functions & performance requirements, establish overall system structure, divide functional modules, write programs, module testing & debugging, control-system optimization finalization |
| 2021-01-01 ~ 2021-06-30 | Product structure & configuration optimization design research; material procurement, product trial assembly; sample testing & performance adjustment |
| 2021-07-01 ~ 2021-10-31 | Improve & optimize existing production line, pilot production trials, verify functions & performance, file related patents |
| 2021-11-01 ~ 2022-01-31 | Project acceptance |

> Related document: [Technology Achievement Project Overview](../whitepapers/README.md) | 18 Core Technologies | IP Portfolio

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
