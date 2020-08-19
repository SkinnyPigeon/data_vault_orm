operations_hubs = {
    'table': 'operations',
    'hubs': [
        {
            'hub': 'hub_object',
            'keys': [
                'operation_id'
            ]
        },
        {
            'hub': 'hub_person',
            'keys': [
                'serums_id'
            ]
        }
    ]
}

operations_satellites = {
    'satellites': [
        {
            'satellite': 'sat_object_patient_details',
            'columns': [
                'description'
            ],
            'hub': 'hub_object',
            'hub_id' : 0
        }
    ]
}


    
operations_links = {
    'links': [
        {
            'link': 'person_object_link',
            'values': {
                'person_id': 0,
                'object_id': 0
            }
        }
    ]
}   