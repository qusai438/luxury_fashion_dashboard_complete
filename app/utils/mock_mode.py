import os

def is_simulation():
    return os.getenv("SIMULATION_MODE", "False").lower() == "true"

def simulate_value(label=""):
    return f"🧪 Simulated: {label}"

def simulate_response(data=None, label="Response"):
    return data or {"status": "ok", "message": f"🧪 Simulated {label}"}

def get_api_key(service_name):
    if is_simulation():
        return simulate_value(f"{service_name}_api_key")
    from ..services.api_key_manager import get_api_key_real  # if exists
    return get_api_key_real(service_name)
