from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from .forms import AddAsset
from . import main
from .. import db
from ..models import Asset

@main.route('/', methods=['GET'])
def index():
    return render_template('views/index.html')

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
