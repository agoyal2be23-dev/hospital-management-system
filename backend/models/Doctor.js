const db = require('./database');

class Doctor {
  static create(doctorData) {
    return new Promise((resolve, reject) => {
      const {
        firstName, lastName, email, phone, specialization,
        licenseNumber, department, experience, qualifications,
        consultationFee, availability
      } = doctorData;

      const sql = `INSERT INTO doctors (
        firstName, lastName, email, phone, specialization,
        licenseNumber, department, experience, qualifications,
        consultationFee, availability
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`;

      db.run(sql, [
        firstName, lastName, email, phone, specialization,
        licenseNumber, department, experience, qualifications,
        consultationFee, availability
      ], function(err) {
        if (err) {
          reject(err);
        } else {
          resolve({ id: this.lastID, ...doctorData });
        }
      });
    });
  }

  static findAll() {
    return new Promise((resolve, reject) => {
      db.all('SELECT * FROM doctors ORDER BY createdAt DESC', [], (err, rows) => {
        if (err) {
          reject(err);
        } else {
          resolve(rows);
        }
      });
    });
  }

  static findById(id) {
    return new Promise((resolve, reject) => {
      db.get('SELECT * FROM doctors WHERE id = ?', [id], (err, row) => {
        if (err) {
          reject(err);
        } else {
          resolve(row);
        }
      });
    });
  }

  static findBySpecialization(specialization) {
    return new Promise((resolve, reject) => {
      db.all('SELECT * FROM doctors WHERE specialization = ?', [specialization], (err, rows) => {
        if (err) {
          reject(err);
        } else {
          resolve(rows);
        }
      });
    });
  }

  static update(id, doctorData) {
    return new Promise((resolve, reject) => {
      const {
        firstName, lastName, email, phone, specialization,
        licenseNumber, department, experience, qualifications,
        consultationFee, availability
      } = doctorData;

      const sql = `UPDATE doctors SET 
        firstName = ?, lastName = ?, email = ?, phone = ?,
        specialization = ?, licenseNumber = ?, department = ?,
        experience = ?, qualifications = ?, consultationFee = ?,
        availability = ?, updatedAt = CURRENT_TIMESTAMP
        WHERE id = ?`;

      db.run(sql, [
        firstName, lastName, email, phone, specialization,
        licenseNumber, department, experience, qualifications,
        consultationFee, availability, id
      ], function(err) {
        if (err) {
          reject(err);
        } else {
          resolve({ id, ...doctorData });
        }
      });
    });
  }

  static delete(id) {
    return new Promise((resolve, reject) => {
      db.run('DELETE FROM doctors WHERE id = ?', [id], function(err) {
        if (err) {
          reject(err);
        } else {
          resolve({ deleted: this.changes > 0 });
        }
      });
    });
  }

  static search(searchTerm) {
    return new Promise((resolve, reject) => {
      const sql = `SELECT * FROM doctors 
        WHERE firstName LIKE ? OR lastName LIKE ? OR specialization LIKE ? OR department LIKE ?
        ORDER BY createdAt DESC`;
      
      const term = `%${searchTerm}%`;
      db.all(sql, [term, term, term, term], (err, rows) => {
        if (err) {
          reject(err);
        } else {
          resolve(rows);
        }
      });
    });
  }
}

module.exports = Doctor;