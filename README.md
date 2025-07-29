# Todo API – Django + DRF

This project is a secure and user-authenticated Todo API built with Django and Django Rest Framework (DRF).  
Each user can create, read, update, and delete their own tasks. The API includes filtering, custom serializers, and permission handling.

---

## Features

- User-authenticated task management (only logged-in users can access)
- List and filter tasks (by status)
- Task detail view with full description
- Create, update, and delete endpoints
- Access control: one user cannot access another user’s tasks
- Smart use of serializers (brief list + detailed view separation)
- Query param filtering: `/tasks/?status=true`

---

## API Endpoints (English Version)

| Method | URL                | Description                                                                                                                |
| ------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| GET    | `/tasks/`          | Returns a list of tasks owned by the authenticated user.<br>Only the `title` field is returned for each task (list view).  |
| GET    | `/tasks/<int:pk>/` | Returns the full details (`title`, `description`, `status`, etc.) of a single task.<br>User must be the owner of the task. |
| POST   | `/tasks/`          | Creates a new task for the logged-in user. Requires `title`, `description`, and `status`.                                  |
| PUT    | `/tasks/<int:pk>/` | Updates the specified task. Only the task owner can perform this action.                                                   |
| DELETE | `/tasks/<int:pk>/` | Deletes the specified task. Only the task owner can perform this action.                                                   |

> All endpoints are protected by `IsAuthenticated` — authentication is required for all actions.
> Optional query parameter:
> `/tasks/?status=true` → Filter tasks by completion status.
