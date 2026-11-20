from pydantic import BaseModel, ConfigDict
from llm_sdk import Small_LLM_Model


class Functions(BaseModel):
    name: str
    description: str
    parameters: dict[str, dict[str, str]]
    returns: dict[str, str]

    def __str__(self) -> str:
        return f"name: {self.name}, description: {self.description}," \
               f"parameters: {str(self.parameters)}, returns: " \
                   f"{str(self.returns)}"


class Available(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    tasks: list[dict[str, str]]
    functions: list[Functions]
    llm: Small_LLM_Model
    out: str

    def __str__(self) -> str:
        return str(self.tasks) + "\n" + str(self.functions)
