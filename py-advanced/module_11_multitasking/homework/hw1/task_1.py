import logging
import threading
import random
import time

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


class Philosopher(threading.Thread):
    running = True  # used to check if everyone is finished eating

    def __init__(self, left_fork: threading.Lock, right_fork: threading.Lock):
        super().__init__()
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.running:
            logger.info(f'Philosopher {self.getName()} start thinking.')
            # Philosopher is thinking (but really is sleeping).
            time.sleep(random.randint(1, 10))
            logger.info(f'Philosopher {self.getName()} is hungry.')

            with self.left_fork:
                logger.info(f'Philosopher {self.getName()} acquired left fork')
                if self.right_fork.locked():
                    continue
                with self.right_fork:
                    logger.info(f'Philosopher {self.getName()} acquired right fork')
                    self.dining()

    def dining(self):
        logger.info(f'Philosopher {self.getName()} starts eating.')
        time.sleep(random.randint(1, 10))
        logger.info(f'Philosopher {self.getName()} finishes eating and leaves to think.')


def main():
    forks = [threading.Lock() for n in range(5)]  # initialising array of Lock's i.e forks

    # here (i+1)%5 is used to get right and left forks circularly between 1-5
    philosophers = [
        Philosopher(forks[i % 5], forks[(i + 1) % 5])
        for i in range(5)
    ]
    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(200)
    Philosopher.running = False
    logger.info("Now we're finishing.")


if __name__ == "__main__":
    main()
