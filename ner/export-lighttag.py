import argparse
from pathlib import Path
from tqdm import tqdm
import json
import jsonpickle as jp
jp.set_encoder_options('simplejson', sort_keys=True, indent=4, ensure_ascii=False)


def export_to_lighttag(fn, ex_type):
    text = fn.read_text()
    examples = text.split('\n')[:-1]

    all_examples = []
    for i, e in enumerate(examples):
        example = {'order': i, 'ex': e, 'type': ex_type}
        all_examples.append(example)

    return all_examples, len(all_examples)

def divide_into_2(l):
    mid = len(l) // 2
    return l[:mid], l[mid:]


if __name__ == "__main__":
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--path", type=str, help="path to corpus")
    args = ap.parse_args()

    path = Path(args.path)
    #lists = path/'lists.txt'
    citations = path/'citations.txt'
    
    #list_exs, n_lists = export_to_lighttag(lists, 'list')
    citation_exs, n_citations = export_to_lighttag(citations, 'citation')
    
    #citations from ebook
    pre_citations = path/'citations.json'
    if pre_citations.is_file():
        with pre_citations.open() as f:
            citations_json = json.load(f)
    if citations_json:
        citation_exs.extend(citations_json)
        n_citations += len(citations_json)


    n_citations = 1000
    citation_exs = citation_exs[n_citations:]
    output_fn = path.parent/'toupload'/f'citations-{n_citations}:.json'

    output_fn.write_text(jp.dumps(citation_exs))
