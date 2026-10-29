def verify_api_key(key: str) -> bool:
    if not key or len(key.strip()) == 0:
        return False
    return key.startswith("sk_live_")
