from apyori import apriori
import pandas as pd


book_data = pd.read_excel('apriori.xlsx')
book_data.head()

data = book_data.drop(['No', 'ID Transaksi'], axis=1)

# Membuat list dalam list dari transaksi pembelian barang
records = []
for i in range(data.shape[0]):
    records.append([str(data.values[i,j]).split(',') for j in range(data.shape[1])])

trx = [[] for trx in range(len(records))]
for i in range(len(records)):
    for j in records[i][0]:
        trx[i].append(j)

print("panjang data :", data.shape[0])


# Menggunakan fungsi apriori untuk membuat asosiasi
association_rules = apriori(trx, min_support=0.05, min_confidence=0.20,min_lift=1)
# Membuat list hasil dari algoritma apriori
association_results = association_rules

# Menampilkan hasil asosiasi dari item 

pd.set_option('display.max_rows', 1000)
Result=pd.DataFrame(columns=['Rule','Support','Confidence'])

# membuat dan mengkalsifikasikan rekomendasi berdasarkan data buku
harry_potter = []
paper_umbrella = []
moudy = []
the_dragon_republic = []
the_poppy_war = []
hidden_world = []
whiteandgrey = []
selena = []

for item in association_results:
    pair = item[2]
    for i in pair:
        items = ''.join([str (x) for x in i[0]])
        if i[3]!=1:
            if (str([ x for x in i[0]]) == "['harry potter']" and len([x for x in i[1]]) <2):
                
                harry_potter.append(
                ''.join([str (x) for x in i[1]])
                )
            elif (str([x for x in i[0]]) == "['paper umbrella']" and len([x for x in i[1]]) <2):
                paper_umbrella.append(
                ''.join([str (x) for x in i[1]])
                )
            elif (str([x for x in i[0]]) == "['moudy']" and len([x for x in i[1]]) <2):
                moudy.append(
                ''.join([str (x) for x in i[1]])
                )
            elif (str([x for x in i[0]]) == "['the dragon republic']" and len([x for x in i[1]]) <2):
                the_dragon_republic.append(
                ''.join([str (x) for x in i[1]])
                )
            elif (str([x for x in i[0]]) == "['the poppy war']" and len([x for x in i[1]]) <2):
                the_poppy_war.append(
                ''.join([str (x) for x in i[1]])
                )
            elif (str([x for x in i[0]]) == "['hidden world']" and len([x for x in i[1]]) <2):
                hidden_world.append(
                ''.join([str (x) for x in i[1]])
                )
            elif (str([x for x in i[0]]) == "['white and grey']" and len([x for x in i[1]]) <2):
                whiteandgrey.append(
                ''.join([str (x) for x in i[1]])
                )
            elif (str([x for x in i[0]]) == "['selena']" and len([x for x in i[1]]) <2):
                selena.append(
                ''.join([str (x) for x in i[1]])
                )
            Result=Result.append({
                'Rule':str([x for x in i[0]])+ " -> " +str([x for x in i[1]]),
                'Support':str(round(item[1]*100,2))+'%',
                'Confidence':str(round(i[2] *100,2))+'%'
                },ignore_index=True)
                
                
# print(len(Result))
print(Result)


print("harry potter:", harry_potter)
print("paper umbrella:",paper_umbrella)
print("moudy:",moudy)
print("the dragon republic:",the_dragon_republic)
print("the poppy war:",the_poppy_war)
print("hidden world:",hidden_world)
print("white and grey:",whiteandgrey)
print("selena:",selena)


no_thisword = "hidden world"
justonebook = []


for i in range(len(Result)):
    if no_thisword in Result.at[i,"Rule"]:
        justonebook.append(Result.at[i,"Rule"])
        
        

# print(justonebook)
# if no_thisword in justonebook[1]:
#     print(justonebook[1])
# else:
#     print("none")


