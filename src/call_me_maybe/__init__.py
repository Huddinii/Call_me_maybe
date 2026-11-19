from llm_sdk import Small_LLM_Model
import json
import call_me_maybe.Model as Model


def main() -> None:
    llm = Small_LLM_Model()
    with open("data/input/function_calling_tests.json") as t:
        tasks = json.load(t)
    with open("data/input/functions_definition.json") as f:
        functions = json.load(f)
    # print(tasks)
    # print(functions)
    m = Model.Available(tasks=tasks, functions=functions, llm=llm)
    print(str(m))
    # vocab = json.load(open(llm.get_path_to_vocab_file(), "r"))
    # print(vocab)
    # test = llm.encode("What is the sum of 2 and 3?")
    # in_ids: list[int] = test[0].tolist()
    # with open(llm.get_path_to_vocab_file()) as f:
    #     print(f.readline())
    # generated = []
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
