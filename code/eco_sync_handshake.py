# eco_sync_handshake.py
def eco_sync_handshake():
    metrics = {"energy_wh": 2.9, "co2_g": 4.34, "water_ml": 30}
    disclaimer = f"AI: ~{metrics['energy_wh']} Wh, {metrics['co2_g']} g CO₂, {metrics['water_ml']} mL water used. Justice for Boxtown. #GreenTreatyZero"
    return disclaimer
print(eco_sync_handshake())
