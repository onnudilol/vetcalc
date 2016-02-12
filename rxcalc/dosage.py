from collections import OrderedDict

DOSAGE_INJECTION = {
    'Adequan': [1/50, '100 mg/mL', 'Non-steroidal anti-inflammatory', 'IM',
                'Adequan Canine (for dogs) is used to control symptoms associated with degenerative or traumatic arthritis.'],

    'Aminophylline': [1/10, '25 mg/mL', 'Bronchodilator', 'IV',
                      'Treating active symptoms and blockage of airway due to asthma or other lung diseases such as emphysema or bronchitis. It is used in combination with other medicines.'],

    'Amikacin': [0.27, '250 mg/mL', 'Antibiotic', 'IM/IV/SQ',
                 'Treating certain serious bacterial infections. Amikacin is an aminoglycoside antibiotic. It works by inhibiting the production of bacterial proteins, which causes bacterial cell death.'],

    'Ampicillin (Wrapped bottle)': [1/60, '200 mg/mL', 'Antibiotic', 'SQ',
                                    'Ampicillin is a penicillin-like antibiotic used to treat certain infections caused by bacteria such as pneumonia; bronchitis; and ear, lung, skin, and urinary tract infections. Antibiotics will not work for colds, flu, or other viral infections.'],

    'Ampicillin': [1/10, '100 mg/mL', 'Antibiotic', 'IV',
                   'Ampicillin is a penicillin-like antibiotic used to treat certain infections caused by bacteria such as pneumonia; bronchitis; and ear, lung, skin, and urinary tract infections. Antibiotics will not work for colds, flu, or other viral infections.'],

    'Atropine': [0.034, '0.54 mg/mL', 'Involuntary nervous system blocker', 'IM/IV/SQ',
                 'It can treat heart rhythm problems, stomach or bowel problems, and certain types of poisoning when injected. It can also decrease saliva before surgery and dilate the pupils before an eye exam.'],

    'Azithromycin': [1/5, 'N/A', 'Antibiotic', 'SID',
                     'Azithromycin is used to treat certain bacterial infections, such as bronchitis; pneumonia; sexually transmitted diseases (STD); and infections of the ears, lungs, sinuses, skin, throat, and reproductive organs. Azithromycin also is used to treat or prevent disseminated Mycobacterium avium complex (MAC) infection [a type of lung infection that often affects people with human immunodeficiency virus (HIV)]. Azithromycin is in a class of medications called macrolide antibiotics. It works by stopping the growth of bacteria. Antibiotics will not kill viruses that can cause colds, flu, or other infections.'],

    'Baytril': [1/20, '2.27%', 'Antibiotic', 'IV/SQ',
                'Baytril Taste Tabs are used to treat many types of bacterial infections. It\'s a fluroquinolone antibiotic used for infections of the urinary tract, skin, prostate, GI tract, liver, and lungs.'],

    'BAAK': [1/20, 'N/A', 'Sedative', 'IM',
             'It makes dogs sleepy.'],

    'Buprenex': [0.015, '0.3 mg/mL', 'Narcotic analgesic', 'IM/IV/SQ',
                 'In veterinary medicine, buprenorphine can be administered to canines and felines. A veterinarian may see fit to prescribe buprenorphine for the management of pain associated with tissue inflammation due to infection or pathological disease, tissue necrosis, tissue spasms, ischemia and trauma resulting from wounds, fractures and joint injuries.'],

    'Buprenex (Current)': [0.03, '0.15 mg/mL', 'Narcotic analgesic', 'IM/IV/SQ',
                           'In veterinary medicine, buprenorphine can be administered to canines and felines. A veterinarian may see fit to prescribe buprenorphine for the management of pain associated with tissue inflammation due to infection or pathological disease, tissue necrosis, tissue spasms, ischemia and trauma resulting from wounds, fractures and joint injuries.'],

    'Cefazolin': [1/10, 'N/A', 'Antibiotic', 'IV',
                  'Cefazolin is an antibiotic, commonly known as Kefzol® and Ancef®, of the cephalosporin class. It is related to the penicillin drugs in how it kills bacteria, but cephalosporins have a much broader range of activity against bacteria than penicillins. Cefazolin is used in both dogs and cats to treat a variety of bacterial infections, including skin infections, wound infections, bone infections, pneumonia and bladder infections'],

    'Diphenhydramine': [1/100, '50 mg/mL', 'Antihistamine', 'IV',
                        'Diphenhydramine is an antihistamine that reduces the effects of natural chemical histamine in the body. Histamine can produce symptoms of sneezing, itching, watery eyes, and runny nose. Diphenhydramine is used to treat sneezing, runny nose, watery eyes, hives, skin rash, itching, and other cold or allergy symptoms. Diphenhydramine is also used to treat motion sickness, to induce sleep, and to treat certain symptoms of Parkinson\'s disease.'],

    'Depo-Medrol': [1/10, '20 mg/mL', 'Anti-inflammatory', 'IM/SQ',
                    'Treats asthma, allergic reactions, inflammation, flare-ups of ongoing illnesses, and many other medical problems. May also be used to lessen some symptoms of cancer.'],

    'Dexamethasone SP': [1/10, '4 mg/mL', 'Anti-inflammatory', 'SQ',
                         'Dexamethasone is many times more potent than other anti-inflammatory and immunosuppressing drugs including hydrocortisone and prednisone. It is often mixed with other drugs to treat difficult ear, eye, and skin infections. It reaches every system in the body and therefore is used to treat many disorders'],

    'Epinephrine': [0.045, '1 mg/mL', 'Vasoconstrictor', 'IV',
                    'Epinephrine injection is used along with emergency medical treatment to treat life-threatening allergic reactions caused by insect bites or stings, foods, medications, latex, and other causes. Epinephrine is in a class of medications called alpha- and beta-adrenergic agonists (sympathomimetic agents). It works by relaxing the muscles in the airways and tightening the blood vessels.'],

    'Famotidine': [0.023, '10 mg/mL', 'Antacid', 'IV/SQ',
                   'Famotidine is a non-prescription medication used in dogs and cats to reduce the amount of stomach acid being produced. Although Famotidine is not FDA-approved for use in veterinary medicine, it is a commonly accepted practice for veterinarians to prescribe this medication for dogs and cats.'],

    'Hydromorphone (Mild)': [0.045, '2 mg/mL', 'Narcotic analgesic', 'IM/IV/SQ',
                             'Hydromorphone is used to treat moderate to severe pain. The extended-release form of this medicine is for around-the-clock treatment of moderate to severe pain. This form of hydromorphone is not for use on an as-needed basis for pain.'],

    'Hydromorphone (Severe)': [0.068, '2 mg/mL', 'Narcotic analgesic', 'IM/IV/SQ',
                               'Hydromorphone is used to treat moderate to severe pain. The extended-release form of this medicine is for around-the-clock treatment of moderate to severe pain. This form of hydromorphone is not for use on an as-needed basis for pain.'],

    'Ivermectin': [0.0136, '1%', 'Antiparasitic', 'SQ',
                   'Ivermectin/Pyrantel for dogs is a heartworm preventative that also controls roundworms and hookworms. Ivermectin/Pyrantel is a generic equivalent to Heartgard Plus. It has the same active ingredients and is the same strength.'],

    'Ketoprofen': [1/100, '100 mg/mL', 'Non-steroidal anti-inflammatory', 'SQ',
                   'Ketoprofen is used to relieve pain from various conditions. It also reduces pain, swelling, and joint stiffness from arthritis.'],

    'Lasix 5%': [1/100, '100 mg/mL', 'Diuretic', 'SQ',
                 'Lasix treats fluid retention (edema) in people with congestive heart failure, liver disease, or a kidney disorder such as nephrotic syndrome. This medication is also used to treat high blood pressure (hypertension).'],

    'Loperamide HCl': [0.227, '50 mg/mL', 'Antidiarrheal', 'PO TID',
                       'Loperamide, sold under the brand name Imodium among others, is a medication used to decrease the frequency of diarrhea. It is often used for this purpose in gastroenteritis, inflammatory bowel disease, and short bowel syndrome. It is not recommended for those with blood in the stool. The medication is taken by mouth.'],

    'Metronidazole': [1.363, '5 mg/mL', 'Antibiotic', 'IV (Ask vet)',
                      'Metronidazole is used to treat bacterial infections of the vagina, stomach, skin, joints, and respiratory tract. This medication will not treat a vaginal yeast infection.'],

    'Metoclopramide': [0.018, '5 mg/mL', 'Anti-nausea', 'SQ/PO',
                       'Metoclopramide is used short-term to treat heartburn caused by gastroesophageal reflux in people who have used other medications without relief of symptoms. Metoclopramide is also used to treat slow gastric emptying in people with diabetes (also called diabetic gastroparesis), which can cause nausea, vomiting, heartburn, loss of appetite, and a feeling of fullness after meals.'],

    'Propoflo': [0.2, '10 mg/mL', 'General anesthetic', 'IV',
                 'Propofol is an injectable short-acting hypnotic that produces rapid, smooth and excitement-free anesthesia induction. '],

    'Strongid Paste': [1/10, 'N/A', 'Dewormer', 'PO',
                       'A dewormer  approved for the removal and control of mature infections of large strongyles (Strongylus vulgaris, S. edentatus, S. equinus); pinworms (Oxyuris equi); large roundworms (Parascaris equorum); and small strongyles'],

    'Rimadyl': [0.02, '50 mg/mL', 'Non-steroidal anti-inflammatory', 'IM/SQ',
                'It provides day-to-day treatment for pain and inflammation from arthritis in geriatric dogs, joint pain, osteoarthritis, hip dysplasia, and other forms of joint deterioration. It is also used to relieve short-term post-operative pain, inflammation, and swelling after spaying, neutering, and other procedures.'],

    'Kenalog': [1/125, '2 mg/mL', 'Anti-inflammatory', 'SQ',
                'Triamcinolone is often used to treat red and itchy skin caused by a number of conditions. It is a corticosteroid, which reduces swelling. Triamcinolone is also often used in conjunction with antimicrobial and antifungal drugs in the drugs Animax and Panolog to treat ear and skin disorders caused by allergies or infections.'],

    'Vitamin K (Minimum)': [0.113, 'N/A', 'Vitamin', 'SQ',
                            'Vitamin K is used to treat and prevent low levels of certain substances (blood clotting factors) that the body naturally produces.'],

    'Vitamin K (Maximum)': [0.227, 'N/A', 'Vitamin', 'SQ',
                            'Vitamin K is used to treat and prevent low levels of certain substances (blood clotting factors) that the body naturally produces.'],

    'Ket/Val Cocktail Injection': [1/30, 'N/A', 'General anesthetic', 'IV',
                                   'Used to induce rapid anesthesia.'],

    'Convenia': [0.0454545, 'N/A', 'Antibiotic', 'SQ',
                 'It is used for the treatment of skin infections caused by Pasturella multocida in cats, and Staphylococcus intermedius/S. canis in dogs. It is approved as a broad-spectrum, third-generation cephalosporin for subcutaneous injection lasting 14 days for treating skin and soft tissue infections.'],

    'Euthasol': [1/10, 'N/A', 'Euthanasia', 'IV',
                 'Indicated for use in dogs to induce painless, humane, and rapid euthanasia resulting from cerebral death triggered by active ingredients pentobarbital sodium and phenytoin sodium.'],

    'Butorphanol': [0.0045454545, '1 mg/mL', 'Narcotic analgesic', 'IM/IV',
                    'Treating or preventing moderate to severe pain due to surgery, labor, or other causes.'],

    'Acepromazine': [0.0022727, '10 mg/mL', 'Sedative', 'IM/SQ',
                     'Acepromazine is the most common tranquilizer and central nervous system depressant given to pets. It is used to prevent anxiety associated with thunder, fireworks, vet or groomer visits, and other things your pet may fear. It is effective treatment against motion sickness and nausea associated with car or plane rides.'],

    'Diazepam': [0.09090909090909, '5 mg/mL', 'Sedative', 'IV',
                 'Diazepam is used to treat anxiety disorders, alcohol withdrawal symptoms, or muscle spasms. Diazepam is sometimes used with other medications to treat seizures.'],

    'Methocarbamol': [0.227272727, '100 mg/mL', 'Muscle relaxant', 'IV',
                      'Methocarbamol is used together with rest and physical therapy to treat skeletal muscle conditions such as pain or injury.'],

    'Cerenia': [1/22, 'N/A', 'Anti-nausea', 'SQ',
                'Cerenia is indicated for the prevention of acute vomiting and prevention of vomiting due to motion sickness in dogs. It is intended for use in dogs 8 weeks of age or older.']
}

DOSAGE_RX = {

}
