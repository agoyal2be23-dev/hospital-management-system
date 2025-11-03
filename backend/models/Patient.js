const db = require('./database');

class Patient {
  static create(patientData) {
    return new Promise((resolve, reject) => {
      const {
        firstName, lastName, email, phone, dateOfBirth, gender,
        address, emergencyContact, emergencyPhone, medicalHistory,
        allergies, bloodType
      } = patientData;

      const sql = `INSERT INTO patients (
        firstName, lastName, email, phone, dateOfBirth, gender,
        address, emergencyContact, emergencyPhone, medicalHistory,
        allergies, bloodType
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`;

      db.run(sql, [
        firstName, lastName, email, phone, dateOfBirth, gender,
        address, emergencyContact, emergencyPhone, medicalHistory,
        allergies, bloodType
      ], function(err) {
        if (err) {
          reject(err);
        } else {
          resolve({ id: this.lastID, ...patientData });
        }
      });
    });
  }

  static findAll() {
    return new Promise((resolve, reject) => {
      db.all('SELECT * FROM patients ORDER BY createdAt DESC', [], (err, rows) => {
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
      db.get('SELECT * FROM patients WHERE id = ?', [id], (err, row) => {
        if (err) {
          reject(err);
        } else {
          resolve(row);
        }
      });
    });
  }

  static update(id, patientData) {
    return new Promise((resolve, reject) => {
      const {
        firstName, lastName, email, phone, dateOfBirth, gender,
        address, emergencyContact, emergencyPhone, medicalHistory,
        allergies, bloodType
      } = patientData;

      const sql = `UPDATE patients SET 
        firstName = ?, lastName = ?, email = ?, phone = ?, 
        dateOfBirth = ?, gender = ?, address = ?, 
        emergencyContact = ?, emergencyPhone = ?, medicalHistory = ?,
        allergies = ?, bloodType = ?, updatedAt = CURRENT_TIMESTAMP
        WHERE id = ?`;

      db.run(sql, [
        firstName, lastName, email, phone, dateOfBirth, gender,
        address, emergencyContact, emergencyPhone, medicalHistory,
        allergies, bloodType, id
      ], function(err) {
        if (err) {
          reject(err);
        } else {
          resolve({ id, ...patientData });
        }
      });
    });
  }

  static delete(id) {
    return new Promise((resolve, reject) => {
      db.run('DELETE FROM patients WHERE id = ?', [id], function(err) {
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
      const sql = `SELECT * FROM patients 
        WHERE firstName LIKE ? OR lastName LIKE ? OR email LIKE ? OR phone LIKE ?
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

module.exports = Patient;