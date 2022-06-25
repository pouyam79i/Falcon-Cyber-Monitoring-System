const api = require('./api.js');

getUser = async function() {
    try {
      const user = await api.call('users.getFullUser', {
        id: {
          _: 'inputUserSelf',
        },
      });
  
      return user;
    } catch (error) {
      return null;
    }
  }

module.exports = {
  getUser,
};
