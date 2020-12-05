categorical_features = [
    'language',
    'canton',
    'typology'
]

skewed_features = [
    'residents',
    'population_density',
    'households',
    'employed_total',
    'employed_primary_sector',
    'employed_secondary_sector',
    'employed_tertiary_sector',
    'workplaces_total',
    'workplaces_primary_sector',
    'workplaces_secondary_sector',
    'workplaces_tertiary_sector',
    'new_housing_rate',
    'surface_area',
    'agricultural_area_change',
    'unproductive_area_percent',
    'total_tax_income',
    'per_capita_tax_income',
    'n_machines',
    'tvm_distance'
]

unskewed_features = [
    'population_change',
    'foreign_nationals_percent',
    'age_0_19',
    'age_20_64',
    'age_65_over',
    'marriage_rate',
    'divorce_rate',
    'birth_rate',
    'mortality_rate',
    'households_size',
    'settlement_urban_area_percent',
    'settlement_urban_area_change',
    'agricultural_area_percent',
    'wooded_area_percent',
    'dwelling_vacancy_rate',
    'social_assistance_rate',
    'health_region',
    'health_premium_child',
    'health_premium_young',
    'health_premium_adult',
    'rel_share_rk',
    'rel_share_ref',
    'rel_share_other',
    'rel_share_none',
    'unemployed',
    'unemployment_rate',
    'crime_rate_stgb',
    'e_cntr',
    'n_cntr',
    'z_min',
    'airport_distance',
    'geneva_distance'
]


def cols_idxs(df, feats):
    return [df.columns.get_loc(c) for c in feats]
