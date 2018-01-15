const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

const UserSchema = new mongoose.Schema({
    email: {
        type: String,
        index: { Unique: true }
    },
    password: String
})

UserSchema.methods.comparePassword = function comparePassword(password, callback) {
  // bcrypt will automatically add salt and then compare the password from db
  bcrypt.compare(password, this.password, callback);
};

UserSchema.pre('save', function saveHook(next) {
    const user = this;
  
    // proceed furhter only if the password is modified or the user is new.
    if (!user.isModified('password')) return next();
  
    return bcrypt.genSalt((saltError, salt) => {
      if (saltError) { return next(saltError); }
  
      return bcrypt.hash(user.password, salt, (hashError, hash) => {
        if (hashError) { return next(hashError); }
  
        // replace a password string with hashed value.
        user.password = hash;

        return next();
      });
    });
  });

module.exports = mongoose.model('User', UserSchema);