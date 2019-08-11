from names_dataset import NameDataset

m = NameDataset()
exceptions = ['roi', 'may', 'not', 'will', 'happy']


def identify_name(s):
    if (m.search_first_name(s) or m.search_last_name(s)) and (s.lower() not in exceptions):
        return s
    else:
        return "none"
