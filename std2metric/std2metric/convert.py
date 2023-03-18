import argparse
import asyncio

parser = argparse.ArgumentParser(
    prog="Convert various standard/imperial measurements to metric and vice versa",
    description="What the program does",
    epilog="Text at the bottom of help",
)

ML_TO_OZ = 0.03381402


async def main(*args, **kwargs):
    pass


if __name__ == "__main__":
    asyncio.run(
        main(),
    )
