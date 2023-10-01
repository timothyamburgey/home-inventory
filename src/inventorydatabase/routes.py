from inventorydatabase.models import InventoryItem
from inventorydatabase.form import AddItemForm
from flask import render_template, redirect, flash, url_for, request
from inventorydatabase import app
from inventorydatabase import session


@app.route('/')
@app.route('/home')
def home():
    inventory_items = InventoryItem.query.all()
    return render_template('index.html', item_data=inventory_items)

@app.route('/about')
@app.route('/about-the-app')
def about():
    return render_template('about.html')

@app.route('/add', methods=['GET', 'POST'])
def add_redirect():
    form = AddItemForm()
    if form.validate_on_submit():
        flash(f'Item {form.item_name.data} has been added to the inventory!', 'success')
        new_item = InventoryItem(item_name=form.item_name.data, item_location=form.item_location.data, item_quantity=form.item_quantity.data, item_value=form.item_value.data)
        session.add(new_item)
        session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form, title='Add Inventory Item')

@app.route('/edit')
@app.route('/edit-item')
def edit_redirect():
    return redirect('/')

@app.route('/delete')
@app.route('/delete-item')
def delete_redirect():
    return redirect('/')

@app.route('/delete/<int:item_id>', methods=['GET', 'POST'])
def delete_item(item_id):
    item_id = item_id
    item_to_delete = session.query(InventoryItem).filter_by(id=item_id).first()
    item_to_delete.id = item_id
    print(item_to_delete)
    session.delete(item_to_delete)
    session.commit()
    flash(f'Item {item_to_delete.item_name} has been deleted from the inventory!', 'success')
    return redirect(url_for('home'))

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item_id = item_id
    item_to_edit = session.query(InventoryItem).filter_by(id=item_id).first()
    item_to_edit.id = item_id
    print(item_to_edit)
    form = AddItemForm()
    if form.validate_on_submit():
        flash(f'Item {form.item_name.data} has been updated!', 'success')
        item_to_edit.item_name = form.item_name.data
        item_to_edit.item_location = form.item_location.data
        item_to_edit.item_quantity = form.item_quantity.data
        item_to_edit.item_value = form.item_value.data

        session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.item_name.data = item_to_edit.item_name
        form.item_location.data = item_to_edit.item_location
        form.item_quantity.data = item_to_edit.item_quantity
        form.item_value.data = item_to_edit.item_value
    return render_template('edit.html', form=form, title='Edit Inventory Item', item=item_to_edit)