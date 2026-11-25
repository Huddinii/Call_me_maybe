from pydantic import BaseModel, ConfigDict
from llm_sdk import Small_LLM_Model
from typing import Any
import json
import numpy


class Functions(BaseModel):
    name: str
    description: str
    parameters: dict[str, dict[str, str]]
    returns: dict[str, str]

    def __dict__(self) -> dict[Any]:
        return {"name": self.name, "description": self.description,
                "parameters": self.parameters, "returns": self.returns}


class StructuredOut(BaseModel):
    prompt: str
    name: str
    parameters: dict[str, Any]

    def __dict__(self) -> dict[Any]:
        return {"prompt": self.prompt, "name": self.name,
                "parameters": self.parameters}


class Available(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    tasks: list[dict[str, str]]
    functions: list[Functions]
    llm: Small_LLM_Model
    out_path: str

    def __str__(self) -> str:
        func = ""
        for f in self.functions:
            func = func + str(vars(f)) + "\n"
        return str(self.tasks) + "\n" + str(func)

    def generate_json(self) -> None:
        out = []
        sum_fn = self.llm.encode("fn_sum")
        print(sum_fn)
        ids = sum_fn[0].tolist()
        print(self.llm.decode(ids[0]), self.llm.decode(ids[1]))
        constraints = [(5, "name:"), (100, "parameters:")]
        for t in self.tasks:
            result = {"prompt": t['prompt']}
            prompt = (f"Choose the best matching function and extract its"
                      " arguments.\nAvailable functions:"
                      f"{json.dumps([vars(f) for f in self.functions])}"
                      f"\nTask: {t['prompt']}\n")
            out_ids = []
            for c in constraints:
                in_ids = self.llm.encode(prompt + c)[0].tolist()
                logits = self.llm.get_logits_from_input_ids(in_ids)
                next_id = numpy.argmax(logits)
                in_ids.append(next_id)
                out_ids.append(next_id)
            out.append(result)
            print(self.llm.decode(out_ids))
