SET SQL_SAFE_UPDATES = 0;
SELECT primary_job, salary FROM nj_teachers_salaries.teacher WHERE salary between 50000 and 70000 order by salary;
UPDATE nj_teachers_salaries.teacher
SET experience_total=99999
WHERE experience_total = 0;
SELECT experience_total FROM nj_teachers_salaries.teacher where experience_total = 99999;
UPDATE nj_teachers_salaries.teacher
SET experience_total = 0
WHERE experience_total = 99999;
SELECT experience_total FROM nj_teachers_salaries.teacher where experience_total = 99999;
