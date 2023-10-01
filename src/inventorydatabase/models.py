from inventorydatabase import db


class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), nullable=False)
    item_location = db.Column(db.String(50), nullable=False)
    item_quantity = db.Column(db.Integer, nullable=False)
    item_value = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"InventoryItem('{self.item_name}', '{self.item_location}', '{self.item_quantity}', '{self.item_value}')"

