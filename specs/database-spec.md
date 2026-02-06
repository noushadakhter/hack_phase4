# Database Specification

This document details the database schema, including table structures, fields, types, and relationships for the Todo AI Chatbot application. The ORM to be used is SQLModel.

---

### 1. `User` Table

- **Description:** Stores user account information.
- **Model Name:** `User`
- **Fields:**
  - `id` (int, Primary Key): Unique identifier for the user. Auto-incrementing.
  - `email` (str, Unique, Indexed): The user's email address. Used for login.
  - `password_hash` (str): The user's hashed password.
  - `created_at` (datetime, Auto-generated): Timestamp of when the user account was created.

---

### 2. `Task` Table

- **Description:** Stores individual to-do items for users.
- **Model Name:** `Task`
- **Fields:**
  - `id` (int, Primary Key): Unique identifier for the task. Auto-incrementing.
  - `user_id` (int, Foreign Key to `User.id`): The ID of the user who owns this task.
  - `title` (str): The main content of the task.
  - `description` (str, Nullable): An optional, more detailed description.
  - `completed` (bool, Default: `false`): The completion status of the task.
  - `created_at` (datetime, Auto-generated): Timestamp of when the task was created.
  - `updated_at` (datetime, Auto-generated on update): Timestamp of the last update.

---

### 3. `Conversation` Table

- **Description:** Stores a record of a single chat conversation session. This allows for resuming conversations.
- **Model Name:** `Conversation`
- **Fields:**
  - `id` (int, Primary Key): Unique identifier for the conversation. Auto-incrementing.
  - `user_id` (int, Foreign Key to `User.id`): The ID of the user who initiated the conversation.
  - `created_at` (datetime, Auto-generated): Timestamp of when the conversation started.
  - `updated_at` (datetime, Auto-generated on update): Timestamp of the last message in the conversation.

---

### 4. `Message` Table

- **Description:** Stores an individual message within a conversation.
- **Model Name:** `Message`
- **Fields:**
  - `id` (int, Primary Key): Unique identifier for the message. Auto-incrementing.
  - `conversation_id` (int, Foreign Key to `Conversation.id`): The conversation this message belongs to.
  - `user_id` (int, Foreign Key to `User.id`): The user associated with the conversation.
  - `role` (str): The role of the message's author.
    - **Allowed Values:** `"user"`, `"assistant"`
  - `content` (str): The text content of the message.
  - `created_at` (datetime, Auto-generated): Timestamp of when the message was sent.

---

### 5. Relationships

- A `User` can have many `Task`s.
- A `User` can have many `Conversation`s.
- A `User` can have many `Message`s.
- A `Conversation` can have many `Message`s.
- A `Conversation` belongs to one `User`.
- A `Task` belongs to one `User`.
- A `Message` belongs to one `Conversation`.
- A `Message` belongs to one `User`.
