from llm_sdk import Small_LLM_Model
import json
import argparse
from .Model import Available


parser = argparse.ArgumentParser()
parser.add_argument('--functions_definition', nargs='?')
parser.add_argument('--input', nargs='?')
parser.add_argument('--output', nargs='?')
args = parser.parse_args()
try:
    with open(args.input) as t:
        tasks = json.load(t)
    with open(args.functions_definition) as f:
        functions = json.load(f)
    llm = Small_LLM_Model()
except FileNotFoundError as e:
    print(e)
except json.decoder.JSONDecodeError as e:
    print(e)
else:
    m = Available(tasks=tasks, functions=functions, llm=llm,
                  out_path=args.output)
    m.generate_json()


# parser.parse_args(['--input'])
# parser.parse_args(['--output'])
# llm = Small_LLM_Model()
# print(tasks)
# print(functions)
# m = Model.Available(tasks=tasks, functions=functions, llm=llm)
# print(str(m))
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
