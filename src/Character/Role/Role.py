from abc import ABC, abstractmethod
class Role(ABC):

    def __init__(self, name):
        super().__init__()

        self.role_name: str = name
        self.base_status: "CharacterStatusDTO"

    @abstractmethod
    def get_base_status(self) -> "CharacterStatusDTO":
        pass

    @abstractmethod
    def get_level_progression(self) -> "CharacterStatusDTO":
        pass