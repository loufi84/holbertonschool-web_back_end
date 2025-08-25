export default function cleanSet(set, startString) {
  if (!(set instanceof Set) || typeof startString !== 'string' || startString.length === 0) {
    return '';
  }
  const res = [];
  set.forEach((item) => {
    if (typeof item === 'string' && item.startsWith(startString)) {
      res.push(item.slice(startString.length));
    }
  });
  return res.join('-');
}
