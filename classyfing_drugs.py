import numpy as np
import pandas as pd

#For plotting
import matplotlib.pyplot as plt
import seaborn as sns

#For text processing
from textblob import TextBlob

df = pd.read_csv('C:\Python\Drugs\drugsComTrain_raw.tsv',sep='\t')


#--------------------2. What are the groups/classification of drugs?--------------------
# We will be classifying the drugs based on their sufixes, 
# Source: https://accesspharmacy.mhmedical.com/content.aspx?bookid=1549&sectionid=93411751
# Source: https://www.drugs.com/inn-stems.html
drug_suffixes = {
    "afil": "Phosphodiesterase inhibitors",
    "asone": "Corticosteroid",
    "bicin" : "Antineoplastic",
    "ane": "Inhaled anesthetics",
    "dazole": "Anthelmintic",
    "dipine": "Calcium channel blocker",
    "dronate": "Bisphosphonate",
    "eprazole": "Proton pump inhibitor (PPI)" ,
    "azepam": "Benzodiazepinea",
    "fenac": "NSAID",
    "floxacin": "Quinolone antibiotic",
    "gliptin": "Antidiabetic inhibitor of the DPP-4 enzyme",
    "glitazone": "Antidiabetic thiazolidinedione",
    "iramine": "Antihistamine",
    "lamide": "Carbonic anhydrase inhibitor",
    "mab": "Monoclonal antibody",
    "mustine": "Alkylating agent (antineoplastic)",
    "mycin": "Antibiotic",
    "nacin": "Muscarinic antagonist (anticholinergic)",
    "nazole": "Antifungal",
    "olone": "Corticosteroid",
    "onide": "Corticosteroid",
    "oprazole": "Proton pump inhibitor (PPI)",
    "parin": "Antithrombotic",
    "profen": "NSAID",
    "ridone": "atypical antipsychotic",
    "sartan": "angiotensin II receptor antagonist",
    "semide": "loop diuretic (water pill)",
    "setron": "serotonin 5-HT3 receptor antagonist",
    "statin": "HMG-CoA reductase inhibitor",
    "tadine": "antihistamine",
    "thiazide": "thiazide diuretic (water pill)",
    "tinib": "antineoplastic (kinase inhibitor)",
    "trel": "female hormone (progestin)",
    "tretin": "retinoid; dermatologic agent; form of vitamin A",
    "tyline" : "tricyclic antidepressant (TCA)",
    "vir": "antiviral; anti-HIV",
    "vudine": "antiviral; nucleoside analogues",
    "zepam": "benzodiazepine",
    "zodone": "antidepressant",
    "zolam": "Benzodiazepinea",
    "azine": "Phenothiazines",
    "azole": "Azole antifungals",
    "barbital": "Barbiturates",
    "caine": "Local anesthetics",
    "cillin": "Penicillin antibiotics",
    "cycline": "Tetracycline antibiotics",
    "etine": "Selective serotonin reuptake inhibitors",
    "feb": "Selective estrogen response modifiers",
    "fene": "Selective estrogen response modifiers",
    "floxacin": "Fluoroquinolone",
    "fungin": "Echinocandins",
    "grastim": "Granulocyte colony stimulating factors",
    "gramostim": "Granulocyte colony stimulating factors",
    "ide": "Loop diuretics",
    "ipine": "Dihydropyridine calcium channel blockers",
    "ipramine": "Tricyclic antidepressants",
    "ium": "Nondepolarizing paralytics",
    "uronium": "Nondepolarizing paralytics",
    "lukast": "LTD4 receptor antagonist",
    "navir": "Protease inhibitors",
    "olol": "Beta blockers",
    "oxin": "Cardiac glycoside",
    "phylline": "Methylxanthine",
    "pril": "ACE inhibitor",
    "quine": "Quinolone derivatives",
    "statin": "HMG-CoA reductase inhibitors",
    "tecan": "Topoisomerase I inhibitor",
    "terol": "β2 agonist",
    "tidine": "Second generation antihistamine",
    "tine": "Allylamine antifungals",
    "toposide": "Topoisomerase II inhibitor",
    "triptan": "5-HT1B/1D agonist",
    "tropin": "Pituitary hormone",
    "vaptan": "Vasopressin receptor antagonist",
    "zosin": "α1 antagonist",
    "ac":   "anti-inflammatory agents, ibufenac derivatives",
"actide":	"synthetic polypeptides with a corticotrophin-like action",
"adol":	"analgesics",
"adom":	"analgesics, tifluadom derivatives",
"afenone":	"antiarrhythmics, propafenone derivatives",
"aldrate":	"antacids, aluminium salts",
"alox":	"antacids, aluminium derivatives",
"amivir": 	"neuraminidase inhibitors",
"anserin":	"serotonin receptor antagonists (mostly 5-HT2)",
"antel":	"anthelminthics (underfined group)",
"apine":	"psychoactive",
"arabine":	"arabinofuranosyl derivatives",
"arit":	"antiarthritic substances",
"arol":	"anticoagulants, dicoumarol derivatives",
"pase":	"lipase",
"astine":	"antihistaminics",
"azenil":	"benzodiazepine receptor antagonists/agonists (benzodiazepine derivatives)",
"azepam":	"diazepam derivatives",
"azepide":	"cholecystokinin receptor antagonist",
"azocine":	"narcotic antagonists/agonists related to 6,7-benzomorphan",
"azoline":	"antihistaminics or local vasoconstrictors, antazoline derivatives",
"azosin":	"antihypertensive substances, prazosin derivatives",
"bactam":	"b-lactamase inhibitors",
"bamate":	"tranquillizers, propanediol and pentanediol derivatives",
"bendazole":	"anthelminthics, tiabendazole derivatives",
"bradine":	"bradycardic agents",
"buzone":	"anti-inflammatory analgesics, phenylbutazone derivatives",
"caine": "local anaesthetics",
"carbef":	"antibiotics, carbacepham derivatives",
"carnil":	"benzodiazepine receptor antagonists/agonists (carboline derivatives)",
"cavir":	"carbocyclic nucleosides",
"cic":	"hepatoprotectice substances with a carboxylic acid group",
"cidin":	"naturally occurring antibiotics (undefined group)",
"cillin	antibiotics": "6-aminopenicillanic acid derivatives",
"citabine":	"nucleoside antiviral or antineoplastic agents, cytarabine or azarabine derivatives",
"clone": "hypnotic tranquillizers",
"conazole": "systemic antifungal agents, miconazole derivatives",
"crinat": "diuretics, etacrynic acid derivatives",
"crine": "acetylcholinesterase inhibitors, tacrine derivatives",
"cromil": "antiallergics, cromoglicic acid derivatives",
"curium": "curare-like substances",
"cycline": "antibiotics, tetracycline derivatives",
"dan": "cardiac stimulants, pimobendan derivatives",
"dapsone": "Antimycobacterials, diaminodiphenylsulfone derivatives",
"dermin": "epidermal growth factors",
"dil": "vasodilators",
"dipine": "calcium channel blockers, nifedipine derivatives",
"dismase": "superoxide dismutase activity",
"dopa": "dopamine receptor agonists, dopamine derivatives, used as antiparkinsonism/prolactin inhibitors;",
"dox": "antibacterials, quinoline dioxide derivatives",
"dralazine": "antihypertensives, hydrazinephthalazine derivatives",
"dronic acid": "calcium metabolism regulator, pharmaceutical aid",
"ectin": "antiparasitics, ivermectin derivatives",
"entan": "endothelin receptor antagonists",
"eptacog": "blood coagulation VII",
"eridine": "analgesics, pethidine derivatives",
"etanide": "diuretics, piretanide derivatives",
"exakin": "ll-6 derivatives",
"exine": "mucolytic, bromhexine derivatives",
"fenamic acid": "anti-inflammatory, anthranilic acid derivatives",
"fenin": "diagnostic aids; (phenylcarbamoyl)methyl iminodiacetic acid derivatives",
"fenine": "analgesics, glafenine derivatives - (subgroup of fenamic acid group)",
"fentanil": "narcotic analgesics, fentanil derivatives",
"fermin": "fibrinoblast growth factors",
"fiban": "Fibrinogen receptor antagonists (glycoprotein lib/llla receptor antagonists",
"fibrate": "clofibrate derivatives",
"flapon": "5-lipoxygenase-activating protein (FLAP) inhibitor",
"flurane": "general inhalation anaesthetics, halogenated alkane derivatives",
"formin": "antihyperglycaemics, phenformin derivatives",
"fos": "insecticides, anthelmintics,pesticides etc., phosphorous derivatives",
"fosvos": "insecticides, anthelmintics,pesticides etc., phosphorous derivatives",
"fradil": "calcium channel blockers acting as vasodilators",
"frine": "sympathomimetic, phenethyl derivatives",
"fungin": "antifungal antibiotics",
"fylline": "N-methylated xanthine derivatives",
"gatran": "thrombin inhibitor, antithrombotic agents",
"giline": "MAO-inhibitors type B",
"gillin": "antibiotics produced by Aspergillus strains",
"golide": "dopamine receptor agonists, ergoline derivatives",
"gramostim": "granulocyte macrophage colony stimulating factor (GM-CSF) type substances",
"grastim": "granulocyte colony stimulatory factor (G-CSF) type) substances",
"grel": "platelet aggregation inhibitors",
"icam": "anti-inflammatory, isoxicam derivatives",
"ifene": "antiestrogens, clomifene and tamoxifen derivatives",
"ilide": "Class III antiarrhythmics, sematilide derivatives",
"imod": "immunomodulators, both stimulant/suppressie and stimulant",
"imus": "immunosuppressants (other than antineoplastics)",
"iptan": "serotonin (5HT1) receptor agonists, sumatriptan derivatives",
"irudin": "hirudin derivatives",
"isomide": "antiarrhythmics, disopyramide derivatives",
"izine": "diphenylmethyl piperazine derivatives",
"kacin": "antibiotics, kanamycin and bekanamycin derivatives (obtained from Streptomyces kanamyceticus);",
"kalant": "potassium channel blockers",
"kalim": "potassium channel activators, antihypertensive",
"kinra": "interleukin receptor antagonists",
"kiren": "renin inhibitors",
"leukin": "ll-2 derivatives",
"lipastat": "pancreatic lipase inhibitors",
"lukast": "leukotriene receptor antagonist",
"mab": "monoclonal antibodies",
"mantadine": "adamantine derivatives",
"meline": "cholinergic agents, arecoline derivatives",
"mer": "polymers",
"mesine": "sigma receptor ligands",
"mestane": "aromatase inhibitors",
"metacin": "anti-inflammatory, indometacin derivatives",
"micin": "antibiotics obtained from various Micromonospora",
"monam": "monobactam antibiotics",
"morelin": "growth hormone release-stimulating peptides",
"mostim": "macrophage stimulating factors (M-CSF) type substances",
"motine": "antivirals, quinoline derivatives",
"moxin": "monoamine oxidase inhibitors, hydrazine derivatives",
"mustine": "antineoplastic, alkylating agents, (b-chloroethyl) amine derivatives",
"mycin": "antibiotics, produced by Streptomyces strains",
"nakin": "ll-1 derivatives",
"nercept": "tumour necrosis factor antagonist",
"nermin": "tumour necrosis factor",
"nicate": "antihypercholesterolaemic and/or vasodilating nicotinic acid esters",
"nidazole": "antiprotozoals, metronidazole derivatives",
"nixin": "anti-inflammatory, anilinonicotinic acid derivatives",
"nonacog": "blood coagulation factor IX",
"octocog": "blood coagulation factor VIII",
"olol": "b-adrenoreceptor antagonists",
"alol": "aromatic ring –CH-CH2-NH-R related to -olols",
"olone": "steroids other than prednisolone derivatives",
"opamine": "dopaminergic agents dopamine derivatives used as cardiac stimulat/antihypertensives/diuretics",
"onide": "steroids for topical use, acetal derivatives",
"nidine": "antihypertensives, clonidine derivatives",
"orex": "anoretics",
"oxacin": "antibacterials, nalidixic acid derivatives",
"oxan": "benzodioxane derivatives",
"oxane": "benzodioxane derivatives",
"oxanide": "antiparasitics, salicylanides and analogues",
"oxef": "antibiotics, oxacefalosporanic acid derivatives",
"oxetine": "antidepressants, fluoxetine derivatives",
"pafant": "platelet-activating factor antagonists",
"pamide": "diuretics, sulfamoylbenzoic acid derivatives",
"pamil": "coronary vasodilators, verapamil derivatives",
"parcin": "glycopeptides antibiotics",
"parin": "heparin derivatives including low molecular mass heparins",
"penem": "analogues of penicillanic acid antibiotics modified in the five-membered ring",
"peridol": "(antipsychotics, haloperidol derivatives",
"peridone": "antipsychotics, risperidone derivatives",
"perone": "tranquillizers, neuroleptics, 4’-fluoro-4-piperidinobutyrophenone derivatives;",
"pidem": "hypnotics/sedatives, zolpidem derivatives",
"pin": "tricyclic compounds",
"pine": "tricyclic compounds",
"piprazole": "psychotropics, phenylpiperazine derivatives",
"pirox": "antimycotic pyridine derivatives",
"planin": "antibacterials (Actinoplanes strains)",
"platin": "antineoplastic agents, platinum derivatives",
"plestim": "interleukin-3 analogues and derivatives",
"plon": "pyrazolo[-]pyrimidine derivatives, used as anxiolytics, sedatives, hypnotics",
"poetin": "erythropoietin type blood factors",
"porfin": "benzoporphyrin derivatives",
"pramine": "substances of the imipramine group",
"prazole": "antiulcer, benzimidazole derivatives",
"pressin": "vasoconstrictors, vasopressin derivatives",
"pride": "sulpiride derivatives",
"pril": "angiotensin-converting enzyme inhibitors",
"prilat": "angiotensin-converting enzyme inhibitors",
"prim": "antibacterials, trimethoprim derivatives",
"profen": "anti-inflammatory agents, ibuprofen derivatives",
"quinil": "benzodiazepine receptor partial agonists (quinoline derivatives)",
"racetam": "amide type nootrope agents, piracetam derivatives",
"relix": "hormone-release inhibiting peptides",
"renone": "aldosterone antagonists, spironolactone derivates",
"ribine": "ribofuranil-derivatives of the pyrazofurin type",
"rinone": "cardiac stimulants, amrinone derivatives",
"rozole": "aromatase inhibitors, imidozole-triazole derivatives",
"rubicin": "antineoplastic antibiotics, daunorubicin derivatives",
"sartan": "angiotensin II receptor antagonists, antihypertensive (non-peptidic)",
"semide": "diuretics, furosemide derivatives",
"sermin": "insulin-like growth factor",
"serpine": "derivatives of Rauwolfia alkaloids",
"setron": "serotonin receptor antagonists (5-HT3)",
"spirone": "anxiolytics, buspirone derivatives",
"stat": "enzyme inhibitors",
"steine": "mucolytics, other than bromhexine derivatives",
"stim": "colony stimulating factors",
"sulfan": "antineoplastic, alkylating agents, methanesulfonates",
"tecan": "antineoplastics, topoisomerase I inhibitors",
"tepa": "antineoplastics, thiotepa derivatives",
"teplase": "tissue plasminogen activators",
"terol": "bronchodilators, phenethylamine derivatives",
"terone": "antiandrogens",
"tiazem": "calcium channel blockers, diltiazem derivatives",
"tide": "peptides and glycopeptides",
"tidine": "histamine H2-receptor antagonists, cimetidine derivatives",
"tirelin": "thyrotropin releasing hormone analogues",
"tizide": "diuretics, chlorothiazide derivatives",
"tocin": "oxytocin derivatives",
"toin": "antiepileptics, hydantoin derivatives",
"trexate": "folic acid analogues",
"tricin": "antibiotics, polyene derivatives",
"triptyline": "antidepressants, dibenzo[a,d]cycloheptane or cyclopheptene derivatives",
"troban": "thromboxane A2-receptor antagonists; antithrombotic agents",
"trodast": "thromboxane A2 receptor antagonists, antiasthmatics",
"uplase": "urokinase-type-plasminogen activators",
"uracil": "uracil derivatives used as thyroid antagonists and as antineoplastics",
"uridine": "uridine derivatives used as antiviral agents and as antineoplastics; also -udine­",
"vastatin": "antilipidemic substances, HMG CoA reductase inhibitors",
"verine": "spasmolytics with a papaverine-like action",
"virsen": "neuraminidase inhibitors",
"vudine": "antiviral; antineoplastics, zidovudine derivatives",
"xanox": "antiallergic respiratory tract drugs, xanoxic acid derivatives",
"zofone": "alozafone derivatives",
"zepine": "tricyclic compounds"
}

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



