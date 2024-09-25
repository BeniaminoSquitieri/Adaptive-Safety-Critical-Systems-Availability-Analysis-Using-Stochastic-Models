# Adaptive-Safety-Critical-Systems-Availability-Analysis-Using-Stochastic-Models

## Project Overview

This project focuses on the application of safety-critical systems, particularly in the context of **reconfigurable communication systems** that must adapt quickly during emergencies. The main framework for our study is based on **Service Function Chains (SFC)**, a model that enables flexible and adaptive systems through virtualized network nodes connected in series.

### Objective

The primary goal of this project is to evaluate the stationary availability of three interconnected systems:
1. **S1**: A fault-tolerant monitoring station.
2. **S2**: A Service Function Chain (SFC) network node.
3. **S3**: A processing system.

The analysis is carried out using **stochastic methodologies** and aims to optimize the configuration of these systems, ensuring a stationary availability of at least **A0 = 0.999999**. Special attention is given to the **hardware component (PHY)** of the SFC network node, estimating its **failure** and **repair rates** using Maximum Likelihood Estimation (MLE). The project also explores **sensitivity analysis** to identify critical parameters that may reduce system availability below the desired threshold.

## System Architecture

The system consists of three interconnected subsystems:

1. **S1: Monitoring Station**  
   Comprises two redundant subsystems, each containing a sensor and a storage unit. The system functions if at least one subsystem is operational.

2. **S2: SFC Network Node**  
   Modeled as a 5-layer structure, where at least one of three containers must function for the node to remain operational. The SFC node is potentially redundant.

3. **S3: Processing System**  
   Composed of multiple processors, each consisting of a CPU, storage, software, operating system, and hardware. The system fails if all processors are non-operational.

## Methodology

The project utilizes several **availability modeling techniques**:
- **Continuous Time Markov Chains (CTMC)**
- **Reliability Block Diagrams (RBD)**
- **Stochastic Reward Networks (SRN)**

Each technique is applied to different subsystems, and their respective advantages and limitations are compared.

## Key Components

### Availability Models

- **CTMC**: Used to model the behavior of components like sensors, storage units, and CPUs, accounting for failure and repair transitions.
- **RBD**: Provides a visual representation of system reliability by modeling components in series or parallel.
- **SRN**: Extends basic Petri networks to model more complex systems, particularly for the SFC network node.

### Maximum Likelihood Estimation (MLE)

The project estimates the **failure** and **repair rates** of the hardware component (PHY) using MLE. The datasets provided contain repair and failure times, some of which are **censored** (i.e., incomplete data), and MLE is adapted to handle these cases.

### Sensitivity Analysis

The sensitivity analysis focuses on identifying critical failure and repair rate parameters for the Docker component (DCK) of the SFC node. By varying these parameters, the analysis aims to assess their impact on overall system availability.

## Project Structure

1. **Introduction**: Describes the system architecture and the objectives.
2. **Availability Models**: Details the techniques used for modeling system availability, including CTMC, SRN, and RBD.
3. **System Analysis**: Provides a detailed analysis of the three subsystems (S1, S2, S3) and their availability models.
4. **Failure and Repair Rate Estimation**: Discusses the application of MLE for estimating failure and repair rates for the PHY component.
5. **Sensitivity Analysis**: Explores variations in key parameters and their effect on system availability.

## How to Run

The project includes several **Python scripts** for optimizing system availability. To execute the main script, follow these steps:

1. Clone the repository.
2. Install required dependencies using `pip install -r requirements.txt`.
3. Run the main optimization script:
   ```bash
   python main.py

