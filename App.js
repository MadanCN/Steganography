import React, { useState } from 'react';
import axios from 'axios';

const SteganographyApp = () => {
  const [operationType, setOperationType] = useState('text');
  const [inputText, setInputText] = useState('');
  const [responseMessage, setResponseMessage] = useState('');

  const handleOperationTypeChange = (e) => {
    setOperationType(e.target.value);
  };

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const encodeData = async () => {
    try {
      const requestData = { data: inputText };

      const response = await axios.post(`http://localhost:5000/encode_text`, requestData, {
        headers: {
          'Content-Type': 'application/json',
        },
      });

      setResponseMessage(response.data.message);
    } catch (error) {
      setResponseMessage('An error occurred while encoding the text.');
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Steganography App</h1>
      <div>
        <label htmlFor="operationType">Operation Type:</label>
        <select id="operationType" value={operationType} onChange={handleOperationTypeChange}>
          <option value="text">Text</option>
          {/* Add other options for image, audio, video here */}
        </select>
      </div>
      {operationType === 'text' && (
        <div>
          <label htmlFor="inputText">Input Text:</label>
          <input type="text" id="inputText" value={inputText} onChange={handleInputChange} />
        </div>
      )}
      <button onClick={encodeData}>Encode</button>
      {responseMessage && <p>{responseMessage}</p>}
    </div>
  );
};

export default SteganographyApp;
