WEIGHT = int()

DOSAGE_INJECTION = {
    'Adequan': ['100 mg/mL', WEIGHT / 50, 'IM'],
    'Aminophylline': ['25 mg/mL', WEIGHT / 10, 'IV'],
    'Amikacin': ['250 mg/mL', WEIGHT * 0.27, 'IM/IV/SQ'],
    'Ampicillin (Wrapped bottle)': ['200 mg/mL', WEIGHT / 60, 'SQ'],
    'Ampicillin': ['100 mg/mL', WEIGHT / 10, 'IV'],
    'Atropine': ['0.54 mg/mL', WEIGHT * 0.034, 'IM/IV/SQ'],
    'Azith': ['N/A', WEIGHT / 5, 'SID'],
    'Baytril': ['2.27%', WEIGHT / 20, 'IV/SQ'],
    'BAAK': ['N/A', WEIGHT / 20, 'IM'],
    'Buprenex': ['0.3 mg/mL', WEIGHT * 0.015, 'IM/IV/SQ'],
    'Buprenex (Current)': ['0.15 mg/mL', WEIGHT * 0.03, 'IM/IV/SQ'],
    'Cefazolin': ['N/A', WEIGHT / 10, 'IV'],
    'Diphenhydramine': ['50 mg/mL', WEIGHT / 100, 'IV'],
    'Depo-Medrol': ['20 mg/mL', WEIGHT / 10, 'IM/SQ'],
    'Dexamethasone SP': ['4 mg/mL', WEIGHT / 10, 'SQ'],
    'Epinephrine': ['1 mg/mL', WEIGHT * 0.045, 'IV'],
    'Famotidine': ['10 mg/mL', WEIGHT * 0.023, 'IV/SQ'],
    'Hydromorphone (Mild)': ['2 mg/mL', WEIGHT * 0.045, 'IM/IV/SQ'],
    'Hydromorphone (Severe)': ['2 mg/mL', WEIGHT * 0.068, 'IM/IV/SQ'],
    'Ivermectin': ['1%', WEIGHT * 0.0136, 'SQ'],
    'Ketoprofen': ['100 mg/mL', WEIGHT / 100, 'SQ'],
    'Lasix 5%': ['100 mg/mL', WEIGHT / 100, 'SQ'],
    'Loperamide HCl': ['50 mg/mL', WEIGHT * 0.227, 'PO TID'],
    'Metronidazole': ['5 mg/mL', WEIGHT * 1.363, 'IV (Ask vet)'],
    'Metoclopramide': ['5 mg/mL', WEIGHT * 0.018, 'SQ/PO'],
    'Propoflo': ['10 mg/mL', WEIGHT * 0.2, 'IV'],
    'Strongid Paste': ['N/A', WEIGHT / 10, 'PO'],
    'Rimadyl': ['50 mg/mL', WEIGHT * 0.02, 'IM/SQ'],
    'Kenalog': ['2 mg/mL', WEIGHT / 125, 'SQ'],
    'Vitamin K (Minimum)': ['N/A', WEIGHT * 0.113, 'SQ'],
    'Vitamin K (Maximum)': ['N/A', WEIGHT * 0.227, 'SQ'],
    'Ket/Val Cocktail Injection': ['N/A', WEIGHT / 30, ''],
    'Convenia': ['N/A', WEIGHT * 0.0454545, 'SQ'],
    'Euthasol': ['N/A', WEIGHT / 10, 'IV'],
    'Butorphanol': ['1 mg/mL', WEIGHT * 0.0045454545, 'IM/IV'],
    'Acepromazine': ['10 mg/mL', WEIGHT * 0.0022727, 'IM/SQ'],
    'Diazepam': ['5 mg/mL', WEIGHT * 0.09090909090909, 'IV'],
    'Methocarbamol': ['100 mg/mL', WEIGHT * 0.227272727, 'IV'],
    'Cerenia': ['N/A', WEIGHT / 22, 'SQ']
}

DOSAGE_RX = {

}
