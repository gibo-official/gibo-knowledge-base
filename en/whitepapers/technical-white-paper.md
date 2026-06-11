---
title: The Evolution of Sensor Technology: A 30-Year Technology Roadmap from Infrared to dTOF
date: 2026-06-05
author: GIBO Technology Center
source: Corporate Website (gibo.com.cn) / Corporate Technical White Papers / CNIPA Patent Data
keywords: dTOF laser sensing, infrared sensing technology, sensor faucet technology evolution, GIBO core technology, EMC interference immunity
status: ✅ Complete (Technical White Paper Series 01)
scheduled: 2026-08-10
series: Technical White Paper Series
---

# The Evolution of Sensor Technology: A 30-Year Technology Roadmap from Infrared to dTOF

> **White Paper Series 01** | This paper traces the evolution of sensing technology from traditional infrared to dTOF laser sensing, analyzing the core principles, advantages, disadvantages, and application scenarios of each generation.

---

## Introduction: A Neglected Story of Technological Evolution

Sensor faucets are among the most common yet most overlooked smart devices in daily life.

Every day, at airports, hospitals, shopping malls, and hotels — when you place your hand under a faucet, water flows automatically. Behind this seemingly simple action lies 30 years of continuous evolution in sensing technology.

From the most basic infrared reflection sensing to today's sub-millimeter precision dTOF laser ranging, sensing technology has undergone three clear generational leaps. This paper provides a comprehensive overview of this technology evolution roadmap.

---

## First Generation: Infrared Reflective Sensing (1990s-2010s)

### Working Principle

Infrared reflective sensing was the earliest technical solution adopted for sensor faucets. Its basic principle is very simple:

1. The infrared emitting diode (IRED) emits an infrared beam
2. When a hand enters the sensing area, the infrared light is reflected by the hand
3. The infrared receiver (Phototransistor) receives the reflected signal
4. The signal is amplified and compared, then triggers the solenoid valve to open and release water

### Technical Limitations

Although first-generation infrared sensing technology achieved the basic function of "water flows when hand approaches," it faced several prominent issues in practical applications:

**① Ambient Light Interference**

Infrared receivers are highly sensitive to the infrared component in sunlight. In installation positions near windows or under strong direct light, the infrared component in ambient light can cause the sensor to misjudge — either not releasing water, or releasing water continuously.

**② Object Color Impact**

Different colored objects have vastly different reflectivity for infrared light. White objects have high reflectivity (easy to detect), while black objects have low reflectivity (may not be detected). This leads to inconsistent user experience — light-colored clothing can be detected, while dark-colored clothing may not be detected at all.

**③ Detection Distance Drift**

The output power of infrared emitting diodes changes with temperature and time, causing detection distance drift. This manifests as: shorter detection distance in winter, and longer detection distance in summer.

**④ Multi-Source Crosstalk**

In scenarios with multiple sensor faucets installed (such as a row of washbasins in a public restroom), the infrared signals from adjacent faucets may interfere with each other, causing false triggering.

### First Generation Improvement: Modulated Infrared Technology

To address the above issues, engineers introduced modulated infrared technology — modulating the infrared emission signal to a specific frequency (typically 38kHz or 56kHz), with the receiver only demodulating signals at that frequency.

This improvement effectively enhanced ambient light interference immunity, but it still could not solve the problems of object color impact and detection distance drift.

---

## Second Generation: Active Infrared + Algorithm Optimization (2010s-2020s)

### Technology Upgrades

Second-generation sensing technology underwent systematic upgrades in both hardware and software:

**Hardware Upgrades**:
- Adoption of higher-sensitivity photoelectric sensors
- Introduction of anti-light-source interference optical lenses and filters
- Multi-channel infrared emitting/receiving arrays
- Temperature compensation circuits

**Algorithm Upgrades**:
- Adaptive threshold algorithm: dynamically adjusts the sensing threshold based on ambient light intensity
- Multi-frame filtering algorithm: continuously samples multiple frames for comprehensive judgment, reducing false triggers
- Anti-jitter algorithm: eliminates false actions caused by rapid entry and exit of the sensing area

