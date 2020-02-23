# 讀取檔案
data = []
with open('G:\Work\source\\file\\amazon_reviews.txt','r') as f:
    total_size = 0

    for line in f:
        if 'good' in line:
            data.append(line)
    # list comprehension
    #
    data = [line for line in f if 'good' in line]

    for d in data:
        total_size += len(d)
    print(total_size / len(data))
    print(data[0])