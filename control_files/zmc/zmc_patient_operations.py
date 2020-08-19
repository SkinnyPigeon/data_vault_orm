zmc_patient_operations_hubs = {
    'table': 'zmc.patient_measurements',
    'hubs': [
        {
            'hub': 'zmc.hub_event',
            'keys': 'serums_id'
        }
    ]
}

zmc_patient_operations_satellites = {
    'satellites': [
        {
            'satellite': 'zmc.sat_event_patient_opperations',
            'columns': [
                'anatomical_location', 'date', 'notes'
            ],
            'hub': 'zmc.hub_person',
            'hub_id': 0
        }
    ]
}

zmc_patient_operations_links = {
    'links': []
}