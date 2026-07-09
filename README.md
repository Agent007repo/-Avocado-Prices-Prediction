# Predicting Avocado Prices with Prophet

This project forecasts Hass avocado prices using Facebook Prophet. It covers exploratory analysis, national and regional forecasting, seasonal decomposition, and business-readable interpretation of time-series components.

![avocado](visualizations/00_cover_image.png)

## What This Shows

- Business time-series forecasting
- Prophet model setup and interpretation
- National vs. regional forecast comparison
- Seasonality and trend decomposition
- Communicating uncertainty through forecast intervals

## Problem Statement

Avocado prices are volatile and seasonally driven. This analysis uses weekly retail scan data to understand historical price behavior and generate 365-day forecasts at both national and West-region levels.

## Dataset

Source: Hass Avocado Board data via Kaggle

Coverage: weekly retail scan data from 2015 to 2018 across U.S. regions.

## Methodology

1. Load and inspect weekly avocado price data.
2. Prepare Prophet-compatible `ds` and `y` fields.
3. Fit a national price model and generate a 365-day forecast.
4. Repeat the workflow for the West region.
5. Compare trend, weekly seasonality, yearly seasonality, and forecast uncertainty.

## Key Takeaways

- Prophet captures recurring seasonal price patterns in a business-readable way.
- Regional modeling adds useful signal beyond the national aggregate.
- Component decomposition is the most valuable output because it explains why prices move, not only what the point forecast is.
- Forecast intervals widen over time, correctly reflecting greater long-horizon uncertainty.

## Repository Contents

| Path | Purpose |
|---|---|
| `Avocado_Prices_Prediction_STRIPPED.ipynb` | Main notebook without heavy embedded outputs |
| `visualizations/` | Forecast and EDA images used in this README |
| `README.md` | Project explanation and run guide |

## How To Run

```bash
git clone https://github.com/Agent007repo/-Avocado-Prices-Prediction.git
cd -- -Avocado-Prices-Prediction
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook Avocado_Prices_Prediction_STRIPPED.ipynb
```

Download `avocado.csv` from Kaggle and place it in the repository root before running the notebook.

## Recruiter Signal

This is a forecasting and business-analytics project. It is useful evidence for analyst, data product, and applied ML roles where interpretable time-series communication matters.
