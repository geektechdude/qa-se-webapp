from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from .forms import AddAsset, SearchAsset, EditAsset
from .tables import Results
from . import main
from .. import db
from ..models import Asset

@main.route('/', methods=['GET', 'POST'])
def index():
    search = SearchAsset(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('views/index.html', form=search)

@main.route('/asset/add', methods=['GET','POST'])
@login_required
def add_asset():
    form = AddAsset()
    if form.validate_on_submit():
        asset = Asset(serial_number = form.serial_number.data,
                    device_model = form.device_model.data,
                    assigned_to = form.assigned_to.data,
                    assigned_by = current_user.id)
        db.session.add(asset)
        db.session.commit()
        flash('Asset Added')
        return redirect(url_for('main.index'))
    return render_template('views/add_asset.html',form=form)

@main.route('/asset/results', methods=['GET'])
@login_required
def search_results(search):
    search_result = []
    search_string = search.data['search_criteria']
    search_query = db.session.query(Asset).filter(Asset.serial_number.contains(search_string))
    search_result = search_query.all()

    if not search_result:
        # Display a warning message if serial number not found
        flash('No results found. Please try a different Serial Number')
        return redirect('/')
    else:
        # Return results via the results template
        table = Results(search_result)
        table.border = True
        return render_template('views/results_asset.html', table=table)

@main.route('/asset/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    asset = Asset.query.filter_by(id=id).first_or_404()
    form = EditAsset()
    if form.validate_on_submit():
        asset = Asset(device_model = form.device_model.data,
                    assigned_to = form.assigned_to.data,
                    assigned_by = current_user.id)
        db.session.add(asset)
        db.session.commit()
        flash('Asset Updated')
        return redirect(url_for('main.index'))
    form.device_model.data = asset.device_model
    form.assigned_to.data = asset.assigned_to
    return render_template('views/edit_asset.html',form=form)
    

