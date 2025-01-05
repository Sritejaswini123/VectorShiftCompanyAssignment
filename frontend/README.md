# VectorShift Frontend Technical Assessment

This project implements the frontend and backend requirements for the VectorShift technical assessment. It is built using **React.js** for the frontend and **FastAPI** for the backend.

## Overview

The project is designed to showcase:

1. Node abstraction for reusability and maintainability.
2. Styling for a clean and unified user interface.
3. Dynamic logic for nodes, including text input functionality.
4. Backend integration to handle pipeline data and validate Directed Acyclic Graph (DAG) properties.

The repository consists of two main folders:

- `frontend`: Contains the React.js application.
- `backend`: Contains the FastAPI application.

---

## Features

### Part 1: Node Abstraction

The project implements an abstraction for reusable nodes. The base abstraction allows creating nodes with varying functionalities and styles easily.

- **Predefined Nodes**:

  - Input Node
  - LLM Node
  - Output Node
  - Text Node

- **Additional Nodes Created**:
  - **Checkbox Node**: Allows toggling values.
  - **File Upload Node**: Enables file upload functionality.
  - **Multiselect Node**: Allows selecting multiple options.
  - **Date Node**: For date input.
  - **Notes Node**: Used for freeform notes.

Each node demonstrates the flexibility of the abstraction layer, including dynamic connections, input/output handles, and individual functionalities.

### Part 2: Styling

The nodes and other components are styled for a visually appealing interface using:

- Custom gradients for buttons and backgrounds.
- Shadows and rounded edges for a polished look.
- Dynamic resizing for input fields (e.g., text areas).

### Part 3: Text Node Logic

1. **Dynamic Resizing**:

   - The Text Node dynamically adjusts its size (width and height) based on the text input, ensuring better visibility.

2. **Dynamic Handles**:
   - Supports variables defined in double curly brackets (`{{variable_name}}`).
   - Automatically adds input handles for these variables on the left side of the node.

### Part 4: Backend Integration

The frontend connects to the FastAPI backend to:

1. Submit the pipeline data (nodes and edges).
2. Receive the number of nodes, edges, and whether the pipeline forms a Directed Acyclic Graph (DAG).
3. Display results in a modal notification.

The backend includes:

- Endpoint for pipeline parsing (`/pipelines/parse`), which calculates:
  - Total nodes.
  - Total edges.
  - DAG validation logic.

---

## Installation and Usage

### Prerequisites

- **Node.js** (v14+)
- **Python** (v3.8+)
- **FastAPI** and required Python libraries (`pip install fastapi uvicorn pydantic`)

### Clone the Repository

```bash
git clone https://github.com/Sritejaswini123/VectorShift.git
cd VectorShift
```
