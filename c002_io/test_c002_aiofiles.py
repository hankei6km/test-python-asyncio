from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest
from c002_aiofiles import (
    async_create_file_with_data,
    async_create_multi_files_with_data,
    create_file_with_data,
    create_multi_files_with_data,
)

CREATE_FILE_SIZE = 2**28
CREATE_FILE_NUM = 10
#CREATE_FILE_NUM = 5


@pytest.fixture(scope="function")
def named_tempfile():
    fw = NamedTemporaryFile("w")
    yield fw
    fw.close()


@pytest.fixture(scope="function")
def named_tempfiles():
    # files = [NamedTemporaryFile(
    #     "w", dir="/tmp" if i % 2 == 0 else "/home/vscode/tmp") for i in range(CREATE_FILE_NUM)]
    # files = [NamedTemporaryFile("w", dir="/home/vscode/tmp")
    #          for _ in range(CREATE_FILE_NUM)]
    files = [NamedTemporaryFile("w") for _ in range(CREATE_FILE_NUM)]
    yield files
    for fw in files:
        fw.close()


@pytest.fixture(scope="module")
def huge_bytes():
    return b"\0" * CREATE_FILE_SIZE


# -----------------------------------------------------------
# 指定されたデータをファイルに書き込むテスト
# -----------------------------------------------------------
def test_create_file_with_data(benchmark, named_tempfile, huge_bytes):
    @benchmark
    def _():
        create_file_with_data(Path(named_tempfile.name), huge_bytes)


@pytest.mark.asyncio
async def test_async_create_file_with_data(aio_benchmark, named_tempfile, huge_bytes):
    @aio_benchmark
    async def _():
        await async_create_file_with_data(Path(named_tempfile.name), huge_bytes)


# -----------------------------------------------------------
# 指定されたデータを指定された数だけファイルに書き込むテスト
# -----------------------------------------------------------
def test_create_multi_files_with_data(benchmark, named_tempfiles, huge_bytes):
    @benchmark
    def _():
        create_multi_files_with_data(
            [Path(named_tempfile.name) for named_tempfile in named_tempfiles],
            huge_bytes,
        )


@pytest.mark.asyncio
async def test_async_create_multi_files_with_data(aio_benchmark, named_tempfiles, huge_bytes):
    @aio_benchmark
    async def _():
        await async_create_multi_files_with_data(
            [Path(named_tempfile.name) for named_tempfile in named_tempfiles],
            huge_bytes,
        )
