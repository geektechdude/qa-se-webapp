from flask_table import Table, Col, LinkCol


class Results(Table):
    id = Col('id')
    serial_number = Col('Serial Number')
    device_model = Col('Device Model')
    assigned_to = Col('Assigned To')
    assigned_by = Col('Assigned By')
    edit = LinkCol('Edit', 'main.edit', url_kwargs=dict(id='id'))
