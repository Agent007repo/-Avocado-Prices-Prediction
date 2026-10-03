"""Select one published weekly price series without mixing regions/types."""
import numpy as np
import pandas as pd


def prepare_series(data, region='TotalUS', avocado_type='conventional'):
    required = {'Date', 'AveragePrice', 'region', 'type'}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f'Missing columns: {sorted(missing)}')
    selected = data.loc[(data['region'] == region) & (data['type'] == avocado_type),
                        ['Date', 'AveragePrice']].copy()
    if selected.empty:
        raise ValueError(f'No observations for {region}/{avocado_type}.')
    selected.columns = ['ds', 'y']
    selected['ds'] = pd.to_datetime(selected['ds'], errors='raise')
    selected['y'] = pd.to_numeric(selected['y'], errors='raise')
    if selected.isna().any().any() or not np.isfinite(selected['y']).all():
        raise ValueError('Dates and prices must be present and finite.')
    if selected['ds'].duplicated().any():
        raise ValueError('Expected one observation per date for the chosen series.')
    return selected.sort_values('ds').reset_index(drop=True)
