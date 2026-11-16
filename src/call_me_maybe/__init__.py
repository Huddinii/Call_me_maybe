from llm_sdk import Small_LLM_Model


def main() -> None:
    llm = Small_LLM_Model()
    test = llm.encode("Teststring")
    print(test)
    out = llm.decode(test)
    print(out)
