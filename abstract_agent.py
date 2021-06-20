from abc import ABC, abstractmethod
from dice import roll_dice
from player import Player
from player_agent import PlayerAgent
from guard_agent import GuardAgent
from tile import Tile
from typing import List, Union
import random

FISTS = 2
KNIFE = 4
GUN = 6
BANANA = 9000

#stash move

class AbstractAgent(ABC):
    def __init__(self, position) -> None:
        self.position = position
        self.hp = 10
        self.total_hp = 10
        self.gold = 0
        self.weapon = KNIFE
        self.is_dead = False
        self.attack_dice = (2, 8)
        self.defence = 12

    def look_around(self) -> List[List[Tile]]:
        """Looks around and returns a 2D array of tiles around"""
        # TODO: Add look around code
        pass

    def listen(self) -> List[List[Tile]]:
        """Listens and returns a 2D array of objects heard"""
        # TODO: Add listen code
        pass

    def fight(self, agent: Union[GuardAgent, PlayerAgent, Player]) -> Union[GuardAgent, PlayerAgent, Player]:
        """Fight another agent

        Args:
            agent (Union[GuardAgent, PlayerAgent, Player]): The agent this agent is fighting against

        Returns:
            Union[GuardAgent, PlayerAgent, Player]: The agent fought and any damage/death done
        """

        # TODO: Add fight code

        self_attack = roll_dice(*self.attack_dice)
        agent_attack = roll_dice(*agent.attack_dice)

        self_damage = self.__get_damage()
        agent_damage = agent.__get_damage()

        # Player always gets priority
        if agent.defence <= self_attack:
            agent.__take_damage(self_damage)

        if not agent.is_dead and self.defence <= agent_attack:
            self.__take_damage(agent_damage)

        return agent

    def __take_damage(self, damage: int):
        """Take damage and calculate death

        Args:
            damage (int): The damge done to self
        """
        self.hp -= damage
        if self.hp <= 0:
            self.is_dead = True

    def __get_damage(self) -> int:
        """Get damage to be dealt by weapon

        Returns:
            int: The damage that can be dealt
        """
        

        # Shouldn't get here, but in case...
        return self.weapon

    def draw(self):
        # If we want the agents to draw themselves, do it here
        pass

    def get_perceived_power(self) -> int:
        """Returns the perceived power other agents will see you at.
        Perceived health is good (100%), wounded (75%), and bloodied
        (33%).

        Returns:
            int: The perceived power others will see you at
        """
        hp_percent = self.hp / self.total_hp
        hp_perceived = 0
        if hp_percent >= 0.75:
            hp_perceived = int(self.total_hp)
        elif hp_percent >= 0.333:
            hp_perceived = int(self.total_hp * 0.75)
        else:
            hp_perceived = int(self.total_hp * 0.333)
        
        return hp_perceived + self.weapon

