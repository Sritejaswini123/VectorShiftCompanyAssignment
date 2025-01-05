# VectorShift Frontend Technical Assessment  

This project is a solution to the VectorShift Frontend Technical Assessment, showcasing the implementation of a pipeline-based user interface with React.js for the frontend and FastAPI for the backend. The application allows users to create and manipulate nodes and edges, style components, and integrate frontend pipelines with backend logic.  

---

## How It Works  

### Project Overview  
The project is divided into two main components:  

**Frontend:**  
- Built using React.js, it provides a user interface to create, style, and interact with different types of nodes.  
- Users can define edges between nodes and create directed acyclic graphs (DAG).  

**Backend:**  
- Implemented using FastAPI, it processes data sent from the frontend to determine the number of nodes, edges, and whether the graph is a DAG.  

---

## Frontend Features  
- A "Submit" button allows users to send the pipeline (nodes and edges) to the backend for processing.  
- A modal popup displays the backend response, including:  
  - Number of nodes in the pipeline.  
  - Number of edges in the pipeline.  
  - Whether the pipeline forms a Directed Acyclic Graph (DAG).  

---

## Backend Features  

**Pipeline Analysis:**  
- The backend receives nodes and edges from the frontend via the `/pipelines/parse` endpoint.  
- Processes and calculates:  
  - The total number of nodes and edges.  
  - Whether the pipeline forms a Directed Acyclic Graph (DAG) using a topological sorting algorithm.  

**LLM Integration:**  
- The `/llm/query` endpoint interacts with the Hugging Face GPT-2 model.  
- Generates responses based on user input provided in the LLM Node.  

**CORS Configuration:**  
- Configured to handle CORS requests from the frontend.  

---

## Workflow  

### Node Creation  
- Users drag and drop nodes into the pipeline workspace.  
- Nodes can be connected to each other by defining edges.  

### Text Input in Text Node  
- Users input text into a Text Node.  
- Dynamic handles are generated for variables defined in `{{variableName}}` format.  

### Submit Pipeline  
- Users click the "Submit" button to send the pipeline data to the backend.  
- The backend processes the data and returns a response.  

### Response Display  
- A modal popup displays the backend response:  
  - Total number of nodes.  
  - Total number of edges.  
  - Whether the pipeline is a DAG.  

---

## Technologies Used  

### Frontend  
- React.js  
- Styled Components  
- React Flow  

### Backend  
- FastAPI  
- Hugging Face GPT-2  
- CORS Middleware  

---


![image](https://github.com/user-attachments/assets/b8057a9c-49ce-47fd-a320-5a853f5dc55c)
![Screenshot 2025-01-05 083105](https://github.com/user-attachments/assets/16b2f003-2d1f-4043-b4c7-6930c1774f80)

![Screenshot 2025-01-05 083759](https://github.com/user-attachments/assets/863cc109-ed6e-4ec9-87d9-e85a1dd10fdd)

