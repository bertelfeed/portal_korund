INSERT INTO Topic (topic_name, topic_description) VALUES
('Физика', 'Научное исследование свойств и закономерностей материи и энергии.'),
('Информатика', 'Изучение автоматической обработки информации, включая теоретические основы и применение.'),
('Математика', 'Исследование количественных и пространственных отношений, структур и изменений.');

INSERT INTO Employee (last_name, first_name, middle_name, employment_status, employee_number, role, email, additional_info, photo, birth_date, hire_date, termination_date) VALUES
('Эйнштейн', 'Альберт', NULL, 'активный', 'E001', 'Физик', 'einstein@example.com', 'Нобелевский лауреат по физике 1921 года', 'photo_einstein.jpg', '1879-03-14', '1905-01-01', NULL),
('Лавлейс', 'Ада', NULL, 'активный', 'E002', 'Программист', 'lovelace@example.com', 'Первая программистка в мире', 'photo_lovelace.jpg', '1815-12-10', '1842-01-01', NULL),
('Кюри', 'Мария', NULL, 'активный', 'E003', 'Химик', 'curie@example.com', 'Нобелевский лауреат по химии и физике', 'photo_curie.jpg', '1867-11-07', '1903-01-01', NULL);

INSERT INTO Phone (phone_number, phone_type, employee_id) VALUES
('+1234567890', 'Мобильный', 1),
('+0987654321', 'Рабочий', 2),
('+1122334455', 'Домашний', 3);

INSERT INTO News (title, description, topic_id, photo, employee_id, status, show_author) VALUES
('Новая теория относительности', 'Альберт Эйнштейн представил новую теорию относительности.', 1, 'photo_news_einstein.jpg', 1, 'опубликовано', TRUE),
('Ада Лавлейс: Первая программистка', 'Ада Лавлейс написала первый алгоритм для вычислительной машины.', 2, 'photo_news_lovelace.jpg', 2, 'опубликовано', TRUE),
('Открытие радия', 'Мария Кюри открыла новый элемент - радий.', 3, 'photo_news_curie.jpg', 3, 'опубликовано', TRUE);

INSERT INTO File (file_name, file_path, file_type, news_id) VALUES
('relativity_paper.pdf', '/files/relativity_paper.pdf', 'PDF', 1),
('ada_algorithm.txt', '/files/ada_algorithm.txt', 'TXT', 2),
('radium_discovery.doc', '/files/radium_discovery.doc', 'DOC', 3);

INSERT INTO Chat (chat_name) VALUES
('Обсуждение теории относительности'),
('История программирования'),
('Радиоактивные элементы');

INSERT INTO Chat_Participant (chat_id, employee_id) VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO Message (chat_id, employee_id, message_content, attached_file) VALUES
(1, 1, 'Добро пожаловать в обсуждение теории относительности!', NULL),
(2, 2, 'Начнем обсуждение истории программирования.', NULL),
(3, 3, 'Рассмотрим радиоактивные элементы и их свойства.', NULL);

INSERT INTO Education (employee_id, institution, degree, major, graduation_year) VALUES
(1, 'Цюрихский политехнический институт', 'Доктор наук', 'Физика', 1900),
(2, 'Королевский колледж Лондона', 'Бакалавр', 'Математика', 1835),
(3, 'Парижский университет', 'Доктор наук', 'Химия', 1903);

INSERT INTO Activity_Log (employee_id, activity) VALUES
(1, 'Создание новой теории относительности'),
(2, 'Разработка алгоритма для вычислительной машины'),
(3, 'Открытие нового химического элемента');

INSERT INTO Activity_Log (employee_id, activity) VALUES
(1, 'Создание новой теории относительности'),
(2, 'Разработка алгоритма для вычислительной машины'),
(3, 'Открытие нового химического элемента');

INSERT INTO Event (event_name, event_description, start_time, end_time, employee_id, participant_list) VALUES
('Презентация теории относительности', 'Альберт Эйнштейн представит свою новую теорию.', '2024-06-15 10:00:00', '2024-06-15 12:00:00', 1, '["Альберт Эйнштейн", "Нильс Бор", "Вернер Гейзенберг"]'),
('Лекция о программировании', 'Ада Лавлейс расскажет о своем алгоритме.', '2024-06-16 14:00:00', '2024-06-16 16:00:00', 2, '["Ада Лавлейс", "Чарльз Бэббидж"]'),
('Семинар по радиоактивности', 'Мария Кюри расскажет о своих открытиях.', '2024-06-17 09:00:00', '2024-06-17 11:00:00', 3, '["Мария Кюри", "Пьер Кюри"]');

INSERT INTO Project (project_name, project_description, start_date, end_date, project_status, project_leader_id) VALUES
('Теория относительности', 'Исследование относительности времени и пространства.', '1905-01-01', '1915-01-01', 'завершен', 1),
('Аналитическая машина', 'Разработка алгоритмов для вычислительной машины.', '1835-01-01', '1852-01-01', 'завершен', 2),
('Исследование радиоактивности', 'Изучение свойств радиоактивных элементов.', '1898-01-01', '1903-01-01', 'завершен', 3);

INSERT INTO Task (task_name, task_description, start_date, end_date, task_status, project_id, assignee_id) VALUES
('Разработка уравнений', 'Разработка уравнений для теории относительности.', '1905-01-01', '1910-01-01', 'завершена', 1, 1),
('Написание алгоритма', 'Написание первого алгоритма для вычислительной машины.', '1835-01-01', '1842-01-01', 'завершена', 2, 2),
('Открытие радия', 'Открытие нового химического элемента - радий.', '1898-01-01', '1902-01-01', 'завершена', 3, 3);

INSERT INTO Document_Archive (document_name, document_path, document_type, employee_id, upload_date) VALUES
('Теория относительности', '/documents/relativity.pdf', 'PDF', 1, '1905-11-25'),
('Алгоритм Лавлейс', '/documents/lovelace_algorithm.txt', 'TXT', 2, '1842-06-12'),
('Исследование радиоактивности', '/documents/radioactivity_study.doc', 'DOC', 3, '1903-12-10');
