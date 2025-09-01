const fs = require('fs');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      if (lines.lenght <= 1) {
        resolve({});
        return;
      }

      const students = lines.slice(1);
      const fields = {};

      for (const line of students) {
        const parts = line.split(',');
        if (parts.length >= 4) {
          const firstname = parts[0].trim();
          const field = parts[3].trim();

          if (!fields[field]) fields[field] = [];
          fields[field].push(firstname);
        }
      }

      resolve(fields);
    });
  });
}

module.exports = readDatabase;
