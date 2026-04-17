# Avocado Prices Prediction Using Facebook Prophet

A time series forecasting project that uses **Facebook Prophet** to predict future avocado prices using the Hass Avocado Board retail dataset. The project is structured in two parts: a national-level forecast across all data, and a region-specific forecast for the West region.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Why Facebook Prophet?](#why-facebook-prophet)
- [Methodology](#methodology)
  - [Part 1: National Price Forecast](#part-1-national-price-forecast)
  - [Part 2: West Region Forecast](#part-2-west-region-forecast)
- [Tech Stack](#tech-stack)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Key Takeaways](#key-takeaways)

---

## Project Overview

Avocado prices exhibit strong seasonality, regional variation, and long-term trend patterns driven by supply logistics and consumer demand cycles. This project applies Facebook's open-source **Prophet** library to model these dynamics and generate 365-day forward forecasts at both the national and regional level.

**Core objectives:**
- Understand historical avocado price trends and seasonality patterns
- Build a Prophet time series model on national aggregate price data
- Drill down to a region-specific model (West region) to capture local price dynamics
- Visualize forecast decomposition: trend, weekly seasonality, and yearly seasonality components

---

## Dataset

**Source:** [Hass Avocado Board](https://hassavocadoboard.com/) via Kaggle  
**Coverage:** Weekly retail scan data, 2015-2018, across 54 U.S. regions  

**Key columns used in this project:**

| Column | Description |
|---|---|
| `Date` | Date of weekly observation (renamed to `ds` for Prophet) |
| `AveragePrice` | Average retail price per avocado unit (renamed to `y` for Prophet) |
| `region` | U.S. city or regional aggregate (used for Part 2 filtering) |
| `type` | Conventional or organic |
| `year` | Year of observation |
| `Total Volume` | Total avocados sold that week |
| `4046` | Volume of small/medium Hass avocados sold (PLU 4046) |
| `4225` | Volume of large Hass avocados sold (PLU 4225) |
| `4770` | Volume of extra-large Hass avocados sold (PLU 4770) |

> Note: PLU codes apply only to Hass avocados. Other varieties (e.g., greenskins) are excluded from this dataset.

---

## Why Facebook Prophet?

Prophet is particularly well-suited to this problem for three reasons:

1. **Strong seasonality** - Avocado prices follow clear yearly and weekly cycles tied to harvest schedules and consumer behavior (e.g., Super Bowl demand spikes)
2. **Multiple seasons of historical data** - The dataset spans 2015-2018, giving Prophet enough signal to learn robust seasonal patterns
3. **Handles missing data and outliers** - Prophet's additive decomposition model is robust to irregularities without requiring manual imputation

Prophet models the time series as:

```
y(t) = trend(t) + seasonality(t) + holidays(t) + error(t)
```

Where non-linear trends are fit using piecewise linear or logistic growth, and seasonal components are modeled using Fourier series.

---

## Methodology

### Part 1: National Price Forecast

**Goal:** Forecast average avocado prices nationally over the next 365 days.

**Steps:**
1. Load the full dataset and sort chronologically by `Date`
2. Visualize the raw time series: `Date` vs. `AveragePrice` to observe baseline trends
3. Explore the distribution of observations across `region` and `year` using count plots
4. Subset to the two columns Prophet requires: `Date` and `AveragePrice`
5. Rename columns to Prophet's required format: `ds` (datestamp) and `y` (target)
6. Instantiate and fit the Prophet model on the full national dataset
7. Generate a 365-day future dataframe using `make_future_dataframe(periods=365)`
8. Run `.predict()` to generate the forecast with confidence intervals
9. Plot the forecast using `m.plot(forecast)` with date on the x-axis and price on the y-axis
10. Plot forecast components using `m.plot_components(forecast)` to decompose trend, weekly, and yearly seasonality

**Key outputs:**
- Full 365-day price forecast with uncertainty intervals (`yhat_lower`, `yhat`, `yhat_upper`)
- Component plots showing the underlying trend direction and seasonal patterns by week/year

---

### Part 2: West Region Forecast

**Goal:** Repeat the same forecasting pipeline scoped specifically to the **West** region to capture regional price dynamics.

**Steps:**
1. Reload the original dataset
2. Filter to `region == 'West'` to isolate West Coast retail scan data
3. Sort by `Date` and visualize the regional price time series
4. Rename to `ds`/`y` format and fit a fresh Prophet model
5. Generate a 365-day forecast
6. Plot the regional forecast and component decomposition

**Why the West region?** West Coast markets (California, Oregon, Washington) are among the largest avocado retail markets in the U.S. and are geographically closest to major production regions in Mexico and California, making them analytically interesting for supply-side price dynamics.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Prophet](https://img.shields.io/badge/Facebook%20Prophet-1877F2?style=flat-square&logo=meta&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)
![Seaborn](https://img.shields.io/badge/Seaborn-2E4057?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

---

## How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/Agent007repo/-Avocado-Prices-Prediction.git
cd -Avocado-Prices-Prediction
```

2. **Install dependencies:**
```bash
pip install prophet pandas numpy matplotlib seaborn jupyter
```

> If you encounter installation issues with Prophet, try the conda route:
> ```bash
> conda install -c conda-forge prophet
> ```

3. **Get the dataset:**
   - Download `avocado.csv` from [Kaggle - Avocado Prices](https://www.kaggle.com/datasets/neuromusic/avocado-prices)
   - Place it in the root directory of the project

4. **Launch the notebook:**
```bash
jupyter notebook "Project 4 - Avocado Prices Prediction.ipynb"
```

Run all cells top to bottom. Part 1 (national forecast) runs first, Part 2 (West region) follows.

---

## Project Structure

```
-Avocado-Prices-Prediction/
├── Project 4 - Avocado Prices Prediction.ipynb   # Main analysis notebook
├── avocado.csv                                    # Dataset (download separately)
└── README.md                                      # This file
```

---

## Key Takeaways

- **Prophet captures seasonality cleanly** - The component decomposition reveals a clear yearly price cycle, with prices typically rising in winter/spring and declining in summer months, consistent with harvest and shipping cycles
- **National vs. regional dynamics differ** - The West region's price trajectory differs meaningfully from the national average, reinforcing that region-level modeling adds value beyond aggregate forecasts
- **Simple pipeline, strong interpretability** - Prophet requires minimal feature engineering compared to traditional regression approaches; the trade-off is less control over predictor variables, but the additive decomposition makes the model's reasoning fully transparent
- **Forecast uncertainty widens appropriately** - Confidence intervals expand as the forecast extends further into the future, which is the correct statistical behavior for this type of model

---

## About Prophet

Prophet is open-source forecasting software released by Facebook's Core Data Science team. It is designed for business time series data with strong seasonal patterns and handles missing data, outliers, and trend changes gracefully.

- Paper: [Forecasting at Scale (Taylor & Letham, 2018)](https://peerj.com/preprints/3190/)
- Docs: [facebook.github.io/prophet](https://facebook.github.io/prophet/docs/quick_start.html)

---

## Author

**Samarth Annigeri**
Master of Management in Analytics, McGill University
[LinkedIn](https://www.linkedin.com/in/samarth-annigeri-14326a178/) | [Portfolio](https://theindianmagenta.notion.site/Product-Portfolio-f56b69796af74829a005df99d3cadf4b)
