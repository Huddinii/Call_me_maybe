from huggingface_hub import inspect_job
from llm_sdk import Small_LLM_Model
import numpy
import json


def main() -> None:
    llm = Small_LLM_Model()
    # vocab = json.load(open(llm.get_path_to_vocab_file(), "r"))
    # print(vocab)
    test = llm.encode("What is the sum of 2 and 3?")
    in_ids: list[int] = test[0].tolist()
    with open(llm.get_path_to_vocab_file()) as f:
        print(f.readline())
    generated = []
    # for _ in range(200):
    #     logits = llm.get_logits_from_input_ids(in_ids)
    #     next_id = max(range(len(logits)), key=logits.__getitem__)
    #     next_id = logits.index(max(logits))
    #     next_id = numpy.argmax(logits)
    #     in_ids.append(next_id)
    #     generated.append(next_id)
    # print(llm.decode(generated))
    # with open('out.txt', 'w') as f:
    #     print(output, file=f)
    # print(llm.decode(test))
    # print(llm.get_path_to_vocab_file())
