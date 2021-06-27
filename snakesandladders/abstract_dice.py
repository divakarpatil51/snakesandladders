from abc import ABC, abstractmethod


class AbstractDice(ABC):

    @staticmethod
    @abstractmethod
    def roll():
        raise NotImplementedError("Child class must implement this method.")
