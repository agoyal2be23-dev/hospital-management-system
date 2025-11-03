const db = require('./database');

class Appointment {
  static create(appointmentData) {
    return new Promise((resolve, reject) => {
      const {
        patientId, doctorId, appointmentDate, appointmentTime,
        duration, reason, notes
      } = appointmentData;

      const sql = `INSERT INTO appointments (
        patientId, doctorId, appointmentDate, appointmentTime,
        duration, reason, notes
      ) VALUES (?, ?, ?, ?, ?, ?, ?)`;

      db.run(sql, [
        patientId, doctorId, appointmentDate, appointmentTime,
        duration || 30, reason, notes
      ], function(err) {
        if (err) {
          reject(err);
        } else {
          resolve({ id: this.lastID, ...appointmentData });
        }
      });
    });
  }

  static findAll() {
    return new Promise((resolve, reject) => {
      const sql = `SELECT 
        a.*,
        p.firstName as patientFirstName,
        p.lastName as patientLastName,
        p.phone as patientPhone,
        d.firstName as doctorFirstName,
        d.lastName as doctorLastName,
        d.specialization as doctorSpecialization
      FROM appointments a
      JOIN patients p ON a.patientId = p.id
      JOIN doctors d ON a.doctorId = d.id
      ORDER BY a.appointmentDate DESC, a.appointmentTime DESC`;

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
        a.*,
        p.firstName as patientFirstName,
        p.lastName as patientLastName,
        p.phone as patientPhone,
        d.firstName as doctorFirstName,
        d.lastName as doctorLastName,
        d.specialization as doctorSpecialization
      FROM appointments a
      JOIN patients p ON a.patientId = p.id
      JOIN doctors d ON a.doctorId = d.id
      WHERE a.id = ?`;

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
        a.*,
        d.firstName as doctorFirstName,
        d.lastName as doctorLastName,
        d.specialization as doctorSpecialization
      FROM appointments a
      JOIN doctors d ON a.doctorId = d.id
      WHERE a.patientId = ?
      ORDER BY a.appointmentDate DESC, a.appointmentTime DESC`;

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
        a.*,
        p.firstName as patientFirstName,
        p.lastName as patientLastName,
        p.phone as patientPhone
      FROM appointments a
      JOIN patients p ON a.patientId = p.id
      WHERE a.doctorId = ?
      ORDER BY a.appointmentDate DESC, a.appointmentTime DESC`;

      db.all(sql, [doctorId], (err, rows) => {
        if (err) {
          reject(err);
        } else {
          resolve(rows);
        }
      });
    });
  }

  static update(id, appointmentData) {
    return new Promise((resolve, reject) => {
      const {
        patientId, doctorId, appointmentDate, appointmentTime,
        duration, status, reason, notes
      } = appointmentData;

      const sql = `UPDATE appointments SET 
        patientId = ?, doctorId = ?, appointmentDate = ?,
        appointmentTime = ?, duration = ?, status = ?,
        reason = ?, notes = ?, updatedAt = CURRENT_TIMESTAMP
        WHERE id = ?`;

      db.run(sql, [
        patientId, doctorId, appointmentDate, appointmentTime,
        duration, status, reason, notes, id
      ], function(err) {
        if (err) {
          reject(err);
        } else {
          resolve({ id, ...appointmentData });
        }
      });
    });
  }

  static updateStatus(id, status) {
    return new Promise((resolve, reject) => {
      const sql = `UPDATE appointments SET 
        status = ?, updatedAt = CURRENT_TIMESTAMP
        WHERE id = ?`;

      db.run(sql, [status, id], function(err) {
        if (err) {
          reject(err);
        } else {
          resolve({ id, status });
        }
      });
    });
  }

  static delete(id) {
    return new Promise((resolve, reject) => {
      db.run('DELETE FROM appointments WHERE id = ?', [id], function(err) {
        if (err) {
          reject(err);
        } else {
          resolve({ deleted: this.changes > 0 });
        }
      });
    });
  }

  static findByDate(date) {
    return new Promise((resolve, reject) => {
      const sql = `SELECT 
        a.*,
        p.firstName as patientFirstName,
        p.lastName as patientLastName,
        d.firstName as doctorFirstName,
        d.lastName as doctorLastName,
        d.specialization as doctorSpecialization
      FROM appointments a
      JOIN patients p ON a.patientId = p.id
      JOIN doctors d ON a.doctorId = d.id
      WHERE a.appointmentDate = ?
      ORDER BY a.appointmentTime`;

      db.all(sql, [date], (err, rows) => {
        if (err) {
          reject(err);
        } else {
          resolve(rows);
        }
      });
    });
  }
}

module.exports = Appointment;