## Project Overview

The Smart Home Energy Management project aims to optimize energy usage in a home environment using machine learning and IoT technologies. The project focuses on integrating a pre-made dataset containing simulated smart home appliances and areas into a centralized IoT system. The system emphasizes maintaining data integrity through dedicated data processing and cleaning modules and ensures efficient data transfer via a simulated communication protocol.

## Developmental Phase

### Data Collection Module
- Integrates pre-made dataset containing simulated smart home appliances and areas.
- Ensures data integrity through dedicated data processing and cleaning modules.
- Establishes robust connection between simulated devices and the Data Collection Module using a simulated communication protocol.

### Data Preprocessing
- Aggregates and preprocesses data within the Data Collection Module.
- Formulates specific modules to guarantee dataset reliability.
- Addresses challenges in simulating communication protocols and ensuring smooth data flow between components.

## Model Design

### Time Series Model (ARIMA)
- Focuses on time series forecasting to predict overall power consumption (in kW) over the next month.
- Leverages ARIMA model's capabilities in capturing linear trends and seasonality within sequential data.

### Deep Neural Network (DNN)
- Analyzes intricate patterns and non-linear relationships in power consumption.
- Explores variations in power consumption for specific appliances or areas over time.
- Considers date and time dependencies to capture complex, non-linear relationships within feature-rich datasets.

## Optimization Strategy

- Manages and optimizes peak energy demand in smart home environments.
- Utilizes a combined approach leveraging both ARIMA and DNN models.
- Enhances robustness and accuracy of predictions for effective management and mitigation of peak energy demand.

## Tableau Public Dashboard

- Integrates with Tableau Public Dashboard to visualize various aspects of the smart home energy management system:
  - **Status Visualization**: Displays month-to-month status without manipulating the data.
  - **Summary Visualization**: Presents an aggregate summary of the data to provide an overview of energy consumption patterns.
  - **Machine Learning Insights Visualization**:
    - **ARIMA**: Shows a time series line chart comparing predicted versus actual energy consumption for the next month.
    - **DNN**: Displays a time series line chart comparing predicted versus actual energy consumption for one day on an hourly cadence.
