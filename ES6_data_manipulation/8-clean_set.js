export default function cleanSet(set, startString) {
  const res = [];
  set.forEach((item) => {
    if (item.startsWith(startString)) {
      res.push(item.slice(startString.length));
    }
  });
  return res.join('-');
}
