#!/usr/bin/env python3
"""
    This module performs a asynchronous task
    wait_random - returns float
    args: delay is an integer
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it.

    This function generates a random float between 0 and max_delay (inclusive),
    waits for that amount of time asynchronously, and then returns the value.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay time that was waited.

    Raises:
        ValueError: If max_delay is less than 0.

    Example:
        delay = await wait_random(5)
        print(f"Waited for {delay} seconds")
    """
    if max_delay < 0:
        raise ValueError("max_delay must be non-negative")

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


# Example usage
async def main():
    print("Starting...")
    result = await wait_random(5)
    print(f"Waited for {result:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
