-- Тема
CREATE TABLE Topic (
    topic_id SERIAL PRIMARY KEY, -- Идентификатор темы
    topic_name VARCHAR(255) NOT NULL, -- Название темы
    topic_description TEXT NOT NULL -- Описание темы
);

-- Сотрудник
CREATE TABLE Employee (
    employee_id SERIAL PRIMARY KEY, -- Идентификатор сотрудника
    last_name VARCHAR(100) NOT NULL, -- Фамилия
    first_name VARCHAR(100) NOT NULL, -- Имя
    middle_name VARCHAR(100), -- Отчество
    employment_status VARCHAR(50) NOT NULL DEFAULT 'активный', -- Статус работы (по умолчанию 'активный')
    employee_number VARCHAR(50) NOT NULL, -- Номер сотрудника
    role VARCHAR(50) NOT NULL, -- Роль
    email VARCHAR(100) NOT NULL, -- Email
    additional_info TEXT, -- Дополнительная информация
    photo VARCHAR(255), -- Фотография
    birth_date DATE, -- Дата рождения
    hire_date DATE NOT NULL, -- Дата найма
    termination_date DATE -- Дата увольнения
);

-- Телефон
CREATE TABLE Phone (
    phone_id SERIAL PRIMARY KEY, -- Идентификатор телефона
    phone_number VARCHAR(20) NOT NULL, -- Номер телефона
    phone_type VARCHAR(50) NOT NULL, -- Тип телефона
    employee_id INTEGER REFERENCES Employee(employee_id) NOT NULL -- Идентификатор сотрудника (внешний ключ)
);

-- Новость
CREATE TABLE News (
    news_id SERIAL PRIMARY KEY, -- Идентификатор новости
    title VARCHAR(255) NOT NULL, -- Заголовок
    description TEXT NOT NULL, -- Описание
    topic_id INTEGER REFERENCES Topic(topic_id), -- Идентификатор темы (внешний ключ)
    photo VARCHAR(255), -- Фото
    employee_id INTEGER REFERENCES Employee(employee_id), -- Идентификатор сотрудника (внешний ключ)
    status VARCHAR(50) NOT NULL DEFAULT 'черновик', -- Статус (по умолчанию 'черновик')
    show_author BOOLEAN NOT NULL DEFAULT FALSE -- Показывать автора (по умолчанию FALSE)
);

-- Файл
CREATE TABLE File (
    file_id SERIAL PRIMARY KEY, -- Идентификатор файла
    file_name VARCHAR(255) NOT NULL, -- Имя файла
    file_path VARCHAR(255) NOT NULL, -- Путь к файлу
    file_type VARCHAR(50) NOT NULL, -- Тип файла
    news_id INTEGER REFERENCES News(news_id) NOT NULL -- Идентификатор новости (внешний ключ)
);

-- Чат
CREATE TABLE Chat (
    chat_id SERIAL PRIMARY KEY, -- Идентификатор чата
    chat_name VARCHAR(255) NOT NULL, -- Название чата
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL -- Время создания (по умолчанию текущее время)
);

-- Участник чата (для групповых чатов)
CREATE TABLE Chat_Participant (
    chat_participant_id SERIAL PRIMARY KEY, -- Идентификатор участника чата
    chat_id INTEGER REFERENCES Chat(chat_id) NOT NULL, -- Идентификатор чата (внешний ключ)
    employee_id INTEGER REFERENCES Employee(employee_id) NOT NULL -- Идентификатор сотрудника (внешний ключ)
);

-- Сообщение
CREATE TABLE Message (
    message_id SERIAL PRIMARY KEY, -- Идентификатор сообщения
    chat_id INTEGER REFERENCES Chat(chat_id) NOT NULL, -- Идентификатор чата (внешний ключ)
    employee_id INTEGER REFERENCES Employee(employee_id) NOT NULL, -- Идентификатор сотрудника (внешний ключ)
    message_content TEXT NOT NULL, -- Содержание сообщения
    send_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, -- Время отправки (по умолчанию текущее время)
    attached_file VARCHAR(255) -- Вложенный файл
);

