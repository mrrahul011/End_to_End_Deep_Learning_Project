from dataclasses import dataclass
import pathlib


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: pathlib.Path
    source_URL: str
    local_data_file: pathlib.Path
    unzip_dir: pathlib.Path