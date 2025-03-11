---
title: Onboard Terrain Classification via Stacked Intelligent Metasurface-Diffractive Deep Neural Networks from SAR Level-0 Raw Data
author: Xin Li
pubDatetime: 2025-03-10
modDatetime: 2025-03-11
featured: true
draft: false
tags:
  - Paper
ogImage: ""
description: "A concise overview of how a multi-layer metasurface diffracts raw SAR IQ data for onboard land-cover classification in near real-time."
---


## toc

# Onboard Terrain Classification from SAR Level-0 Data Using Stacked Intelligent Metasurfaces

Synthetic Aperture Radar (SAR) satellites like Sentinel-1 generate vast amounts of data daily, typically requiring substantial downlink bandwidth to send raw information back to Earth for processing. But what if we could do the classification tasks *on the satellite itself* — before downlink? In this post, we’ll explore an innovative approach that combines **diffractive deep neural networks (D$^{2}$NN)** and **stacked intelligent metasurfaces (SIM)** to perform real-time terrain classification using raw Sentinel-1 (S1) level-0 In-phase and Quadrature (IQ) data. 

---

## Motivation

1. **Bandwidth Bottleneck**: Traditional workflows transmit large volumes of raw SAR data for ground-based processing, causing delays and high costs.
2. **In-Orbit Processing**: Thanks to technological advances, there is now a growing interest in performing data analysis directly onboard the satellite. Doing so drastically reduces data transfer volumes and latency.
3. **Analogue Computation**: Conventional digital deep neural networks consume significant power and hardware resources. In contrast, diffractive metasurface-based networks operate in the analog wave domain, promising low-power, ultra-fast inference.

---

## Key Idea

Our paper proposes a **Stacked Intelligent Metasurface-Diffractive Deep Neural Network (SIM-D$^{2}$NN)** for classifying terrain (land vs. ocean) *directly from S1 level-0 raw IQ data*. The entire classification pipeline occurs in the electromagnetic (EM) wave domain:

1. **Input Encoding**: We map the raw SAR IQ data as phase modulations onto the first metasurface layer.  
2. **Multiple Layer Transformations**: A series of stacked metasurface layers (each with thousands of programmable meta-atoms) sequentially transforms the passing EM wave, effectively emulating layer-by-layer feature extraction similar to a conventional DNN.  
3. **Compact Output**: Instead of an entire downlinked dataset, only the classification result (e.g., “land” or “ocean”) needs to be transmitted to ground stations.

By design, each metasurface layer applies a learnable phase shift to the incoming wave. This wave *diffraction* replaces the typical linear matrix multiplications found in digital neural networks, creating a low-latency, energy-efficient classification system.

---

## How It Works

### 1. Modulating the Input Layer
- Each IQ data patch (e.g., $128 \times 128$) is first **phase-rotated** and normalized.
- The metasurface’s *0-th layer* is set to match these input values in its phase profile, effectively “encoding” the raw IQ features into the physical wave.

### 2. Diffractive Propagation
- As the EM wave passes through subsequent metasurface layers, it undergoes **layer-by-layer** transformations analogous to hidden layers in a neural network.
- Each metasurface layer has programmable meta-atoms that provide phase shifts (with unit modulus), *learning* the optimum wavefront transformation to discriminate land vs. ocean.

### 3. Classification Output
- The final wavefront reaches a small **receive antenna array** ($K$ elements, where $K$ is number of classes).
- Whichever antenna port observes the *highest wave amplitude* corresponds to the predicted class (e.g., land or ocean).

```math
\hat{k}_j = \arg\max_{k \in \{1,\ldots,K\}} \{|y_{j,k}|^2\}
```
Where $y_{j,k}$ is the complex amplitude at the $k$-th antenna when classifying patch $j$.

---

## Data and Experiments

1. **Dataset**: We used **real S1 level-0 raw IQ data**, divided into small patches ($128 \times 128$) with a stride of 32.
2. **Ground Truth**: A partial decoding of level-0 data guided us to label each patch as “land” or “ocean.”
3. **Phase-Rotation Data Augmentation**: A key trick was rotating the phase of these IQ patches by a fixed angle, then concatenating them — significantly improving robustness to noise and Doppler effects.
4. **Evaluation Metrics**: We measured **precision**, **recall**, **F1 score**, and **overall accuracy**.

### Main Results

- Our multi-layer SIM-D$^{2}$NN achieved around **90\%** for precision, recall, F1, and accuracy — *directly* from raw IQ data!
- This performance is only **5–7\%** behind a purely digital DNN with unconstrained weights, which is impressive given that a metasurface can only modulate phases with unit modulus.
- Data augmentation was crucial: without phase rotation, F1 score dropped from 90.60% to 69.35%.
- Even with limited training data (e.g., just 10% of patches), the metasurface approach maintained strong accuracy.

| Method                     | Precision (%) | Recall (%) | F1 (%) | Accuracy (%) |
|---------------------------:|:------------:|:----------:|:------:|:------------:|
| **SIM-D$^{2}$NN (ours)** |    90.54     |   90.67    | 90.60  |    87.83     |
| Digital DNN (reference)   |    94.78     |   97.14    | 95.95  |    92.91     |

---

## Why It Matters

1. **Reduced Downlink Requirements**  
   By performing classification onboard, we only need to send down *labels or alerts*, **not** gigabytes of raw data. This optimization is especially valuable for time-critical applications like flood mapping or disaster relief.

2. **Energy and Speed Advantages**  
   Metasurface inference is highly parallel and requires minimal power for wave propagation, making it *ideal* for space-borne platforms with strict power budgets.

3. **Scalable to Other Tasks**  
   While this paper focuses on a simple land vs. ocean classification, the diffractive metasurface approach can be extended to more complex terrain or object-detection tasks in remote sensing.

---

## Limitations and Future Directions

- **Linear Transform**: Metasurfaces implement linear transformations well, but they’re less suited for *nonlinear* activations. Future device engineering could explore specialized meta-atoms that mimic nonlinear operations.
- **Channel Robustness**: Real satellite-to-ground channels can suffer from dynamics beyond simple AWGN or mild fading. More robust channel estimation methods could be incorporated.
- **Hardware Complexity**: Deploying stacked metasurfaces in space demands advanced manufacturing and calibration to ensure stability across temperature and radiation conditions.

---

## Conclusion

This work paves the way for **in-orbit classification** of raw SAR data, drastically reducing bandwidth costs and latency. By harnessing the power of **multi-layer diffractive deep neural networks** implemented via **stacked intelligent metasurfaces**, we achieve near real-time terrain classification onboard the satellite. The method unlocks new possibilities for efficient, low-latency remote sensing and sets the stage for further innovations in analog computing.

> If you’re curious to learn more about diffractive neural networks or the broader impact of in-orbit processing, stay tuned for our upcoming publications and code releases!

---

### Citation

```
@article{liu2025onboard,
  title={Onboard Terrain Classification via Stacked Intelligent Metasurface-Diffractive Deep Neural Networks from SAR Level-0 Raw Data},
  author={Liu, Mengbing and Li, Xin and An, Jiancheng and Yuen, Chau},
  journal={ICLR ML4RS Workshop},
  year={2025}
}
```

*Thank you for reading! Feel free to leave your questions, comments, or suggestions.* 