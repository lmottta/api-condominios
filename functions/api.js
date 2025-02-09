const { handler } = require('./api.py');

exports.handler = async (event, context) => {
  try {
    return await handler(event, context);
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Internal server error' }),
      headers: {
        'Content-Type': 'application/json'
      }
    };
  }
}; 