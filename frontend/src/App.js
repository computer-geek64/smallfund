import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [data, setData] = useState('')

  const getText = () => {
    const config = {
      method: 'get',
      url: 'http://128.61.105.83:8000/',
      headers: { }
    };
    
    axios(config)
    .then(function (response) {
      setData(JSON.stringify(response.data));
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
      <button onClick={getText}>Click Me!</button>
      <br />
      {data}
    </div>
  );
}

export default App;
