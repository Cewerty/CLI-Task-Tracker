# Task Tracker CLI

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A simple CLI task manager developed as part of the [roadmap.sh](https://roadmap.sh/projects/task-tracker) project.  
Complies with requirements: JSON storage, native Python, error handling.

## 📦 Installation

```bash
# Install via pip
pip install git+https://github.com/your-username/task-tracker.git

# Or using uv
uv pip install git+https://github.com/your-username/task-tracker.git
```

🚀 Usage
Basic Commands:

```bash
task-cli add "Buy milk"              # Add a task
task-cli update 1 "Buy 2 liters"     # Update a task
task-cli delete 1                    # Delete a task
task-cli mark-done 2                 # Mark as done
task-cli list "not-done"             # List incomplete tasks
```

### Supported Status Filters

done - Completed tasks

not-done - Incomplete tasks

in-progress - Tasks in progress

all - All tasks

## 🛠 Features

Automatic creation of tasks.json on first run

Task ID validation

Human-readable timestamps

Error handling for:

Non-existent tasks

Invalid statuses

## 🛠 Development

Clone the repository:

```bash
git clone https://github.com/your-username/task-tracker.git
```

## 📌 Implementation Details

Zero Dependencies: Uses only Python standard library

Idempotent Operations: Safe command retries

Local Time Handling: Uses system timezone

## Links

[roadmap.sh Project Page](https://roadmap.sh/projects/task-tracker)

[Requirement Checklist](https://roadmap.sh/projects/task-tracker#:~:text=Requirements,edge%20cases%20gracefully.)

## License

MIT License. See [LICENSE](https://github.com/Cewerty/CLI-Task-Tracker/blob/main/LICENSE) for details.
