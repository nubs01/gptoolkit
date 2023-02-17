"""This module provides a database class to store GPT-3 prompts, engines, use-cases and parameters using SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Prompt, Engine, UseCase, Parameter


class Database:
    """Class to manage the GPT-3 database.

    Attributes:
        session: The SQLAlchemy database session.
    """

    def __init__(self, db_file):
        """Creates a new instance of the Database class.

        Args:
            db_file (str): The filename of the database to use.
        """
        engine = create_engine(f'sqlite:///{db_file}')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def insert(self, prompt_text, engine_name, api_key, use_case_name, use_case_description, max_tokens=256, temperature=0.5):
        """Inserts a new parameter into the database.

        Args:
            prompt_text (str): The text of the prompt.
            engine_name (str): The name of the engine.
            api_key (str): The API key of the engine.
            use_case_name (str): The name of the use case.
            use_case_description (str): The description of the use case.
            max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 256.
            temperature (float, optional): The sampling temperature to use. Defaults to 0.5.
        """
        prompt = Prompt(text=prompt_text)
        self.session.add(prompt)
        self.session.flush()

        engine = Engine(name=engine_name, api_key=api_key)
        self.session.add(engine)
        self.session.flush()

        use_case = UseCase(name=use_case_name, description=use_case_description)
        self.session.add(use_case)
        self.session.flush()

        parameter = Parameter(prompt=prompt, engine=engine, use_case=use_case, max_tokens=max_tokens, temperature=temperature)
        self.session.add(parameter)
        self.session.commit()

    def query(self, prompt_text=None, engine_name=None, use_case_name=None):
        """Queries the database for matching parameters.

        Args:
            prompt_text (str, optional): The text of the prompt to match. Defaults to None.
            engine_name (str, optional): The name of the engine to match. Defaults to None.
            use_case_name (str, optional): The name of the use case to match. Defaults to None.

        Returns:
            list of dict: A list of matching parameters, with each element being a dictionary with keys 'prompt_text', 'engine_name', 'api_key', 'use_case_name', 'use_case_description', 'max_tokens', and 'temperature'.
        """
        query = (
            self.session.query(
                Prompt.text,
                Engine.name,
                Engine.api_key,
                UseCase.name,
                UseCase.description,
                Parameter.max_tokens,
                Parameter.temperature
            )
            .join(Prompt)
            .join(Engine)
            .join(UseCase)
        )

        if prompt_text is not None:
            query = query.filter(Prompt.text.ilike(f'%{prompt_text}%'))

        if engine_name is not None:
            query = query.filter(Engine.name.ilike(f'%{engine_name}%'))

        if use_case_name is not None:
            query = query.filter(UseCase.name.ilike(f'%{use_case_name}%'))

        rows = query.all()

        results = []
        for row in rows:
            result = {
                'prompt_text': row[0],
                'engine_name': row[1],
                'api_key': row[2],
                'use_case_name': row[3],
                'use_case_description': row[4],
                'max_tokens': row[5],
                'temperature': row[6]
            }
            results.append(result)

        return results

