import { useState } from 'react';
import { Handle, Position } from 'reactflow';
import { NodeTemplate } from '../NodeTemplate';
import { FormField } from '../FormField';
import { LuBrainCircuit } from 'react-icons/lu';

export const LLMNode = ({ id, data }) => {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleTest = async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await fetch('http://127.0.0.1:8000/llm/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to generate response');
      }

      const data = await response.json();
      setResponse(data.response);
      setError(null);
    } catch (error) {
      console.error('Error:', error);
      setError(error.message);
      setResponse('');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <NodeTemplate
      id={id}
      name='LLM'
      icon={<LuBrainCircuit />}
      handles={[
        {
          type: 'target',
          position: Position.Left,
          id: `${id}-system`,
          style: { top: `${100 / 3}%` },
        },
        {
          type: 'target',
          position: Position.Left,
          id: `${id}-prompt`,
          style: { top: `${200 / 3}%` },
        },
        {
          type: 'source',
          position: Position.Right,
          id: `${id}-response`,
        },
      ]}
    >
      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        <FormField
          label='Prompt:'
          type='textarea'
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />
        
        <button
          onClick={handleTest}
          disabled={isLoading}
          style={{
            background: 'linear-gradient(to bottom left, rgba(29, 23, 74, 1), rgba(60, 21, 115, 1))',
            color: 'white',
            padding: '8px',
            borderRadius: '5px',
            cursor: isLoading ? 'wait' : 'pointer',
            border: 'none',
          }}
        >
          {isLoading ? 'Generating...' : 'Test LLM'}
        </button>

        {error && (
          <div style={{ 
            color: '#ff4444', 
            backgroundColor: 'rgba(255, 68, 68, 0.1)', 
            padding: '8px', 
            borderRadius: '5px', 
            marginTop: '5px' 
          }}>
            Error: {error}
          </div>
        )}

        {response && (
          <div style={{ marginTop: '10px' }}>
            <div style={{ fontWeight: 'bold' }}>Response:</div>
            <div style={{
              padding: '8px',
              backgroundColor: 'rgba(242, 197, 255, 0.1)',
              borderRadius: '5px',
              marginTop: '5px'
            }}>
              {response}
            </div>
          </div>
        )}
      </div>
    </NodeTemplate>
  );
};