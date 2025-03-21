import requests
from pathlib import Path

def download_to_local(url:str, out_path:Path, parent_make_dir:bool=True):
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path} must be a valid pathlib.Path object")
    if parent_make_dir:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        #* Write the file in binary mode to prevent new line conversions
        out_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return False