
def fetch_experience_choices():

    choices_tuple =()
    for years in range(30):
        for months in range(12):
            choice = ('{0} years, {1} months'.format(years,months))
            choice = ((choice,), (choice,))
            import pdb;pdb.set_trace()
            choices_tuple = choices_tuple+(choice)

    return choices_tuple


EXPERIENCE = fetch_experience_choices()




