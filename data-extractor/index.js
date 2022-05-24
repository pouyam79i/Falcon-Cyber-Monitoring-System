// importing libs
const path = require('path');
const MTProto = require('@mtproto/core');

const api_id = YOU_API_ID;
const api_hash = YOU_API_HASH;

// 1. Create instance
const mtproto = new MTProto({
  api_id,
  api_hash,
  
  // defult storage
  storageOptions: {
    path: path.resolve(__dirname, './data/1.json'),
  },
});

// 2. Print the user country code
mtproto.call('help.getNearestDc').then(result => {
  console.log('country:', result.country);
});
