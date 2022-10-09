import asyncio
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import aiofiles

# -----------------------------------------------------------
# 指定されたデータをファイルに書き込む
# -----------------------------------------------------------


def create_file_with_data(path: Path, data: bytes) -> None:
    with path.open("wb") as f:
        f.write(data)


threadPool = ThreadPoolExecutor(max_workers=4)


async def async_create_file_with_data(path: Path, data: bytes) -> None:
    # async with aiofiles.open(path.as_posix(), "wb", executor=threadPool) as f:
    async with aiofiles.open(path.as_posix(), "wb") as f:
        await f.write(data)

# -----------------------------------------------------------
# 指定されたデータを指定された数だけファイルに書き込む
# -----------------------------------------------------------


def create_multi_files_with_data(paths: list[Path], data: bytes) -> None:
    for path in paths:
        create_file_with_data(path, data)


async def async_create_multi_files_with_data(paths: list[Path], data: bytes) -> None:
    await asyncio.gather(*[async_create_file_with_data(path, data) for path in paths])
