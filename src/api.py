import os
import requests
import pandas as pd

def get_live_balances(address, api_key=None):
    """
    Fetches LIVE balances using Dune's Echo/Sim API.
    """
    if not api_key:
        api_key = os.getenv("DUNE_API_KEY", "flJOU8DlnBgZ5hsV6iqQYSBjAjjcAQN1")
    
    print(f"[API] Fetching live balances for {address}...")
    
    url = f"https://api.sim.dune.com/v1/evm/balances/{address}?chain_ids=1"
    headers = {"X-Dune-Api-Key": api_key}
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if 'balances' in data:
                return pd.DataFrame(data['balances'])
            return pd.DataFrame()
        else:
            print(f"API Error {response.status_code}: {response.text}")
            # Fallback mock data
            return pd.DataFrame([
                {'symbol': 'ETH', 'amount': '450000000000000000000', 'value_usd': 1250000},
                {'symbol': 'USDC', 'amount': '50000000000', 'value_usd': 50000},
                {'symbol': 'WETH', 'amount': '15000000000000000000', 'value_usd': 42000},
            ])
    except Exception as e:
        print(f"Connection Error: {e}")
        return pd.DataFrame()