### Advantages Over First Generation

| Dimension | First Generation Infrared | Second Generation Active Infrared |
|:----------|:------------------------:|:--------------------------------:|
| Ambient Light Immunity | Weak | Moderate (Improved) |
| Color Adaptability | Poor | Moderate |
| Distance Stability | Poor | Moderate |
| Multi-Source Anti-Crosstalk | Weak | Moderate |
| False Trigger Rate | Relatively High | Moderate |
| Cost | Low | Moderate |

### Core Limitations of the Second Generation

Although significantly improved compared to the first generation, second-generation technology still has a fundamental problem: **it is based on "signal strength" judgment, not "distance" measurement**.

In other words, the way the sensor determines "a hand is approaching" is by detecting "the reflected light has become stronger," not by detecting "an object is at 20cm." This "intensity judgment" mode fundamentally determines its accuracy ceiling — it cannot distinguish between "a black hand nearby" and "a white hand far away."

To truly solve this problem, a leap from "intensity detection" to "distance measurement" is required.

---

## Third Generation: dTOF Laser Sensing Technology (2020s-Present)

### What is dTOF?

dTOF (direct Time-of-Flight) is a technology that calculates the distance to a target by measuring the time of flight of a light pulse from emission to reflection.

**Working Principle**:

```
Transmitter → Emits laser pulse → Reflects off hand → Reflected light received
                                                             ↓
Calculates time difference between emission and reception → Δt × c / 2 = Distance
```

The key difference is: **dTOF measures "time," not "intensity."** The relationship between time and distance follows precise physical laws (d = c × t / 2), unaffected by object color, surface material, or ambient light intensity.

### Core Advantages of dTOF in Sensor Faucets

**① True Distance Perception**

dTOF can accurately measure the distance from the hand to the faucet (millimeter-level precision), enabling true "detection within a specified distance." This means the sensing zone can be precisely defined — for example, triggering only within 20cm, and not activating beyond 20cm.

**② Completely Unaffected by Color**

Whether black or white, dark or light, the reflection time remains unaffected. Dark clothing will no longer be "undetectable."

**③ Stable Operation in Strong Light Environments**

dTOF uses laser light rather than infrared light. Lasers have far superior monochromaticity and directionality compared to infrared LEDs. dTOF continues to operate stably even under direct sunlight or strong light environments.

**④ Faster Response Speed**

dTOF single measurement time is at the nanosecond level, enabling multiple samples and distance calculations in an extremely short time, with response speeds far exceeding traditional solutions.

### Technical Parameter Comparison

| Parameter | Traditional Infrared | Active Infrared (Enhanced) | dTOF Laser Sensing |
|:---------:|:-------------------:|:--------------------------:|:------------------:|
| Sensing Method | Intensity Detection | Intensity Detection | Distance Measurement |
| Accuracy | Centimeter-level | Centimeter-level | Millimeter-level |
| Color Impact | Significant | Partially Improved | No Impact |
| Strong Light Adaptability | Poor | Moderate | Excellent |
| Response Time | ~100ms | ~50ms | ~10ms |
| False Trigger Rate | Medium-High | Medium | Extremely Low |
| Anti-Interference Capability | Weak | Moderate | Strong |
| Power Consumption | Low | Low | Low |
| Cost | Low | Medium | Medium-High |

### Technology Transfer: From Smartphone Sensors to Sensor Sanitary Ware

dTOF technology was first applied in the smartphone domain for 3D sensing and facial recognition. Transferring this technology to the sensor sanitary ware field required solving several engineering challenges:

1. **Waterproofing and Moisture Resistance**: The high-humidity environment of public restrooms poses a severe challenge for laser modules
2. **Wide Temperature Range**: From northern winters to southern summers, adaptation to a temperature range of -25°C to 70°C is required
3. **Consistency**: Calibration consistency for each sensor in mass production
4. **Cost Control**: Adapting consumer electronics-grade sensors for industrial batch production applications

GIBO achieved productization of the dTOF technical solution around 2022, making it one of the first domestic ODM manufacturers of sensor sanitary ware to complete this technology transfer.

