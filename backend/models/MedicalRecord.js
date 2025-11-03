const db = require('./database');

class MedicalRecord {
  static create(recordData) {
    return new Promise((resolve, reject) => {
      const {
        patientId, doctorId, appointmentId, diagnosis, symptoms,
        treatment, medications, followUpDate, notes, recordDate
      } = recordData;

      const sql = `INSERT INTO medical_records (
        patientId, doctorId, appointmentId, diagnosis, symptoms,
        treatment, medications, followUpDate, notes, recordDate
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`;

      db.run(sql, [
        patientId, doctorId, appointmentId, diagnosis, symptoms,
        treatment, medications, followUpDate, notes, recordDate
      ], function(err) {
        if (err) {
          reject(err);
        } else {
          resolve({ id: this.lastID, ...recordData });
        }
      });
    });
  }

  static findAll() {
    return new Promise((resolve, reject) => {
      const sql = `SELECT 
        mr.*,
        p.firstName as patientFirstName,
        p.lastName as patientLastName,
        d.firstName as doctorFirstName,
        d.lastName as doctorLastName,
        d.specialization as doctorSpecialization
      FROM medical_records mr
      JOIN patients p ON mr.patientId = p.id
      JOIN doctors d ON mr.doctorId = d.id
      ORDER BY mr.recordDate DESC`;

      db.all(sql, [], (err, rows) => {
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
      const sql = `SELECT 
        mr.*,
        p.firstName as patientFirstName,
        p.lastName as patientLastName,
        d.firstName as doctorFirstName,
        d.lastName as doctorLastName,
        d.specialization as doctorSpecialization
      FROM medical_records mr
      JOIN patients p ON mr.patientId = p.id
      JOIN doctors d ON mr.doctorId = d.id
      WHERE mr.id = ?`;

      db.get(sql, [id], (err, row) => {
        if (err) {
          reject(err);
        } else {
          resolve(row);
        }
      });
    });
  }

  static findByPatient(patientId) {
    return new Promise((resolve, reject) => {
      const sql = `SELECT 
        mr.*,
        d.firstName as doctorFirstName,
        d.lastName as doctorLastName,
        d.specialization as doctorSpecialization
      FROM medical_records mr
      JOIN doctors d ON mr.doctorId = d.id
      WHERE mr.patientId = ?
      ORDER BY mr.recordDate DESC`;

      db.all(sql, [patientId], (err, rows) => {
        if (err) {
          reject(err);
        } else {
          resolve(rows);
        }
      });
    });
  }

  static findByDoctor(doctorId) {
    return new Promise((resolve, reject) => {
      const sql = `SELECT 
        mr.*,
        p.firstName as patientFirstName,
        p.lastName as patientLastName
      FROM medical_records mr
      JOIN patients p ON mr.patientId = p.id
      WHERE mr.doctorId = ?
      ORDER BY mr.recordDate DESC`;

      db.all(sql, [doctorId], (err, rows) => {
        if (err) {
          reject(err);
        } else {
          resolve(rows);
        }
      });
    });
  }

  static update(id, recordData) {
    return new Promise((resolve, reject) => {
      const {
        diagnosis, symptoms, treatment, medications,
        followUpDate, notes
      } = recordData;

      const sql = `UPDATE medical_records SET 
        diagnosis = ?, symptoms = ?, treatment = ?,
        medications = ?, followUpDate = ?, notes = ?,
        updatedAt = CURRENT_TIMESTAMP
        WHERE id = ?`;

      db.run(sql, [
        diagnosis, symptoms, treatment, medications,
        followUpDate, notes, id
      ], function(err) {
        if (err) {
          reject(err);
        } else {
          resolve({ id, ...recordData });
        }
      });
    });
  }

  static delete(id) {
    return new Promise((resolve, reject) => {
      db.run('DELETE FROM medical_records WHERE id = ?', [id], function(err) {
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
      const sql = `SELECT 
        mr.*,
        p.firstName as patientFirstName,
        p.lastName as patientLastName,
        d.firstName as doctorFirstName,
        d.lastName as doctorLastName
      FROM medical_records mr
      JOIN patients p ON mr.patientId = p.id
      JOIN doctors d ON mr.doctorId = d.id
      WHERE mr.diagnosis LIKE ? OR mr.symptoms LIKE ? OR mr.treatment LIKE ?
      ORDER BY mr.recordDate DESC`;
      
      const term = `%${searchTerm}%`;
      db.all(sql, [term, term, term], (err, rows) => {
        if (err) {
          reject(err);
        } else {
          resolve(rows);
        }
      });
    });
  }
}

module.exports = MedicalRecord;