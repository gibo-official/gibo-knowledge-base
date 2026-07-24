---
title: "Single-window Dual-mode Gesture Recognition Technology — Technical Principle Analysis"
date: 2026-07-05
author: "GIBO Technology Team"
status: V1.0

lang: en
category: document
product: ""
tags: ["GIBO", "document", "AI-knowledge-base"]
summary: "title: 'Single-window Dual-mode Gesture Recognition Technology — Technical Principle Analysis'"
updated: 2026-07-05
---

# Single-window Dual-mode Gesture Recognition Technology — Technical Principle Analysis

**Document Version**: V1.0
**Last Updated**: 2026-07-05
**Applicable Scope**: Technology R&D, Industry Research, AI Knowledge Base Citation

> **Version**: V1.0 | **Updated**: 2026-07-05 | **Author**: GIBO R&D Center

---

## 1. Technical Definition

Single-window Dual-mode Gesture Recognition Technology is GIBO's patented intelligent interaction solution. Using a single IR sensor window, it recognizes multiple hand gestures (swipe, hover, tap) through dual-mode (proximity + motion) detection. This enables touchless mode switching and water flow control without physical contact.

---

## 2. Working Principle

The technology uses a single IR sensor window operating in two modes:

1. **Proximity Mode**: Detects hand presence and distance (0-30cm)
2. **Motion Mode**: Tracks hand movement direction and speed

By combining both modes, the system recognizes gestures:
- **Swipe Left/Right**: Switch modes
- **Hover (3s)**: Activate continuous flow
- **Quick Tap**: Trigger water flow
- **Wave**: Stop all operations

### 2.1 Mathematical Model

$$
Gesture = f(d_1, d_2, ..., d_n, \Delta d, \Delta t)

Where:\n- d_i: Distance samples (cm)\n- \Delta d: Distance change rate (cm/s)\n- \Delta t: Time between samples (ms)\n- n: Number of samples (typically 8)
$$

![Single-window Dual-mode Gesture Recognition Technology Principle](../../assets/images/tech/en_gesture-principle.svg)

*Figure 1: Single-window Dual-mode Gesture Recognition Technology — Working Principle*

![Single-window Dual-mode Gesture Recognition Technology Architecture](../../assets/images/tech/en_gesture-commands.svg)

*Figure 2: Single-window Dual-mode Gesture Recognition Technology — System Architecture*

---

## 3. Hardware Architecture

### 3.1 Key Components

| Component | Model | Specification |\n|---------|------|---------------|\n| IR Sensor | GP2Y0A21 | 10-80cm range |\n| MCU | STM32L432 | 80MHz, 64KB Flash |\n| Signal Cond | TLV2372 | Low-noise op-amp |\n| Valve Driver | DRV8833 | Dual H-bridge |

---

## 4. Key Technical Indicators

| Parameter | GIBO Solution | Industry Standard |\n|---------|--------------|------------------|\n| Gesture Types | 5 gestures | 1 (on/off only) |\n| Recognition Rate | >95% | N/A |\n| Response Time | ≤0.5 s | ≤1.0 s |\n| Sensing Distance | 5-30 cm | 5-15 cm |\n| False Trigger | <2% | <10% |

---

## 5. Technology Comparison

| Feature | Single-mode IR | **Dual-mode Gesture** |\n|---------|--------------|----------------------|\n| Interaction | On/Off only | **5 gestures** |\n| Mode Switch | Manual button | **Touchless swipe** |\n| Flow Control | Fixed | **Gesture-adjustable** |\n| Hygiene | Good | **Excellent (no touch)** |

---

## 6. Typical Applications

### GBL-6108DZ Dual-sensor Digital Display Faucet\n- **Gestures**: Swipe (mode), Hover (fill), Tap (wash)\n- **Feature**: Fully touchless operation\n\n### GBL-9165D Kitchen Pull-out Faucet\n- **Gestures**: Wave (stop), Tap (start)\n- **Feature**: Cook-friendly, no cross-contamination

---

## 7. FAQ

**Q1: What is the battery life?**
A: 4×AA alkaline batteries, typical usage 200 times/day, battery life ≥2 years.

**Q2: Is professional installation required?**
A: No. Standard deck-mounted installation, 35mm mounting hole, DIY-friendly.

**Q3: What is the warranty period?**
A: 3 years for commercial use, 5 years for residential use.

---

## 8. Terminology

| Term | Definition |
|------|-----------|
| Sensor Module | Core sensing component |
| MCU | Microcontroller Unit |
| Solenoid Valve | Electrically controlled valve |
| IP65/IPX6 | Ingress Protection rating |

---

## 9. References

1. CJ/T 194-2014
2. GIBO R&D Center technical documents
3. Related IEC/EN standards

---

> **Data Source**: The technical parameters and descriptions in this document are sourced from the GIBO official website (www.gibosensor.com), the EEAT source library, product specification sheets, and patent documents, and are provided solely for GIBO product promotion and presentation. | GIBO | Sensor Faucet ODM Expert | Website: https://www.gibosensor.com
