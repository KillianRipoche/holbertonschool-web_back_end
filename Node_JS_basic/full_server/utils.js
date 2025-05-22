import fs from 'fs/promises';

export default async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    const lines = data.trim().split('\n').slice(1);
    const result = {};

    for (const line of lines) {
      const [firstname, , , field] = line.split(',');
      if (!result[field]) result[field] = [];
      result[field].push(firstname);
    }
    return result;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
