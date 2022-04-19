from typing import Any, Dict, Optional


def rename_keys(
    original_dict: Dict[str, Any], key_mapping: Dict[str, Optional[str]]
) -> Dict[str, Any]:
    """Renames keys in the dictionary using the key_mapping. If the value in key_mapping is None then it will remove the key entirely"""
    return {
        key_mapping.get(k, k): v
        for k, v in original_dict.items()
        if k not in key_mapping or key_mapping[k] is not None
    }
