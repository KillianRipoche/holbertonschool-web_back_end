export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  const result = [];
  set.forEach((item) => {
    if (item.startsWith(startString)) {
      const restOfString = item.substring(startString.length);
      result.push(restOfString);
    }
  });

  return result.join('-');
}
