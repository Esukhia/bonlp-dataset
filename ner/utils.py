from pathlib import Path


def find_context(sentence, path):

    def _left_context(idx, sentence, text):
        chunks = text[:idx].split(' ')
        return ' '.join(chunks[-3:])

    def _right_context(idx, sentence, text):
        chunks = text[idx+len(sentence):].split(' ')
        return ' '.join(chunks[:3])

    contexts = []
    fns = path.glob('*.txt')
    for fn in fns:
        text = fn.read_text()
        idx = text.find(sentence)
        if idx >= 0:
            l_context = _left_context(idx, sentence, text)
            r_context = _right_context(idx, sentence, text)
            sentence_with_context = l_context + sentence + r_context
            return sentence_with_context
    return sentence


if __name__ == "__main__":
    path = Path('../data/corpus/derge-kangyur')
    sentence = "གསུམ་པོ་དེ་དག་གང་ཞེ་ན། ཕ་དང་མ་གཉིས་ཆགས་པར་གྱུར་ཅིང་འདུས་པ་དང་། མ་དུས་ལ་བབ་ཅིང་ཟླ་མཚན་དང་ལྡན་པ་དང་། དྲི་ཟ་ཉེ་བར་གནས་ཤིང་འཇུག་པར་འདོད་པ་སྟེ།"
    sentence_with_context = find_context(sentence, path)
    print(sentence_with_context)
