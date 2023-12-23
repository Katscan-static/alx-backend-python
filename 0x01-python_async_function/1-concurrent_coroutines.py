#!/usr/bin/python3
"""
    This module runc comcurrent routines
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
        wait_n:
            routine returns a list of concurrent routines

        Args:
            n (int): number of routines
            max_delay (int): max delay

        Returns:
            list: List of all concurrent routines
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delayi = await task
        delays.append(delay)
    return delays
