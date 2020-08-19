doctors_hubs = {
    'table': 'patient',
    'hubs': [
        {
            'hub': 'hub_person',
            'keys': [
                'doctor_id'
            ]
        }
    ]
}

doctors_satellites = {
    'satellites': [
        {
            'satellite': 'sat_person_doctors_names',
            'columns': [
                'name'
            ],
            'hub': 'hub_person',
            'hub_id' : 0
        }
    ]
}

    
doctors_links = {
    'links': []
}   