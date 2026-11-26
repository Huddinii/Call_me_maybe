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
            # out_ids = []
            prompt, name = self.get_name(prompt)
            result.update(name)
            parameter = self.get_parameters(prompt, t,
                                            [f for f in self.functions
                                             if f.name == name][0])
            result.update(parameter)
            # in_ids = self.llm.encode(prompt)[0].tolist()
            # logits = self.llm.get_logits_from_input_ids(in_ids)
            # next_id = numpy.argmax(logits)
            # in_ids.append(next_id)
            # out_ids.append(next_id)
            out.append(result)
            # print(self.llm.decode(out_ids))

    def get_name(self, prompt: str) -> tuple[str, dict[str, str]]:
        # encode function names
        # compare next logit to function name ids
        # add result to list if compare is true
        # update prompt with next id
        # return final prompt and result
        ...

    def get_parameters(self, prompt: str, task: dict[str, str],
                       func: str) -> dict[str, Any]:
        # encode task
        # compare next logit to task ids
        # if correct check if return fits the function parameter type
        # if all parameters filled return result
        ...
