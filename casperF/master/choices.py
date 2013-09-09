IMAGE_TYPE = (
    ('Cover','Cover'),
    ('Profile','Profile')
                )

INSTITUTE_TYPE = ( ( 'Deemed University', 'Deemed University' ),
                   ( 'Government College', 'Government College' ),
                   ( 'Private College', 'Private College' ),
                   ( 'University Campus', 'University Campus' ),
                   ( 'Trustee College', 'Trustee College' ),
    )


USER_TYPE=(('Faculty','Faculty'),
            ('Student','Student'),
           ('Institute','Institute'),
    )

STATUS_CHOICES= (
		('Pending','Pending'),
		('Rejected','Rejected'),
		('Verified','Verified'),
)


import datetime

def year_choice():
    now = datetime.datetime.now()
    current_year = now.year
    year_list = [( current_year - i, current_year - i ) for i in range( 211 )]
    return year_list

LIST_YEAR = year_choice()