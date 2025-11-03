from flask_backend.app_integrated import app, db, Doctor

def check_doctors():
    with app.app_context():
        doctors = Doctor.query.all()
        print(f"Total doctors in database: {len(doctors)}")
        print("\nAll doctors:")
        for doc in doctors:
            print(f"- Dr. {doc.firstName} {doc.lastName} ({doc.specialization})")
        
        # Check breast cancer specialists specifically
        breast_cancer_docs = Doctor.query.filter(
            Doctor.specialization.ilike('%breast%')
        ).all()
        
        print(f"\nBreast cancer specialists: {len(breast_cancer_docs)}")
        for doc in breast_cancer_docs:
            print(f"- Dr. {doc.firstName} {doc.lastName} ({doc.specialization})")

if __name__ == '__main__':
    check_doctors()