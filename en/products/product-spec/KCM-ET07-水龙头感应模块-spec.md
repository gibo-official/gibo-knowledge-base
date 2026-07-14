# KCM-ET07-水龙头感应模块 Product Specification

**Document Version**: V1.0
**Last Updated**: 2026-07-14
**Applicable Scope**: Product Showcase, Bidding Materials, Industry Research, AI Knowledge Base Citation

> **Positioning Statement**: A faucet sensor module with remote distance adjustment.
>

---

## I. Product Introduction

The **KCM-ET07** is a sensor control module that GIBO builds for basin and kitchen faucets. Carrying the U840_20230728 main control board, when a hand reaches the solenoid opens and when it withdraws it closes—fully non-contact. It is mainly sold to complete-unit makers and contractors: a faucet maker drops this module into a basin faucet to make a sensor faucet, into a urinal flusher to make a sensor flusher, and it works directly for an instant-heating faucet. It solves the most common headache of IR sensor faucets on the engineering site—rigid sensing distance: installed in different faucet structures it is either too sensitive and false-triggers or too dull and won't output, and used to require opening the panel to adjust.

This module ships in default faucet mode with default farthest sensing distance, but the distance can be adjusted on-site from 5~35cm with the standard wireless remote, one step per press; at the limit the LED flashes 3 times as prompt. A veteran can set it standing in front of the faucet—no panel opening, no pre-embedded box. Standby power held at ≤0.2mW; powered by either DC6V 4 alkaline batteries or an AC110~220V-to-6V1A adapter, no power worry for a year once installed.

What complete-unit makers find most cost-effective is "one module fits many faucets": the 26cm factory distance suits most countertop basins; for a small countertop or narrow sink, just retract a few steps by remote—no separate module version per structure. Power-loss keeps valve closed, continuous sensing 60s auto-closes water, and voltage below 4.8V reminds of battery change—all protections built in. The three points below are the product values we think most worth taking out.

### 1.1 Technical Positioning

| Generation | Sensing Principle | Distance Adjust | Fit Method | Representative Product |
|---------|---------|---------|---------|---------|
| Gen 1 | IR reflection intensity | Non-adjustable | Single structure | Early sensor faucet |
| Gen 2 | IR triangular ranging | Limited adjust | Per-structure fit | GBL-8300AD |
| **ET07 (remote-adjustable sensing)** | **Smart sensing + wireless remote distance adjust** | **5~35cm remote step adjust** | **Multi-structure universal** | **KCM-ET07** |

### 1.2 Key Metrics

- Factory sensing distance 26cm±10% (29.7×29.7cm standard white board), remote adjustable range 5~35cm
- Static power ≤0.2mW, powered DC6V (4 alkaline batteries) / AC110~220V to 6V1A
- Open ≤1s, close ≤1.5s, faucet response time ≤512ms
- ESD level 4 (air discharge +15KV / contact ±8KV), fast burst level 4, EMI level 3 3V/m
- Module immersed 20cm / 4h no fogging, boiled in 70°C water 0.5h function normal; 6 light sources 15~91cm direct/oblique no false action
- Continuous sensing 60s±10% auto-close; under-voltage <4.8V flash 5 times, <4.5V flash 10 times close valve

---

## II. Features

### 2.1 Power-On Self-Check, 1-Minute Learning

On power-on the LED blinks once and the solenoid opens then immediately closes; within the next 1 minute sensing makes the LED stay lit and enters learning mode, switching to normal standby after 1 minute. During learning the module self-adapts the environmental baseline—usable once installed, no manual calibration.

### 2.2 Remote Distance Adjust, No Panel Opening

In faucet mode, use the standard wireless remote's distance +/- keys, one step per press; the module lights 0.5s on receiving the remote signal, and at the limit the LED flashes 3 times as prompt. Retract a bit for small countertops, extend for large—set while standing in front of the faucet.

### 2.3 Open on Approach, Close on Leave

Entering the sensing range opens the solenoid with the LED flashing once on valve-open; leaving the range closes the solenoid. The action is crisp, no dithering.

### 2.4 Extremely Low Static Power

Complete-unit standby power ≤0.2mW, a fraction of comparable IR modules; battery-version faucets need no battery change for over a year.

### 2.5 Multiple Power-Loss Protections

On power interruption the solenoid stays closed; continuous sensing beyond 60s±10% auto-closes water; below 4.8V each sensing makes the LED flash 5 times as reminder, below 4.5V flashes 10 times and closes the valve to stop work—property can intervene in time.

### 2.6 Six Light Sources No False Trigger

A 40W incandescent, T8-58W fluorescent, 50W halogen, electronic-ballast daylight, bathroom heater, and a combination of 1000W hairdryer + 40W daylight on the same outlet—at 15~91cm direct or oblique—none cause the module to false-act.

### 2.7 Water Immersion and Boiling Fear Nothing

