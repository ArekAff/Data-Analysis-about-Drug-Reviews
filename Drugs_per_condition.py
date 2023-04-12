from tools import *

#---------------5. The number of drugs per condition----------------

#How many different conditions do we have?
unique_conditions = df['condition'].unique()
print(len(unique_conditions))
#Result: 885
# We have 885 different conditions


###Distributions of conditions

#Which are the most popular conditions?
#print(df['condition'].value_counts().nlargest(20))
#Result:
# Birth Control                28788
# Depression                    9069
# Pain                          6145
# Anxiety                       5904
# Acne                          5588
# Bipolar Disorde               4224
# Insomnia                      3673
# Weight Loss                   3609
# Obesity                       3568
# ADHD                          3383
# Diabetes, Type 2              2554
# Emergency Contraception       2463
# High Blood Pressure           2321
# Vaginal Yeast Infection       2274
# Abnormal Uterine Bleeding     2096
# Bowel Preparation             1859
# ibromyalgia                   1791
# Smoking Cessation             1780
# Migraine                      1694
# Anxiety and Stress            1663
# As we can see the most popular conditions are related to mental health and birth control
# Which checks out with the date we established in classification of drugs because no 1. was female hormone (progestin) which acts as 
# contraception and no 3. was Selective serotonin reuptake inhibitors which are used to treat depression and anxiety

#Plotting the most popular conditions
plt.figure(figsize=(20,10))
df['condition'].value_counts().nlargest(20).head(20).plot(kind='bar')
plt.title("20 most common conditions")
plt.show()

#print(df['condition'].value_counts().nsmallest(20))
#Result:
# Meningococcal Meningitis Prophylaxis                     1
# mist (                                                   1
# Cluster-Tic Syndrome                                     1
# Syringomyelia                                            1
# Gestational Diabetes                                     1
# Aspergillosis, Aspergilloma                              1
# Pseudogout, Prophylaxis                                  1
# Portal Hypertension                                      1
# Reversal of Nondepolarizing Muscle Relaxants             1
# 47</span> users found this comment helpful.              1
# Short Stature for Age                                    1
# Neurotic Depression                                      1
# Cerebral Edema                                           1
# me                                                       1
# Hyperuricemia Secondary to Chemotherapy                  1
# Prevention of Perinatal Group B Streptococcal Disease    1
# Small Bowel or Pancreatic Fistula                        1
# Pemphigoid                                               1
# Keratitis                                                1
# 123</span> users found this comment helpful.             1
#Result are inconclusive we cant say what condition is leat common

### How many drugs per condition?

# conditions with the most drugs (top 20)
print(df.groupby('condition')['drugName'].nunique().nlargest(20))

# Result:
# Not Listed / Othe                             214
# Pain                                          200
# Birth Control                                 172
# High Blood Pressure                           140
# Acne                                          117
# Depression                                    105
# Rheumatoid Arthritis                           98
# Diabetes, Type 2                               89
# Allergic Rhinitis                              88
# Bipolar Disorde                                80
# Osteoarthritis                                 80
# Anxiety                                        78
# Insomnia                                       78
# Abnormal Uterine Bleeding                      74
# Migraine                                       59
# Psoriasis                                      58
# 3</span> users found this comment helpful.     57
# Endometriosis                                  57
# ADHD                                           55
# Asthma, Maintenance                            54
# Most of drugs are not listed to specific condition, the first condition with the most drugs is Pain, followed up by birth control

# Plotting conditions with the most drugs
plt.figure(figsize=(20,10))
df.groupby('condition')['drugName'].nunique().nlargest(20).plot(kind='bar')
plt.title("20 conditions with the most drugs")
plt.grid()
plt.show()