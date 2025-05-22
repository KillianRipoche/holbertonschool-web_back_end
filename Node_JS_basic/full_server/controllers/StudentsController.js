import readDatabase from '../utils.js';

class StudentsController {
  static async getAllStudents(req, res) {
    const filePath = process.argv[2];
    try {
      const data = await readDatabase(filePath);
      const response = ['This is the list of our students'];
      const fields = Object.keys(data).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      for (const field of fields) {
        response.push(`Number of students in ${field}: ${data[field].length}. List: ${data[field].join(', ')}`);
      }
      res.status(200).send(response.join('\n'));
    } catch (error) {
      res.status(500).send(error.message);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const filePath = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const data = await readDatabase(filePath);
      res.status(200).send(`List: ${data[major].join(', ')}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
