const api = require('./api.js');
const {getUser} = require('./authorizer.js');

start = async function () {
    
    const user = await getUser();

    console.log("#### FLAG 1");

    const resolvedPeer = await api.call('contacts.resolveUsername', {
      username: 'mtproto_core',
    });

    console.log("#### FLAG 2");
  
    const channel = resolvedPeer.chats.find(
      (chat) => chat.id === resolvedPeer.peer.channel_id
    );

    console.log("#### FLAG 3");
  
    const inputPeer = {
      _: 'inputPeerChannel',
      channel_id: channel.id,
      access_hash: channel.access_hash,
    };

    console.log("#### FLAG 4");
  
    const LIMIT_COUNT = 10;
    const allMessages = [];
  
    console.log("#### FLAG 5");

    const firstHistoryResult = await api.call('messages.getHistory', {
      peer: inputPeer,
      limit: LIMIT_COUNT,
    });

    console.log("#### FLAG 6");
  
    const historyCount = firstHistoryResult.count;
  
    for (let offset = 0; offset < historyCount; offset += LIMIT_COUNT) {
      const history = await api.call('messages.getHistory', {
        peer: inputPeer,
        add_offset: offset,
        limit: LIMIT_COUNT,
      });
  
      allMessages.push(...history.messages);
    }

    console.log("#### FLAG 7");
  
    console.log('allMessages:', allMessages);
  };
  
start()
