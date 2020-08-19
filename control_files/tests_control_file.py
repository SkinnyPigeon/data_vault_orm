hubs = {
    'table': 'tests',
    'hubs': [
        {
            'hub': 'hub_person',
            'keys': [
                'serums_id', 'doctors_id'
            ]
        },
        {
            'hub': 'hub_location',
            'keys': [
                'hospital_id'
            ]

        },
        {
            'hub': 'hub_object',
            'keys': [
                'test_id'
            ]
        }
    ]
}
satellites = {
    'satellites': [
        {
            'satellite': 'sat_person_test_patients',
            'columns': [
                'patient_name'
            ],
            'hub': 'hub_person',
            'hub_id' : 0
        },
        {
            'satellite': 'sat_person_test_doctors',
            'columns': [
                'doctors_name'
            ],
            'hub': 'hub_person',
            'hub_id': 0
        },
        {
            'satellite': 'sat_location_hospital_address',
            'columns': [
                'hospital_address', 'hospital_postcode'
            ],
            'hub': 'hub_location',
            'hub_id': 0

        },
        {
            'satellite': 'sat_object_test_details',
            'columns': [
                'test_name'
            ],
            'hub': 'hub_object',
            'hub_id': 0
        }
    ]
}
    
links = {
    'links': [
        {
            'link': 'person_object_link',
            'values': {
                'person_id': 0,
                'object_id': 0
            }
        },
        {
            'link': 'person_location_link',
            'values': {
                'person_id': 0,
                'location_id': 0
            }
        },
        {
            'link': 'object_location_link',
            'values': {
                'object_id': 0,
                'location_id': 0
            }
        }
          
    ]
}   
