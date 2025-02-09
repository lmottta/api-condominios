const { handler } = require('./api.py');

exports.handler = async (event, context) => {
  return await handler(event, context);
}; 