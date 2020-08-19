patient_hubs = {
    'table': 'patient',
    'hubs': [
        {
            'hub': 'hub_person',
            'keys': [
                'serums_id'
            ]
        },
        {
            'hub': 'hub_location',
            'keys': [
                'serums_id'
            ]

        }
    ]
}

patient_satellites = {
    'satellites': [
        {
            'satellite': 'sat_person_patient_details',
            'columns': [
                'name', 'age'
            ],
            'hub': 'hub_person',
            'hub_id' : 0
        },
        {
            'satellite': 'sat_location_patient_address',
            'columns': [
                'address', 'postcode'
            ],
            'hub': 'hub_location',
            'hub_id': 0

        }
    ]
}

    
patient_links = {
    'links': [
        {
            'link': 'person_location_link',
            'values': {
                'person_id': 0,
                'location_id': 0
            }
        }
    ]
}   