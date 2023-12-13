
# NEURAL GOD

## Overview

NEURAL GOD is a machine learning project designed to identify and detect vulnerabilities in C/C++ code from various open-source projects, including FFMPEG, QEMU, Android, Linux, and more. The primary goal is to automatically identify vulnerabilities and, if detected, apply fixes or mitigations to enhance the security of the code.

## Features

- **Vulnerability Detection:** NEURAL GOD employs a machine learning model based on the BERT architecture to analyze C/C++ code and identify potential vulnerabilities. The model has been trained on real code datasets, including MSR, Reveal Dataset, and Devign, ensuring it learns from authentic code scenarios rather than synthetic data.

- **Ensemble Learning:** The project utilizes ensemble learning techniques to enhance the performance of the machine learning model. Individual models achieve up to 60% accuracy, but through ensemble learning, the accuracy is significantly improved to around 82%.

- **Mitigation using Davinci Model:** NEURAL GOD incorporates a trained model based on Davinci to perform code mitigation. This ensures that identified vulnerabilities are not only detected but also actively addressed to improve the overall security of the code.

- **User Interaction through Web Interface:** To provide an easy-to-use interface for users, a web page has been developed. Users can interact with the system by entering their OpenAI key and running the Python command `python -m streamlit run final.py`. The frontend opens, allowing users to submit C/C++ files for analysis. The system then analyzes the code to determine if it is vulnerable and, if necessary, applies mitigations.

## Getting Started

To use NEURAL GOD, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/NEURAL-GOD.git
cd NEURAL-GOD
```


2. Obtain an OpenAI key and replace the placeholder in `final.py` with your key.

3. Run the application:

```bash
python -m streamlit run final.py
```

4. Access the web interface at the provided URL and submit your C/C++ files for analysis.

## Disclaimer

NEURAL GOD is a tool designed for educational and research purposes. While it aims to enhance code security, it is not foolproof, and users are encouraged to review and validate the results independently.

## Contribution

Contributions to NEURAL GOD are welcome. Feel free to submit bug reports, feature requests, or pull requests to improve the functionality and performance of the project.
