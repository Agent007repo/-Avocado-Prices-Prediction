# Avocado Prices Prediction

A supervised machine learning project that forecasts average avocado prices across U.S. markets using the Hass Avocado Board dataset. The project covers the full ML pipeline: data cleaning, exploratory analysis, feature engineering, multi-model training, evaluation, and interpretation.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Results](#results)
- [Tech Stack](#tech-stack)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Key Takeaways](#key-takeaways)

---

## Project Overview

Avocado prices are notoriously volatile, driven by seasonality, regional demand shifts, organic vs. conventional supply dynamics, and volume fluctuations across PLU codes. This project uses historical retail price and volume data to build a predictive model for average weekly avocado prices across U.S. regions.

**Core objectives:**
- Understand the key drivers of avocado price variation (region, type, season, volume)
- Engineer meaningful features from raw retail data
- Train and compare multiple regression models
- Identify which features carry the most predictive signal

---

## Dataset

**Source:** [Hass Avocado Board](https://hassavocadoboard.com/) via Kaggle  
**Coverage:** Weekly retail scan data from 2015 to 2018 across 54 U.S. regions  
**Size:** ~18,000 observations

**Key variables:**

| Column | Description |
|---|---|
| `AveragePrice` | Target variable - average price of a single avocado |
| `Total Volume` | Total number of avocados sold |
| `4046` | Volume of small/medium Hass avocados (PLU 4046) |
| `4225` | Volume of large Hass avocados (PLU 4225) |
| `4770` | Volume of extra-large Hass avocados (PLU 4770) |
| `Total Bags` | Total bags sold |
| `type` | Conventional vs. organic |
| `year` | Year of observation |
| `region` | U.S. metro area or regional aggregate |

---

## Methodology

### 1. Data Cleaning and Preprocessing
- Parsed date columns and extracted month/year for temporal features
- Verified no missing values in core features
- Encoded categorical variables (`type`, `region`) using label encoding and one-hot encoding
- Applied log transformation to skewed volume features to normalize distributions

### 2. Exploratory Data Analysis (EDA)
- **Price distribution:** Organic avocados command a significant premium (~$0.50+ on average) over conventional
- **Seasonality:** Clear seasonal patterns with prices peaking in late winter/spring and dipping in summer
- **Regional variation:** Significant regional price spread with metro markets like San Francisco and New York showing higher average prices than southern and midwest markets
- **Volume-price relationship:** Inverse relationship between total volume and average price, consistent with supply-demand dynamics
- **Correlation analysis:** PLU-level volume features show moderate negative correlations with price; bag volumes less predictive

### 3. Feature Engineering
- `month` and `year` extracted from the date field to capture temporal effects
- `is_organic` binary flag from the `type` column
- Log-transformed volume features (`log_total_volume`, `log_4046`, `log_4225`, `log_4770`) to reduce skew
- One-hot encoded `region` to capture market-level fixed effects

### 4. Model Training and Evaluation

The following models were trained and evaluated using an 80/20 train-test split:

| Model | Description |
|---|---|
| Linear Regression | Baseline OLS model |
| Ridge Regression | L2 regularization to handle multicollinearity across region dummies |
| LASSO Regression | L1 regularization for sparse feature selection |
| Random Forest Regressor | Ensemble tree model for non-linear relationships |

**Evaluation metrics used:**
- R-squared (R²)
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

### 5. Model Interpretation
- Feature importance plots from the Random Forest model to identify top predictors
- Residual analysis to assess homoscedasticity and bias
- Actual vs. predicted scatter plots for visual performance validation

---

## Results

The Random Forest Regressor delivered the best out-of-sample performance. Key findings:

- **`is_organic`** was the single most predictive feature, confirming the consistent organic price premium
- **`month`** ranked highly, validating strong seasonality in avocado pricing
- **`region`** one-hot features captured meaningful market-level variation
- **Log-transformed volume features** improved all model performances versus raw volume inputs
- Residual plots showed minimal systematic bias, confirming good model fit

> Note: Exact metric values are available in the notebook output cells.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
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
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

3. **Get the dataset:**
   - Download `avocado.csv` from [Kaggle - Avocado Prices](https://www.kaggle.com/datasets/neuromusic/avocado-prices)
   - Place it in the root directory of the project

4. **Launch the notebook:**
```bash
jupyter notebook "Project 4 - Avocado Prices Prediction.ipynb"
```

Run all cells sequentially.

---

## Project Structure

```
-Avocado-Prices-Prediction/
├── Project 4 - Avocado Prices Prediction.ipynb   # Main analysis notebook
└── README.md                                      # This file
```

---

## Key Takeaways

- Type (organic vs. conventional) and seasonal timing are the dominant price drivers, outweighing regional and volume effects in predictive importance
- Log-transforming heavily skewed volume features before modeling is essential for regression model performance
- Random Forest captured non-linear interactions (e.g., between region and season) that linear models missed
- A simple feature engineering step (extracting month from date) meaningfully improved all model performances

---

## Author

**Samarth Annigeri**  
Master of Management in Analytics, McGill University  
[LinkedIn](https://www.linkedin.com/in/samarth-annigeri-14326a178/) | [Portfolio](https://theindianmagenta.notion.site/Product-Portfolio-f56b69796af74829a005df99d3cadf4b)
