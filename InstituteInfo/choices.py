__author__ = 'harshit'
import datetime

def year_choice():
    now = datetime.datetime.now()
    current_year = now.year
    year_list = [( current_year - i, current_year - i ) for i in range( 211 )]
    return year_list

LIST_YEAR = year_choice()

INSTITUTE_TYPE = ( ( 'Deemed University', 'Deemed University' ),
                   ( 'Government College', 'Government College' ),
                   ( 'Private College', 'Private College' ),
                   ( 'University Campus', 'University Campus' ),
                   ( 'Trustee College', 'Trustee College' ),
    )


INSTITUTE_USER=(('Chairman','Chairman'),
                ('Admission user','Admission user'),
                ('Form user','Form user'),
    )

USER_TYPE=(('Faculty','Faculty'),
            ('Student','Student'),
    )