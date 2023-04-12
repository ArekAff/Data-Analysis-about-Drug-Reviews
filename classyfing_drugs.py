from tools import *

#--------------------2. What are the groups/classification of drugs?--------------------
# We will be classifying the drugs based on their sufixes, 
# Source: https://accesspharmacy.mhmedical.com/content.aspx?bookid=1549&sectionid=93411751
# Source: https://www.drugs.com/inn-stems.html
data = open("dane.txt")
drug_suffixes = {}
for line in data:
    k,v = line.rstrip().lstrip().split("\t")
    drug_suffixes[k] = v

def classify_drug(drugname): #function to classify the drug based on the suffix
    for i in drug_suffixes.keys():
        if drugname.endswith(i):
            return drug_suffixes[i]

df['drugClass'] = df['drugName'].apply(classify_drug) #applying the function to the drugName column

print(df[['drugName','drugClass']])

arr = np.array(df['drugClass'].unique()) #unique drug classes

print(len(arr)) #number of unique drug classes
# Result: 144


#Which class of drug is the most common?
#print(df['drugClass'].value_counts().head(10))
# Result:
# female hormone (progestin)                       9695
# Loop diuretics                                   3212
# Selective serotonin reuptake inhibitors          3061
# Antifungal                                       2083
# psychoactive                                     1920
# diazepam derivatives                             1819
# antibiotics, produced by Streptomyces strains    1590
# antiandrogens                                    1361
# analgesics                                       1216
# Nondepolarizing paralytics                       1186
# This shows that the most common drug that has the review is classified as female hormone (progestin)

plt.figure(figsize=(20,10))
df['drugClass'].value_counts().nlargest(20).plot(kind='bar') #plotting the top 20 drug classes
plt.title("Distribution of Drugs by Class")
plt.show() 

#print(df['drugClass'].value_counts().nsmallest(20)) # the least common drug classes
#Result:
# acetylcholinesterase inhibitors, tacrine derivatives                                              1
# analogues of penicillanic acid antibiotics modified in the five-membered ring                     1
# hirudin derivatives                                                                               1
# Vasopressin receptor antagonist                                                                   1
# bradycardic agents                                                                                1
# antiallergics, cromoglicic acid derivatives                                                       1
# antineoplastics, topoisomerase I inhibitors                                                       1
# antibiotics, carbacepham derivatives                                                              1
# oxytocin derivatives                                                                              1
# aldosterone antagonists, spironolactone derivates                                                 2
# antineoplastic, alkylating agents, methanesulfonates                                              2
# antibiotics, kanamycin and bekanamycin derivatives (obtained from Streptomyces kanamyceticus);    2
# growth hormone release-stimulating peptides                                                       3
# N-methylated xanthine derivatives                                                                 3
# hormone-release inhibiting peptides                                                               3
# b-lactamase inhibitors                                                                            3

#Those are the least common drug classes

#Distribution of drugs per Drug Group based on size
drugs_Groups = df.groupby('drugClass').size()

#Converting the series to a dataframe
drug_group_df = pd.DataFrame({'drug_Class': drugs_Groups.index, 'count': drugs_Groups.values})

# Seaborn Plot
plt.figure(figsize=(20,10))
g = sns.barplot(x="drug_Class", y="count", data=drug_group_df) #plotting the drug classes
g.set_xticklabels(g.get_xticklabels(), rotation=90) #rotating the x-axis labels
plt.show()



#This concludes the analysis about classifications of drugs 





#Which class of drugs has the highest average rating?
average_rating_per_class = df.groupby('drugClass')['rating'].mean()
plt.figure(figsize=(20,10))
average_rating_per_class.hist()
plt.title("Histogram of Average Rating per Drug Class")
plt.grid(True)
plt.show()
#Results show that most of the drugs classified by their classes have an average rating of 7-8

#which group of drugs has the highest average rating?
print(average_rating_per_class.nlargest(20))
#Result:
# acetylcholinesterase inhibitors, tacrine derivatives                    10.000000
# antiallergics, cromoglicic acid derivatives                             10.000000
# antineoplastic, alkylating agents, methanesulfonates                    10.000000
# bradycardic agents                                                      10.000000
# hirudin derivatives                                                     10.000000
# ll-2 derivatives                                                        10.000000
# oxytocin derivatives                                                    10.000000
# ribofuranil-derivatives of the pyrazofurin type                         10.000000
# benzodioxane derivatives                                                 9.800000
# mucolytics, other than bromhexine derivatives                            9.555556
# vasoconstrictors, vasopressin derivatives                                9.538462
# antineoplastic, alkylating agents, (b-chloroethyl) amine derivatives     9.250000
# heparin derivatives including low molecular mass heparins                9.222222
# analgesics, pethidine derivatives                                        9.106383
# Methylxanthine                                                           9.000000
# Vasopressin receptor antagonist                                          9.000000
# antibiotics, carbacepham derivatives                                     9.000000
# hormone-release inhibiting peptides                                      9.000000
# Barbiturates                                                             8.894737
# Benzodiazepinea                                                          8.837451



