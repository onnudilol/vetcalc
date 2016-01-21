from collections import OrderedDict

DOSAGE_INJECTION = {
    'Adequan': ['100 mg/mL', 1 / 50, 'IM'],
    'Aminophylline': ['25 mg/mL', 1 / 10, 'IV'],
    'Amikacin': ['250 mg/mL', 0.27, 'IM/IV/SQ'],
    'Ampicillin (Wrapped bottle)': ['200 mg/mL', 1 / 60, 'SQ'],
    'Ampicillin': ['100 mg/mL', 1 / 10, 'IV'],
    'Atropine': ['0.54 mg/mL', 0.034, 'IM/IV/SQ'],
    'Azith': ['N/A', 1 / 5, 'SID'],
    'Baytril': ['2.27%', 1 / 20, 'IV/SQ'],
    'BAAK': ['N/A', 1 / 20, 'IM'],
    'Buprenex': ['0.3 mg/mL', 0.015, 'IM/IV/SQ'],
    'Buprenex (Current)': ['0.15 mg/mL', 0.03, 'IM/IV/SQ'],
    'Cefazolin': ['N/A', 1 / 10, 'IV'],
    'Diphenhydramine': ['50 mg/mL', 1 / 100, 'IV'],
    'Depo-Medrol': ['20 mg/mL', 1 / 10, 'IM/SQ'],
    'Dexamethasone SP': ['4 mg/mL', 1 / 10, 'SQ'],
    'Epinephrine': ['1 mg/mL', 0.045, 'IV'],
    'Famotidine': ['10 mg/mL', 0.023, 'IV/SQ'],
    'Hydromorphone (Mild)': ['2 mg/mL', 0.045, 'IM/IV/SQ'],
    'Hydromorphone (Severe)': ['2 mg/mL', 0.068, 'IM/IV/SQ'],
    'Ivermectin': ['1%', 0.0136, 'SQ'],
    'Ketoprofen': ['100 mg/mL', 1 / 100, 'SQ'],
    'Lasix 5%': ['100 mg/mL', 1 / 100, 'SQ'],
    'Loperamide HCl': ['50 mg/mL', 0.227, 'PO TID'],
    'Metronidazole': ['5 mg/mL', 1.363, 'IV (Ask vet)'],
    'Metoclopramide': ['5 mg/mL', 0.018, 'SQ/PO'],
    'Propoflo': ['10 mg/mL', 0.2, 'IV'],
    'Strongid Paste': ['N/A', 1 / 10, 'PO'],
    'Rimadyl': ['50 mg/mL', 0.02, 'IM/SQ'],
    'Kenalog': ['2 mg/mL', 1 / 125, 'SQ'],
    'Vitamin K (Minimum)': ['N/A', 0.113, 'SQ'],
    'Vitamin K (Maximum)': ['N/A', 0.227, 'SQ'],
    'Ket/Val Cocktail Injection': ['N/A', 1 / 30, ''],
    'Convenia': ['N/A', 0.0454545, 'SQ'],
    'Euthasol': ['N/A', 1 / 10, 'IV'],
    'Butorphanol': ['1 mg/mL', 0.0045454545, 'IM/IV'],
    'Acepromazine': ['10 mg/mL', 0.0022727, 'IM/SQ'],
    'Diazepam': ['5 mg/mL', 0.09090909090909, 'IV'],
    'Methocarbamol': ['100 mg/mL', 0.227272727, 'IV'],
    'Cerenia': ['N/A', 1 / 22, 'SQ']
}

DOSAGE_RX = {

}


def create_ordered_dict(unordered_dict):
    return OrderedDict(sorted(unordered_dict.items(), key=lambda t: t[0]))
