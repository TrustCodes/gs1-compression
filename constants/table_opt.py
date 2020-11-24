"""tableOpt is the ptimised encoding of combinations of GS1 Application
Identifiers. It contains optimisations for pre-defined sequences of
GS1 Application Identifiers. We'll initially use 0A-0F through 9A-9F
to keep AH - EH unallocated and reserve FH for support for non-GS1 keys
from the URI query string.
"""
TABLE_OPT = {"0A": ["01", "22"], "0B": ["01", "10"], "0C": ["01", "21"],
             "0D": ["01", "17"], "0E": ["01", "7003"], "0F": ["01", "30"],
             "1A": ["01", "10", "21", "17"], "1B": ["01", "15"],
             "1C": ["01", "11"], "1D": ["01", "16"], "1E": ["01", "91"],
             "1F": ["01", "10", "15"], "2A": ["01", "3100"],
             "2B": ["01", "3101"], "2C": ["01", "3102"], "2D": ["01", "3103"],
             "2E": ["01", "3104"], "2F": ["01", "3105"], "3A": ["01", "3200"],
             "3B": ["01", "3201"], "3C": ["01", "3202"], "3D": ["01", "3203"],
             "3E": ["01", "3204"], "3F": ["01", "3205"], "9A": ["8010", "8011"],
             "9B": ["8017", "8019"], "9C": ["8018", "8019"],
             "9D": ["414", "254"], "A0": ["01", "3920"], "A1": ["01", "3921"],
             "A2": ["01", "3922"], "A3": ["01", "3923"], "A4": ["01", "3924"],
             "A5": ["01", "3925"], "A6": ["01", "3926"], "A7": ["01", "3927"],
             "A8": ["01", "3928"], "A9": ["01", "3929"], "C0": ["255", "3900"],
             "C1": ["255", "3901"], "C2": ["255", "3902"],
             "C3": ["255", "3903"], "C4": ["255", "3904"],
             "C5": ["255", "3905"], "C6": ["255", "3906"],
             "C7": ["255", "3907"], "C8": ["255", "3908"],
             "C9": ["255", "3909"], "CA": ["255", "3940"],
             "CB": ["255", "3941"], "CC": ["255", "3942"],
             "CD": ["255", "3943"]}
