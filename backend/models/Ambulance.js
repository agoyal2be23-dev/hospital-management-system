const mongoose = require('mongoose');

const AmbulanceSchema = new mongoose.Schema({
  number: { type: String, required: true },
  status: { type: String, enum: ['available', 'booked', 'maintenance'], default: 'available' },
  location: {
    latitude: { type: Number },
    longitude: { type: Number }
  },
  lastUpdated: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Ambulance', AmbulanceSchema);