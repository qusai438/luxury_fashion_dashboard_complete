from app.extensions import db

class APIKey(db.Model):
    __tablename__ = "api_keys"

    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(50), unique=True, nullable=False)
    key_value = db.Column(db.Text, nullable=False)

    @staticmethod
    def get(service_name):
        record = APIKey.query.filter_by(service_name=service_name).first()
        return record.key_value if record else ""

    @staticmethod
    def set(service_name, key_value):
        record = APIKey.query.filter_by(service_name=service_name).first()
        if record:
            record.key_value = key_value
        else:
            record = APIKey(service_name=service_name, key_value=key_value)
            db.session.add(record)
