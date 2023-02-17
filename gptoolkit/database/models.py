"""This module provides the database models for GPT-3 prompts, engines,
use-cases and parameters using SQLAlchemy."""

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Prompt(Base):
    """Class to define the prompts table in the database.

    Attributes:
        id (int): The ID of the prompt.
        text (str): The text of the prompt.
    """

    __tablename__ = 'prompts'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)


class Engine(Base):
    """Class to define the engines table in the database.

    Attributes:
        id (int): The ID of the engine.
        name (str): The name of the engine.
        api_key (str): The API key of the engine.
    """

    __tablename__ = 'engines'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    api_key = Column(String, nullable=False)


class UseCase(Base):
    """Class to define the use cases table in the database.

    Attributes:
        id (int): The ID of the use case.
        name (str): The name of the use case.
        description (str): The description of the use case.
    """

    __tablename__ = 'use_cases'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)


class Parameter(Base):
    """Class to define the parameters table in the database.

    Attributes:
        id (int): The ID of the parameter.
        prompt_id (int): The ID of the prompt.
        engine_id (int): The ID of the engine.
        use_case_id (int): The ID of the use case.
        max_tokens (int): The maximum number of tokens to generate.
        temperature (float): The sampling temperature to use.
        prompt (Prompt): The prompt associated with this parameter.
        engine (Engine): The engine associated with this parameter.
        use_case (UseCase): The use case associated with this parameter.
    """

    __tablename__ = 'parameters'

    id = Column(Integer, primary_key=True)
    prompt_id = Column(Integer, ForeignKey('prompts.id'), nullable=False)
    engine_id = Column(Integer, ForeignKey('engines.id'), nullable=False)
    use_case_id = Column(Integer, ForeignKey('use_cases.id'), nullable=False)
    max_tokens = Column(Integer, nullable=False)
    temperature = Column(Float, nullable=False)

    prompt = relationship('Prompt', backref='parameters')
    engine = relationship('Engine', backref='parameters')
    use_case = relationship('UseCase', backref='parameters')