-- Образование
CREATE TABLE Education (
    education_id SERIAL PRIMARY KEY, -- Идентификатор образования
    employee_id INTEGER REFERENCES Employee(employee_id) NOT NULL, -- Идентификатор сотрудника (внешний ключ)
    institution VARCHAR(255) NOT NULL, -- Учебное заведение
    degree VARCHAR(100) NOT NULL, -- Степень
    major VARCHAR(100) NOT NULL, -- Специальность
    graduation_year INTEGER NOT NULL -- Год окончания
);

-- Лог действий
CREATE TABLE Activity_Log (
    activity_log_id SERIAL PRIMARY KEY, -- Идентификатор лога действий
    employee_id INTEGER REFERENCES Employee(employee_id) NOT NULL, -- Идентификатор сотрудника (внешний ключ)
    activity TEXT NOT NULL, -- Действие
    activity_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL -- Время действия (по умолчанию текущее время)
);

-- Уведомление
CREATE TABLE Notification (
    notification_id SERIAL PRIMARY KEY, -- Идентификатор уведомления
    employee_id INTEGER REFERENCES Employee(employee_id) NOT NULL, -- Идентификатор сотрудника (внешний ключ)
    notification_text TEXT NOT NULL, -- Текст уведомления
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, -- Время создания (по умолчанию текущее время)
    status VARCHAR(50) NOT NULL DEFAULT 'непрочитано' -- Статус (по умолчанию 'непрочитано')
);

-- Событие
CREATE TABLE Event (
    event_id SERIAL PRIMARY KEY, -- Идентификатор события
    event_name VARCHAR(255) NOT NULL, -- Название события
    event_description TEXT, -- Описание события
    start_time TIMESTAMP NOT NULL, -- Дата и время начала
    end_time TIMESTAMP NOT NULL, -- Дата и время окончания
    employee_id INTEGER REFERENCES Employee(employee_id) NOT NULL, -- Идентификатор сотрудника (внешний ключ)
    participant_list TEXT -- Список участников (можно использовать JSON или другой подходящий формат)
);

-- Проект
CREATE TABLE Project (
    project_id SERIAL PRIMARY KEY, -- Идентификатор проекта
    project_name VARCHAR(255) NOT NULL, -- Название проекта
    project_description TEXT, -- Описание проекта
    start_date DATE NOT NULL, -- Дата начала
    end_date DATE, -- Дата окончания
    project_status VARCHAR(50) NOT NULL DEFAULT 'активный', -- Статус проекта (по умолчанию 'активный')
    project_leader_id INTEGER REFERENCES Employee(employee_id) -- Идентификатор руководителя проекта (внешний ключ)
);

-- Задача
CREATE TABLE Task (
    task_id SERIAL PRIMARY KEY, -- Идентификатор задачи
    task_name VARCHAR(255) NOT NULL, -- Название задачи
    task_description TEXT, -- Описание задачи
    start_date DATE NOT NULL, -- Дата начала
    end_date DATE, -- Дата окончания
    task_status VARCHAR(50) NOT NULL DEFAULT 'в процессе', -- Статус задачи (по умолчанию 'в процессе')
    project_id INTEGER REFERENCES Project(project_id) NOT NULL, -- Идентификатор проекта (внешний ключ)
    assignee_id INTEGER REFERENCES Employee(employee_id) -- Идентификатор исполнителя (внешний ключ)
);

-- Архив рабочих документов
CREATE TABLE Document_Archive (
    document_id SERIAL PRIMARY KEY, -- Идентификатор документа
    document_name VARCHAR(255) NOT NULL, -- Имя документа
    document_path VARCHAR(255) NOT NULL, -- Путь к документу
    document_type VARCHAR(50) NOT NULL, -- Тип документа
    employee_id INTEGER REFERENCES Employee(employee_id) NOT NULL, -- Идентификатор сотрудника (внешний ключ)
    upload_date DATE NOT NULL -- Дата добавления
);
