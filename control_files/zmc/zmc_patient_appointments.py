zmc_patient_appointments_hubs = {
    'table': 'zmc.patient_appointments',
    'hubs': [
        {
            'hub': 'zmc.hub_event',
            'keys': 'serums_id'
        }
    ]
}

zmc_patient_appointments_satellites = {
    'satellites': [
        {
            'satellite': 'zmc.sat_event_patient_appointments',
            'columns': [
                'type', 'date', 'notes'
            ],
            'hub': 'zmc.hub_event',
            'hub_id': 0
        }
    ]
}

zmc_patient_appointments_links = {
    'links': []
}