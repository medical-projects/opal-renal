"""
Defining the patient flows for our system.
"""

flows = {
    'default': {
        'enter': {
            'controller': 'RenalHospitalNumberCtrl',
            'template'  : '/templates/modals/hospital_number.html/'
        },
        'exit': {
            'controller': 'RenalDischargeEpisodeCtrl',
            'template'  : '/templates/modals/discharge_episode.html/'
        }
    }
}
