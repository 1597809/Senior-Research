import pandas as pd
import numpy as np
from tqdm import tqdm

df = pd.read_csv('data/combined/data_02.csv')

state_data = {
    'Alabama': {'Population': 5024279, 'Storm Likeliness': 0.75, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Tornado', 'Hurricane', 'Flood', 'Wind', 'Hail'], 'Unlikely Storms': ['Snow', 'Wildfire', 'Dust']},
    'Alaska': {'Population': 731545, 'Storm Likeliness': 0.3, 'Most Likely Storms': ['Snow', 'Heavy Rain', 'Thunderstorm', 'Hail'], 'Likely Storms': ['Wind', 'Flood'], 'Unlikely Storms': ['Hurricane', 'Tornado', 'Wildfire', 'Dust']},
    'Arizona': {'Population': 7151502, 'Storm Likeliness': 0.4, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Dust', 'Wildfire', 'Wind', 'Flood', 'Hail'], 'Unlikely Storms': ['Snow', 'Tornado', 'Hurricane']},
    'Arkansas': {'Population': 3017825, 'Storm Likeliness': 0.65, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Tornado', 'Hail', 'Wind', 'Flood', 'Snow'], 'Unlikely Storms': ['Hurricane', 'Wildfire', 'Dust']},
    'California': {'Population': 39512223, 'Storm Likeliness': 0.6, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Wildfire', 'Flood', 'Wind', 'Hail', 'Snow'], 'Unlikely Storms': ['Dust', 'Tornado', 'Hurricane']},
    'Colorado': {'Population': 5085817, 'Storm Likeliness': 0.55, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Snow', 'Hail', 'Wind', 'Tornado', 'Flood'], 'Unlikely Storms': ['Dust', 'Hurricane', 'Wildfire']},
    'Connecticut': {'Population': 3565287, 'Storm Likeliness': 0.7, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Snow', 'Hail', 'Flood', 'Wind'], 'Unlikely Storms': ['Hurricane', 'Tornado', 'Wildfire', 'Dust']},
    'Delaware': {'Population': 973764, 'Storm Likeliness': 0.75, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Hurricane', 'Flood', 'Wind', 'Snow', 'Hail'], 'Unlikely Storms': ['Wildfire', 'Dust', 'Tornado']},
    'Florida': {'Population': 21538187, 'Storm Likeliness': 0.9, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Hurricane', 'Wind', 'Flood'], 'Unlikely Storms': ['Wildfire', 'Hail', 'Tornado', 'Dust', 'Snow']},
    'Georgia': {'Population': 10689881, 'Storm Likeliness': 0.75, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Hurricane', 'Tornado', 'Flood', 'Wind', 'Hail'], 'Unlikely Storms': ['Snow', 'Wildfire', 'Dust']},
    'Hawaii': {'Population': 1415872, 'Storm Likeliness': 0.5, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Hurricane', 'Wind', 'Flood'], 'Unlikely Storms': ['Tornado', 'Hail', 'Dust', 'Snow', 'Wildfire']},
    'Idaho': {'Population': 1839106, 'Storm Likeliness': 0.4, 'Most Likely Storms': ['Snow', 'Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Wind', 'Hail', 'Wildfire'], 'Unlikely Storms': ['Flood', 'Tornado', 'Hurricane', 'Dust']},
    'Illinois': {'Population': 12671821, 'Storm Likeliness': 0.6, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Tornado', 'Wind', 'Flood', 'Hail', 'Snow'], 'Unlikely Storms': ['Hurricane', 'Wildfire', 'Dust']},
    'Indiana': {'Population': 6732219, 'Storm Likeliness': 0.65, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Tornado', 'Wind', 'Hail', 'Flood', 'Snow'], 'Unlikely Storms': ['Hurricane', 'Wildfire', 'Dust']},
    'Iowa': {'Population': 3155070, 'Storm Likeliness': 0.7, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Tornado', 'Wind', 'Hail', 'Snow'], 'Unlikely Storms': ['Hurricane', 'Flood', 'Wildfire', 'Dust']},
    'Kansas': {'Population': 2913314, 'Storm Likeliness': 0.8, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Tornado', 'Hail', 'Wind', 'Flood', 'Snow'], 'Unlikely Storms': ['Hurricane', 'Wildfire', 'Dust']},
    'Kentucky': {'Population': 4467673, 'Storm Likeliness': 0.65, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Tornado', 'Wind', 'Flood', 'Hail', 'Snow'], 'Unlikely Storms': ['Hurricane', 'Wildfire', 'Dust']},
    'Louisiana': {'Population': 4648794, 'Storm Likeliness': 0.90, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Hurricane', 'Wind', 'Flood', 'Tornado', 'Hail'], 'Unlikely Storms': ['Snow', 'Wildfire', 'Dust']},
    'Maine': {'Population': 1344212, 'Storm Likeliness': 0.6, 'Most Likely Storms': ['Snow', 'Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Wind', 'Flood', 'Hail'], 'Unlikely Storms': ['Hurricane', 'Tornado', 'Wildfire', 'Dust']},
    'Maryland': {'Population': 6045680, 'Storm Likeliness': 0.75, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Hurricane', 'Snow', 'Wind', 'Flood', 'Hail'], 'Unlikely Storms': ['Wildfire', 'Tornado', 'Dust']},
    'Massachusetts': {'Population': 6892503, 'Storm Likeliness': 0.7, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Snow', 'Wind', 'Hail', 'Flood'], 'Unlikely Storms': ['Hurricane', 'Wildfire', 'Tornado', 'Dust']},
    'Michigan': {'Population': 9986857, 'Storm Likeliness': 0.7, 'Most Likely Storms': ['Snow', 'Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Wind', 'Flood', 'Hail'], 'Unlikely Storms': ['Hurricane', 'Tornado', 'Wildfire', 'Dust']},
    'Minnesota': {'Population': 5639632, 'Storm Likeliness': 0.65, 'Most Likely Storms': ['Snow', 'Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Tornado', 'Wind', 'Hail', 'Flood'], 'Unlikely Storms': ['Hurricane', 'Wildfire', 'Dust']},
    'Mississippi': {'Population': 2976149, 'Storm Likeliness': 0.7, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Hurricane', 'Wind', 'Tornado', 'Hail', 'Flood'], 'Unlikely Storms': ['Wildfire', 'Snow', 'Dust']},
    'Missouri': {'Population': 6137428, 'Storm Likeliness': 0.75, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Tornado', 'Hail', 'Wind', 'Flood', 'Snow'], 'Unlikely Storms': ['Hurricane', 'Dust']},
    'Montana': {'Population': 1068778, 'Storm Likeliness': 0.45, 'Most Likely Storms': ['Snow', 'Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Wind', 'Hail', 'Wildfire'], 'Unlikely Storms': ['Hurricane', 'Flood', 'Tornado', 'Dust']},
    'Nebraska': {'Population': 1934408, 'Storm Likeliness': 0.75, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Tornado', 'Wind', 'Hail', 'Snow'], 'Unlikely Storms': ['Hurricane', 'Dust']},
    'Nevada': {'Population': 3080156, 'Storm Likeliness': 0.45, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Wind', 'Hail', 'Snow', 'Wildfire', 'Dust'], 'Unlikely Storms': ['Tornado', 'Flood', 'Hurricane']},
    'New Hampshire': {'Population': 1359711, 'Storm Likeliness': 0.6, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm', 'Snow'], 'Likely Storms': ['Wind', 'Flood', 'Hail'], 'Unlikely Storms': ['Hurricane', 'Tornado', 'Wildfire', 'Dust']},
    'New Jersey': {'Population': 8882190, 'Storm Likeliness': 0.75, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Wind', 'Snow', 'Flood', 'Hail', 'Hurricane'], 'Unlikely Storms': ['Tornado', 'Dust', 'Wildfire']},
    'New Mexico': {'Population': 2096829, 'Storm Likeliness': 0.5, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Tornado', 'Wind', 'Hail', 'Flood', 'Wildfire', 'Dust'], 'Unlikely Storms': ['Snow', 'Hurricane']},
    'New York': {'Population': 19453561, 'Storm Likeliness': 0.7, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm', 'Snow'], 'Likely Storms': ['Wind', 'Flood', 'Hail'], 'Unlikely Storms': ['Tornado', 'Wildfire', 'Dust', 'Hurricane']},
    'North Carolina': {'Population': 10488084, 'Storm Likeliness': 0.8, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Hurricane', 'Wind', 'Tornado', 'Hail', 'Flood', 'Snow'], 'Unlikely Storms': ['Wildfire', 'Dust']},
    'North Dakota': {'Population': 762062, 'Storm Likeliness': 0.45, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm', 'Snow'], 'Likely Storms': ['Wind', 'Tornado', 'Hail'], 'Unlikely Storms': ['Flood', 'Wildfire', 'Dust', 'Hurricane']},
    'Ohio': {'Population': 11689100, 'Storm Likeliness': 0.7, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Wind', 'Hail', 'Tornado', 'Flood', 'Snow'], 'Unlikely Storms': ['Wildfire', 'Dust', 'Hurricane']},
    'Oklahoma': {'Population': 3956971, 'Storm Likeliness': 0.80, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Tornado', 'Hail', 'Wind', 'Flood', 'Snow'], 'Unlikely Storms': ['Wildfire', 'Dust', 'Hurricane']},
    'Oregon': {'Population': 4217737, 'Storm Likeliness': 0.5, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm', 'Snow'], 'Likely Storms': ['Wind', 'Hail', 'Wildfire'], 'Unlikely Storms': ['Flood', 'Tornado', 'Dust', 'Hurricane']},
    'Pennsylvania': {'Population': 12801989, 'Storm Likeliness': 0.6, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Wind', 'Hail', 'Flood', 'Tornado', 'Snow'], 'Unlikely Storms': ['Wildfire', 'Dust', 'Hurricane']},
    'Rhode Island': {'Population': 1059361, 'Storm Likeliness': 0.6, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Wind', 'Hail', 'Snow', 'Flood'], 'Unlikely Storms': ['Tornado', 'Wildfire', 'Dust', 'Hurricane']},
    'South Carolina': {'Population': 5148714, 'Storm Likeliness': 0.85, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Hurricane', 'Wind', 'Tornado', 'Flood', 'Hail'], 'Unlikely Storms': ['Wildfire', 'Snow', 'Dust']},
    'South Dakota': {'Population': 884659, 'Storm Likeliness': 0.5, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm', 'Snow'], 'Likely Storms': ['Wind', 'Tornado', 'Hail'], 'Unlikely Storms': ['Flood', 'Wildfire', 'Dust', 'Hurricane']},
    'Tennessee': {'Population': 6829174, 'Storm Likeliness': 0.7, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Snow', 'Wind', 'Tornado', 'Hail', 'Flood'], 'Unlikely Storms': ['Dust', 'Wildfire']},
    'Texas': {'Population': 29145505, 'Storm Likeliness': 0.75, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Hurricane', 'Wind', 'Tornado', 'Hail', 'Flood'], 'Unlikely Storms': ['Wildfire', 'Snow', 'Dust']},
    'Utah': {'Population': 3205958, 'Storm Likeliness': 0.5, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Wind', 'Hail', 'Wildfire', 'Snow', 'Dust'], 'Unlikely Storms': ['Tornado', 'Flood', 'Hurricane']},
    'Vermont': {'Population': 623989, 'Storm Likeliness': 0.6, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm', 'Snow'], 'Likely Storms': ['Wind', 'Flood', 'Hail'], 'Unlikely Storms': ['Tornado', 'Wildfire', 'Dust', 'Hurricane']},
    'Virginia': {'Population': 8535519, 'Storm Likeliness': 0.75, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Wind', 'Hurricane', 'Tornado', 'Flood', 'Snow', 'Hail'], 'Unlikely Storms': ['Wildfire', 'Dust']},
    'Washington': {'Population': 7693612, 'Storm Likeliness': 0.65, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm', 'Snow'], 'Likely Storms': ['Wind', 'Hail', 'Wildfire'], 'Unlikely Storms': ['Flood', 'Tornado', 'Dust', 'Hurricane']},
    'West Virginia': {'Population': 1792147, 'Storm Likeliness': 0.7, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm'], 'Likely Storms': ['Snow', 'Wind', 'Flood', 'Hail'], 'Unlikely Storms': ['Wildfire', 'Tornado', 'Dust', 'Hurricane']},
    'Wisconsin': {'Population': 5822434, 'Storm Likeliness': 0.7, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm', 'Snow'], 'Likely Storms': ['Wind', 'Hail', 'Flood', 'Tornado'], 'Unlikely Storms': ['Wildfire', 'Dust', 'Hurricane']},
    'Wyoming': {'Population': 578759, 'Storm Likeliness': 0.45, 'Most Likely Storms': ['Heavy Rain', 'Thunderstorm', 'Snow'], 'Likely Storms': ['Wind', 'Hail', 'Wildfire'], 'Unlikely Storms': ['Flood', 'Tornado', 'Dust', 'Hurricane']}
}

state_county_counts = df.groupby('State')['County'].nunique().to_dict()

def estimate_state_total_claims(year, state):
    population = state_data[state]['Population']
    storm_likeliness = state_data[state]['Storm Likeliness']
    
    claims = 1000
    claims *= (np.log(year - 1970) / np.log(2023 - 1970))
    claims *= ((population / 39512223) * 0.5 + 1)
    claims  *= ((storm_likeliness ** 3) + 0.5)
    
    return round(claims, 2)

def distribute_claims_to_counties(state_total_claims, counties):    
    claim_list = np.random.lognormal(mean=0.1, sigma=1.0, size=counties)
    np.random.shuffle(claim_list)
    claim_list = claim_list / np.sum(claim_list) * state_total_claims
    claim_list += np.random.randint(-5, 6, size=counties)
    claim_list = np.abs(claim_list)
    claim_list = claim_list / np.sum(claim_list) * state_total_claims
    claim_list = np.round(claim_list)
    
    num_zeros = int(counties * 0.2)
    zeros = np.zeros(num_zeros)
    claim_list = claim_list.tolist()
    claim_list = claim_list[:counties - num_zeros] + zeros.tolist()
        
    np.random.shuffle(claim_list)
    
    return claim_list

def estimate_dollars_paid(claims_paid):
    
    dollars = 5000 * claims_paid * np.random.lognormal(mean=0, sigma=0.5)
        
    return round(dollars, 2)

def estimate_total_storms(claims_paid):
    return max(1, round(claims_paid * np.random.uniform(0.1, 0.8) + np.random.uniform(0, 2)))

def distribute_storms(state, total_storms):
    storms = ['Dust', 'Flood', 'Hail', 'Hurricane', 'Heavy Rain', 'Snow', 'Thunderstorm', 'Tornado', 'Wildfire', 'Wind']
    
    distributed_storms = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
    for storm in range(total_storms):
        probability = np.random.uniform(0.0, 1.0)
                        
        if probability < 0.80:
            weights = np.linspace(1.5, 1, len(state_data[state]['Most Likely Storms']))
            weights = weights / np.sum(weights)
            distributed_storms[storms.index(np.random.choice(state_data[state]['Most Likely Storms'], p=weights))] += 1
        elif probability < 0.99:
            weights = np.linspace(1.5, 1, len(state_data[state]['Likely Storms']))
            weights = weights / np.sum(weights)
            distributed_storms[storms.index(np.random.choice(state_data[state]['Likely Storms'], p=weights))] += 1
        else:
            weights = np.linspace(1.5, 1, len(state_data[state]['Unlikely Storms']))
            weights = weights / np.sum(weights)
            distributed_storms[storms.index(np.random.choice(state_data[state]['Unlikely Storms'], p=weights))] += 1
            
    return distributed_storms

for year in tqdm(range(1980, 2024), desc="Processing Years"):
    for state in state_data:
        state_total_claims = estimate_state_total_claims(year, state)
        
        counties = state_county_counts[state]
        
        county_claims = distribute_claims_to_counties(state_total_claims, counties)
                
        state_df = df[(df['Year'] == year) & (df['State'] == state)]
        
        if len(state_df) != counties:
            raise ValueError(f"Mismatch in county count for {state} in {year}: Expected {counties}, found {len(state_df)}")
        
        for county_idx, (county_index, _) in enumerate(state_df.iterrows()):
            claims_paid = int(county_claims[county_idx])
            dollars_paid = estimate_dollars_paid(claims_paid)
            total_storms = estimate_total_storms(claims_paid)
            distributed_storms = distribute_storms(state, total_storms)
            df.at[county_index, 'Claims Paid'] = claims_paid
            df.at[county_index, 'Dollars Paid'] = dollars_paid
            df.at[county_index, 'Total Storms'] = total_storms
            df.at[county_index, 'Dust'] = distributed_storms[0]
            df.at[county_index, 'Flood'] = distributed_storms[1]
            df.at[county_index, 'Hail'] = distributed_storms[2]
            df.at[county_index, 'Hurricane'] = distributed_storms[3]
            df.at[county_index, 'Heavy Rain'] = distributed_storms[4]
            df.at[county_index, 'Snow'] = distributed_storms[5]
            df.at[county_index, 'Thunderstorm'] = distributed_storms[6]
            df.at[county_index, 'Tornado'] = distributed_storms[7]
            df.at[county_index, 'Wildfire'] = distributed_storms[8]
            df.at[county_index, 'Wind'] = distributed_storms[9]

df.to_csv('data/combined/data_03.csv', index=False)

print("Dataset updated successfully!")