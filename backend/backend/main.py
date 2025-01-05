from fastapi import FastAPI, Form,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from huggingface_hub import InferenceApi


app = FastAPI()

#Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:3000', 'http://localhost:3000', 'http://127.0.0.1:3001', 'http://localhost:3001'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )
# Hugging Face Inference API setup
HF_ACCESS_TOKEN = "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"
model = "gpt2"  # Specify the Hugging Face model to use
inference_api = InferenceApi(repo_id=model, token=HF_ACCESS_TOKEN)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}



# Request model for the /llm/query endpoint
class LLMRequest(BaseModel):
    prompt: str
# Endpoint to handle LLM queries

@app.post("/llm/query")
async def query_llm(request: LLMRequest):
    # Validate the prompt
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    
    # Query Hugging Face API
    try:
        # Set parameters for the inference
        params = {
            "max_length": 100,  # Adjust as needed
            "temperature": 0.7,  # Adjust as needed
            "return_full_text": False  # Only get the generated text
        }
        
        # Generate text
        response = inference_api(
            inputs=request.prompt,
            params=params
        )
        
        # Handle the response based on its type
        if isinstance(response, list):
            # Some models return a list of generated texts
            generated_text = response[0].get('generated_text', '')
        elif isinstance(response, dict):
            # Some models return a dictionary
            generated_text = response.get('generated_text', '')
        elif isinstance(response, str):
            # Some models return just a string
            generated_text = response
        else:
            raise HTTPException(
                status_code=500, 
                detail="Unexpected response format from Hugging Face API"
            )
        
        return {"response": generated_text}
        
    except Exception as e:
        # Log the full error message for debugging
        print(f"Error occurred: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred while generating text: {str(e)}"
        )






class PipelineData(BaseModel):
    nodes: list
    edges: list


@app.post('/pipelines/parse')
def parse_pipeline(pipeline: PipelineData):
    print(pipeline)
    print(pipeline.nodes, pipeline.edges)
    num_nodes = len(pipeline.nodes)
    num_edges = len(pipeline.edges)

    #Logic to determine if it is a DAG
    degrees = {}

    stack = []

    for edge in pipeline.edges:
        if edge["target"] in degrees:
            degrees[edge["target"]] += 1
        else:
            degrees[edge["target"]] = 1

    for node in pipeline.nodes:
        if node["id"] not in degrees:
            stack.append(node["id"])

    
    while len(stack) > 0 :
        #get first element of stack
        currentNode = stack.pop(0)

        #find the connections of that node in edges
        for edge in pipeline.edges:
            if currentNode == edge["source"]:
                connection = edge["target"]
                print(connection)
                degrees[connection] -= 1
                if degrees[connection] == 0:
                    stack.append(edge["target"])

    dag = True

    #loop through
    for connection in degrees.values():
        if connection > 0:
            dag = False
            break

    return {'num_nodes': num_nodes, 'num_edges': num_edges, 'is_dag': dag}