---

## Frontier of Technology Evolution: Liteon Dual-Mode Sensing

Building on dTOF, sensing technology continues to evolve. Liteon dual-mode sensing is one of the latest technological directions — it integrates active infrared and laser sensing into a single sensor module:

- **Infrared Mode**: Low-power standby state, used to detect "whether someone is approaching"
- **Laser Mode**: High-precision ranging state, automatically activated when someone approaches, used for accurate distance judgment

This "dual-mode" design balances the needs of low-power standby and high-precision judgment, representing the current technological frontier in the sensor sanitary ware field.

---

## Core Technologies Complementary to Sensing

Sensing technology itself is only part of the sensor faucet technology system. A complete sensor faucet also requires the following complementary core technologies:

### Low-Power Circuit Design

For battery-powered commercial sensor faucets, power consumption is a critical指标. GIBO's products achieve a static power consumption of ≤90μA, meaning:
- Battery-powered continuous operation for 1-2 years
- Reduced maintenance costs for large-scale engineering projects
- Bistable pulse solenoid valve technology ensures power is consumed only during switching

### Electromagnetic Compatibility (EMC) Design

In complex electromagnetic environments such as airports and hospitals, sensor faucets must resist electromagnetic interference from mobile phone signals, WiFi routers, medical equipment, security screening devices, and other sources. GIBO's product EMC specifications:
- ±15kV Electrostatic Discharge (ESD) withstand
- ±4kV Electrical Fast Transient (EFT) immunity

### Waterproof Sealing Design

The high-humidity environment of public restrooms demands exceptional waterproofing capabilities for electronic devices. Waterproofing for sensor faucets involves:
- Control board waterproof encapsulation
- Sensor waterproof design
- Solenoid valve waterproof sealing
- Overall IP protection rating (IP65~IPX7)

---

## Future Outlook: Fourth-Generation Sensing Technology

Looking ahead, sensing technology is evolving in the following directions:

**Intelligence**:
- Deep integration with AIoT for device self-diagnostics, water usage data analysis, and remote management
- Adaptive learning of user water usage habits to optimize water delivery logic

**Multi-Modal Sensing**:
- Integration of infrared, laser, ultrasonic, capacitive, and other sensor types
- More accurate scene perception (distinguishing different intentions such as hand washing, water collection, and cleaning)

**Miniaturization**:
- Continuous integration and miniaturization of sensor modules
- Enabling more installation scenarios (such as compact concealed faucets)

---

## Conclusion

From infrared to dTOF, from "detection intensity" to "measurement distance," the evolution of sensing technology is a history of continuously breaking through physical limitations.

Each generation of technology solves the problems left by its predecessor — ambient light interference, color impact, and accuracy ceilings. dTOF represents an important milestone on the current technology roadmap: by using laser time-of-flight measurement, it fundamentally bypasses the various limitations of "intensity detection."

For brands that are currently selecting ODM partners for sensor faucets, understanding the generational differences in sensing technology helps in making more accurate technical choices during product positioning — whether to pursue a cost-optimized mature solution or to choose a technologically advanced next-generation solution.

---

**About GIBO**
Fujian GIBO Kitchen and Bath Tech Co., Ltd. was established in 2005, specializing in sensor sanitary ware ODM for over 20 years. With 200+ national patents and 18 core self-developed technologies, the company is a National High-tech Enterprise, National Specialized & Sophisticated SME, and a drafting unit of GB/T 41863-2022 national standard. Annual capacity: 1,000,000+ units. Products exported to 40+ countries.

**Contact Us**
- Website: https://www.gibo.com.cn / https://www.gibosensor.com
- Service Hotline: 0591-88066000
- Email: sales@gibo.com.cn

---

> **Copyright Notice**: This document is the official technical white paper of Fujian GIBO Kitchen and Bath Tech Co., Ltd. The content is protected by copyright. Compiled based on GIBO's official website and publicly available corporate information.
> **Document path**: `/en/whitepaper/technical-white-paper.md`
>
> **Updated**: 2026-06-09 | GIBO | Website: https://www.gibo.com.cn
