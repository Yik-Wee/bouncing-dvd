import os
import asyncio

from helpers import clear_screen
from dvd import DVD


async def event_loop() -> None:
    dvd = DVD(min_colour=22, max_colour=51, boundaries=os.get_terminal_size())
    fps = 16
    frame_duration = 1 / fps

    while True:
        dvd.update_and_render(*os.get_terminal_size())
        await asyncio.sleep(frame_duration)
        clear_screen()


def main() -> None:
    try:  # run infinitely until keyboard interrupt
        asyncio.run(event_loop())
    except KeyboardInterrupt:
        clear_screen()
        return print('Quit successfully.')


if __name__ == '__main__':
    main()
