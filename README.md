# WebController: Car Control Demo via Web Interface

This project demonstrates how to control a car's movements in its early stages through a **web interface**. The data from the web interface is sent to the **STM32** via **SPI** communication from the **Raspberry Pi**, enabling manual control of the car. This is a demo setup that focuses on the integration of the web interface with the car control system, after we have developed the necessary **SPI** communication and **motor transmission adjustments**. The project builds upon these elements before incorporating **image processing** for autonomous functionality.

## 📜 Project Overview

The main goal of this project is to:

1. Create a **web interface** for controlling a car.
2. Send control data from **Raspberry Pi 5** to an **STM32** via **SPI** connection.
3. Control the car manually using the data received from the web interface.

## 🛠️ Installation

To get started with this project, follow the steps below:

1. **Clone the repository** to your local machine:

```bash
    git clone https://github.com/yourusername/WebController.git
```
2. **Set up a virtual environment** (recommended using venv):

Navigate to the project folder and create a virtual environment:

```bash
    python -m venv venv
```
Activate the virtual environment:

On **Windows**:
```bash
    .\venv\Scripts\activate
```

On **Linux/macOS**:
```bash
  source venv/bin/activate
```

3. **Install required Python libraries** using the **requirements.txt** file:

```bash
pip install -r requirements.txt
```

Note: When installing on Windows, you may encounter errors while installing the spidev library. This is expected, as spidev is not fully supported on Windows. Consider using a Linux-based environment for development or look into alternative ways to set up SPI communication on Windows.
