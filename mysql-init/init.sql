CREATE TABLE IF NOT EXISTS articles (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titre VARCHAR(255) NOT NULL,
  contenu TEXT DEFAULT NULL,
  dt_publication DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO articles (titre, contenu)
VALUES
  ('Article 1', 'Contenu de l\'article 1'),
  ('Article 2', 'Contenu de l\'article 2'),
  ('Article 3', 'Contenu de l\'article 3'),
  ('Article 4', 'Contenu de l\'article 4'),
  ('Article 5', 'Contenu de l\'article 5');
