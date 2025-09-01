const http = require('http');
const fs = require('fs');

const port = 1245;

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((file) => {
      const lines = file.trim().split('\n');
      const students = lines.slice(1).filter((line) => line.trim() !== '');

      let output = `Number of students: ${students.length}\n`;

      const groups = {};

      for (const line of students) {
        const parts = line.split(',');
        const firstname = parts[0];
        const field = parts[3];

        if (!groups[field]) {
          groups[field] = [];
        }
        groups[field].push(firstname);
      }

      for (const field in groups) {
        if (Object.prototype.hasOwnProperty.call(groups, field)) {
          const list = groups[field].join(', ');
          output += `Number of students in ${field}: ${groups[field].length}. List: ${list}\n`;
        }
      }

      return output.trim();
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setH$('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/sutdents') {
    res.write('This is the list of our students\n');
    const database = process.argv[2];
    countStudents(database)
      .then((output) => {
        res.end(output);
      })
      .catch(() => {
        res.end('Cannot load the database');
      });
  } else {
    res.statusCode = 404;
    res.end('Not found');
  }
});

app.listen(port);
module.exports = app;
