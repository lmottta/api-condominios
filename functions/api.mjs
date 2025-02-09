import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { spawn } = require('child_process');

export const handler = async (event, context) => {
  try {
    // Configurar CORS
    const headers = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE'
    };

    // Executar o script Python
    const pythonProcess = spawn('python', ['functions/api.py', JSON.stringify(event)]);
    
    return new Promise((resolve, reject) => {
      let result = '';
      
      pythonProcess.stdout.on('data', (data) => {
        result += data.toString();
      });

      pythonProcess.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
      });

      pythonProcess.on('close', (code) => {
        if (code !== 0) {
          resolve({
            statusCode: 500,
            headers,
            body: JSON.stringify({ error: 'Internal server error' })
          });
        } else {
          try {
            const response = JSON.parse(result);
            resolve({
              statusCode: 200,
              headers,
              body: JSON.stringify(response)
            });
          } catch (e) {
            resolve({
              statusCode: 200,
              headers,
              body: result
            });
          }
        }
      });
    });
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Internal server error' })
    };
  }
}; 