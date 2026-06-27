# Avocado Price Forecasting with Prophet

Business forecasting notebook using Facebook Prophet to model avocado price trends and seasonality from Hass Avocado Board retail scan data.

## Project Maturity

Notebook forecasting project. This is useful as a clear business-time-series example, but it should be treated as a supporting project rather than a flagship ML engineering artifact.

## Problem

Avocado prices vary by time, region, and season. This project explores whether Prophet can capture trend and seasonal components for national and West-region avocado prices.

## Dataset

Source: Hass Avocado Board data via Kaggle  
Coverage: weekly retail scan data from 2015-2018 across U.S. regions

## Main Artifact

- `Avocado_Prices_Prediction_STRIPPED.ipynb`: notebook with the forecasting workflow.

## Included Visualizations

The repository currently includes these visualization files:

- `visualizations/01_national_price_timeseries.png`
- `visualizations/04_national_prophet_forecast.png`
- `visualizations/05_national_prophet_components.png`
- `visualizations/07_west_prophet_forecast.png`
- `visualizations/08_west_prophet_components.png`

## Methodology

1. Load and inspect avocado price data.
2. Prepare Prophet-compatible date and target columns.
3. Fit a national price forecasting model.
4. Fit a West-region forecasting model.
5. Compare trend and seasonal components.
6. Interpret forecast behavior and uncertainty intervals.

## Local Setup

Because the repository name starts with a hyphen, use `cd --` when entering the directory from a shell.

```bash
git clone https://github.com/Agent007repo/-Avocado-Prices-Prediction.git
cd -- -Avocado-Prices-Prediction
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook Avocado_Prices_Prediction_STRIPPED.ipynb
```

Download `avocado.csv` from Kaggle and place it in the root directory before running the notebook.

## Recruiter Signal

This project shows practical forecasting, business interpretation, and time-series decomposition. It is easy for nontechnical reviewers to understand.

## Technical Reviewer Signal

This is a basic forecasting notebook. To make it stronger, the notebook should be executed with outputs, forecast error metrics should be added, and the repository should be renamed without the leading hyphen.

## Known Limitations

- The notebook currently has stripped outputs.
- Some original visualizations referenced by older README versions are not present.
- Prophet is useful for interpretable seasonality but should be compared with simpler baselines and other forecasting methods.
- Forecast quality should be measured with holdout metrics, not only visual inspection.

## Recommended Next Improvements

- Rename repository to `avocado-price-forecasting`.
- Re-run the notebook and keep outputs visible.
- Add train/test forecast error metrics.
- Add baseline comparisons.
- Add all generated visualizations under `visualizations/`.
