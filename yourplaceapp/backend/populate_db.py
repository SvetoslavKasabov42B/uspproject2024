from app import app, db
from models import Apartment

# Ensure you are running inside the application context
with app.app_context():
    db.create_all()

    # Add sample data
    sample_apartments = [
        Apartment(title="Modern Apartment", description="A modern apartment with all amenities.", price=1200),
        Apartment(title="Cozy Studio", description="A small but cozy studio apartment.", price=800),
        Apartment(title="Luxury Villa", description="A luxurious villa with a pool and garden.", price=5000),
    ]

    db.session.bulk_save_objects(sample_apartments)
    db.session.commit()
