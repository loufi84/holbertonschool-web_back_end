export default function getStudentsByLocation(studentsList, city) {
  return studentsList.filter((loc) => loc.location === city);
}
