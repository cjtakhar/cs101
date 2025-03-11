SELECT * FROM nj_teachers_salaries.teacher;
SELECT 'salary', 'experience_total' FROM nj_teachers_salaries.teacher 
UNION

(SELECT DISTINCT salary, experience_total FROM nj_teachers_salaries.teacher
ORDER BY RAND(7)
LIMIT 777);