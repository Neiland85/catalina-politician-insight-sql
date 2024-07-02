-- Consultas SQL para Catalina Politician Insight

-- Obtener información básica del político por nombre
SELECT * FROM politicians WHERE name = 'nombre_del_politico';

-- Otra consulta de ejemplo
SELECT * FROM donations WHERE politician_id = (SELECT id FROM politicians WHERE name = 'nombre_del_politico');

