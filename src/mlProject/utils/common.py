import os
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
from src.mlProject import logger
import json
import joblib 
from ensure import ensure_annotations
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.

    Raises:
        ValueError: If the yaml file cannot be read or parsed.
        e: empty file or does not exist.    

    Returns:
        ConfigBox: ConfigBox object containing the yaml data.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise ValueError(f"yaml file: {path_to_yaml} cannot be loaded. Error: {e}")

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        ignore_log (bool, optional): ignore if multiple directories are created. Defaults to True.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")    

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        path (Path): Path to save the JSON file.
        data (dict): Dictionary to save as JSON.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns a ConfigBox object.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: data as class attributes instead of dictionary keys. This allows for dot notation access to the data.
    """
    with open(path, "r") as f:
        data = json.load(f)
    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data as a binary file using joblib.

    Args:
        data (Any): Data to save.
        path (Path): Path to save the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a binary file using joblib.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Loaded data.
    """
    data = joblib.load(filename=path)
    logger.info(f"Binary file loaded from: {path}")
    return data    

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in KB
    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"