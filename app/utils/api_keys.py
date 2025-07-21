from app.models.api_key import APIKey

def get_api_key(service_name: str) -> str | None:
    """Fetch and decrypt the API key for a given service."""
    service = service_name.strip().lower()
    key = APIKey.query.filter_by(service_name=service).first()
    if key:
        try:
            return key.get_key()
        except Exception:
            return None
    return None

# Optional helpers
def get_openai_key() -> str | None:
    return get_api_key("openai")

def get_shopify_token() -> str | None:
    return get_api_key("shopify")

def get_meta_ads_token() -> str | None:
    return get_api_key("meta_ads")
