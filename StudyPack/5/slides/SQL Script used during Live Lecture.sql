SELECT * FROM nj_teachers_salaries.teacher;
-- SELECT count(primary_job) FROM teacher.nj_teachers_salaries;
-- SELECT last_name, first_name, max(salary) FROM teacher.nj_teachers_salaries WHERE primary_job ='Preschool' GROUP BY last_name, first_name, salary order by salary DESC;
-- SELECT salary FROM nj_teachers_salaries.teacher WHERE last_name= 'Smith' AND first_name='Brittany M';
-- SELECT last_name, first_name, salary FROM teacher.nj_teachers_salaries WHERE primary_job = 'Preschool' order by salary DESC;
-- SELECT COUNT(primary_job='Preschool') FROM teacher.nj_teachers_salaries WHERE district='Passaic City';
-- SELECT AVG(experience_total) FROM teacher.nj_teachers_salaries WHERE district='Passaic City' AND primary_job = 'Preschool';
-- SELECT experience_total FROM teacher.nj_teachers_salaries WHERE primary_job = 'Preschool' order by experience_total+0 DESC;