The sensing window and potted part immersed 20cm deep for 4 hours show no water droplets or fogging and function normally; placed in 70°C boiling water for 0.5h then cooled to room temperature, the sensing window still shows no droplets or fogging and functions normally. Usable in high-humidity steam environments.

---

## III. Core Selling Points

### Selling Point 1: Remote Distance Adjust, No On-Site Disassembly—5~35cm per Structure, Flash 3 Times at Limit

IR sensor faucets most easily fail on the engineering site: the same module in a deep and a shallow basin gives one too-sensitive and one too-dull distance; the traditional fix was opening the panel to change parameters. The ET07 uses wireless remote to extend the distance from 5cm to 35cm on-site, one step at a time, flashing 3 times at the end to tell the worker "reached the limit." One module version covers countertop basins, kitchen sinks, and urinals—easier stocking and after-sales; contractors adjust after install without returning to factory.

### Selling Point 2: Ultra-Low Standby, One Battery Change a Year—Standby ≤0.2mW, 4 Batteries Over a Year

The module's static power is ≤0.2mW, about 33μA at 6V supply; estimating from 4 AA alkaline batteries at ~2400mAh, pure standby theoretically lasts about 8 years, and counting dozens of valve-open actions daily, one faucet changing batteries once a year is easily enough. For a 50-station mall, if devices changed batteries monthly, that is 20-plus man-hours a year just climbing ladders; the ET07 once a year makes that labor essentially zero.

### Selling Point 3: Six Strong Light Sources Immune, Stable Anywhere—ESD Air 15KV, Burst Level 4, Complex Environment Normal

The module passes ESD level 4 (air discharge +15KV, contact ±8KV), fast transient burst level 4, and EMI level 3 (80M~1000MHz, 3V/m), working normally beside mall escalators, variable-frequency AC, and near LED screens. Paired with six-light-source non-false-trigger, it withstands "sensing dead zones" like under mirror-front lights, directly below bathroom heaters, and by windows—complete-unit makers bidding commercial projects need basically no extra anti-interference remediation.

---

## IV. Specification & Performance Parameters

### 4.1 Electrical Parameters

| Parameter | Specification |
|--------|------|
| Power Spec | DC6V (4 alkaline dry batteries) / AC110V~220V to 6V1A switching power adapter |
| Main Control Board | U840_20230728 |
| Static Power | ≤ 0.2mW |
| Output Pulse Width | 30mS |
| Response Time | Faucet ≤ 512mS |
| LED Indicator | Red |

### 4.2 Sensing Performance

| Parameter | Specification |
|--------|------|
| Factory Sensing Distance | 26cm ±10% (for 29.7×29.7cm standard white board) |
| Sensing Distance Adjustable Range | 5~35cm (for 29.7×29.7cm standard white board, remote step adjust) |
| Open / Close Time | ≤1s / ≤1.5s (connected to conventional faucet solenoid water path) |
| Timed Close | Continuous sensing 60s±10% auto-close |
| Remote Function | Distance +/- keys step adjust; lights 0.5s on signal, flashes 3 times at limit |

### 4.3 Power & Protection

| Parameter | Specification |
|--------|------|
| Power-Loss Protection | Solenoid stays closed when power interrupted |
| Under-Voltage Protection (>4.8V) | Each sensing LED flashes 5 times, 1.5s interval, solenoid still works |
| Under-Voltage Protection (<4.5V) | Each sensing LED flashes 10 times, 0.5s interval, module closes valve and stops work |
| Static Power | ≤ 0.2mW |

### 4.4 EMC & Protection

| Test Item | Test Standard / Condition | Result |
|---------|---------------|------|
| ESD | Level 4, air discharge +15KV, contact ±8KV | Normal operation |
| EMI | Level 3, 80MHz~1000MHz, 3V/m | Not disturbed |
| Fast Transient Burst (EFT) | Level 4 | Normal operation |
| Module Waterproof | Sensing window immersed 20cm / 4h | No seepage, no fogging |
| Module Waterproof | Boiled in 70°C water 0.5h, cooled to room temp | Normal function |
| Light Interference | 6 light sources 15~91cm direct / oblique | No false trigger |

### 4.5 Operating & Storage Environment

| Parameter | Specification |
|--------|------|
| Working Scenario | Kitchen/bath space |
| Operating Ambient Temperature | 5°C ~ 50°C |
| Operating Humidity | 10%RH ~ 95%RH |
| Working Water Pressure | 0.05MPa ~ 0.8MPa |
| Storage Temperature | -10°C ~ 55°C |
| Storage Humidity | ≤ 95%RH |

### 4.6 Applicable Standards

| Standard No. | Standard Name |
|---------|---------|
| CJ/T 194-2014 | Non-contact Water Supply Fixtures |
| GB/T 4798.1 | Environmental Conditions for Electric and Electronic Products — Part 1: Storage |
| GB/T 4798.2 | Environmental Conditions for Electric and Electronic Products — Part 2: Transportation |

