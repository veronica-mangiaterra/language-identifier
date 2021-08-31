def pre_processing (path):
    text = open(path, "r", encoding= "utf-8")
    words = text.read().split(" ")
    a = []
    for word in words:
        word = word.lower() 
        word = re.sub(r'[\u0600-\u06FF]+', "", word) #here the function deletes the arabic characters
        word = re.sub(u'[\u4E00-\u9FA5]', "", word) #here the function delates the chinese characters
        word = re.sub("[0-9]", "", word)
        word = re.sub(r'[^\w\s]', "", word) #deleting everything that is not an alphanumeric character or a word space
        word = re.sub("\n", "", word)
        a.append(word)
    b = " ".join(a)
    text.close()
    text_write = open(path, "w", encoding = "utf-8")
    text_write.write(b)
    return b
new_path = [r"C:/Users/user/Documents/1m/class1/linear.txt", r"C:/Users/user/Documents/1m/class2/linear.txt"]
for path in new_path:
    pre_processing(path)
def fivek_most_frequent (path):
    d= {}
    text = open(path, "r", encoding= "utf-8")

    splitted = text.read().split(" ")
    for word in splitted:
        if word not in d:
            d[word]=1
        if word in d:
            d[word]+=1
    dict_ = dict(sorted(d.items(),key=lambda item: item[1], reverse=True))#this function takes the single argument x and returns x[1]
    dict_keys= dict_.keys()
    fivek = " ".join(list(dict_keys)[:5000])
    return fivek
 
ita_fivek = fivek_most_frequent(r"C:\Users\user\Documents\text\it_txt.txt")
fr_fivek = fivek_most_frequent(r"C:\Users\user\Documents\text\fr_txt.txt")
es_fivek = fivek_most_frequent(r"C:\Users\user\Documents\text\es_txt.txt")
ne_fivek = fivek_most_frequent(r"C:\Users\user\Documents\text\ne_txt.txt")

data = {'Text': [ita_fivek, fr_fivek, es_fivek, ne_fivek],
        'Language': ["Italian", "French", "Spanish", "Dutch"]}
df_fivek = pd.DataFrame(data)

ita_df = pd.read_csv(r"C:\Users\user\Desktop\it_txt.txt", "utf-8", header= None, names= ["Italian"], engine="python")
fr_df = pd.read_csv(r"C:\Users\user\Desktop\fr_txt.txt", "utf-8", header= None, names= ["French"], engine="python")
es_df = pd.read_csv(r"C:\Users\user\Desktop\es_txt.txt", "utf-8", header= None, names= ["Spanish"], engine="python")
ne_df = pd.read_csv(r"C:\Users\user\Desktop\ne_txt.txt", "utf-8", header= None, names= ["Dutch"], engine="python")

def pre_process (csv_df, lang, data_list):
    for i, line in csv_df.iterrows():
        line = line[lang]
        if len(line) != 0:
            line = line.lower()
            line = re.sub("[0-9]", "", line)
            line = re.sub(r'[^\w\s]', "", line)
            line = re.sub(r'[\u0600-\u06FF]+', "", line)
            line = re.sub(u'[\u4E00-\u9FA5]', "", line)
            data_list.append(line)
    return None
    
data_ita= []
data_fr = []
data_es = []
data_ne= []
pre_process(ita_df, "Italian", data_ita)
pre_process(fr_df, "French", data_fr)
pre_process(es_df, "Spanish", data_es)
pre_process(ne_df, "Dutch", data_ne)

df_oneM = pd.DataFrame({"Text": data_ita+data_fr+data_es+data_ne,})
df_oneM.loc[:len(data_ita)-1, "Language"] = 'Italian'
df_oneM.loc[len(data_ita):len(data_ita)+len(data_fr)-1, "Language"]= "French"
df_oneM.loc[len(data_ita)+len(data_fr):len(data_ita)+len(data_fr)+len(data_es)-1,"Language"] = 'Spanish'
df_oneM.loc[len(data_ita)+len(data_fr)+len(data_es):,"Language"] = 'Dutch'
