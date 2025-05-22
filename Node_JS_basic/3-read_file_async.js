const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf-8')
    .then((data) => {
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1).map((line) => line.split(','));

      const fields = {};
      for (const student of students) {
        const field = student[3];
        const firstname = student[0];
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      }

      process.stdout.write(`Number of students: ${students.length}\n`);
      for (const field in fields) {
        process.stdout.write(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`);
      }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