---

## V. Installation Instructions

### 5.1 Before Installation

1. Confirm power is DC6V (battery box) or AC110~220V to 6V1A adapter.
2. Do not place obstructions larger than 1cm within about 35cm in front of the sensing window (this module's farthest sensing is 35cm).
3. Do not face the sensing window directly at sunlight or strong light.
4. Check the U840 main control board wire order and terminal model/color; confirm solenoid drive wire matches.

### 5.2 Notes

- Always cut water and power before install/repair.
- Each AC-powered unit should have a separate power switch and reliable grounding.
- Use high-performance alkaline batteries; do not mix old and new.
- Do not hot-plug sensor module terminals.
- Remote distance adjust must be done with the module powered-on and in standby; at the limit position the LED flashes 3 times meaning reached.

### 5.3 Installation Steps

1. Fix the main control board and module to the faucet or flusher body, sensing window toward the use direction.
2. Connect power (battery box or adapter) and the solenoid drive wire.
3. Power on; observe the LED blink once and solenoid actuate once to complete self-check, entering 1-minute learning.
4. Use the remote to set the sensing distance to the step fitting the current countertop.
5. Reach in front of the sensing window to test: valve opens in range, closes on leaving.

### 5.4 Power-On Self-Check

After power-on the LED blinks once and the solenoid actuates once, entering 1-minute learning mode (LED stays lit during sensing), switching to normal standby after 1 minute. Do not keep blocking the sensing window during learning mode.

### 5.5 Remote Tuning and Battery Replacement

Distance is stepped by the standard wireless remote; lights 0.5s on signal, flashes 3 times at limit. Below 4.8V each sensing makes the LED flash 5 times as battery-change reminder; below 4.5V flashes 10 times and auto-closes the valve. Battery change: cut water → remove battery box, replace 4 same-brand new alkaline batteries → reinstall and re-self-check.

---

## VI. Applicable Complete Units & Integration Solutions

### 6.1 Companion Complete Units

The KCM-ET07 is a universal faucet sensing "brain," embeddable into these complete units:

- **Basin Sensor Faucet**: 26cm factory distance fits countertop basins; small countertops just retract by remote.
- **Instant-Heating Sensor Faucet**: dual-power compatible, fits kitchen and public-area hot-water scenarios.
- **Sensor Urinal Flusher**: remote distance adjust fits exposed / concealed different install depths.

### 6.2 ODM Integration Value

- **One Module, Many Structures**: 5~35cm remote distance adjust covers countertop basins, sinks, and urinals—fewer module versions, lower stock for complete-unit makers.
- **On-Site No-Disassembly Tuning**: contractors stand in front of the faucet after install to remote-set distance—no panel opening, no factory return, shorter delivery cycle.
- **Dual-Power Same Source**: battery and adapter versions share one module; one part number covers both power configs.

---

## Appendix

### A. Core Technology Index

| Core Tech No. | Technology Name | Application in This Product |
|:----:|---------|-----------|
| #6 | Low-Power Multi-Stable Agile Sensing Technology | Static power ≤0.2mW, long battery life |
| #7 | Liteon Smart Sensing Technology | Self-adaptive environmental baseline, install-and-use on power-on |
| #5 | Wireless Remote Control Technology | Remote step adjust of sensing distance, flash 3 times at limit |
| #11 | Dual-Mode Strong-Light-Immunity Anti-Interference Algorithm | 6 light sources 15~91cm direct/oblique no false trigger |
| #12 | Military-Grade EMC Technology | ESD level 4 / EFT level 4 / EMI level 3 |

**Related Patents (Granted)**

| Technology Point | Patent Name | Patent No. | Type |
|--------|---------|--------|------|
| Adjustable-distance sensor module | An adjustable-detection-distance sensor module for kitchen/bath equipment | ZL2025 2 1007523.9 | Utility Model |
| Signal detection | A sensor water-output device and signal detection method | ZL201910380558.X | Invention Patent |
| Sensor and manual-control faucet | A sensor and manual-control faucet | ZL2015 2 0753357.7 | Utility Model |
| Dual-mode faucet | A dual-mode faucet | ZL2019 2 2113032.3 | Utility Model |
| Waterproof sensor module | A waterproof sensor module for a water-output device | ZL2020 2 2360603.6 | Utility Model |

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
| Chinese Website | www.gibo.com.cn |
| English Website | www.gibosensor.com |
| Service Hotline | 0591-88066000 |
| Company Email | sales@gibol.com.cn |
| Company Address | Building 3, Liangyuan Science Park, High-Tech Zone, Fuzhou City, Fujian Province |

---

> This document is compiled based on the KCM-ET07 Faucet Sensor Module Specification (V1.0, 2024-07-03). Parameters are subject to the actual unit. GIBO reserves the final right of interpretation and modification of the technical specifications.
>

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
