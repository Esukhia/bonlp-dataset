import argparse
from pathlib import Path
from tqdm import tqdm
import json
import jsonpickle as jp
jp.set_encoder_options('simplejson', sort_keys=True, indent=4, ensure_ascii=False)


def export_to_lighttag(fn):
    text = fn.read_text()
    examples = text.split('\n')[:-1]

    all_examples = []
    for i, e in enumerate(examples):
        example = {'order': i, 'ex': e}
        all_examples.append(example)

    return all_examples, len(all_examples)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--path", type=str, help="path to corpus")
    args = ap.parse_args()

    path = Path(args.path)
    lists = path/'lists.txt'
    citations = path/'citations.txt'
    
    list_exs, n_lists = export_to_lighttag(lists)
    citation_exs, n_citations = export_to_lighttag(citations)
    
    #citations from ebook
    pre_citations = path/'citations.json'
    if pre_citations.is_file():
        with pre_citations.open() as f:
            citations_json = json.load(f)
    if citations_json:
        citation_exs.extend(citations_json)
        n_citations += len(citations_json)

    output_path = path.parent/'toupload'
    output_fn = output_path/f'lists-{n_lists}_citations-{n_citations}.json'

    print('[INFO] Exporting to', output_fn)
    all_examples = list_exs + citation_exs
    print('[INFO] No. of examples:', len(all_examples))
    output_fn.write_text(jp.dumps(all_examples))

