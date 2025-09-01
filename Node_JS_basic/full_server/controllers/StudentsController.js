const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    const db = process.argv[2];

    readDatabase(db)
      .then((fields) => {
        let output = 'This is the list of our students\n';

        const sortedFields = Object.keys(fields).sort(
          (a, b) => a.toLowerCase().localeCompare(b.toLowerCase()),
        );

        sortedFields.forEach((field, index) => {
          const list = fields[field];
          output += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
          if (index !== sortedFields.length - 1) {
            output += '\n';
          }
        });

        res.status(200).send(output);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const db = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must bu CS or SWE');
      return;
    }

    readDatabase(db)
      .then((fields) => {
        const list = fields[major] || [];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;