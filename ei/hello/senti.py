from janome.tokenizer import Tokenizer

# 極性辞書の作成
dict_polarity = {}
with open('/home/kanata/ei/hello/pn_ja.txt', 'r') as f:
    line = f.read()
    lines = line.split('\n')
    for i in range(len(lines)):
        line_components = lines[i].split(':')
        dict_polarity[line_components[0]] = line_components[3]

# 否定語リストの作成
not_list = ['ではない','じゃない','ない', 'ず', 'ん', 'ません', 'なく', 'ぬ', '非', '未', '無', '否定的', '否決', '禁止', '禁じる', '拒否', '拒む', '反対', '許さ', '許可', '許す']

# ネガポジ分析用の関数の作成
def judge_polarity(text):
    t = Tokenizer()
    #形態素解析
    tokens = list(t.tokenize(text)) # ジェネレーターからリストに変換
    pol_val = 0
    for i in range(len(tokens)):
        word = tokens[i].surface
        pos = tokens[i].part_of_speech.split(',')[0]
        if word in not_list:
            # 否定語リストに含まれる場合は極性値を反転させる
            if any(neg in tokens[max(0,i-2):i] for neg in not_list):
                pol_val = -float(dict_polarity[word])
            else:
                pol_val = float(dict_polarity[word])

    if any(neg in text for neg in not_list):
        pol_val = pol_val
                
    




