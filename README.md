# Predicting Avocado Prices with Prophet

A notebook for descriptive exploration and Prophet forecasts of weekly Hass avocado retail prices. National forecasts use the published `TotalUS` series for conventional avocados; the regional example uses `West`, also conventional. Regional and avocado-type observations are never pooled into duplicate timestamps.

## Run

Use Python 3.11+, install `requirements.txt`, and place the Hass Avocado Board/Kaggle `avocado.csv` in this directory. Open `Avocado_Prices_Prediction_STRIPPED.ipynb` in Jupyter and execute from the repository root.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook Avocado_Prices_Prediction_STRIPPED.ipynb
```

`forecast_data.py` validates the selected series, numeric prices, unique dates, and chronological order. Prophet models trend and yearly seasonality and produces 365 daily forecast dates. Daily and weekly seasonalities are disabled because the source has only weekly observations.

## Interpretation and validation

Component plots describe fitted patterns; they do not identify causes of price changes. Forecast intervals are model assumptions, not independently calibrated uncertainty. The notebook does not implement a held-out forecasting benchmark or establish that a regional model improves predictive accuracy. Existing images under `visualizations/` are archived illustrations and may predate the corrected series selection.

```bash
python -m unittest discover -s tests -p test_regressions.py -v
```

Five regression tests cover filtering, date uniqueness, ordering, and invalid inputs. They do not validate Prophet accuracy or rerun the external dataset.
