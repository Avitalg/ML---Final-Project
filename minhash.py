from hashlib import sha1
from datasketch.minhash import MinHash

book_path = "wonder.txt"
r_text = open(book_path).read()
r_text = r_text.lower()
# create mapping of unique chars to integers, and a reverse mapping
chars = sorted(list(set(r_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
# summarize the loaded data
num_chars = len(r_text)
num_vocab = len(chars)
print "Total Characters: ", num_chars
print "Total Vocab: ", num_vocab
# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
for i in range(0, num_chars - seq_length, 1):
	seq_in = r_text[i:i + seq_length]
	dataX.append(seq_in)
n_patterns = len(dataX)
print "Total Patterns: ", n_patterns
seq=[" iar about it, but by and by he remembered that it had not been ticking. at first he thought this eer",
"e ale the boys wfre she lad boen to the boos of the boos, and they were al anr oo the bark of the bark",
" of the boos of the boos afd the nererland thet thet whre hev back on the barkn of the bors. and",
" they were al anr oo the bark of the bark of the boos of the boos of the boos of the boos",
" afd the nererland thet thet whre hev back on the barkn of the bors.",
" and they were al anr oo the bark of the bark of the boos of the boos of the boos of the boos afd the nererland thet",
" thet whre hev back on the barkn of the bors. and they were al anr oo the bark of the bark of",
" the boos of the boos of the boos of the boos afd the nererland thet thet whre hev back on the ",
" barkn of the bors. and they were al anr oo the bark of the bark of the boos of the boos of the boos of the",
" boos afd the nererland thet thet whre hev back on the barkn of the bors. and they were al anr oo the bark of the bark ",
" of the boos of the boos of the boos of the boos afd the nererland thet thet whre hev back on the barkn of the bors."
]

array=[0]*len(seq)
for i in range (len (dataX)):   
   for j  in range(len(seq)):
        data1=dataX[i].split()
        data2=seq[j].split()
        m1 = MinHash()
        m2 = MinHash()
        for d in data1:
            m1.update(d.encode('utf8'))
        for d in data2:
            m2.update(d.encode('utf8'))
        s1 = set(data1)
        s2 = set(data2)
        actual_jaccard = float(len(s1.intersection(s2))) /\
            float(len(s1.union(s2)))
        if array[j]<actual_jaccard:
            array[j]=actual_jaccard
            print array[j]


print array 
#m1 = MinHash()/*
#print dataX[1],len(seq)
#for i in range(len(seq)):
#    m1.update(dataX[i].encode('utf8'))
#for d in seq:
#    m1.update(d.encode('utf8'))
#print("Estimated Jaccard for dataX and seq is", m1.jaccard(m2))
#s1 = set(dataX)
#s2 = set(seq)
#actual_jaccard =     float(len(s1.intersection(s2))) /\
#   float(len(s1.union(s2)))
#print("Actual Jaccard for dataX and seq is", actual_jaccard)
