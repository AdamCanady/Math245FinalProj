import csv
import json
import os

keys = ["tax_value",
        "last_sold_price",
        "property_size",
        "zestimate_amount",
        "bathrooms",
        "zestimate_valuation_range_high",
        "tax_year",
        "zestimate_value_change",
        "latitude",
        "zestimate_percentile",
        "bedrooms",
        "zestimate_last_updated",
        "zillow_id",
        "last_sold_date",
        "year_built",
        "zestimate_valuationRange_low",
        "graph_data_link",
        "home_size",
        "longitude",
        "map_this_home_link",
        "home_type",
        "home_detail_link"]

with open("Zillow55057.csv", 'w') as f:
    e = csv.DictWriter(f, fieldnames=keys)
    e.writeheader()
    for fname in os.listdir("./data"):
        file = open(os.path.join("./data/", fname), 'r').read()
        data = json.loads(file)
        e.writerow(data)
