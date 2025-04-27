import json
from tqdm import tqdm

for x in ['dev', 'train', 'test']:
    with open(f'data/{x}.stanford.json', 'r') as new:
        new_lines = new.readlines()
        with open(f'data/{x}.stanford_new.json', 'w') as out:
            for new_line in tqdm(new_lines):
                new_dict = {'sentences': [{'index': 0, 'line': 1}]}
                b = json.loads(new_line)
                new_dict['sentences'][0]['basicDependencies'] = []
                new_dict['sentences'][0]['tokens'] = []
                for i, word in enumerate(b['word']):
                    governor = b['head_id'][i]
                    dep = b['dep_label'][i]
                    dep_id = i + 1
                    if governor != 0:
                        governor_gloss = b['word'][governor - 1]
                    else:
                        governor_gloss = word
                    dependent_gloss = word

                    dep_dict = {'dep': dep, 'governor': governor, 'governorGloss': governor_gloss, 'dependent': dep_id,
                                'dependentGloss': dependent_gloss}
                    token_dict = {'index': i, 'word': word, 'originalText': word}
                    new_dict['sentences'][0]['basicDependencies'].append(dep_dict)
                    new_dict['sentences'][0]['tokens'].append(token_dict)
                new_dict['ori_sentence'] = b['ori_sentence']
                new_dict['word'] = b['word']
                real_seq_label = []
                c=0
                for seq in b['sequence_label']:
                    if 'B-s' not in seq:
                        real_seq_label.append(seq)
                    else:
                        real_seq_label.append('V')
                        c+=1
                assert c==1
                new_dict['sequence_label'] = b['sequence_label']
                new_dict['syn_label'] = b['syn_label']
                new_dict['ori_syn_label'] = b['ori_syn_label']
                new_dict['pos_label'] = b['pos_label']
                # print(new_dict.keys())
                json.dump(new_dict, out)
                out.write('\n')