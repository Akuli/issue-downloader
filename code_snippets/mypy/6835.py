from typing import Optional

def get_org_id(org_name: str) -> str:
    return 'some_org_id'

def create(org_name: Optional[str], org_id: Optional[str]):
    if not org_name and not org_id:
        raise ValueError('No org specified')
    if not org_id:
        org_id = get_org_id(org_name)
